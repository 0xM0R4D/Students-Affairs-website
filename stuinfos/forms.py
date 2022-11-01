from dataclasses import fields
from django.forms import ModelForm
from.models import stu
from.models import course
from.models import coursestudent


class stuForm(ModelForm):
    class Meta:
        model = stu
        fields = '__all__'
        
  
class courseForm(ModelForm):
    class Meta:
        model = course
        fields = '__all__'
        
  
class coursestudentForm(ModelForm):
    class Meta:
        model = coursestudent
        fields = '__all__'
  

