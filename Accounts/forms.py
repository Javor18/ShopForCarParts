from django.contrib.auth import get_user_model
from django.forms import CharField, BooleanField, PasswordInput
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    content = BooleanField()

    password2 = CharField(
        label="Repeat Password",
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        instance = super(RegisterUserForm, self).save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance

    def clean_email(self):
        print('clean_email')

        email = self.cleaned_data['email']
        try:
            email = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise ValidationError(u'Email "%s" is already in use.' % email)

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']