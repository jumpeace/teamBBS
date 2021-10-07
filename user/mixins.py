from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ログイン後は行きたかったページに行くようになる
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url = '/user/login/')) 
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)