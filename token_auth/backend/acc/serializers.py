from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
        extra_kwargs = {
            "password":{
                'write_only':True,'style': {'input_type': 'password'}
            },
        }

    def validate(self, data):
        email = data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already in use.")
        return data

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)

    #     # Perform additional actions after user creation if needed
    #     # For example, send a welcome email, create a related profile, etc.


# extra_kwargs={
#             "password":{
#                 'write_only':True,'style': {'input_type': 'password'}
#             },
#             "email":{
#                 "validators":[
#                     UniqueValidator(
#                         queryset=User.objects.all()
#                     )
#                 ],
#             }
#         },
        
class UserAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")

        user = authenticate(username=username, password=password)

        if user is not None:
            return {'user': user}
        else:
            raise serializers.ValidationError("Invalid credentials")