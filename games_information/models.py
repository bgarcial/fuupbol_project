from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Field(models.Model):

    FIELD_TYPE_NATURE = 'Grama natural'
    FIELD_TYPE_ARTIFICIAL = 'Grama sintetica'

    FIELD_TYPE_CHOICES = (
        (FIELD_TYPE_NATURE, u'Grama natural'),
        (FIELD_TYPE_ARTIFICIAL, u'Grama sintetica'),
    )



    MODALITY_11 = 'Fútbol 11'
    MODALITY_8 = 'Fútbol 8'
    MODALITY_7 = 'Fútbol 7'
    MODALITY_6 = 'Fútbol 6'
    MODALITY_5 = 'Fútbol 5'
    # FUTSAL_MODALITY = 'Fútbol de salón'

    MODALITY_CHOICES = (
        (MODALITY_11, u'Fútbol 11'),
        (MODALITY_8, u'Fútbol 8'),
        (MODALITY_7, u'Fútbol 7'),
        (MODALITY_6, u'Fútbol 6'),
        (MODALITY_5, u'Fútbol 5'),
    )


    name = models.CharField(
        max_length=150,
        unique=True,
        #primary_key=True,

        )

    field_type = models.CharField(
        choices=FIELD_TYPE_CHOICES,
        default=False,
        blank=False,
        max_length=20,
        verbose_name=('Tipo de material/grama de la cancha')
    )



    modality = models.CharField(
        #choices=MODALITY_CHOICES,
        max_length=40,
        #default=True,
        blank=False,
        verbose_name='Modalidad'
    )
    photo = models.ImageField(upload_to='fields', blank=True, null=True)
    location = models.CharField(max_length=150, blank=False)



    def __str__(self):
        return '%s %s %s' % (self.name, self.field_type, self.location)
        #return '%s' % (self.name,)

class Team(models.Model):



    MODALITY_11 = 'Fútbol 11'
    MODALITY_8 = 'Fútbol 8'
    MODALITY_7 = 'Fútbol 7'
    MODALITY_6 = 'Fútbol 6'
    MODALITY_5 = 'Fútbol 5'
    #FUTSAL_MODALITY = 'Fútbol de salón'

    MODALITY_CHOICES = (

        (MODALITY_11, u'Fútbol 11'),
        (MODALITY_8, u'Fútbol 8'),
        (MODALITY_7, u'Fútbol 7'),
        (MODALITY_6, u'Fútbol 6'),
        (MODALITY_5, u'Fútbol 5'),
    )



    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=64,
                            blank=True,
                            primary_key=True,
                            unique=True,
                            db_index=True,)
    image = models.ImageField(upload_to='fields',blank=True, null=True, verbose_name='Imagen de la plantilla o escudo')

    players = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='players', blank=True,)

    '''
    modality = MultiSelectField(
        max_length=255,
        choices=MODALITY_CHOICES,
        blank=True,
        null=True

    )
    '''
    modality = models.CharField(
        choices=MODALITY_CHOICES,
        max_length=40,
        default=True,
        blank=False,
        verbose_name='Modalidad'
    )

    #listohome_field = models.ManyToManyField(Field)
    #place_origin = models.CharField(max_length=150, blank=True, verbose_name='Lugar de origen')

    place_origin = models.ForeignKey(
        'games_information.Field',
        verbose_name='Lugar de origen',

    )
    #players = Hacer un query de los jugadores
    game_day = models.CharField(max_length=150, blank=False, verbose_name='Reservas o frecuencia de juego')


    def __str__(self):
        return '%s' % (self.name)


class Match(models.Model):

    ACCEPTED_CHALLENGE = 'Aceptado'
    PENDING_CHALLENGE = 'Pendiente'
    CANCELLED_CHALLENGE = 'Cancelado'
    FICHAJE = 'Fichaje'


    STATUS_CHALLENGE_CHOICES = (

        (ACCEPTED_CHALLENGE, u'Aceptado'),
        (PENDING_CHALLENGE, u'Pendiente'),
        (CANCELLED_CHALLENGE, u'Cancelado'),
        (FICHAJE, u'Fichaje'),
    )


    home_team = models.ForeignKey(
        'games_information.Team',
        null=False,
        blank=False,
        verbose_name='Equipo local',
        related_name='hometeam'
    )

    away_team = models.ForeignKey(
        'games_information.Team',
        null=False,
        blank=False,
        verbose_name='Equipo visitante',
        #related_name=''
    )

    check_match_away_team = models.BooleanField(default=False)


    field = models.ForeignKey(
        'games_information.Field',
        null=False,
        blank=False,
        verbose_name='Lugar'

    )

    match_date = models.DateTimeField(default=timezone.now, null=True)

    status_challenge = models.CharField(
        choices=STATUS_CHALLENGE_CHOICES,
        max_length=40,
        default=True,
        blank=False,
        verbose_name='Estado del desafío'
    )
    home_team_players_acept = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='home_team_players_acept', blank=True,)
    away_team_players_acept = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='away_team_players_acept', blank=True,)
    home_team_players_cancel = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='home_team_players_cancel', blank=True,)
    away_team_players_cancel = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='away_team_players_cancel', blank=True,)

    def __str__(self):
        return "{} {} {} {}".format('Cotejo - ', self.home_team, 'vs.', self.away_team)
        #return '%s' % (self.name)

'''
class TrainingCompetitionCenter(models.Model):
    name = models.CharField(max_length=64,blank=True)
    location = models.CharField(max_length=150, blank=False)
    fields = models.ManyToManyField(Field,)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
'''
