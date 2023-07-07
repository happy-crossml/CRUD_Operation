
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    course_choices = (
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('BBA', 'BBA'),
        ('MBA', 'MBA'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
    )
    
    course = forms.ChoiceField(choices=course_choices, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['name', 'email', 'course', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }
  