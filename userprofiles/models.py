from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from .managers import UserManager

#Django Third packages
from multiselectfield import MultiSelectField

# Reason for use UserManager
# http://stackoverflow.com/questions/14723099/attributeerror-manager-object-has-no-attribute-get-by-natural-key-error-in

# Reasons for Manager Methods
# https://docs.djangoproject.com/en/1.9/topics/db/managers/
# https://docs.djangoproject.com/en/dev/ref/contrib/auth/#manager-methods

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # Using PermissionsMixin
    # http://stackoverflow.com/questions/31370333/custom-django-user-object-has-no-attribute-has-module-perms

    GOALKEEPER_POSITION = 'GOALKEEPER'
    CENTRAL_DEFENDER_POSITION = 'DEFENDER'
    RIGHT_DEFENDER_POSITION = 'RIGHT_DEFENDER'
    LEFT_DEFENDER_POSITION = 'LEFT_DEFENDER'
    MIDFIELDER_FORWARD_POSITION = 'MIDFIELDER_FORWARD'
    MIDFIELDER_CENTER_POSITION = 'MIDFIELDER_CENTER'
    MIDFIELDER_DEFENSIVE_POSITION = 'MIDFIELDER_DEFENSIVE'
    MIDFIELDER_LEFT_POSITION = 'MIDFIELDER_LEFT'
    MIDFIELDER_RIGHT_POSITION = 'MIDFIELDER_RIGHT'
    FORWARD_CENTER_POSITION = 'FORWARD_CENTER'
    FORWARD_RIGHT_POSITION = 'FORWARD_RIGHT'
    FORWARD_LEFT_POSITION = 'FORWARD_LEFT'
    SECOND_FORWARD_POSITION = 'SECOND_FORWARD'

    POSITION_CHOICES = (
        (GOALKEEPER_POSITION, u'Portero - PT'),
        (CENTRAL_DEFENDER_POSITION, u'Defensa Central - DFC'),
        (RIGHT_DEFENDER_POSITION, u'Defensa Lateral Derecho - LD'),
        (LEFT_DEFENDER_POSITION, u'Defensa Lateral Izquierdo- LI'),
        (MIDFIELDER_FORWARD_POSITION, u'Media Punta (por el centro adelantado) - MP'),
        (MIDFIELDER_CENTER_POSITION, u'Medio Centro (en el centro) - MC'),
        (MIDFIELDER_DEFENSIVE_POSITION, u'Medio Campo Defensivo - MCD'),
        (MIDFIELDER_LEFT_POSITION, u'Medio Izquierda - MI'),
        (MIDFIELDER_RIGHT_POSITION, u'Medio Derecha - MD'),
        (FORWARD_CENTER_POSITION, u'Delantero Centro (siempre pendientes de meter goles) - DC'),
        (FORWARD_RIGHT_POSITION, u'Extremo Derecho (los más adelantados por la banda) - ED'),
        (FORWARD_LEFT_POSITION, u'Extremo Izquierdo  - EI'),
        (SECOND_FORWARD_POSITION, u'Segundo Delantero - SD'),
    )

    SEX_CHOICES = (
        ('Masculino', "Masculino"),
        ('Femenino', "Femenino"),
    )

    username = models.CharField(
        max_length=15,
        unique=True,
        db_index=True,
        primary_key=True
    )
    # http://stackoverflow.com/questions/25239164/issue-with-createsuperuser-when-implementing-custom-user-model     required ...

    first_name=models.CharField(max_length=50, blank=False,)

    last_name=models.CharField(max_length=50, blank=False,)

    age = models.PositiveSmallIntegerField(null=True)

    photo = models.ImageField(upload_to='avatars')

    sex = models.CharField(
        choices=SEX_CHOICES,
        max_length=12,
        default=False,
        blank=False,
        verbose_name='Sexo'
    )

    is_player = models.BooleanField(default=False)



    team = models.ForeignKey(
        'games_information.Team',
        null=True,
        blank=True,
        verbose_name='Equipo en el que juega',

    )
    '''
    team = models.ManyToManyField(
        'games_information.Team',
        #null=True,
        #blank=True,
        verbose_name='Equipos en los que juega',

    )
    '''

    email = models.EmailField(max_length=254, unique=True)


    is_staff = models.BooleanField(
        default=True,
        help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    #is_coach = models.BooleanField(default=False)
    #is_viewer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    position = MultiSelectField(
        max_length=255,
        choices=POSITION_CHOICES,
        blank=False,

    )

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

        player_full_name = '%s %s %s' % (self.nickname,self.first_name, self.last_name)
        return player_full_name.strip()
        #return "{},{},{}".format(self.nickname, self.first_name, self.last_name )

