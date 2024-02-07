from django.contrib.auth.models import AbstractUser
from django.db import models
from choices import RoleChoice


class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Workspace(models.Model):
    title = models.CharField(
        max_length=225,
        verbose_name='Пространство',
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class WorkspaceRole(models.Manager):
    workspaces = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.Choices(RoleChoice)
