from .models import User

from rest_framework import serializers

from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(LoginSerializer):
    username = None

class RegisterSerializer(RegisterSerializer):
    
    nickname = serializers.CharField(
        required=True,
        max_length=20,
    )

    username = None

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname','')
        return data_dict
        
    