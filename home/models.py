from django.db import models

# Create your models here.
from tinymce import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=120, null=False)
    content = HTMLField('Content', default='<p>New Page, click on Edit Page to create content here.</p>')


def __str__(self):
    return self.title


class LearningFileStorage(models.Model):
    file = models.ImageField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    page_source = models.CharField(default=None, null=True, max_length=32)

    def __str__(self):
        return self.file.name
