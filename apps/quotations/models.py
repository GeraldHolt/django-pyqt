from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _
import uuid
from uuid import UUID
from uuid import uuid4

from apps.accounts.list_of_countries import COUNTRIES
from apps.accounts.models import *

import sys
try:
	from django.db import models
except Exception:
	print("There was an error loading django modules. Make sure you have django installed")
	sys.exit()
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

ITEM_CODES = [
					('Item 1', 'Item 1'),
					('Item 2', 'Item 2'),
					('Item 3', 'Item 3'),
					('Item 4', 'Item 4'),
					('Item 5', 'Item 5'),
					('Item 6', 'Item 6'),
					('Item 7', 'Item 7'),
					('Item 8', 'Item 8'),
					('Item 9', 'Item 9'),
					('Item 10', 'Item 10'),
					('Item 11', 'Item 11'),
					('Item 12', 'Item 12'),
					('Item 14', 'Item 14'),
					('Item 15', 'Item 15'),
					('Item 16', 'Item 16'),
					('Item 17', 'Item 17'),
					('Item 18', 'Item 18'),
					('Item 19', 'Item 19'),
					('Item 20', 'Item 20'),
					('Item 21', 'Item 21'),
					('Item 22', 'Item 22'),
					('Item 23', 'Item 23'),

	]


#------------------------------------------------------------------------------------------------------------------------#
#Setting up general information
#------------------------------------------------------------------------------------------------------------------------#
class ProjectStructure(models.Model):
	Code            = models.CharField(max_length=15, blank=False, null=True, unique=True)
	Description     = models.CharField(max_length=50, blank=False, null=True )
	WBS             = models.CharField(max_length=6, blank=False, null=True)
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('Code',)
		verbose_name = ('Project Structures')

	def __str__(self):
		return f"{self.Code}"

#------------------------------------------------------------------------------------------------------------------------#
class ProjectSubStructure(models.Model):
	Code            = models.CharField(max_length=15, blank=False, null=True, unique=True)
	Description     = models.CharField(max_length=50, blank=False, null=True )
	WBS             = models.CharField(max_length=6, blank=False, null=True)
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('Code',)
		verbose_name = ('Project Sub-Structures')

	def __str__(self):
		return f"{self.Code}"

#------------------------------------------------------------------------------------------------------------------------#
class Discipline(models.Model):
	Code            = models.CharField(max_length=2, blank=False, null=True)
	Description     = models.CharField(max_length=50, blank=False, null=True)
	WBS             = models.ForeignKey(ProjectStructure, null = True, on_delete=models.SET_NULL)
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('Description',)
		verbose_name = ('Disciplines')
	
	def __str__(self):
		return f"{self.Code+' | '+self.Description}"

#------------------------------------------------------------------------------------------------------------------------#
class DocSubItem(models.Model):
	Code            = models.CharField(max_length=6, blank=False, null=True, unique=True)
	Description     = models.CharField(max_length=50, blank=False, null=True)
	WBS             = models.CharField(max_length=3, blank=False, null=True)
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('Description',)
		verbose_name = ('Document Sub-Items')

	def __str__(self):
		return self.Description
#------------------------------------------------------------------------------------------------------------------------#
class DocumentType(models.Model):
	Code            = models.CharField(max_length=3, blank=False, null=True, unique=True)
	Description     = models.CharField(max_length=60, blank=False, null=True)
	WBS             = models.ForeignKey(DocSubItem, null = True, on_delete=models.SET_NULL)
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('Code',)
		verbose_name = ('Document Types')

	def __str__(self):
		return f"{self.Code+' | '+self.Description}"

#------------------------------------------------------------------------------------------------------------------------#
class PurchaseCategory(models.Model):
	Code            = models.CharField(max_length=5, blank=False, null=True, unique=True)
	Category        = models.CharField(max_length=60, blank=False, null=True)
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('Code',)
		verbose_name = ('Purchase Categories')

	def __str__(self):
		return self.Category

#------------------------------------------------------------------------------------------------------------------------#
class DocumentStatus(models.Model):
	Code            = models.CharField(max_length=5, blank=False, null=True, unique=True)
	Status          = models.CharField(max_length=60, blank=False, null=True)
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('Status',)
		verbose_name = ('Document Status')

	def __str__(self):
		return self.Status

#------------------------------------------------------------------------------------------------------------------------#
class ItemCode(models.Model):
	itemCode        = models.CharField(max_length=15, blank=False, null=True, unique = True, verbose_name="Code")
	itemDescrp      = models.CharField(max_length=200, blank=True, null=True, verbose_name="Description")
	id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('itemCode',)
		verbose_name = ('Item Codes')

	def __str__(self):
	   
		template = f'{self.itemCode}'
		return template

#-----------------------------------------------------------------------------------------------------------------------#
class DesignActivity(models.Model):
	itemCode            = models.CharField(max_length=15, blank=False, null=True, unique = True)
	itemDescrp          = models.CharField(max_length=200, blank=True, null=True)
	id                  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('itemCode',)
		verbose_name = ('Design Acitivity')

	def __str__(self):
	   
		template = f'{self.itemDescrp}'
		return template

#-----------------------------------------------------------------------------------------------------------------------#
class SupplyCategory(models.Model):
	itemCode            = models.CharField(max_length=15, blank=False, null=True, unique = True, verbose_name="Code")
	category            = models.CharField(max_length=200, blank=True, null=True, verbose_name="Description")
	id                  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('itemCode',)
		verbose_name = ('Category')

	def __str__(self):
	   
		template = f'{self.category}'
		return template

#-----------------------------------------------------------------------------------------------------------------------#
class SupportActivity(models.Model):
	itemCode            = models.CharField(max_length=15, blank=False, null=True, unique = True, verbose_name="Code")
	itemDescrp          = models.CharField(max_length=200, blank=True, null=True, verbose_name="Description")
	id                  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	class Meta:
		ordering = ('itemCode',)
		verbose_name = ('Support Activity')

	def __str__(self):
	   
		template = f'{self.itemDescrp}'
		return template



#------------------------------------------------------------------------------------------------------------------------#
# Quotations
#-----------------------------------------------------------------------------------------------------------------------#
class MaterialCategory(models.Model):
	itemCode        = models.CharField(
										max_length=15, 
										blank=False, 
										null=True, 
										unique = True
										)
	itemDescrp      = models.CharField(
										max_length=200, 
										blank=True, 
										null=True
										)
	id              = models.UUIDField(
										default=uuid.uuid4, 
										unique=True, 
										primary_key=True, 
										editable=False
										)

	def __str__(self):
	   
		template = f'{self.itemCode}'
		return template

#-----------------------------------------------------------------------------------------------------------------------#
# Quotations
#-----------------------------------------------------------------------------------------------------------------------#
class Quotation(models.Model):
	
	DIVISION = [
		('ABA','ABACUS'),
		('HCE', 'HCE'),
	]

	WORKAREAS = [
		('Design Office', 'Design Office'),
		('Fabrication', 'Fabrication'),
		('Site Support', 'Site Support'),
		('Procurement', 'Procurement'),
	]

	QUOTE_STATUS =  [
		('Open','Open'),
		('Accepted','Accepted'),
		('Rejected','Rejected'),
		('Postponed', 'Postponed'),
		('Cancelled', 'Cancelled'),
	]

	PAYMENT_TERMS =  [
		('30days','30 days after date of invoice'),
		('COD','Cash on Delivery'),
		('progress','Progress payments'),
		('UPFRONT', 'Payment upfront'),
		('DEP1', 'Deposit with progress payments'),
		('DEP2', 'Deposit with final payments'),
	]	

	project    		= models.CharField(max_length=15, blank=True, null=True, unique=True, verbose_name = 'Quote Number')
	companyName     = models.ForeignKey(Company, null = True, on_delete=models.SET_NULL, verbose_name = 'Company')
	clientName      = models.ForeignKey(Contact, null = True, on_delete=models.SET_NULL, verbose_name = 'Contact')
	description     = models.CharField(max_length=300, blank=True, null=True, verbose_name = "Quote Title")
	division        = models.CharField(
										max_length=20, blank=False,
										choices = DIVISION, default = 'HCE', 
										null = True, verbose_name = 'Division'
										)
	date_created    = models.DateField(auto_now_add=True, blank=True,null = True, verbose_name = 'Quote Date')
	quote_status    = models.CharField(
										max_length=20,blank=False,
										choices = QUOTE_STATUS, 
										default='Open', 
										null = False, verbose_name = 'Status'
										)
	delivery        = models.CharField(
										max_length=15, 
										blank=True, 
										null=True, 
										verbose_name ='Delivery (weeks)'
										)
	delivery_details= models.CharField(
										max_length=150, 
										null = True, 
										blank=True,
										default = "Delivery time will be confirmed on receipt of official purchase order",
										verbose_name = 'Notes on Delivery'
										)
	quote_validity  = models.CharField(
										max_length=300, 
										blank=True, 
										null=True, 
										default = "60 days validity",
										verbose_name = 'Validity')
	payment_terms   = models.CharField(
										max_length=300, 
										blank=True,
										default = '30 days after date of invoice',  
										null = True, 
										verbose_name = 'Payment Terms'
										)
	compiler        = models.ForeignKey(
										TeamMember, 
										on_delete=models.CASCADE, 
										blank=True, 
										null=True
										)
	id              = models.UUIDField( 
										default=uuid.uuid4,
										unique=True, 
										primary_key=True, 
										editable=False
										)

	def __str__(self):
	   
		template = f'{self.quoteNumber}'
		return template

#-----------------------------------------------------------------------------------------------------------------------#
# Scope Of Work
#-----------------------------------------------------------------------------------------------------------------------#
class ScopeOfWork(models.Model):
	quoteNumber = models.CharField(max_length=15, unique = True, blank=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
	
	# def save(self, *args, **kwargs):
	#     is_new = not self.pk
	#     super().save(*args, **kwargs)
	#     if is_new:
	#         Child_1.objects.create(parent=self)

	
	def __str__(self):
		return str(self.id)

#-----------------------------------------------------------------------------------------------------------------------#
# Scope of Work Inclusions
#-----------------------------------------------------------------------------------------------------------------------#
class ScopeOfWorkInclusions(models.Model):
	"""
	A Class for Scope Inclusions.
	"""
	

	quoteNumber = models.ForeignKey(
								ScopeOfWork,
								related_name='quoteNumber1',
								on_delete=models.CASCADE
								)
	itemCode = models.CharField(   
								max_length=10,
								blank=False, null=False,
								choices=ITEM_CODES,
								verbose_name = "Item Codes" ,   
								)
	inclusion = models.CharField(   
								max_length=2000,
								blank=False, null=True,
								verbose_name = "Scope of Work" ,   
								)
	quantity = models.IntegerField(
								blank=False, 
								null=True,
								default = 1,
								verbose_name="Qty"
								)
	units = models.CharField(   
								max_length=10,
								blank=False, null=True,
								verbose_name = "Units"  
							)

	delivery_time = models.IntegerField(
								blank=False, 
								null=True,
								default = 1,
								verbose_name="Delivery"
								)

	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
	
	class Meta:
		ordering = ['itemCode']

	# def __str__(self):
	#     return str(self.itemCode)

#-----------------------------------------------------------------------------------------------------------------------#
# Scope of Work Exclusions
#-----------------------------------------------------------------------------------------------------------------------#
class ScopeOfWorkExclusion(models.Model):
	"""
	A Class for Scope exclusion
	"""

	quoteNumber = models.ForeignKey(
								ScopeOfWork,
								on_delete=models.SET_NULL,
								related_name='quoteNumber2',
								null=True,
								verbose_name = "Quote Number"
								)
	itemCode = models.CharField(   
								max_length=10,
								blank=False, null=False,
								choices=ITEM_CODES,
								verbose_name = "Item Codes" ,   
								)
	exclusion = models.CharField(
								max_length=2000, 
								blank=False, 
								null=True,
								verbose_name = "Exclusions")
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)    
	
	class Meta:
		ordering = ['itemCode']

	def __str__(self):
		return self.quoteNumber  

#-----------------------------------------------------------------------------------------------------------------------#
# Design Quotation
#-----------------------------------------------------------------------------------------------------------------------#
class DesignQuotation(models.Model):
	COMPLEXITY = [
		('EASY','EASY'),
		('AVERAGE', 'AVERAGE'),
		('COMPLEX', 'COMPLEX'),
	]

	quoteNumber     = models.ForeignKey(
								ScopeOfWork,
								on_delete=models.SET_NULL,
								related_name='quoteNumber3',
								null=True,
								verbose_name = "Quote Number"
								)
	activityDescr   = models.CharField(
									max_length=200, 
									blank=True, 
									null=True, 
									verbose_name = "Activity Description",
									)
	discipline      = models.ForeignKey(
									Discipline, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Disc.", 
									)
	activity        = models.ForeignKey(
									DesignActivity, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Activity Class"
									)
	resource        = models.ForeignKey(
									Resource, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Resource"
									)
	complexity      = models.CharField(
									max_length=20, 
									blank=False,
									choices = COMPLEXITY, 
									default = 'COMPLEX', 
									null = True, 
									verbose_name = "Complexity"
									)
	estHours        = models.IntegerField(
									verbose_name = " Est. Hrs"
									)

	actualHours        = models.IntegerField(
									null = True,
									blank = True, 
									verbose_name = "Actual. Hrs"
									)

	unitCost        = models.DecimalField(
									max_digits = 10,
									decimal_places = 2,
									blank = True, 
									null = True, 
									verbose_name = "Unit Cost"
									)
	markupMargin    = models.DecimalField(
									max_digits = 4, 
									decimal_places = 1, 
									verbose_name = "Mark-Up"
									)
	itemCode        = models.ForeignKey(
									ItemCode, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Item Code"
									)

	subTotalValue   = models.DecimalField(
									max_digits = 10,
									decimal_places = 2,
									blank = True, 
									null = True, 
									verbose_name = "Sub Total"
									)
	id              = models.UUIDField(
									default=uuid.uuid4, 
									unique=True, 
									primary_key=True, 
									editable=False)

	class Meta:
		ordering = ['itemCode']

	# def __str__(self):
	#     return self.quoteNumber   
	def get_subtotal(self):
		result = self.estHours*self.unitCost*(1+self.markupMargin/100)
		return result
   
	def save(self, *args, **kwargs):
		self.subTotalValue = self.get_subtotal()
		super(DesignQuotation, self).save(*args, **kwargs)

#-----------------------------------------------------------------------------------------------------------------------#
# Supply Quotation     
#-----------------------------------------------------------------------------------------------------------------------#
class SupplyQuotation(models.Model):
	UNITS = [
		('EACH','EACH'),
		('METER', 'METER'),
		('KG', 'KG'),
		]


	quoteNumber         = models.ForeignKey(
								ScopeOfWork,
								on_delete=models.SET_NULL,
								null=True,
								related_name='quoteNumber4',
								verbose_name = "Quote Number"
								)
	activityDescr       = models.CharField(
									max_length=200, 
									blank=True, 
									null=True, 
									verbose_name = "Supply Description",
									)
	materialCode        = models.ForeignKey(
									SupplyCategory, 
									on_delete=models.DO_NOTHING,
									null = False,
									verbose_name= "Category")
	supplier            = models.ForeignKey(
									Company, 
									on_delete=models.DO_NOTHING,
									null = False,
									verbose_name= "Supplier")
	supplierRef         = models.CharField(
									max_length=200, 
									blank=True, 
									null=True,
									verbose_name = 'Reference')
	handFee             = models.DecimalField(
									max_digits = 4, 
									decimal_places = 1,
									verbose_name = "Handl.Fee")
	quantity            = models.IntegerField(verbose_name= "Qty")
	unitsOfMeasure      = models.CharField(
									max_length=20, 
									choices = UNITS, 
									default = 'EACH', 
									blank=False, 
									null=True,
									verbose_name = "Units")
	unitCost            = models.DecimalField(max_digits = 10,decimal_places = 2, blank = True, null = True)
	markupMargin        = models.DecimalField(max_digits = 4, decimal_places = 1)
	supplierDisc        = models.DecimalField(max_digits = 4, decimal_places = 1)
	itemCode            = models.ForeignKey(
									ItemCode, 
									on_delete=models.DO_NOTHING,
									verbose_name = "Item Code")

	subTotalValue   = models.DecimalField(
									max_digits = 10,
									decimal_places = 2,
									blank = True, 
									null = True, 
									verbose_name = "Sub Total"
									)
	id                  = models.UUIDField(
									default=uuid.uuid4, 
									unique=True, 
									primary_key=True, 
									editable=False)

	class Meta:
		ordering = ['itemCode']

	# def __str__(self):
	#     return self.quoteNumber  
	 
	def get_subtotal(self):
		self.costValue = self.quantity*self.unitCost
		self.costValue = self.costValue-self.costValue*self.supplierDisc/100
		self.costValue = self.costValue*(1+self.handFee/100)
		self.quoteValue = self.costValue*(1+self.markupMargin/100)
		print(self.quoteValue)
		return (self.quoteValue)

	def save(self, *args, **kwargs):
		self.subTotalValue = self.get_subtotal()
		super(SupplyQuotation, self).save(*args, **kwargs)

#-----------------------------------------------------------------------------------------------------------------------#
# Support Quotation
#-----------------------------------------------------------------------------------------------------------------------#
class SupportQuotation(models.Model):
	COMPLEXITY = [
		('EASY','EASY'),
		('AVERAGE', 'AVERAGE'),
		('COMPLEX', 'COMPLEX'),
	]

	quoteNumber     = models.ForeignKey(
								ScopeOfWork,
								on_delete=models.SET_NULL,
								null=True,
								related_name='quoteNumber5',
								verbose_name = "Quote Number"
								)
	activityDescr   = models.CharField(
									max_length=200, 
									blank=True, 
									null=True, 
									verbose_name = "Activity Description",
									)
	discipline      = models.ForeignKey(
									Discipline, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Disc.", 
									)
	activity        = models.ForeignKey(
									DesignActivity, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Activity Class"
									)
	resource        = models.ForeignKey(
									Resource, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Resource"
									)
	complexity      = models.CharField(
									max_length=20, 
									blank=False,choices = COMPLEXITY, 
									default = 'COMPLEX', 
									null = True, 
									verbose_name = "Complexity"
									)
	estHours        = models.IntegerField(
									verbose_name = " Est. Hrs"
									)

	actualHours        = models.IntegerField(
									verbose_name = "Actual. Hrs"
									)

	unitCost        = models.DecimalField(
									max_digits = 10,
									decimal_places = 2,
									blank = True, 
									null = True, 
									verbose_name = "Unit Cost"
									)
	markupMargin    = models.DecimalField(
									max_digits = 4, 
									decimal_places = 1, 
									verbose_name = "Mark-Up"
									)
	itemCode        = models.ForeignKey(
									ItemCode, 
									on_delete=models.DO_NOTHING, 
									verbose_name = "Item Code"
									)

	subTotalValue   = models.DecimalField(
									max_digits = 10,
									decimal_places = 2,
									blank = True, 
									null = True, 
									verbose_name = "Sub Total"
									)
	id              = models.UUIDField(
									default=uuid.uuid4, 
									unique=True, 
									primary_key=True, 
									editable=False)

	class Meta:
		ordering = ['itemCode']

	# def __str__(self):
	#     return self.quoteNumber   
	def get_subtotal(self):
		result = self.estHours*self.unitCost*(1+self.markupMargin/100)
		return result
   
	def save(self, *args, **kwargs):
		self.subTotalValue = self.get_subtotal()
		super(SupportQuotation, self).save(*args, **kwargs)


#-----------------------------------------------------------------------------------------------------------------------#
# Temporay Workorders
#-----------------------------------------------------------------------------------------------------------------------#
class SupportQuotation(models.Model):
	pass