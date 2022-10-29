from pylatex import Document, Subsection, Table, Tabular, Center, NoEscape, Math
import numpy as np
import sympy as sp
from sympy import *
import pandas as pd
from pint import UnitRegistry
ureg = UnitRegistry()

#===================================================================================================#
def designCodes():
    code1 = 'SANS 10208: 3 - 2017: Design of structures for the mining industry Part 3: Conveyances'
    code2 = 'SANS 10610: Buildling loading code'
    code3 = 'SANS 10162: Steel design'
    code4 = 'ISO 5048: 1989 E'

    list_codes = [
        code1,
        code2,
        code3,
        code4,
    ]

    return list_codes

#===================================================================================================#
def general_data():
    gen_data = {
        'NM':           ['Conveyor Name','Primary Crusher Discharge Belt', ''],
        'CODE':         ['Conveyor Number','CV-001', ''],
        'DC':           ['Design Capacity',320, 't/h'],
        'NC':           ['Normal Capacity',300, 't/h'],
        'MAT':          ['Material','ROM Coal', ''],
        'MIBD':         ['Minimum Coal Bulk Density',850, 'kg/m^3'],
        'MABD':         ['Maximum Coal Bulk Density',1000, 'kg/m^3'],
        'SUR':          ['Material Surcharge Angle',25, 'deg'],
        'PARS':         ['Particle Size Range','300 - 450', 'mm'],
        'ABA':          ['Abrasiveness','Mild', ''],
        'BW':           ['Belt Width',1500, 'mm'],
        'BS':           ['Belt Speed',1.2, 'm/s'],
        'BC':           ['Belt Class',630, ''],
        'BP':           ['Belt Ply',3, ''],
        'BT':           ['Belt Type','Fabric', ''],
        'TCV':          ['Belt Top Cover',6, 'mm'],
        'BCV':          ['Belt Top Cover',2, 'mm'],
        'HD':           ['Horizontal Distance', 34710, 'mm'],
        'VD':           ['Vertical Distance', 3007, 'mm'],
        'CONFIG':       ['Belt Configuration', 'Straight and angled',''],
        'HP':           ['Head / Drive Pulley Diameter', 500, 'mm'],
        'SP':           ['Snub Pulley Diameter', 300, 'mm'],
        'TP':           ['Tail / Take-up Pulley Diameter', 400, 'mm'],
        'HPL':          ['Head / Drive Pulley Lagging', 'Rubber - Diamond', ''],
        'HPLT':         ['Head / Drive Pulley Lagging Thickness', 12, 'mm'],
        'SPL':          ['Head / Drive Pulley Lagging', 'Rubber - Plain', ''],
        'SPLT':         ['Head / Drive Pulley Lagging Thickness', 10, 'mm'],
        'TPL':          ['Head / Drive Pulley Lagging', 'Rubber - Plain', ''],
        'TPLT':         ['Head / Drive Pulley Lagging Thickness', 10, 'mm'],
        'MOC_B':        ['Material of Construction','Structural and Pulley Shells: EN10025 S355JR', ''],
        'fy_struc':     ['Structural Steel Yield Stress',355, 'MPa'],
        'MOC_S':        ['Material of Construction','Pulley Shafts: EN8', ''],
        'fall_shaft':   ['Pulley Shaft Allowable Stress (Fatigue)',55, 'MPa'],

    }

    return gen_data

#===================================================================================================#
def images():
    images = [
        ['Shaft Plan','Shaft_Plan.jpg', ''],
        ['Skip Drawing','Tumela 18 ton Skip.jpg', ''],
    ]

    return images

#===================================================================================================#
def specific_data():
    spec_data = {
        'TRI':          ['Transition Carry Idler', 20, 'deg'],
        'CI':           ['Normal Carry Idler', 35, 'deg'],
        'II':           ['Impact Idler',35, 'deg'],
        'RI':           ['V-return', 10, 'deg'],
        'CID':          ['Distance between Carry Idlers',1000, 'mm'],
        'RID':          ['Distance between Return Idlers',5000, 'mm'],
        'SCR':          ['Number of Belt Scrapers',1, ''],
        
    }

    return spec_data

#===================================================================================================#
def bulk_solids_data_sheet():
    data = {
        'BD':           ['Bulk Density', 20, 't/m3'],
        'SG':           ['Specific Weight', 2.3, ''],
        'AR':           ['Angle of Repose',35, 'deg'],
        'EIFA':         ['Effective Internal Friction Angle', 10, 'deg'],
        'SIFA':         ['Static Internal Friction Angle', 10, 'deg'],
        'CH':           ['Cohesion',1000, 'mm'],
        'MOS':          ['Moisture',5, '%'],
        'PS':           ['Particle Size',1, 'mm'],
        'SA_ISO':       ['Surge Angle ISO',1, 'deg'],
        'SA_DIN':       ['Surge Angle DIN',1, 'deg'],
        'S_':           ['Particle Code', '', ''],
        'E_':           ['Particle Shape', '', ''],
        'A_':           ['Abrasive', '', ''],
        'D_':           ['Dust', '', ''],
        'SV_':          ['Particle Variation', '', ''],
        'F_':           ['Flowability','',''],
        'C_':           ['Corrosiveness','',''],
        'G_':           ['Tendency Weather','',''],




        
    }

    return spec_data