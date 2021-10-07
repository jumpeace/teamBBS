from django.urls import reverse
from django.http import JsonResponse, Http404
from django.shortcuts import redirect
from config.shortcuts import add_default_context

from django.views import generic
from user.mixins import LoginRequiredMixin

from .models import Team
from manytomany.models import User_Team

from .forms import CreateTeamForm
from manytomany.forms import CreateUserTeamForm

from props.team import props

class team_view:

    class List(LoginRequiredMixin, generic.ListView):
        model = Team
        context_object_name = 'team_list'
        template_name = 'team/list.html'

        def get_queryset(self, **kwargs):
            user_team_list = User_Team.objects.filter(user=self.request.user.id)
            queryset = []
            for user_team in user_team_list:
                queryset.append(user_team.team)
            return queryset

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.list_)
        

    class Create(LoginRequiredMixin, generic.CreateView):
        model = Team
        form_class = CreateTeamForm
        template_name = 'page/form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.create)

        def form_valid(self, form):
            team = form.save(commit=False)
            team.user = self.request.user
            result = super().form_valid(form)
            User_Team.objects.create(user=self.request.user, team=team, is_owner=True)
            return result

        def get_success_url(self):
            return reverse('team:list')

    # チームのオーナーしか表示できないようにする
    class Detail(LoginRequiredMixin, generic.DetailView):
        model = Team
        pk_url_kwarg = 'team_id'
        context_object_name = 'team'
        template_name = 'team/detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            user_team = User_Team.objects.filter(user=self.request.user.id, team=self.kwargs['team_id'])[0]
            context['is_owner'] = user_team and user_team.is_owner

            return add_default_context(context, self, props.detail)

    def update(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if request.method != 'POST':
            return redirect('team:detail', team_id=kwargs['team_id'])
        new_names = request.POST.getlist('new_name')
        if len(new_names) == 0:
            raise Http404('Invalid request.')

        new_name = new_names[0]

        obj = Team.objects.get(pk=kwargs['team_id'])
        obj.name = new_name
        obj.save()

        response = {'new_name': new_name}
        return JsonResponse(response)

    @staticmethod
    def delete(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if (request.method != 'POST'):
            return redirect('team:detail', team_id=kwargs['team_id'])

        obj = Team.objects.get(pk=kwargs['team_id'])
        obj.delete()

        return redirect('team:list')


    class user:
        class List(LoginRequiredMixin, generic.ListView):
            model = User_Team
            context_object_name = 'object_list'
            template_name = 'team/user/list.html'

            def get_queryset(self, **kwargs):
                return User_Team.objects.filter(team=self.kwargs['team_id'])

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return add_default_context(context, self, props.user.list_)

        class Create(LoginRequiredMixin, generic.CreateView):
            model = User_Team
            form_class = CreateUserTeamForm
            template_name = 'page/form.html'

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                return add_default_context(context, self, props.user.create)

            def form_valid(self, form):
                user_team = form.save(commit=False)
                user_team.user = self.request.user
                result = super().form_valid(form)
                return result

            def get_success_url(self):
                return reverse('team:channel:list', kwargs={'team_id': int(self.request.POST['team'])})

        @staticmethod
        def delete(request, **kwargs):
            # セキュリティ甘そう
            if not request.user.is_authenticated:
                return redirect('index')
            if (request.method != 'POST'):
                return redirect('team:detail', team_id=kwargs['team_id'])
            
            user_delete_ids = request.POST.getlist('user_delete_id')            
            user_delete_id = int(user_delete_ids[0])
            if user_delete_id == request.user.id:
                return redirect('team:user:list', team_id=kwargs['team_id'])
            
            obj = User_Team.objects.filter(team=kwargs['team_id'], user=user_delete_id)
            obj.delete()

            return redirect('team:user:list', team_id=kwargs['team_id'])
