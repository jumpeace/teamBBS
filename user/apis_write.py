from .models import User
from .forms import CreateUserForm, AuthUserForm

from django.contrib.auth import login, logout, authenticate

class user_api_w():

    @staticmethod
    def register(request):
        results_write = {}
        r_val = {}

        results_write['register'] = {}
        form = CreateUserForm(request.POST)

        if not form.is_valid():
            r_val['register_form'] = form
            return r_val

        form.save()

        # ユーザー認証
        user = User.objects.get(email=request.POST['email'])

        # ログイン処理
        login(request, user, backend='user.backends.AuthUserBackend')

        # 成功
        return r_val

    @staticmethod
    def set_is_login(val, user):

        if not user:
            return False

        user.is_login = val
        user.save()

        return True

    @staticmethod
    def login_(request):
        r_val = {}

        form = AuthUserForm(request.POST)

        # バリデーション
        if not form.is_valid():
            r_val['login_form'] = form
            return r_val

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        login(request, user)

        # 成功
        return r_val

    @staticmethod
    def logout_(request, user):
        if not user_api_w.set_is_login(False, user):
            return False
        logout(request)
        return True


