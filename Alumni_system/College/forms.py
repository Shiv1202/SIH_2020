from django import forms
from Users.models import Colleges


class CollegeLoginForm(forms.ModelForm):
    class Meta:
        model = Colleges
        fields = [
            'college_name',
            'college_code',
            'college_pass'
        ]
        widgets = {
            'college_name' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'College Name',
                'id' : 'clgname',
                'required' : True
            }),
            'college_code' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'College Code',
                'id' : 'clgcode',
                'required' : True
            }),
            'college_pass' : forms.PasswordInput(attrs = {
                'class' : 'form-control',
                'id' : 'pwd',
                'placeholder' : 'Enter Password',
                'required' : True
            })
        }
   
    def clean(self):
        cleaned_data = super(CollegeLoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')