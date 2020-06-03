from django import forms
from .models import TeacherFile


class TeacherFileForm(forms.ModelForm):

    class Meta:
        model = TeacherFile

        fields = ("the_file", "name", "description")
