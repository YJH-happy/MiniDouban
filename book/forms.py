from django.forms import ModelForm, Textarea
from .models import Reviewbook

class ReviewForm(ModelForm) :
    def __init__(self, *args, **kwargs) :
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class':'form-check-input'})

    class Meta:
        model = Reviewbook
        fields = ['text', 'watchAgain']
        labels = {
            'text':('说说你看过之后的感受吧...'),
            'watchAgain':('是否会再次阅读'),
        }
        widgets = {
            'text':Textarea(attrs={'rows':4}),
        }