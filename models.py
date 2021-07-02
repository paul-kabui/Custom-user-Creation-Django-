from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

#user manager
class CustomAccountManager(BaseUserManager):

    def create_user(self,email,user_name, first_name, last_name, telephone_No, password=None, is_active=True, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError(_("User must provide email address"))
        if not password:
            raise ValueError(_("User must provide a password"))
        email = self.normalize_email(email)
        user = self.model(
                        email=email,
                        user_name=user_name,
                        first_name=first_name,
                        last_name=last_name,
                        telephone_No=telephone_No
                        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.superuser = is_superuser
        user.save()
        return user

    def create_staffuser(self,email,user_name, first_name, last_name, telephone_No, password=None, is_active=True, is_staff=False, is_superuser=False):
        staffuser = self.create_user(
            email=email,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            telephone_No=telephone_No,
            password = password,
            is_staff = True
        )
        return staffuser

    def create_superuser(self,email,user_name, first_name, last_name, telephone_No, password=None, is_active=True, is_staff=False, is_superuser=False):
        superUser = self.create_user(
            email=email,
            user_name=user_name,
            telephone_No=telephone_No,
            first_name=first_name,
            last_name=last_name,
            password = password,
            is_staff = True,
            is_superuser= True
        )
        return superUser




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email Address"),max_length=225, unique=True, blank=False, null=False)
    user_name  = models.CharField(max_length=225, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225, blank=True, null=True)
    telephone_No = models.CharField(unique=True, max_length=25, blank=False, null=False)
    start_date = models.DateField(default=timezone.now)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    
    objects = CustomAccountManager() # account manager

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name", "telephone_No", "first_name", "last_name"]
    
    def __str__(self):
        return self.user_name
    
    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.superuser