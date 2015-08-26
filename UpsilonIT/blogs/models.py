from django.conf import settings
from django.db import models
from django.utils.timezone import now as datetime_now
from core.utils import upload_to_blogs, upload_to_posts
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    modified_at = models.DateTimeField(_('modified at'), default=datetime_now())
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to=upload_to_blogs, verbose_name=_('Image'), blank=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name='posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    created_at = models.DateTimeField(_('created at'), default=datetime_now)
    modified_at = models.DateTimeField(_('modified at'), default=datetime_now)
    image = models.ImageField(upload_to=upload_to_posts, verbose_name=_('Image'), blank=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title