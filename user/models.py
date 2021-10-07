from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    # ユーザーの作成
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("メールアドレスを入力してください")

        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    # スーパーユーザーの作成
    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    created_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    last_login_date = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    # ユーザー作成時に尋ねるフィールドを尋ねている
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    # 許可されているか（たぶんadminの許可）
    def has_perm(self, perm, obj=None):
        return self.is_superuser or self.is_staff

    # ないとadminに入れない
    def has_module_perms(self, app_label):
        return True
