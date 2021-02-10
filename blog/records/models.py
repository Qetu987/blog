from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from django.urls import reverse
from os import listdir
from os.path import isfile, join, isdir
import markdown
import os

# Create your models here.
def parse_md(txt):
    try:
        txt = txt.decode('UTF-8')
    except:
        pass
    return mark_safe(markdown.markdown(txt,extensions=['extra', 'smarty'], output_format='html5'))



class Blog(models.Model):
	name = models.CharField(max_length=250, verbose_name=_(u'Name'), blank=True, null = True)
	desc = models.TextField(verbose_name=_(u'Description'), blank=True, null = True)
	name_slug = models.CharField(verbose_name='Name slug',max_length=250, blank=True, null = True)
	is_active = models.BooleanField(verbose_name=_('Is published?'), default=False)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog_detail', kwargs={'slug': self.name_slug })
