from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from config.shortcuts import add_default_context

from django.views import generic
from user.mixins import LoginRequiredMixin

from .models import Role
from user.models import User
from team.models import Team
from manytomany.models import User_Role, User_Team

from .forms import CreateRoleForm

from props.role import props

class role_view:
    class List(LoginRequiredMixin, generic.ListView):
        model = Role
        template_name = 'role/list.html'

        def get_queryset(self):
            return Role.objects.filter(team=self.kwargs['team_id'])

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.list_)


    class Create(LoginRequiredMixin, generic.CreateView):
        model = Role
        form_class = CreateRoleForm
        template_name = 'page/form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.create)

        def form_valid(self, form):
            role = form.save(commit=False)
            team = Team.objects.get(pk=self.kwargs['team_id'])
            role.team = team
            return super().form_valid(form)

        def get_success_url(self):
            return reverse('team:role:list', kwargs={'team_id': self.kwargs['team_id']})

    # TODOそのチームのオーナーでなければ表示しない
    class Detail(LoginRequiredMixin, generic.DetailView):
        model = Role
        pk_url_kwarg = 'role_id'
        template_name = 'role/detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.detail)

    @staticmethod
    def update(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if (request.method != 'POST'):
            return redirect('team:role:detail', team_id=kwargs['team_id'], role_id=kwargs['role_id'])

        new_names = request.POST.getlist('new_name')
        if len(new_names) == 0:
            raise Http404('Invalid request.')

        new_name = new_names[0]

        obj = Role.objects.get(pk=kwargs['role_id'])
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
            return redirect('team:role:detail', team_id=kwargs['team_id'], role_id=kwargs['role_id'])

        obj = Role.objects.get(pk=kwargs['role_id'])
        obj.delete()

        return redirect('team:role:list', team_id=kwargs['team_id'])

    class user:
        class List(LoginRequiredMixin, generic.ListView):
            model = User_Role
            context_object_name = 'role_user_list'
            template_name = 'role/user/list.html'

            def get_queryset(self):
                return User_Role.objects.filter(role=self.kwargs['role_id'])

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)

                team_user_queryset = User_Team.objects.filter(team=self.kwargs['team_id'])
                team_user_list = [team_user for team_user in team_user_queryset]

                for role_user in context['role_user_list']:
                    for i, team_user in enumerate(team_user_list):
                        if team_user.user.id == role_user.user.id:
                            team_user_list.pop(i)
                context['team_user_list'] = team_user_list
                return add_default_context(context, self, props.user.list_)

        # TODO 同じユーザーが同じ役職に複数つけないようにする
        @staticmethod
        def create(request, **kwargs):
            # セキュリティ甘そう
            if not request.user.is_authenticated:
                return redirect('index')
            if (request.method != 'POST'):
                return redirect('team:role:user_list', team_id=kwargs['team_id'], role_id=kwargs['role_id'])

            new_user_ids = request.POST.getlist('new_user')
            if len(new_user_ids) == 0:
                raise Http404('Invalid request.')
            new_user = User.objects.get(pk=new_user_ids[0])
            role = Role.objects.get(pk=kwargs['role_id'])
            if not role:
                raise Http404('Role does not exist.')

            new_object = User_Role.objects.create(user=new_user, role=role)

            response = {'new_user': {'id': new_object.user.id, 'email': new_object.user.email}}
            return JsonResponse(response)

        @staticmethod
        def delete(request, **kwargs):
            if not request.user.is_authenticated:
                return redirect('index')
            if (request.method != 'POST'):
                return redirect('team:role:user_list', team_id=kwargs['team_id'], role_id=kwargs['role_id'])
            delete_pks = request.POST.getlist('delete_pk')
            for delete_pk in delete_pks:
                obj = User_Role.objects.get(pk=delete_pk)
                obj.delete()
            return JsonResponse({})