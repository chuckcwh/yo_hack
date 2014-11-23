from django import forms
from django.contrib.auth.forms import UserCreationForm
from yo_hack_app.models import Profile, Action, Family


class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class ActionForm(forms.ModelForm):
    HELLO = 0
    HELP = 1
    LOCATION = 2
    ACTIONS = (
        (HELLO, "hello"),
        (HELP, "help"),
        (LOCATION, "location"),
    )
    action = forms.ChoiceField(choices=[])
    text = forms.CharField()
    receiver = forms.ChoiceField(choices=[])

    class Meta:
        model = Action
        fields = ('action', 'text', 'receiver')

    def __init__(self, profile, *args, **kwargs):
        super(ActionForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].choices = [(receiver.pk, receiver.you.username) for receiver in Family.objects.filter(me=profile)]
        self.fields['action'].choices = self.ACTIONS

# class FamilyForm(forms.ModelForm):
#     class Meta:
#         model = Family
#         fields = ('you')
#
#     def __init__(self