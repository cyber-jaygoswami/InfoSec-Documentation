from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']

        labels = {
            'first_name':'Name'
        }
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control form-control-lg'})

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'   
        labels = {
            'feedback_user':'Feedback'
        }

    def __init__(self,username,email,*args,**kwargs):
        super(FeedbackForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control form-control-lg'})
            if name == "name":
                field.widget.attrs.update({'value': username})
                field.widget.attrs.update({'readonly' : 'true'})
            if name == "email":
                field.widget.attrs.update({'value': email })
                field.widget.attrs.update({'readonly' : 'true'})