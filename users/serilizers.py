from rest_framework import serializers
from .models import CustomUser
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'address', 'phone_number']
        
        def create(self, validated_data):
            user = CustomUser.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
                email=validated_data.get('email', ''),
                address=validated_data.get('address', ''),
                phone_number=validated_data.get('phone_number', '')
            )
            return user