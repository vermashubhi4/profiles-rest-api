from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """"Creates User Profile"""
        if not email:
            raise ValueError("Users must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self,email,name, password):
        """Create and save a new super user profile"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for the users in the system"""
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the User"""
        return self.name

    def get_short_name(self):
        """Retrieve full name of the User"""
        return self.name

    def __str__(self):
        """Retrieve string representation of our user"""
        return self.email
