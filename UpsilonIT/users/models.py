from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.utils import upload_to_users
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        (0, _('none')),
        (1, _('male')),
        (2, _('female')),
    )

    email = models.EmailField(_('email adress'), max_length=255, unique=True, db_index=True)
    first_name = models.CharField(_('first name'), max_length=255, blank=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    created_at = models.DateField(_('created at'), auto_now_add=True)
    phone = models.CharField(_('phone'), max_length=15)
    avatar = models.ImageField(upload_to=upload_to_users, verbose_name=_('Avatar'), blank=True)
    gender = models.IntegerField(choices=GENDER, verbose_name=_('Gender'),
                                 blank=True, null=True)
    age = models.PositiveSmallIntegerField(verbose_name=_('Age'), null=True,
                                           blank=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name