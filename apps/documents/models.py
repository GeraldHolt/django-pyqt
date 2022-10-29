from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from pytz import common_timezones_set
from apps.accounts.list_of_countries import COUNTRIES

import uuid
from uuid import UUID
from uuid import uuid4

import sys

# from apps.accounts.models import Quotation

try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Make sure you have django installed")
    sys.exit()
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

#------------------------------------------------------------------------------------------------------------------------#
# Site Conditions
#------------------------------------------------------------------------------------------------------------------------#
class SiteConditions(models.Model):
    pass
    # project = models.ForeignKey(
    #                             Quotation,
    #                             null = True, 
    #                             on_delete=models.SET_NULL, 
    #                             verbose_name = 'Project'
    #                             )
    

#------------------------------------------------------------------------------------------------------------------------#
# Mass Balance
#------------------------------------------------------------------------------------------------------------------------#
class MassBalance(models.Model):
    project             = models.CharField(
                                            max_length=50,
                                            blank=True,
                                            null=True,
                                            verbose_name="Project Number"
                                            )

    stream                  = models.CharField(
                                max_length=15,
                                unique = True,
                                verbose_name='Stream Number'
                                )

    stream_descrip          = models.CharField(
                                max_length=50,
                                blank=True,
                                null=True,
                                verbose_name='Stream Description'
                                )
    area                    = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Area')

    total_mass_flow         = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Total Mass Flow t/h'
                                
                                )

    solid_mass_flow         = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Solid Mass Flow t/h'
                                )

    water_mass_flow         = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Water Mass Flow t/h'
                                )

    slurry_mass_flow         = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Slurry Mass Flow m3/h'
                                )

    percentage_moisture     = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Percentate moisture wt %'
                                )

    percentage_solids       = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Percentate solids wt %'
                                )

    solids_density           = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Solids Density t/m3'
                                )

    water_density            = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Water Density t/m3'
                                )

    solids_bulk_density      = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Solids Bulk Density t/m3'
                                )

    slurry_density           = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='Slurry Density t/m3'
                                )
    solid_particle_size_P100 = models.CharField(
                                max_length=10,
                                blank=True,
                                null=True,
                                verbose_name='P100 (mm)'
                                )
    comments                 = models.CharField(
                                max_length=200,
                                blank=True,
                                null=True,
                                verbose_name='Notes'
                                )

    updated                = models.CharField(
                                max_length=200,
                                blank=True,
                                null=True,
                                verbose_name='Notes'
                                )

    id                      = models.UUIDField(
                                default=uuid.uuid4,
                                unique=True,
                                primary_key=True,
                                editable=False
                                )


                        