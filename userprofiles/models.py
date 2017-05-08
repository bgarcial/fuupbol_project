from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from .managers import UserManager
from django import forms

#Django Third packages

# Reason for use UserManager
# http://stackoverflow.com/questions/14723099/attributeerror-manager-object-has-no-attribute-get-by-natural-key-error-in

# Reasons for Manager Methods
# https://docs.djangoproject.com/en/1.9/topics/db/managers/
# https://docs.djangoproject.com/en/dev/ref/contrib/auth/#manager-methods

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    # Using PermissionsMixin
    # http://stackoverflow.com/questions/31370333/custom-django-user-object-has-no-attribute-has-module-perms

    POSITION_CHOICES = (
        ('Portero', u'Portero'),
        ('Defensa Central', u'Defensa Central'),
        ('Lateral Derecho', u'Lateral Derecho'),
        ('Lateral Izquierdo', u'Lateral Izquierdo'),
        ('Centrocampista', u'Centrocampista'),
        ('Media punta', u'Media punta'),
        ('Delantero', u'Delantero'),
    )

    SEX_CHOICES = (
        ('Masculino', "Masculino"),
        ('Femenino', "Femenino"),
    )


    username = models.CharField(
        _('username'),
        max_length=30,
        # primary_key=True,
        # unique=True,
        # null = True,
        # blank=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            RegexValidator(
                r'^[\w.ñ@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    # http://stackoverflow.com/questions/25239164/issue-with-createsuperuser-when-implementing-custom-user-model     required ...

    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    last_name=models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    age = models.PositiveSmallIntegerField(null=True)

    photo = models.ImageField(upload_to='avatars', blank=True, null=True)

    sex = models.CharField(
        choices=SEX_CHOICES,
        max_length=12,
        default=False,
        blank=True,
        verbose_name='Sexo',
        null=True,
    )

    is_player = models.BooleanField(default=False)

    team = models.ForeignKey(
        'games_information.Team',
        blank=True,
        null=True,
        verbose_name='Equipo en el que juega',
        related_name='players'

    )
    '''
    team = models.ManyToManyField(
        'games_information.Team',
        #null=True,
        #blank=True,
        verbose_name='Equipos en los que juega',

    )
    '''

    email = models.EmailField(max_length=254, primary_key=True)

    is_staff = models.BooleanField(
        default=True,
        help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # is_coach = models.BooleanField(default=False)
    # is_viewer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    position = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        )

    '''
    position = MultiSelectField(
        max_length=255,
        choices=POSITION_CHOICES,
        blank=False,
        null=True,

    )
    '''

    weight = models.DecimalField(max_digits=5,decimal_places=2, null=True)

    height = models.DecimalField(max_digits=5,decimal_places=2,null=True)

    nickname = models.CharField(max_length=64,blank=True)

    number_matches = models.PositiveIntegerField(null=True, blank=True)

    accomplished_matches = models.PositiveIntegerField(null=True,blank=True)

    time_available = models.CharField(max_length=255, blank=True)

    leg_profile = models.CharField(max_length=64, blank=True)

    number_shirt_preferred = models.CharField(max_length=255, blank=True)

    team_support = models.CharField(max_length=255, blank=True)

    player_preferred = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'auth_user'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def __str__(self):

        player_email_identifier = '%s' % (self.email)
        # return player_full_name.strip()
        return player_email_identifier
        # return "{},{},{}".format(self.nickname, self.first_name, self.last_name )

