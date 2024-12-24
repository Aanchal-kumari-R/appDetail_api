from rest_framework import serializers 
from .models import AppData 

class AppSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = AppData  
        fields = ['id','app_name','version','description']