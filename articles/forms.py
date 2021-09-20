from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils import timezone

from articles.models import Article


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description',
                  'restricted_access', 'draft',
                  'content',
                  'author',
                  'created_at']

    draft = forms.CheckboxInput(
        check_test=False
    )
    description = forms.CharField(
        required=False
    )

    restricted_access = forms.CheckboxInput(
        check_test=False
    )

    created_at = forms.DateField(
        required=False,
        disabled=True

    )
    content = forms.CharField(
        required=False
    )

    author = forms.CharField(
        required=False,
        disabled=True
    )

    def __init__(self, *args, author, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.initial['author'] = author.id
        self.initial['created_at'] = timezone.now()
        self.initial['created_at'] = timezone.now()
        self.helper.form_method = 'post'
        self.helper.form_action = 'write_article'
        self.helper.add_input(Submit('submit', 'Submit'))
