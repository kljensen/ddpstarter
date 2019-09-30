from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    # This is our custom user model. See
    # https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    # for why we want to do this. Our user has all the columns
    # in the AbstractUser class (the Django default user type)
    # in addition to the columns we put into the BaseModel class.
    pass


class AwayPlan(BaseModel):
    # Old model:
    # CREATE TABLE 'simple' (
    # 'uid' integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    # 'byedate' date NOT NULL,
    # 'hidate' date NOT NULL,
    # 'triptitle' text NOT NULL,
    # 'userID' INTEGER, 'timestamp'  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    # 'certainty' text);

    CERTAINTY_CHOICES = ['LOW', 'MEDIUM', 'HIGH']
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    start_date = models.DateTimeField(
        help_text="The date on which your time away will start",
        verbose_name="trip start date",
    )
    end_date = models.DateTimeField(
        help_text="The date on which you will return home",
        verbose_name="trip end date",
    )
    title = models.TextField(
        help_text="A title for this trip away",
        max_length=150,
        verbose_name="trip title",
    )
    # This will store 0, 1, 2 in the database for "LOW", "MEDIUM", and "HIGH"
    certainty = models.PositiveIntegerField(
        help_text="The certainty with which you'll actually go on your trip",
        choices=enumerate(CERTAINTY_CHOICES),
        verbose_name="trip certainty",
    )
