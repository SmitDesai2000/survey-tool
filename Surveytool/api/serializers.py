from rest_framework import serializers
from .models import question,info


class infoSerializers(serializers.ModelSerializer):
    class Meta:                                    
        model=info            #Serializer model for info model
        #field=['id','name','age','Phone_No','city','created_at']
        fields='__all__'


class questionSerializers(serializers.ModelSerializer):
    class Meta:
        model=question              # Serializer model for question model
        #field=['Enter_your_question']
        fields='__all__'


