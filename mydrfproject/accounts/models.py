from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    otp = models.CharField(_('one-time password'), max_length=6, null=True, blank=True)
    email_verified = models.BooleanField(_('email verified'), default=False)

    def __str__(self):
        return self.username
