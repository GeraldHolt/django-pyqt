from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.accounts.list_of_countries import COUNTRIES

import uuid
from uuid import UUID
from uuid import uuid4

import sys
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Make sure you have django installed")
    sys.exit()
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


#------------------------------------------------------------------------------------------------------------------------#
# Company Data
#------------------------------------------------------------------------------------------------------------------------#
class Company(models.Model):
    COMPANY_OPERATION_STATUS = [
                                ('Operational','Operational'),
                                ('Closed','Closed'),
                                ]

    compID              = models.CharField(max_length=15, blank=False, null=True, unique = True, verbose_name='Company Code')
    companyName         = models.CharField(max_length=200, blank=False, null=True, verbose_name = 'Company Name')
    date_created        = models.CharField(max_length=50, null = True, verbose_name = 'Date Created')
    date_latest_quote   = models.CharField(max_length=50,blank=True, null = True, verbose_name = 'Latest Quotation')
    date_latest_order   = models.CharField(max_length=50,blank=True, null = True, verbose_name = 'Latest Order')
    company_status      = models.CharField(max_length= 11, choices=COMPANY_OPERATION_STATUS, default='Operational', verbose_name='Status')
    customer            = models.CharField(max_length=50,default = True, verbose_name='Customer')
    supplier            = models.CharField(max_length=50,default = False, verbose_name = 'Supplier')
    company_reg_no      = models.CharField(max_length=50, blank=True, null=True, verbose_name = 'Registration Number')
    VAT_no              = models.CharField(max_length=50, blank=True, null=True, verbose_name = 'VAT Number')
    companyWeb          = models.CharField(max_length=50,blank=True, null=True, verbose_name = 'Company Website' )
    #companyLogo         = models.FileField(blank=True, null=True, upload_to='assets/images/')
    address1            = models.CharField(max_length=200, blank=True, null=True, verbose_name = 'Address 1')
    address2            = models.CharField(max_length=200, blank=True, null=True, verbose_name = 'Address 2')
    city                = models.CharField(max_length=200, blank=True, null=True, verbose_name = 'City')
    postalCode          = models.CharField(max_length=20, blank=True, null=True, verbose_name = 'Postal Code')
    province            = models.CharField(max_length=200, blank=True, null=True, verbose_name = 'Province')
    country             = models.CharField(max_length=200, choices = COUNTRIES, default='South Africa', verbose_name = 'Country')
    businessPhone       = models.CharField(max_length=100,blank=True, null=True, verbose_name = 'Business Phone')
    companyEmail        = models.CharField(max_length=100,blank=True, null=True, verbose_name = 'Company Email')
    id                  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ('companyName',)
        verbose_name = ('Company')
        verbose_name_plural = ('Companies')

    def __str__(self):
        return f"{self.companyName}"


def company_created_handler(sender, instance, created,*args, **kwargs):
    print(args, kwargs)

post_save.connect(company_created_handler, sender = Company)

#------------------------------------------------------------------------------------------------------------------------#
# Contatcts
#------------------------------------------------------------------------------------------------------------------------#

class Contact(models.Model):
    contID          = models.CharField(max_length=15, blank=False, null=True, unique = True, verbose_name='Contact ID')

    lastName        = models.CharField(
                                        max_length=200, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name = 'Last Name'
                                        )
    firstName       = models.CharField(
                                        max_length=200, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name = 'First Name'
                                        )
    companyName     = models.ForeignKey(
                                        Company, 
                                        null = True, 
                                        on_delete=models.SET_NULL, 
                                        related_name = "clients", 
                                        verbose_name = 'Company Name'
                                        )
    contactEmail    = models.EmailField(
                                        blank=True, 
                                        null=True, 
                                        verbose_name = 'Contact Email'
                                        )
    jobTitle        = models.CharField(
                                        max_length=200, 
                                        blank=True, 
                                        null=True, 
                                        verbose_name = 'Work Title'
                                        )
    contactBusPhone = models.CharField(
                                        max_length=100,
                                        blank=True, 
                                        null=True, 
                                        verbose_name = 'Business Phone'
                                        )
    contactMobile   = models.CharField(
                                        max_length=100,
                                        blank=True, 
                                        null=True, 
                                        verbose_name = 'Mobile Phone'
                                        )
    date_of_birth   = models.CharField(
                                        max_length=100,
                                        null=True, 
                                        verbose_name='Date of Birth'
                                        )
    id              = models.UUIDField(
                                        default=uuid.uuid4, 
                                        unique=True, 
                                        primary_key=True, 
                                        editable=False)

    class Meta:
        ordering = ('firstName','lastName')
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')
    
    # def __str__(self):
    #     return f"{self.firstName +' '+ self.lastName}"

METHOD = {
    ('Phone', 'Phone'),
    ('Email', 'Email'),
    ('Website', 'Website'),
    ('LinkedIn', 'LinkedIn')
}
# class ContactHistory(models.Model):
#     logDate = models.DateTimeField(auto_now_add=True, verbose_name="Contact Date/Time")
#     contactName = models.ForeignKey(Contact, null = True, on_delete=models.PROTECT, verbose_name = 'Contact Name')
#     title = models.CharField(max_length=300, blank=True, null=True, verbose_name = "Log Title")
#     method = models.CharField(max_length=20, choices = METHOD, verbose_name = 'Method')
#     description = models.TextField(verbose_name="Logging Information")

#------------------------------------------------------------------------------------------------------------------------#
# Division Data
#------------------------------------------------------------------------------------------------------------------------#
class Division(models.Model):
    divisionCode    = models.CharField(
                                        max_length=20, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="Division Code"
                                        )
    divisionName    = models.CharField(
                                        max_length=100, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="Division Name"
                                        )
    companyLogo     = models.ImageField(
                                        upload_to='assets/images/', 
                                        blank=True, null=True, 
                                        verbose_name="Division Logo"
                                        )
    regNumber       = models.CharField(
                                        max_length=30, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="Registration Number"
                                        )
    vatNumber       = models.CharField(
                                        max_length=30, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="VAT Number"
                                        )
    address1        = models.CharField(
                                        max_length=50, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="Address Line 1"
                                        )
    address2        = models.CharField(
                                        max_length=50, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="Address Line 2"
                                        )
    city            = models.CharField(
                                        max_length=50, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="City"
                                        )
    province        = models.CharField(
                                        max_length=50, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="Province"
                                        )
    country         = models.CharField(
                                        max_length=200, 
                                        choices = COUNTRIES, 
                                        blank=True, 
                                        null=True, 
                                        verbose_name="Country"
                                        )
    contactNumber   = models.CharField(
                                        max_length=50, 
                                        blank=False, 
                                        null=True, 
                                        verbose_name="Phone Number"
                                        )
    webSite         = models.CharField(
                                        max_length=150, 
                                        blank=True, 
                                        null=True, 
                                        verbose_name="Web Site"
                                        )
    id              = models.UUIDField(
                                        default=uuid.uuid4, 
                                        unique=True, 
                                        primary_key=True, 
                                        editable=False
                                        )

    def __str__(self):
        return self.divisionName

#------------------------------------------------------------------------------------------------------------------------#
# Resources and Rates
#------------------------------------------------------------------------------------------------------------------------#

class Resource(models.Model):
    resourceID          = models.CharField(
                                            max_length=15, 
                                            blank=False, 
                                            null=True, 
                                            unique=True, 
                                            verbose_name="Code"
                                            )
    resourceName        = models.CharField(
                                            max_length=50, 
                                            blank=False, 
                                            null=True, 
                                            verbose_name="Resource",
                                            )
    easyRate            = models.DecimalField(
                                            max_digits = 10,
                                            decimal_places = 2, 
                                            verbose_name="Easy"
                                            )
    averageRate         = models.DecimalField(
                                            max_digits = 10,
                                            decimal_places = 2, 
                                            verbose_name="Average"
                                            )
    complexRate         = models.DecimalField(
                                            max_digits = 10,
                                            decimal_places = 2, 
                                            verbose_name="Complex"
                                            )
    id                  = models.UUIDField(
                                            primary_key=True, 
                                            default=uuid.uuid4, 
                                            editable=False
                                            ) 
    
    class Meta:
        ordering = ["resourceID"]

    def __str__(self):
        return f"{self.resourceName}"
  

#------------------------------------------------------------------------------------------------------------------------#
# Team Member Detail
#------------------------------------------------------------------------------------------------------------------------#
class TeamMember(models.Model):
    user                = models.OneToOneField(
                                            User,
                                            related_name='employee_profile', 
                                            on_delete=models.CASCADE, 
                                            verbose_name='Team Member'
                                            )
    designation         = models.ForeignKey(
                                            Resource,
                                            on_delete=models.CASCADE, 
                                            verbose_name = "Designation"
                                            )
    phoneNumber         = models.CharField(
                                            max_length=15, 
                                            verbose_name=_('Phone Number')
                                            )
   
    companyName         = models.CharField(
                                            max_length=50, 
                                            blank=True, 
                                            null=True, 
                                            default = "HCE/ABACUS",
                                            verbose_name="Company Name")
    id                  = models.UUIDField(
                                            primary_key=True, 
                                            default=uuid.uuid4, 
                                            editable=False
                                            ) 

    def __str__(self):
        return f"{self.user.first_name}" + ' ' + f"{self.user.last_name}"


