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

	list_codes = [
		code1,
		code2,
		code3,
	]

	return list_codes

#===================================================================================================#
def general_data():
	gen_data = {
		'DM':           ['Design Method','Limit States (Rope Break Conditions)', ''],
		'MOC_B':        ['Material of Construction','Main Body: EN10025 S355JR', ''],
		'MOC_L':        ['Material of Construction','Liners: VRN 500', ''],
		'fy':           ['Yield Stress',355, 'MPa'],
		'W_skip':       ['Skip Weight',9878, 'kg'],
		'W_pay':        ['Payload',18000, 'kg'],
		'V_winder':     ['Winding Speed',15, 'm/s'],
		'D_rope':       ['Winding Rope Diameter',54, 'mm'],
		'M_rope_unit':  ['Winding Rope Unit Mass',12.45, 'kg/m'],
		'RBF':          ['Rope Break Force',2319, 'kN'],
		'a_winder':     ['Winder Acceleration',0.8 ,'m/s^2'],
		'a_trip':       ['Winder Trip Acceleration',5, 'm/s^2'],
		'S_travel':     ['Winder Travel Distance',1023, 'm'],
		'Cycles':       ['Number of Cycles per Month', 3000, ''],
		'SIH':          ['Skip Internal Height',5600 , 'mm'],
		'SIW':          ['Skip Internal Width',1557 , 'mm'],
		'SID':          ['Skip Internal Depth',1400, 'mm'],
		'OH':           ['Skip Overall Height',10713 , 'mm'],
		'OW':           ['Skip Overall Width',1856, 'mm'],
		'OD':           ['Skip Overall Depth',1743 , 'mm'],
		'BD':           ['Ore Bulk Density',1950, 'kg/m^3' ]

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
		'S_rails':      ['Spacing between rails',1800, 'mm'],
		'Spec_rail':    ['Top Hat Guide Specification','340 x 175mm', ''],
		'MOC_R':        ['Top Hat Guide Material Specification','EN10025 S355JR', ''],
		'M_rail_unit':  ['Top Hat Guide Unit Mass',85.95, 'kg/m'],
		'B_rail_width': ['Top Hat Guide Width', 175, 'mm'],
		'k_bunt':       ['Bunton Stiffness',1608000, 'N/m'],
		'k_rail':       ['Guide Stiffnes', 1600000, 'N/m'],
	}

	return spec_data

#===================================================================================================#
def permanent_loads():
	gen_data = general_data()

	W_pay = gen_data['W_pay'][1]
	g = 9.81

	data = {
		'm_1':                          ['Skip Bridle Sides',1167, 'kg'],
		'm_2':                          ['Skip Bridle Top Transom',1522  ,'kg'],
		'm_3':                          ['Skip Bridle Bottom Transom',850,'kg'],
		'm_4':                          ['Skip Unit',6336,'kg'],
	}

	m_1 = (data['m_1'][1])
	m_3 = (data['m_3'][1])
	m_4 = (data['m_4'][1])

	data["G_c = (m_1 + m_3 + m_4)g"] = ['Permanent Load', round((m_1+m_3+m_4)*g), "N"]

	return data

#===================================================================================================#
def holding_engage_loads():
	gen_data = general_data()
	perm_data = permanent_loads()


	W_pay = gen_data['W_pay'][1]
	G_c = perm_data["G_c = (m_1 + m_3 + m_4)g"][1]
   
	g = 9.81

	data = {
		'\\alpha_k':                    ['Engagement Impact Factor',1.5,''],
		'P':                            ['Personnel Load', 0, 'kg'],
		'M':                            ['Equipment or Rolling Stock', 0, 'kg'],                   
		'R':                            ['Material Static Load', W_pay, 'kg'],
		'T':                            ['Tail Rope Load', 0, 'kg']                       
	}

	P = data['P'][1]
	M = data['M'][1]
	R = data['R'][1]
	T = data['T'][1]
	alpha_k = data['\\alpha_k'][1]

	data['C_y'] = ['Maximum Applicable Load', max(P, M, R)*g, 'N' ] 

	C_y = data['C_y'][1]

	data['K = \\alpha_k(G_c+C_y+T)'] = ['Holding Device Engagement Load', (C_y + T+ G_c)*alpha_k, 'N']

	return data

#===================================================================================================#
def holding_security_loads():
	gen_data = general_data()
	perm_data = permanent_loads()


	W_pay = gen_data['W_pay'][1]
	G_c = perm_data["G_c = (m_1 + m_3 + m_4)g"][1]

   
	g = 9.81

	data = {
		'\\alpha_s':                        ['Engagement Impact Factor',2,''],
		'P':                                ['Personnel Load', 0, 'kg'],
		'M':                                ['Equipment or Rolling Stock', 0, 'kg'],                   
		'R':                                ['Material Static Load', W_pay, 'kg'],
		'T':                                ['Tail Rope Load', 0, 'kg']                       
	}
	P = data['P'][1]
	M = data['M'][1]
	R = data['R'][1]
	T = data['T'][1]
	alpha_s = data['\\alpha_s'][1]

	data['C_y'] = ['Maximum Applicable Load', max(P, M, R)*g, 'N' ] 

	C_y = data['C_y'][1]

	data['K_c = \\alpha_s(G_c+C_y+T)'] = ['Holding Device Engagement Load', (C_y+T+G_c)*alpha_s, 'N']

	return data

#===================================================================================================#
def lateral_imposed():
	gen_data = general_data()
	perm_data = permanent_loads()
	spec = specific_data()


	m_1 = perm_data['m_1'][1]
	m_3 = perm_data['m_3'][1]
	m_4 = perm_data['m_4'][1]

	W_pay = gen_data['W_pay'][1]
	G_c = perm_data["G_c = (m_1 + m_3 + m_4)g"][1]

	L_b = spec['S_rails'][1]/1000
	V = gen_data['V_winder'][1]
	k_b = spec['k_bunt'][1]
	k_g = spec['k_rail'][1]


	g = 9.81

	data = {
		'\\Delta_c':                        ['Clearance between Roller and Slipper',10 ,'mm'],
		'\\alpha_n':                        ['Slipper Plate Impact Factor',2,''],
		'k_r':                              ['Guide Roller Assembly Stiffness', 500000, 'N/m'],
		'k_b':                              ['Bunton Stiffness',k_b, 'N/m'],
		'k_g':                              ['Guide Stiffnes', k_g, 'N/m'],
		'I_x':                              ['Moment of Inertia about X-axis',80510 , 'kg.m^2'],
		'I_y':                              ['Moment of Inertia about Y-axis',6838, 'kg.m^2'],
		'I_z':                              ['Moment of Inertia about Z-axis',82050, 'kg.m^2'],
		'h_x':                              ['Distance from slipper to center of gravity',892, 'mm'],
		'h_y':                              ['Distance from slipper to center of gravity',4847, 'mm'], 
		'h_z':                              ['Distance from slipper to center of gravity',28 , 'mm'],                  
	}

	Delta_c = data['\\Delta_c'][1]
	alpha_n = data['\\alpha_n'][1]
	I_xx = data['I_x'][1]
	I_yy = data['I_y'][1]
	I_zz = data['I_z'][1]
	h_y = data['h_y'][1]
	h_x = data['h_x'][1]
	k_r = data['k_r'][1]

	data['H_f'] = ['Guide Roller Lateral Load',k_r*Delta_c , 'N' ] 
	data['r_k'] = ['Steelwork Stiffness Ratio', k_b/k_g, ' ']
	data['m_c'] = ['Weight of Skip System', (m_1 + m_3 + m_4), 'kg']

	m_c = data['m_c'][1]
	
	m_eyx = (m_c*I_zz)/(I_zz + m_c*(h_y/1000)**2)
	m_eyz = (m_c*I_xx*I_yy)/(I_xx*I_yy + m_c*I_xx*(h_y/1000)**2 + m_c*I_yy*(h_x/1000)**2)



	data['m_x = (m_c I_z) / (I_z + m_c (h_y)^2)'] = ['Effective Mass About y - x Plane', round(m_eyx,0), 'kg' ]
	data['m_z = (m_c I_x I_y)/(I_x I_y +(m_c I_x (h_y)^2) + (m_c I_y (h_x)^2)'] = ['Effective Mass About y - z Plane', round(m_eyz,0), 'kg' ]
	data['K_x = (k_b L_b^2)/m_x V^2'] = ['Non-Dimensional Laterial Stiffness', round(k_b*((L_b)**2)/(m_eyx*V**2)), ""]
	data['K_z = (k_b L_b^2)/m_z V^2'] = ['Non-Dimensional Laterial Stiffness', round(k_b*((L_b)**2)/(m_eyz*V**2)), ""]
	data['P_b'] = ['Plate Coefficient from graph',0.05 , '' ]
	data['e'] = ['Maximum Moving Misalighnment',0.01 , 'm' ] 

	P_b = data['P_b'][1]
	e = data['e'][1]

	H_s = round((alpha_n*P_b*((400*m_eyz*e*V**2)/((L_b)**2))))

	data['H_s'] = ['Lateral Slipper Pad Load',H_s , 'N' ] 

	print(H_s)

	return data

#===================================================================================================#
def winder_acceleration_loads():
	gen_data = general_data()
	perm_data = permanent_loads()
	spec = specific_data()
	hol_eng = holding_security_loads()


	a_o = gen_data['a_winder'][1]
	a_t = gen_data['a_trip'][1]
	G_c = perm_data['G_c = (m_1 + m_3 + m_4)g'][1]
	C_y = hol_eng['C_y'][1]
	g = 9.81


	data = {
		'\\alpha_d':                        ['Dynamic Impact Factor',2,''],
		'a_o':                              ['Winder Acceleration and Deceleration', a_o, 'm/s^2'],
		'a_t':                              ['Winder Trip Acceleration', a_o, 'm/s^2'],
		'G_c':                              ['Skip Self Weight', G_c, 'N'],
		'C_y':                              ['Content Load', C_y, 'N'],
		'T':                                ['Tail Rope Load', 0, 'N'],
	}

	alpha_d = data['\\alpha_d'][1]
	a_o = data['a_o'][1]
	T = data['T'][1]
	A_o = round(alpha_d*a_o*(G_c+C_y+T)/g)
	A_t = round(alpha_d*a_t*(G_c+C_y+T)/g)

	data['A_o = (\\alpha_d) a_o (G_c + C_y + T)/g'] = ['Acceleration Load', A_o,'N' ]
	data['A_t = (\\alpha_d) a_t (G_c + C_y + T)/g'] = ['Acceleration Trip Out Load', A_o,'N' ]

	return data

#===================================================================================================#
def emergency_loads():
	gen_data = general_data()
	E_r = gen_data['RBF'][1]

	data = {
		'E_r':                          ['Emergency Load', E_r*1000, 'N'],
	}

	return data

#===================================================================================================#
def vertical_friction_loads():
	lateral = lateral_imposed()
	H_s = lateral['H_s'][1]

	data = {
		'H_s':                          [lateral['H_s'][0], H_s, 'N'],
		'F_v = 0.5 H_s':                ['Vertical Friction Load', 0.5*H_s, 'N']
	}

	return data

#===================================================================================================#
def skip_filling_loads():
	gen_data = general_data()
	R = gen_data['W_pay'][1]

	data = {
		'\\alpha_v':                        ['Filling Impact Factor in Stationary Position',1.5,''],
		
	}
	
	alpha_v = data['\\alpha_v'][1]
	R_d = alpha_v*R
	data['R_d = \\alpha_v R'] = ['Vertical Friction Load', R_d, 'N']

	return data

#===================================================================================================#
def rock_gravity_pressures():
	gen_data = general_data()
	R = gen_data['W_pay'][1]
	SIH = gen_data['SIH'][1]
	BD = gen_data['BD'][1]
	g = 9.81
	p_o = BD*g*SIH/1000

	data = {
		'\\rho_b':                          ['Bulk Density of Ore',BD,'kg/m^3'],
		'z':                                ['Maximum Container Height', SIH, 'mm'],
		'p_o = \\rho_b g z':                ['Rock Pressure', p_o, 'N/m^2']
		
	}
	return data

#===================================================================================================#
def filling_travel_pressures():
	gen_data = general_data()
	press1 = rock_gravity_pressures()

	p_o = press1['p_o = \\rho_b g z'][1] 

	data = {
		'\\alpha_p':                  ['Filling Impact Factor',1.5,''],
		'h_d':                        ['Drop Height Estimate for Single Rock',25,'m'],
		'd_i':                        ['Deformation of Skip Door',0.05*1750,'mm'],
		'm_r':                        ['Largest Rock Size Estimate',0.5*2750,'kg'],
	}

	d_i = data['d_i'][1]
	m_r = data['m_r'][1]
	h_d = data['h_d'][1]
	alpha_p = data['\\alpha_p'][1]
	g = 9.81
	p_1 = p_o*alpha_p
	p_2 = p_o*alpha_p
	Z_i = 0.5*h_d*g*m_r
	R_i = Z_i/d_i
	

	data['p_1 = \\alpha_p p_o'] = ['Skip Bottom Pressure', p_1, 'N/m^2']
	data['p_2 = \\alpha_p p_o'] = ['Skip Side Pressure', p_2, 'N/m^2']
	# data['p_3 = \\alpha_p p_o'] = ['Skip Side or Bottom Pressure during Emptying', 0.3*p_3, 'N/m^2']
	data['Z_i = 0.5 h_d g m_r'] = ['Impact Energy', Z_i, 'N/m^2']
	data['R_i = Z_i/d_i'] = ['Impact Load', R_i, 'N/m^2']

	return data

#===================================================================================================#
def tipping_roller_loads():
	gen_data = general_data()
	perm_data = permanent_loads()
	spec = specific_data()
	hol_eng = holding_security_loads()

	G_c = perm_data['G_c = (m_1 + m_3 + m_4)g'][1]
	R = gen_data['W_pay'][1]
	g = 9.81

	data = {
		'\\alpha_t':                        ['Tipping Impact Factor',2,''],
		
	}

	alpha_t = data['\\alpha_t'][1]
	R_t = alpha_t*0.25*(R*g+G_c)

	data['R_t = \\alpha_t 0.25(R + G_c)'] = ['Tipping Rollers Load',R_t, 'N']

	return data