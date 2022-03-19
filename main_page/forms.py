from django import forms
from .models import RecievedMessages

class ReceivedMessagesForm(forms.ModelForm):
    class Meta:
        model = RecievedMessages
        fields = '__all__'


class ReceivedMessagesSpanishForm(forms.ModelForm):
    class Meta:
        model = RecievedMessages
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nombre"
        self.fields['message'].label = "Mensaje"