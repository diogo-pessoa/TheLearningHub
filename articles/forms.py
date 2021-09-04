from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Article


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'restricted_access', 'draft', 'content']

    title = forms.CharField(
        label="Main title",
        initial='My Very Fine article',
        max_length=118,
        required=True,
    )

    description = forms.CharField(
        label="Brief Summary",
        max_length=254,
        required=False,
    )

    restricted_access = forms.BooleanField(
        label="Restrict_access?",
        required=True,
        initial=False,
        widget=forms.CheckboxInput
    )

    draft = forms.BooleanField(
        label="Draft?",
        required=True,
        widget=forms.CheckboxInput,
    )

    content = forms.CharField(
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'create_article_id'
        self.helper.form_class = 'card-content'
        self.helper.form_method = 'post'
        self.helper.form_action = 'write_article'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.author = args[1]
        self.created_at = datetime.now
