from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from personal_space.models import UserProfile, UserNoteFromVideoClass


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name',
                  'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))


class UserNotesFromClassForm(forms.ModelForm):
    class Meta:
        model = UserNoteFromVideoClass
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
