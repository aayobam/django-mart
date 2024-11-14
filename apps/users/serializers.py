from rest_framework import serializers
from apps.users.models import CustomUser
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainSerializer


class UserSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=120,
        min_length=8,
        write_only=True,
        help_text="must not be less than 8",
        style={"input_type": "password"},
        required=True,
    )
    confirm_password = serializers.CharField(
        max_length=120,
        min_length=8,
        write_only=True,
        help_text="must match password",
        style={"input_type": "password"},
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "phone_no",
            "email",
            "password",
            "confirm_password",
            "detail_url",
        ]

    def get_detail_url(self, obj):
        return obj.get_absolute_url()

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email already exist in our database.")
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("confirm_password"):
            raise ValidationError("Passwords do not match.")
        return attrs

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for key, value in validated_data.items():
            setattr(key, value, instance)

        if password is None:
            instance.set_password(password)
        instance.save()
        return instance


class EmailTokenObtainSerializer(TokenObtainSerializer):
    username_field = CustomUser.EMAIL_FIELD


class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
    """
    Generates refresh token for users and returns new access token
    """

    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        user = UserSerializer(self.user)
        data["user"] = user.data
        return data
