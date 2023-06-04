from django.forms import ModelForm
from .myforms import Nachrichts


class PostForm(ModelForm):
    class Meta:
        managed = True
        model = Nachrichts
        fields = ["name", "email", "subject", "message"]

    def clean(self):
        super().clean()
        return self.cleaned_data
