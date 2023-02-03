from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta:
        verbose_name_plural = 'CustomUser'

    def __str__(self):
        return 'username'