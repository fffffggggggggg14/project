from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomAdminManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('يجب أن يكون لدى المسؤول اسم مستخدم')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomAdmin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, verbose_name='اسم المستخدم')
    email = models.EmailField(verbose_name='عنوان البريد الإلكتروني', max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=False, verbose_name='موظف')
    is_active = models.BooleanField(default=True, verbose_name='نشط')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الانضمام')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomAdminManager()

    class Meta:
        verbose_name = 'مسؤول مخصص'
        verbose_name_plural = 'المسؤولون المخصصون'

    def __str__(self):
        return self.username
