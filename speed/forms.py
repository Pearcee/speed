from django import forms

from .models import Speed

class PostForm(forms.ModelForm):

    class Meta:
        model = Speed
        fields = ('ServerName','Timestamp',)

        