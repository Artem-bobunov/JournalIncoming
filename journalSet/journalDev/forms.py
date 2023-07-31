from django.forms import *
from .models import Journal

class restSerializer(ModelForm):
    
    class Meta:
        model = Journal
        fields = "__all__"
        widgets = {
                    'reg':TextInput(attrs={'class': 'form-control','placeholders':'Регистрационный номер'}),
                    'dateInput': TextInput(attrs={'class': 'form-control','type': 'date','format':'%d.%m.%Y'}),
                    'otKogo': TextInput(attrs={'class': "form-control"}),
                    'vxnumber': TextInput(attrs={'class': "form-control",}),
                    'isxnumber': TextInput(attrs={'class': "form-control"}),
                    'summary': TextInput(attrs={'class': "form-control"}),
                    'executor': Select(attrs={'class': "form-control"}),
                    'perfomance': Select(attrs={'class': "form-control"}),
                    'control': TextInput(attrs={'class': "form-control"}),
                    'answertMail': TextInput(attrs={'class': "form-control"}),
                    'note': TextInput(attrs={'class': "form-control"}),
                    'nd': Select(attrs={'class': "form-control"}),
        }