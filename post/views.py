from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from config.shortcuts import add_default_context

from django.views import generic
from user.mixins import LoginRequiredMixin

from .models import Post
from channel.models import Channel

from .forms import CreatePostForm

from props.post import props


class post_view:
    class List(LoginRequiredMixin, generic.ListView):
        model = Post
        context_object_name = 'post_list'
        template_name = 'post/list.html'

        def get_queryset(self):
            return Post.objects.filter(channel=self.kwargs['channel_id'])

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return add_default_context(context, self, props.list_)

    @staticmethod
    def create(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if (request.method != 'POST'):
            return redirect('team:channel:post:list', team_id=kwargs['team_id'], channel_id=kwargs['channel_id'])

        new_contents = request.POST.getlist("new_content")
        if len(new_contents) == 0:
            raise Http404('Invalid request.')

        new_content = new_contents[0]
        channel = Channel.objects.get(pk=kwargs['channel_id'])
        if not channel:
            raise Http404('Channel does not exist.')

        obj = Post.objects.create(content=new_content, user=request.user, channel=channel)
        # TODO なかったら Http500 出すようにする

        response = {'new_post': {'id': obj.id, 'content': obj.content}}
        return JsonResponse(response)

    @staticmethod
    class Detail(LoginRequiredMixin, generic.DetailView):
        model = Post
        pk_url_kwarg = 'post_id'
        context_object_name = 'post'
        template_name = 'post/detail.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['user'] = self.request.user
            return add_default_context(context, self, props.detail)

    @staticmethod
    def update(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if (request.method != 'POST'):
            return redirect('team:channel:post:detail', team_id=kwargs['team_id'], channel_id=kwargs['channel_id'], post_id=kwargs['post_id'])

        contents = request.POST.getlist("content")
        if len(contents) == 0:
            raise Http404('Invalid request.')

        content = contents[0]

        obj = Post.objects.get(pk=kwargs['post_id'])
        obj.content = content
        obj.save()

        response = {'content': content}
        return JsonResponse(response)

    @staticmethod
    def delete(request, **kwargs):
        # セキュリティ甘そう
        if not request.user.is_authenticated:
            return redirect('index')
        if (request.method != 'POST'):
            return redirect('team:channel:post:detail', team_id=kwargs['team_id'], channel_id=kwargs['channel_id'], post_id=kwargs['post_id'])

        # 403 か 404 出す
        obj = Post.objects.get(pk=kwargs['post_id'])
        obj.delete()

        return redirect('team:channel:post:list', team_id=kwargs['team_id'], channel_id=kwargs['channel_id'])