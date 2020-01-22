import datetime
from django import forms
from .models import Alumni_User, Colleges, Permanent_User



college_choices = [
    ('college name', 'College Name'),
    ('test1', 'Test1'),
    ('test2', 'Test2'),
    ('test3', 'Test3')
]


year_choices = [
    ('batch', 'Batch')
] 
 
for i in range(1990, datetime.date.today().year + 1):
    year_choices.append((str(i), i))
    
class RegistrationForm(forms.ModelForm):
    
    c_password = forms.CharField(max_length = 20, min_length = 8,
    widget = forms.PasswordInput(
        attrs = {'class' : 'form-control',
                'id' : 'rpwd',
                'placeholder' : 'Confirm Password'}))
    
    class Meta:
        model = Alumni_User
        fields = [
            'name',
            'email',
            'college_name',
            'graduation_yr',
            'roll_no',
            'password'
        ]
        widgets = {
            'name' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Name',
                'id' : 'uname',
                'required' : True
            }),
            'email' : forms.EmailInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'E-mail',
                'id' : 'uname'
            }),
            'college_name' : forms.Select(attrs = {
                'class' : 'form-control',
                'id' : 'College',
                'required' : True
            }, choices = college_choices),
            'graduation_yr' : forms.Select(attrs = {
                'class' :  'form-control form-control2',
                'id' : 'batch',
                'placeholder' : 'Batch',
                'required' : True
            }, choices = year_choices),
            'roll_no' : forms.NumberInput(attrs = {
                'class' : 'form-control form-control3',
                'id' : 'rollno',
                'placeholder' : 'Roll No.'
            }),
            'password' : forms.PasswordInput(attrs = {
                'class' : 'form-control',
                'id' : 'pwd',
                'placeholder' : 'Enter Password',
                'required' : True
            })
        }
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        c_password = cleaned_data.get("c_password")
        if password != c_password:
            raise forms.ValidationError(
            "Password Does not match."
        )

class LogInForm(forms.ModelForm):
    class Meta:
        model = Alumni_User
        fields = [
            'email',
            'password'
        ]
        widgets = {
            'email' : forms.EmailInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'E-mail',
                'id' : 'uname'
            }),
            'password' : forms.PasswordInput(attrs = {
                'class' : 'form-control',
                'id' : 'pwd',
                'placeholder' : 'Enter Password',
                'required' : True
            })
        }
   
    def clean(self):
        cleaned_data = super(LogInForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

class ForgetForm(forms.ModelForm):

    class Meta:
        model = Permanent_User           #Plz change it with permanent table
        fields = [
            'email'
        ]
        widgets = {
            'email' : forms.EmailInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'E-mail',
                'id' : 'uname'
            })}

class PasswordUpdationForm(forms.ModelForm):
    
    c_password = forms.CharField(max_length = 20, min_length = 8,
    widget = forms.PasswordInput(
        attrs = {'class' : 'form-control',
                'id' : 'rpwd',
                'placeholder' : 'Confirm Password'}))
    
    class Meta:
        model = Permanent_User                         #Plz change it with permanent table
        fields = [
            'password'
        ]
        widgets = {
            'password' : forms.PasswordInput(attrs = {
                'class' : 'form-control',
                'id' : 'pwd',
                'placeholder' : 'Enter Password',
                'required' : True
            })
        }
    def clean(self):
        cleaned_data = super(PasswordUpdationForm, self).clean()
        password = cleaned_data.get("password")
        c_password = cleaned_data.get("c_password")
        if password != c_password:
            raise forms.ValidationError(
            "Password Does not match."
        )