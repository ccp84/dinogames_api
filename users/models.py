from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, firstname, lastname, password, **other_fields):
        """ 
        Creates and saves a superuser from the custom user model
        Based on the example here:
        https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, firstname, lastname, password, **other_fields)

    def create_user(self, email, username, firstname, lastname, password, **other_fields):
        """ 
        Creates a user instance from the custom user model 
        """

        if not username:
            raise ValueError('You must provide a username')

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          firstname=firstname, lastname=lastname, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    """ 
    Customised user model over writing the base user model.
    I have followed the django documentation here to create this model:
    https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model
    """
    ICON_CHOICES = (
        ("puzzle-piece", "Puzzle"),
        ("dice", "Dice"),
        ("chess", "Chess"),
        ("hat-wizard", "Wizard"),
        ("book-skull", "Pirate"),
    )
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    profilepic = models.ImageField(
        upload_to='profiles/', default='../defaultprofile_yqihgb.webp')
    profileicon = models.CharField(
        max_length=25, choices=ICON_CHOICES, default="dice")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstname', 'lastname']

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username
