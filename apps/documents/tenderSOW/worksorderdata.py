import os

#=============================================================================================#
LOGO = "C:\\_EEMS\\apps\\accounts\\logos\\MAC.jpg"
DOC_TITLE = "TECHNICAL SCOPE OF WORK"
DESIGN_COMPANY = "MAC MINING AND CONSTRUCTION PARTNERS LIMITED"
ADDRESS_1 = "Plot 19A"
ADDRESS_2 = "Okpoti Street"
ADDRESS_3 = "Adenta, Accra, Ghana"
WEBSITE = "www.macpartnersltd.com"
PHONE = "+233-0254-1525"
COMPANY_EMAIL = "gerald@macpartnersltd.com"
ENGINEER = "Gerald Holt (Pr.Eng)"
ECSA = "20020259"

#=============================================================================================#
FILENAME = "H-MAC539-RFT-OE-0331-001-SHT-001"
CUSTOMER_COMPANY = "Cardinal Namdini Mining Ltd"
PROJECT_NAME = "RIVER WATER ABSTRACTION"
PROJECT_NUMBER = "H-MAC539"
CUSTOMER = "Bright Dzah"
EMAIL = "bright.dzah@cardinalresources.com.au"

#=============================================================================================#
DESIGN_CODES = {
                'DESIGN_CODE_1' : ["SANS 10208:","Design of structure for the mining industry Part 3: Conveyances"],
                'DESIGN_CODE_2' : ["SANS 10160:", "Buidling Loading Code"],
                'DESIGN_CODE_3' : ["SANS 10162:", "Steel Design Code"],
				'DESIGN_CODE_4' : ["SANS 10100-1:", "The Structural use of concrete Part 1 – Design"],
				'DESIGN_CODE_5' : ["SANS 10100-2:", "The Structural use of concrete Part 2 – Materials and Execution of Work"],
				'DESIGN_CODE_6' : ["SANS 10144:", "Detailing of steel reinforcement for concrete"],
				'DESIGN_CODE_7' : ["SANS 10161:", "The design of foundations for buildings"],
				'DESIGN_CODE_8' : ["SANS 110:","Sealing components for the building industry, two components, polysulphide base"],
				'DESIGN_CODE_9' : ["SANS 10164:", "The structural use of masonry Part 1"],
				'DESIGN_CODE_10' : ["BS 2853:", "The design and testing of steel overhead one way beams"],
				'DESIGN_CODE_11' : ["AWS D1.1:", "Structural Welding Code - Steel"],
				'DESIGN_CODE_23' : ["SANS 10120-3:", "Corrosion protection systems for steelwork"],
				'DESIGN_CODE_12' : ["EN 10025:","Hot rolled products of structural steel"],
				'DESIGN_CODE_13' : ["SANS 986:", "Pre-cast reinforced concrete culverts"],
				'DESIGN_CODE_14' : ["SANS 1077:", "Sealing compound for the building and construction industry, two components, polyurethane base"],
				'DESIGN_CODE_15' : ["BS 3148:", "Test for water for making concrete"],
				'DESIGN_CODE_16' : ["BS 5075-1:", "Concrete admixtures"],
				'DESIGN_CODE_17' : ["BS 5075-2:", "Specification for accelerating admixtures, retarding admixtures and water reducing admixtures"],
				'DESIGN_CODE_18' : ["BS 5075-3:", "Specification for air-entraining admixtures"],
				'DESIGN_CODE_19' : ["BS 5075-4:", "Specification for superplasticizing admixtures"],
				'DESIGN_CODE_20' : ["BS 5838:", "Specification for dry packed cementitious mixes"],
				'DESIGN_CODE_21' : ["BS 5838-1:", "Prepacked concrete mixes"],
				'DESIGN_CODE_22' : ["BS 5838-2:", "Prepacked mortar mixes"],


               }
#=============================================================================================#
SKETCH_1 = ["C:\\_EEMS\\apps\\documents\\tenderSOW\\images\\BasicFlowChart.jpg", "width=450px", "Basic Flow Diagram"]
SKETCH_2 = ["C:\\_EEMS\\apps\\documents\\tenderSOW\\images\\OverallLayout.jpg", "500px", "Overall River Abstraction Layout"]
SKETCH_3 = ["C:\\_EEMS\\apps\\documents\\tenderSOW\\images\\RiverAbstract1.jpg", "500px", "River Abstraction Detail 1"]
SKETCH_4 = ["C:\\_EEMS\\apps\\documents\\tenderSOW\\images\\RiverAbstract2.jpg", "500px", "River Abstraction Detail 2"]
SKETCH_5 = ["C:\\_EEMS\\apps\\documents\\tenderSOW\\images\\RiverAbstract3.jpg", "560px", "River Abstraction Detail 3"]
SKETCH_6 = ["C:\\_EEMS\\apps\\documents\\tenderSOW\\images\\Booster.jpg", "500px", "Booster Station"]
#SKETCH_7 = ["C:\\_EEMS\\apps\\documents\\images\\BasicFlowChart.png", "50px", "Slipper Plate Load Coefficient Pb"]

#=============================================================================================#
SECTION_1 = "REVISION HISTORY"
SECTION_2 = "CUSTOMER DETAILS"
SECTION_3 = "PROJECT DATA"
SECTION_3_1 = "Applicable Codes"
SECTION_3_2 = "Site Conditions"
SECTION_3_3 = "Sketches and Drawings"

SECTION_4 = "PROJECT INFORMATION"
SECTION_4_1 = "Introduction"
SECTION_4_2 = "River Abstraction"
SECTION_4_3 = "Booster Station"

SECTION_5 = "PHASE 1: SCOPE OF WORK"
SECTION_5_1 = "Battery Limits"
TEXT7 = r"""This tender is for Phase 1 of the project. Phase 1 is the earthworks and civils works for the causeway and catchpit. It is important that these activities are completed before the end of January 2023 as this is the time when the river is the lowest. The low river level is crucial for the safe installation of the intake water pipe."""
TEXT8 = r"""The battery limits for Phase 1 are as follows:"""
BULLET10 = r"""All earthworks and filling from the booster station to the river abstraction area."""
BULLET11 = r"""The excvation and installation of the steel sections for the catch pit."""
BULLET12 = r"""The excvation and installation of the water intake pipe and the final cut through the river bank."""
BULLET13 = r"""The installation of the hoist system at the river abstraction area."""

SECTION_5_2 = "Work Description"
SECTION_5_3 = "Work Description"
SECTION_5_4 = "Bill of Quantities"

#=============================================================================================#
REVISION_TABLE = {
	'Revision': 'Rev',
	'Description': 'Issued for Approval',
	'Date': 'Date',
	'Issued by': 'Gerald Holt',
	'Reviewed by': 'Gerald Holt',
	'Approved': 'Client',
	}

#=============================================================================================#
TEXT1 = r"""Namdini is approximately 50 km southeast of the regional town of Bolgatanga in Northern Ghana and around 60 km south of the Burkina Faso border (Figure 19). Namdini lies within the Nangodi Greenstone Belt, one of a series of southwest–northeast trending granite-greenstone belts which host significant gold mineralization in Ghana and Burkina Faso.
The Talensi district which was part of the Talensi-Nabdam district became a separate district in 2012, through Legislative Instrument LI 2110, with Tongo as the capital. The district, which is one of the thirteen Municipalities and Districts in the Upper East Region, is bordered to the north by the Bolgatanga Municipality, to the south by West and East Mamprusi Districts (both in the Northern Region), to the west by Kassena-Nankana District, and to the east by the Bawku West and Nabdam Districts. The district lies between latitude 10° 15' and 10° 60' North of the equator and longitude 0° 31' and 1° 05' West of the Greenwich Meridian and covers a land area of 838.4 km2 with a total population of 81,194, which constitutes 7.8% of the regional population. It is made up of 96 towns and villages with a settlement pattern which is predominantly rural.
The topographic relief within the project area is generally flat with gently undulating terrain, rising to the south where the area is overlain by sediments. Elevation varies from 175 to 250 meters above mean sea level (“AMSL”) with average elevation at approximately 190 m. Physiography is primarily savannah grassland characterized by short, scattered drought-resistant trees, scrub, and grass that is seasonally burned by bushfires or scorched by the sun during the long dry season."""
TEXT2 = r"""As part of the water requirements for the process plant, river water abstraction is one of the methods that will be used to supply water to the plant as well as for the camp and accommodation area. The point of abstraction has been identified which is 10,910 meters from the plant. 
Water will be abstracted by means of vertical spindle pumps, which will discharge into breakwater tanks of the booster station, 350 meters from the river in a northern direction. The booster station will accommodate the diesel generator, MCC, diesel storage, and the booster pumps which will transfer the water to the raw water storage. 
Except for areas above ground and the abstraction point, all the piping will be HDPE piping buried next to the main road to the process plant.  Piping passing underneath the main road will also be constructed from steel. The line will be equipped with valve boxes and vacuum breakers as well as the necessary scour points. Also, along the line, a T-off will be installed for the supply line to the camp.
"""
TEXT3 = r"""The point of abstraction is provided by the client. The coordinates of the abstraction point are X=748698.3955, Y=1178401.56, Z= 144.569 (cartesian system). This position was selected as it is the highest point along the river. This is important to accommodate the river level fluctuations and to ensure that the abstraction system is able to perform under these different conditions."""

TEXT4 = r""" The following are the attributes of the river abstraction configuration:"""

BULLET1 = r"""The catchpit centre is 45 meters from the riverbank. This distance has been increased from 20 meters to 45 meters to allow space for the causeway, access turning radius and soil stability."""
BULLET2 = r"""The level of the slab around the catch pit is at 143,990 mASL. The top of the catch pit ring beam is 145,330 mASL."""
BULLET3 = r"""Once the abstraction pump chamber earth, civil, and mechanical works are completed, the embankment left in situ to river to be removed during low level conditions of river. The section of soil embankment to be removed after construction of pump chamber must be stabilized by gabions."""
BULLET4 = r"""The centre of the inlet of the water intake pipe is at level 127,600 mASL. Note that the intake slope has been changed to the opposite of that of the original conceptual design. The intake water pipe slopes at 1° downward to the bottom of the catch pit bottom. The centre of the pipe enters the pit at level 126,400 mASL."""
BULLET5 = r"""As the area between transfer pump station and river embankment will flood due to its low elevation, a causeway (complete with culverts to allow water flow) has been incorporated for access to abstraction pumps."""
BULLET6 = r"""The power supply to abstraction pumps to run on the causeway."""

TEXT5 = r"""The point of abstraction is provided by the client. The coordinates of the abstraction point are X=748698.3955, Y=1178401.56, Z= 144.569 (cartesian system)."""
TEXT6 = r"""The following are the attributes of the booster station configuration:"""

BULLET7 = r"""The station consists of two areas. On the western side of the causeway is the booster station and on the earstern side the contractor's laydown area."""
BULLET8 = r"""The booster pump station will house the buffer tanks, booster pumps and substation."""
BULLET9 = r"""The area will also be equipped with a building consisting of a security office, control room, store room, workshop and the substation."""

