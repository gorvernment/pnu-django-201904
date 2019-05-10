from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    quiz = forms.IntegerField(label='3+3=?')

    def clean_quiz(self):
        quiz = self.cleaned_data.get('quiz')
        if quiz != 6:
            raise forms.ValidationError('땡~!')
        return quiz