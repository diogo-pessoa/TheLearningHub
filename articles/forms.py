from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce.widgets import TinyMCE

from articles.models import Article, Topic


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title',
                  'description',
                  'topic',
                  'premium_content', 'draft',
                  'content',
                  'author',
                  'last_update_at']

    draft = forms.CheckboxInput(
        check_test=False
    )
    description = forms.CharField(
        required=False
    )

    restricted_access = forms.CheckboxInput(
        check_test=False
    )

    last_update_at = forms.DateField(
        required=False,
        disabled=True

    )
    content = forms.CharField(
        widget=TinyMCE(attrs={
            'required': False,
            'cols': 30,
            'rows': 10
        }))

    author = forms.ModelChoiceField(
        required=True,
        queryset=User.objects.filter(is_staff=True)
    )

    topic = forms.ModelChoiceField(
        required=False,
        queryset=Topic.objects.all(),
        initial="General"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.initial['last_update_at'] = timezone.now()
        self.helper.add_input(Submit('submit', 'Submit'))
        labels = {
            'title': 'Article title',
            'description': 'Description',
            'premium_content': 'Premium Content',
            'draft': 'Draft',
            'author': 'Author',
            'topic': 'Topic',
            'last_update_at': 'Last Updated:',
            'content': ' Article content'
        }
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label
