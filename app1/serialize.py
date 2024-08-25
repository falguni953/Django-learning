from .models import *
from rest_framework import serializers

class userregister_serialize(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ['id','name','email','mob','password']


# new model serialize with new options..
class serialize_user(serializers.ModelSerializer):
    class Meta:
        model = register
        # if we want to serialize all the fields then we can use this below..
        fields = '__all__'
         
        # if we want to add specific fields the we can use below..
        # fields = ['id','name','email']

        # suppose we have 20 fields in a model and we only want to remove any
        # 1 or 2 fields then we can use this below code..
        # exclude = ['password'] 

    def validate(self, data):

        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({'error':"the data in name can't be numaric!!.."})
        return data
    

class serialize_category(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class serialize_products(serializers.ModelSerializer):
    category = serialize_category()
    class Meta:
        model = product
        fields = '__all__'

