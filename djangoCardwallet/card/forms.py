from django import forms
from cardwallet.models import PersonalcardInfo
from django.contrib.auth.models import User

class cashForm(forms.Form):
    class Meta:
        model = PersonalcardInfo
        fields = ['balance']
class deleteCard(forms.Form):
    class Meta:
        model = PersonalcardInfo
        fields = ['u_num','pcn']