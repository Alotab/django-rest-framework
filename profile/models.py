from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.contrib.auth.models import Group, Permission
# from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# REACT NEW USER 
# function to create profile image path in the project
def get_profile_image_filepath(self, filename):
        return f"profile_images/{self.pk}/{'profile_image.png'}"


def get_default_profile_image():
    return "projectImages/default.jpg"

# class User(AbstractUser):
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(unique=True, blank=True)
#     profile_image = models.ImageField(max_length=100, upload_to=get_profile_image_filepath, null=True, default=get_default_profile_image)

#     def __str__(self) -> str:
#         return f"{self.first_name} {self.last_name}"
    
#     def get_profile_image_filename(self):
#         return str(self.profile_image)[str(self.profile_image).index(f"profile_images/{self.pk}/"):]


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True, blank=True)
    # profile_picture = models.ImageField(upload_to=get_profile_image_filepath, null=True, default=get_default_profile_image)
    profile_picture = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # def get_profile_image_filename(self):
    #     return str(self.profile_picture)[str(self.profile_picture).index(f"profile_images/{self.pk}/"):]









## function to create profile image path in the project
# def get_profile_image_filepath(self, filename):
#     return f"profile_images/{self.pk}/{'profile_image.png'}"

# def get_default_profile_image():
#     return "projectImages/default.jpg"


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_("email address"), unique=True) # make email field required and unique
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     profile_image = models.ImageField(max_length=100, upload_to=get_profile_image_filepath, null=True, default=get_default_profile_image)
#     location = models.CharField(max_length=100, blank=True)
#     date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     groups = models.ManyToManyField(
#         Group, 
#         verbose_name=_('groups'), 
#         blank=True, 
#         help_text=_('The groups this user belongs to. A user will get a persmission granted to each of their groups'),
#         related_name='customuser_group',
#         related_query_name='user',
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name="customuser_user_permissions",
#         related_query_name="user",
#     )
        


#     # 
#     USERNAME_FIELD = "email"  # set this field which defines the unique identifier for the User model to "email"
#     REQUIRED_FIELDS = [] 

#     objects = CustomUserManager()  # specify that all objects for the class come from the CustomeUserManager

#     def __str__(self) -> str:
#         return f"{self.first_name} {self.last_name}"
    
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
    
#     def has_module_perms(self, app_label):
#         return True
    
#     def get_short_name(self):
#         return f"{self.first_name}"
    
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
    
#     # change the name of profile image to the default name
#     def get_profile_image_filename(self):
#         return str(self.profile_iamge)[str(self.profile_image).index(f"profile_images/{self.pk}/"):]



