from django.db.models import Choices


class RoleChoices(Choices):
    ADMIN = 'admin'
    MEMBER = 'member'
    OWNER = 'owner'
