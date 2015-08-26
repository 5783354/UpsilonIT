from users.serializers import UserSerializer
from users.models import User
from users.permissions import IsStaffOrTargetUser
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),