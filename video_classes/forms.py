from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from video_classes.models import VideoClass


class VideoClassForm(forms.ModelForm):
    class Meta:
        model = VideoClass
        fields = [
            'title',
            'topic',
            'description',
            'author',
            'video_path',
            'premium_content',
            'draft',
            'last_update_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
