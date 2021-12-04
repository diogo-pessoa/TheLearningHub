from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from home.models import Page, LearningFileStorage


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__()
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = LearningFileStorage
        fields = [
            'file'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        print(self.helper.get_attributes())
        self.helper.add_input(Submit('submit', 'Upload File'))
