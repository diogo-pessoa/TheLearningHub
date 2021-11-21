from django.db import models

# Create your models here.
from tinymce import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=120, null=False)
    content = HTMLField('Content', default='<p>New Page, click on Edit Page to create content here.</p>')


def __str__(self):
    return self.title


