from pyexpat import model
from rest_framework import serializers
from App.models import Ebook,User

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = ('title','author','genre','review','favorite')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
    def create(self,validate_data):
        user = User.objects.create(username = validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()
        return user