from config.shortcuts import add_default_context
from django.http import JsonResponse, Http404
from django.shortcuts import redirect
from django.urls import reverse

from django.views import generic
from user.mixins import LoginRequiredMixin

from .models import Channel
from team.models import Team

from .forms import CreateChannelForm

from props.channel import props

class channel_view:
    class List(LoginRequiredMixin, generic.ListView):
        model = Channel
        context_object_name = 'channel_list'
        template_name = 'channel/list.html'

        def get_queryset(self, **kwargs):
            return Channel.objects.filter(team=self.kwargs['team_id'])

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.list_)

    class Create(LoginRequiredMixin, generic.CreateView):
        model = Channel
        form_class = CreateChannelForm
        template_name = 'page/form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.create)

        def form_valid(self, form):
            channel = form.save(commit=False)
            team = Team.objects.get(pk=self.kwargs['team_id'])
            # TODO どうエラーメッセージを出すか考える
            if not team:
                return
            channel.team = team
            result = super().form_valid(form)
            return result

        def get_success_url(self):
            return reverse('team:channel:list', kwargs={'team_id': self.kwargs['team_id']})

    # TODO チームのオーナー以外見れないようにする
    class Detail(LoginRequiredMixin, generic.DetailView):
        model = Channel
        pk_url_kwarg = 'channel_id'
        context_object_name = 'channel'
        template_name = 'channel/detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.detail)

    @staticmethod
    def update(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if (request.method != 'POST'):
            return redirect('team:channel:detail', team_id=kwargs['team_id'], channel_id=kwargs['channel_id'])
        new_names = request.POST.getlist('new_channel_name')
        if len(new_names) == 0:
            raise Http404('Invalid request.')

        new_name = new_names[0]

        obj = Channel.objects.get(pk=kwargs['channel_id'])
        obj.name = new_name
        obj.save()

        response = {'name': new_name}
        return JsonResponse(response)

    @staticmethod
    def delete(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if (request.method != 'POST'):
            return redirect('team:channel:detail', team_id=kwargs['team_id'], channel_id=kwargs['channel_id'])

        # 403 か 404 出す
        obj = Channel.objects.get(pk=kwargs['channel_id'])
        obj.delete()

        return redirect('team:channel:list', team_id=kwargs['team_id'])
