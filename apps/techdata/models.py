from random import choices
from telnetlib import SGA
from turtle import width
from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth import get_user_model
from matplotlib.projections import projection_registry
from pyparsing import condition_as_parse_action
from apps.quotations.models import MaterialCategory
from apps.accounts.list_of_countries import COUNTRIES
import uuid
from uuid import UUID
from uuid import uuid4
from apps.techdata.lookuptables import *

import sys
try:
	from django.db import models
except Exception:
	print("There was an error loading django modules. Make sure you have django installed")
	sys.exit()
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


#------------------------------------------------------------------------------------------------------------------------#
# Steel Sections
#------------------------------------------------------------------------------------------------------------------------#
class SAISCSteelSections(models.Model):

	designation = models.CharField(max_length=25, blank=False, null=True, unique = True, verbose_name='Designation')
	profile = models.CharField(max_length=30, blank=False, null=True, verbose_name = 'Profile Type')
	unit_mass = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Unit Mass (kg/m)')
	h = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Height (mm)')
	b = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Width (mm)')
	c = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Lip Height (mm)')
	d = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Diameter (mm)')
	tw = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Wed / Wall Thickness (mm)')
	tf = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Flange Thickness (mm)')
	r1 = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Web Radius (mm)')
	r2 = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Flange Radius (mm)')
	b1 = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Taper Centre (mm)')
	Beta = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Taper Flange Angle (deg)')
	A = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Cross sectional Area (mm2)')
	Ix = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Second Moment of Area about x-x (mm4)')
	Zx = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Sectional Modulus about x-x (mm3)')
	rx = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Radius of Gyration about x-x (mm)')
	Iy = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Second Moment of Area about y-y (mm4)')
	Zy = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Sectional Modulus about y-y (mm3)')
	ry = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Radius of Gyration about y-y (mm)')
	Iu = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Second Moment of Area about u-u (mm4)')
	Zu = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Sectional Modulus about u-u (mm3)')
	ru = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Radius of Gyration about u-u (mm)')
	Iv = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Second Moment of Area about v-v (mm4)')
	Zv = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Sectional Modulus about v-v (mm3)')
	rv = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Radius of Gyration about v-v (mm)')
	J = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Polar Moment (mm4)')
	Cw = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Warping Constant (mm6)')
	Zplx = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Plastic Sectional Modulus about x-x (mm3)')
	Zply = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Plastic Sectional Modulus about y-y (mm3)')
	h_tf = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Height to Flange Thickness Ratio')
	hw = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Internal Height (mm)')
	ac = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Shear Centre (mm)')
	ax = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Shear Centre (mm)')
	ay = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Shear Centre (mm)')
	alpha = models.CharField(max_length=30, blank=True, null = True, verbose_name = '(deg)')
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


	def __str__(self):
		return f"{self.designation}"


#------------------------------------------------------------------------------------------------------------------------#
# SANS 1123 Plate Flanges
#------------------------------------------------------------------------------------------------------------------------#
class SANSPlateFlanges(models.Model):

	designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
	nom_bore = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Nominal Bore Diameter')
	flange_mass = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Flange Mass (kg)')
	pressureRating = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Flange Pressure Rating (kPa)')
	flange_type = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Flange Type Configuration')
	pipeOutsideDia = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Pipe Outside Diameter (mm)')
	flangeOutsideDia = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Flange Outside Diameter (mm)')
	flangeThickness = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Flange Thickness (mm)')
	raisedFaceDia = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Raised Face Diameter (mm)')
	raisedFaceThick = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Raised Face Thickness (mm)')
	boltSize = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Bolt Size')
	NOB = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Number of Bolts')
	boltHoleSize = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Bolt Hole Diameter (mm)')
	PCD = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Bolt Holes Centres (mm)')
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return f"{self.designation}"

#------------------------------------------------------------------------------------------------------------------------#
# Recommended Sole Plate and Plummerblock
#------------------------------------------------------------------------------------------------------------------------#
class SolePLatePlummerBlock(models.Model):
    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    bearingshaftDia = models.CharField(max_length=40,choices = PREFERREDJOURNALSIZES, blank=True, null=True, verbose_name = 'Bearing SHaft Diameter (mm)') 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.designation}"


#------------------------------------------------------------------------------------------------------------------------#
# Standard Conveyor Belt Class
#------------------------------------------------------------------------------------------------------------------------#
class ConveyorBeltClass(models.Model):
    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
	
    def __str__(self):
        return f"{self.designation}"

#------------------------------------------------------------------------------------------------------------------------#
# Standard Belt Conveyor Idlers
#------------------------------------------------------------------------------------------------------------------------#
class CarryIdler(models.Model):
    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    series = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Series')
    beltWidth = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Belt Width (mm)')
    idlerDiameter = models.CharField(max_length=40,choices = IDLERDIAMETERS, blank=True, null=True, verbose_name = 'Idler Designation')  
    idlerFaceLength = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Face Length (mm)')
    idlerFrameLength = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Idler Frame (mm)')
    idlerFrameMountCtrs = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Idler Mount Centres (mm)')
    topOfBottomRoller = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Distance to Top of Bottom Roller (mm)')
    numOfMountHoles = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Number of Mount Hole')
    mountHoleSize = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Mount Holes Dimensions')
    rotatingMass = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Rotating Mass (kg)')
    totalMass = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Total Mass (kg)')
    height = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Carry Idler Height (mm)')
    width = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Distance between Trough Idlers (mm)')
    bearingSpec = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Bearing Specification')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.designation}"

		
class ReturnIdler(models.Model):
    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    series = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Series')
    beltWidth = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Belt Width (mm)')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#------------------------------------------------------------------------------------------------------------------------#
# Standard Belt Conveyor Idler Sets
#------------------------------------------------------------------------------------------------------------------------#
class ConveyorCarryIdler(models.Model):
    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    beltWidth = models.CharField(max_length=40,choices = BELTWIDTH, blank=True, null = True, verbose_name = 'Belt Width (mm)')
    series = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Series')
    troughAngle = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Trough Angle (deg)')
    numOfRollers = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Number of Rollers')
    idlerDesignation = models.ForeignKey(CarryIdler, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Idler Designation')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.designation}"

class ConveyorReturnIdler(models.Model):
    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    beltWidth = models.CharField(max_length=40,choices = BELTWIDTH, blank=True, null = True, verbose_name = 'Belt Width (mm)')
    series = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Series')
    vAngle = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'V Angle (deg)')
    numOfRollers = models.CharField(max_length=10, blank=True, null = True, verbose_name = 'Number of Rollers')
    idlerDesignation = models.ForeignKey(ReturnIdler,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Idler Designation')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.designation}"

#------------------------------------------------------------------------------------------------------------------------#
# Standard Belt Conveyor Diameter 
#------------------------------------------------------------------------------------------------------------------------#
class ConveyorPulley(models.Model):

    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    pulleyType = models.CharField(max_length=40,choices = PULLEYTYPES, blank=True, null = True, verbose_name = 'Pulley Type')
    pulleyLoadType = models.CharField(max_length=40,choices = PULLEYLOADTYPES, blank=True, null = True, verbose_name = 'Belt Width (mm)')
    outsideDia = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Pulley Outside Diameter (mm)')
    beltWidth = models.CharField(max_length=40,choices = BELTWIDTH, blank=True, null = True, verbose_name = 'Belt Width (mm)')
    faceLength = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Face Length (mm)')
    wallThickness = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Wall Thickness (mm)')
    hubeType = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Hub Type')
    shaftDiameter = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Shaft Diameter (mm)')
    bearingDiameter = models.CharField(max_length=40,choices = PREFERREDJOURNALSIZES, blank=True, null = True, verbose_name = 'Bearing Diameter (mm)')
    soleplate = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Sole Plate)')
    hubThickness = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Hub Thickness (mm)')
    bearingCentre = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Bearing Centres (mm)')
    plummberBlock = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Plummer Block')
    lagging = models.CharField(max_length=40,choices = RUBBERLAGGING, blank=True, null = True, verbose_name = 'Lagging Type')
    laggingThick = models.CharField(max_length=30, blank=True, null = True, verbose_name = 'Lagging Thickness (mm)')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.designation}"

#------------------------------------------------------------------------------------------------------------------------#
# Bulk Material Data
#------------------------------------------------------------------------------------------------------------------------#
class BulkMaterialData(models.Model):
    code = models.CharField(max_length=40, blank=True, null=True, unique = True, verbose_name='Code') 
    material = models.CharField(max_length=40, blank=False, null=True, verbose_name='Material') 
    condition = models.CharField(max_length=40, blank=False, null=True, verbose_name='Condition') 
    minBD = models.CharField(max_length=10, blank=False, null=True, verbose_name='Minimum Bulk Density (kg/m^3)') 
    maxBD = models.CharField(max_length=10, blank=False, null=True, verbose_name='Maximum Bulk Density (kg/m^3)') 
    SG = models.CharField(max_length=10, blank=False, null=True, verbose_name='Specific Weight')
    maxBeltIncline = models.CharField(max_length=10, blank=False, null=True, verbose_name='Maximum Belt Incline (deg)')
    maxBeltLoadingAngle = models.CharField(max_length=10, blank=False, null=True, verbose_name='Maximum Belt Loading (deg)')
    angleOfRepose = models.CharField(max_length=10, blank=False, null=True, verbose_name='Angle of Repose (deg)')
    minInternalFrictionAngle = models.CharField(max_length=10, blank=False, null=True, verbose_name='Minimum Internal Friction Angle (deg)')
    maxInternalFrictionAngle = models.CharField(max_length=10, blank=False, null=True, verbose_name='MAximum Internal Friction Angle (deg)')
    minWallFrictionAngle = models.CharField(max_length=10, blank=False, null=True, verbose_name='Minimum Wall Friction Angle (deg)')
    maxWallFrictionAngle = models.CharField(max_length=10, blank=False, null=True, verbose_name='Minimum Wall Friction Angle (deg)')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.code}"

#------------------------------------------------------------------------------------------------------------------------#
# Standard Belt Conveyor
#------------------------------------------------------------------------------------------------------------------------#
class ConveyorBelt(models.Model):
    designation = models.CharField(max_length=40, blank=False, null=True, unique = True, verbose_name='Designation')
    project = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Project Number')
    beltWidth = models.CharField(max_length=40,choices = BELTWIDTH, blank=True, null=True, verbose_name = 'Belt Width')
    beltClass = models.ForeignKey(ConveyorBeltClass,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Belt Class')
    beltType = models.CharField(max_length=40,choices = BELTTYPES, blank=True, null=True, verbose_name = 'Belt Construction')
    beltTopCover = models.CharField(max_length=5, blank=True, null=True, verbose_name = 'Top Cover (mm)')
    beltBottomCover = models.CharField(max_length=5, blank=True, null=True, verbose_name = 'Bottom Cover (mm)')
    feedRate = models.CharField(max_length=8, blank=True, null=True, verbose_name = 'Feed Rate (t/h)')
    beltSpeed = models.CharField(max_length=8, blank=True, null=True, verbose_name = 'Belt Speed (m/s)')
    material = models.ForeignKey(BulkMaterialData,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Feed Material')
    horizontalDist = models.CharField(max_length=10, blank=True, null=True, verbose_name = 'Horizontal Distance (mm)')
    verticalList = models.CharField(max_length=10, blank=True, null=True, verbose_name = 'Vertical Lift (mm)')
    maxInclinedAngle = models.CharField(max_length=5, blank=True, null=True, verbose_name = 'Maximum Inclined Angle (deg)')
    maxLoadingAngle = models.CharField(max_length=5, blank=True, null=True, verbose_name = 'Maximum Belt Loading Angle (deg)')
    # Steel Construction Data
    # mainStringer = models.ForeignKey(SAISCSteelSections, on_delete=models.DO_NOTHING,blank=True, null=True, verbose_name = 'Main Stringer')
    # mainStringer_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number of Main Stringer')
    # mainStringers_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Main Stringers (mm)')
    # bottomStringer = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Bottom Stringer')
    # bottomStringer_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number of Bottom Stringers')
    # bottomStringer_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Bottom Stringer (mm)')
    # walkwayStringer = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Walkway Stringer')
    # walkwayStringer_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Walkway Stringers')
    # walkwayStringer_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Walkway Stringer (mm)')
    # verticalUpright = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Vertical Upright')
    # verticalUpright_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Vertical Uprights')
    # verticalUpright_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Vertical Uprights (mm)')
    # verticalDiagonal = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Vertical Upright')
    # verticalDiagonal_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Vertical Uprights')
    # verticalDiagonal_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Vertical Uprights (mm)')
    # topHorizontalTie = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Top Horizontal Tie')
    # topHorizontalTie_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Top Horizontal Ties')
    # topHorizontalTie_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Top Horizontal Ties (mm)')
    # bottomHorizontalTie = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Bottom Horizontal Tie')
    # bottomHorizontalTie_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Bottom Horizontal Tie')
    # bottomHorizontalTie_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Bottom Horizontal Tie (mm)')
    # topDiagonal = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Top Horizontal Tie')
    # topDiagonal_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Top Horizontal Ties')
    # topDiagonal_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Top Horizontal Ties (mm)')
    # bottomDiagonal = models.ForeignKey(SAISCSteelSections,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Bottom Horizontal Tie')
    # bottomDiagonal_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Bottom Horizontal Tie')
    # bottomDiagonal_len = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Length Bottom Horizontal Tie (mm)')
     # Pulley data
    # headPulley = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Head Pulley') 
    # snubPulley = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Snub Pulley') 
    # bendPulley_1 = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Bend Pulley No.1')
    # bendPulley_2 = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Bend Pulley No.2')
    # bendPulley_3 = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Bend Pulley No.3')
    # bendPulley_4 = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Bend Pulley No.4')
    # take_upPulley = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Take Up Pulley')
    # tailPulley = models.ForeignKey(ConveyorPulley,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Tail Pulley')
    # # Idlers data
    # transIdler = models.ForeignKey(ConveyorCarryIdler,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Transition Idler')
    # transIdler_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Transition Idler Sets')
    # carryIdler = models.ForeignKey(ConveyorCarryIdler,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Carry Idler')
    # carryIdler_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Carry Idler Sets')
    # impactIdler = models.ForeignKey(ConveyorCarryIdler,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Impact Idler')
    # impactIdler_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Impact Idler Sets')
    # returnIdler = models.ForeignKey(ConveyorCarryIdler,on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name = 'Return Idler')
    # returnIdler_qty = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Number Returny Idler Sets')
    # # Belt Scraper
    # primaryScraper = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Model and Make')
    # secondaryScraper = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Model and Make')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return f"{self.designation}"
