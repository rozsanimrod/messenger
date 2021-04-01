from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile, genders
from django.forms import IntegerField, ChoiceField, BooleanField


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('email', 'first_name', 'last_name', 'username')

    age = IntegerField()
    genders = ChoiceField(choices=genders)
    accepted_terms = BooleanField()

    def save(self, commit=True):
        user = super().save(commit=True)
        profile = UserProfile(user=user,
                              age=self.cleaned_data.get('age'),
                              gender=self.cleaned_data.get('gender'),
                              accepted_terms=self.cleaned_data.get('accepted_terms'),)
        if commit:
            profile.save()
        return user

