from django.db import models
from datetime import date
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from markdown import markdown


class Icon(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    
    def __str__(self):
        return "%s - %s" % (self.id, self.name)

class Note(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content_markdown = models.TextField()
    content_html = models.TextField()
    date_published = models.DateField(default=date.today)
    slug = models.SlugField(max_length=255)
    label = models.CharField(max_length=255, db_index=True)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return "%s - %s" % (self.id, self.title)
    
@receiver(pre_save, sender=Note, dispatch_uid="pre_save_note")
def pre_save_note(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    instance.content_html = markdown(instance.content_markdown, safe_mode='escape')