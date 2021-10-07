from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class AuthUserBackend(ModelBackend):

    # 認証のバックエンドのオーバーライド
    def authenticate(self, request, email=None, password=None, **args):
        UserModel = get_user_model()
        if email is None:
            email = args.get(UserModel.USERNAME_FIELD)

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user