from pylatex import Document, Subsection, Table, Tabular, Center, NoEscape, Math
import numpy as np
import sympy as sp
from sympy import *
import pandas as pd
from pint import UnitRegistry
import math
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
        'UTS':          ['Ultimate Tensile Strength',1900, 'MPa'],
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
    data['A_t = (\\alpha_d) a_t (G_c + C_y + T)/g'] = ['Acceleration Trip Out Load', A_t,'N' ]

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
def general_skip_loads():
    gen_data = general_data()
    perm_data = permanent_loads()
    spec = specific_data()
    hol_eng = holding_security_loads()

    g = 9.81
    E_rope = 103000   #N/mm^2
    G_c = perm_data['G_c = (m_1 + m_3 + m_4)g'][1]
    R = gen_data['W_pay'][1]
    BD = gen_data['BD'][1]
    SIW = gen_data['SIW'][1]
    SID = gen_data['SID'][1]
    D_rope = gen_data['D_rope'][1]
    V_winder = gen_data['V_winder'][1]
    L_rope = gen_data['S_travel'][1]
    a_o = gen_data['a_winder'][1]
    a_t = gen_data['a_trip'][1]
    RBF = gen_data['RBF'][1]
    UTS = gen_data['UTS'][1]
    Vol_req = round(R/BD,1)
    Ore_ht = round(Vol_req/((SIW/1000)*(SID/1000)),1)
    R_area = math.pi*0.25*(D_rope**2)
    print(R_area)
    r_stretch = round(R*g*L_rope*1000/(E_rope*R_area),1)
    print(r_stretch)
    
    data = {
        'R':                      [gen_data['W_pay'][0], R, 'kg'],
        'R_l':                    [gen_data['W_pay'][0], R*g, 'N'],
        'V_w':                    [gen_data['V_winder'][0], V_winder, 'm/s'],
        'a_w':                    [gen_data['a_winder'][0], a_o, 'm/s^2'],
        'a_t':                    [gen_data['a_trip'][0], a_t, 'm/s^2'],
        'Rope_d':                 [gen_data['D_rope'][0], D_rope, 'm/s^2'],
        'RBF':                    [gen_data['RBF'][0], RBF, 'kN'],
        'UTS':                    [gen_data['UTS'][0], UTS, 'MPa'],
        '\\rho_b':                [gen_data['BD'][0],BD,'kg/m^3'],
        'b':                      [gen_data['SIW'][0], SIW, 'mm'],
        'w':                      [gen_data['SID'][0], SIW, 'mm'],
        'Vol = R / \\rho_b':      ['Skip Volume Required',Vol_req, 'm^3' ],
        'h = Vol/(b w)':          ['Ore Height in Skip', Ore_ht, 'm' ],
        '\\Delta L':              ['Rope Strentch Under Payload',r_stretch, 'mm' ]  
    }

    return data


#===================================================================================================#
def rock_loads():
    gen_data = general_data()
    gen_skip = general_skip_loads()
    perm_data = permanent_loads()
    R = gen_data['W_pay'][1]
    Ore_ht = gen_skip['h = Vol/(b w)'][1]
    BD = gen_data['BD'][1]
    g = 9.81
    p_o = BD*g*Ore_ht/1000
    p_1 = round(1 * p_o,1)
    p_2 = round(0.5 * p_o, 1)
    p_3 = round(1.5 * p_o, 1)
    p_4 = round(0.2 * p_o, 1)
    G_c = perm_data['G_c = (m_1 + m_3 + m_4)g'][1]

    alpha_v = 1.5
    alpha_t = 2
    R_d = alpha_v*R
    R_t = alpha_t*0.25*(R+G_c)

   

    data = {
        '\\alpha_v':                        ['Filling Impact Factor in Stationary Position',alpha_v,''],
        '\\alpha_t':                        ['Load on Tipping Rollers Impact Factor',alpha_t,''],
        'R':                                ['Static Load', R*g, 'N'],
        'R_d = (\\alpha_v)(R)':             ['Bridle Transom Load While Filling', R_d, 'N'],
        'p_o = \\rho_b g h':                ['Rock Pressure', p_o, 'N/m^2'],
        'p_1 = 1 p_o':                      ['Pressure on the Door', p_1, 'N/m^2'],
        'p_2 = 0.5 p_o':                    ['Pressure on the Back of Skip', p_2, 'N/m^2'],
        'p_3 = 0.5 p_o':                    ['Pressure on the Lower Portion Skip Back', p_3, 'N/m^2'],
        'p_4 = 0.2 p_o':                    ['Pressure on the Front and Sides of Skip', p_4, 'N/m^2'],
    }
    return data


#===================================================================================================#
def properties_double_plate(h,w,t_p):
    
    H = h + 2*t_p
    A = round(2*(w*t_p),0)
    I_x = round((w/12)*(H**3-h**3),0)
    I_y = round((t_p*w**3)/6,0)
    Z_e = round((w/6*H)*(H**3-h**3),0)
    Z_p = round(2*(w*t_p*(h-t_p/2)),0)
    J = I_x+I_y
    expr_H = 'H = h + 2t_p'
    expr_A = 'A = 2(wt_p)'
    expr_I_x = 'I_x = w/12(H^3-h^3)'
    expr_I_y = 'I_y = t_pw^3/6'
    expr_Ze = 'Z_e = w/6H(H^3-h^3)'
    expr_Zp = 'Z_p = 2(wt_p(h-t_p/2)'
    expr_J = 'J = I_x + I_y'

    results = {
                'A': A,
                'H': H,
                'I_x': I_x,
                'I_y': I_y,
                'J': J,
                'Z_e': Z_e,
                'Z_p': Z_p,
                'expr_H': expr_H,
                'expr_A': expr_A,
                'expr_I_x': expr_I_x,
                'expr_I_y': expr_I_y,
                'expr_J': expr_J,
                'expr_Z_e': expr_Ze,
                'expr_Z_p': expr_Zp
    }
    return results





#===================================================================================================#
def properties_channel(b,h,t_w, t_f):
    h_w = h - 2*t_f
    b_f = b - t_w


    A = 2*b*t_f + h_w*t_w
    x_c = (1/A)*(0.5*h_w*t_w**2 + t_f*b**2)
    I_x = (b*h**3)/12 - (b_f*h_w**3)/12
    I_y = (h_w*t_w**3)/3+2*(t_f*b**3)/3 - A*x_c**2
    Z_p = (b*h**2)/4 - (b_f*h_w**2)/4
    J = I_x+I_y
    C_w = (1/144)*(t_f**3)*(b**3)+(1/36)*((h - t_f/2)**3)*(t_w**3)

    expr_A = 'A=2bt_f + h_w*t_w'
    expr_x_c = 'x_c=(0.5h_wt_w^2 + t_fb^2)/A'
    expr_I_x = 'I_x=bh^3/12 - b_fh_w^3/12'
    expr_I_y = 'I_y=h_wt_w^3/3+2t_fb^3/3 - Ax_c^2)'
    expr_Z_p = 'Z_p=bh^2/4 - b_fh_w^2/4'
    expr_J = 'J = I_x + I_y'
    expr_C_w = 'C_w = (1/144)(t_f^3b^3)+(1/36)(h - t_f/2)^3)t_w^3'

    results = {
                'b':b,
                'h':h,
                't_w': t_w,
                't_f': t_f,
                'A': round(A,0),
                'x_c': round(x_c,0),
                'I_x': round(I_x,0),
                'I_y': round(I_y,0),
                'J': round(J,0),
                'C_w': round(C_w,0),
                'Z_p': round(Z_p,0),
                'expr_A': expr_A,
                'expr_x_c': expr_x_c,
                'expr_I_x': expr_I_x,
                'expr_I_y': expr_I_y,
                'expr_Z_p': expr_Z_p,
                'expr_J': expr_J,
                'expr_C_w': expr_C_w,
    }
    return results

#===================================================================================================#
def top_transom():
    gen_data = general_data()
    gen_skip = general_skip_loads()
    perm_data = permanent_loads()

    RBF = gen_data['RBF'][1]
    L = 1700 # Length of transom
    E = 200000 # Modulus of Elastisity MPa
    G = 70000 # Shear Modulus MPa
    f_y = 355 #Yield Stress MPa
    t_w = 10.2 # Web Thickness mm
    t_f = 15.6 # Flange Thickness mm
    h = 533 # Beam Height mm
    b = 109 # Beam Width mm
    w = 110 # Plate Width mm
    t_p = 20 # Plate Thickness
    
    plate = properties_double_plate(h,w,t_p)
    prop = properties_channel(b,h,t_w, t_f)
    Z_p = prop['Z_p']
    I_x = prop['I_x']
    I_y = prop['I_y']
    A= prop['A']
    J = prop['J']
    C_w = prop['C_w']

    Z_p_p = plate['Z_p']
    I_x_p = plate['I_x']
    I_y_p = plate['I_y']
    A_p= plate['A']
    J_p = plate['J']

    I_x = I_x + I_x_p
    I_y = I_y + I_y_p
    Z_p = Z_p + Z_p_p
    J = J + J_p
    A = A + A_p

    M_p = round(Z_p*f_y/1000**2,1)
    M_pall = round(0.67*M_p,1)
    pi = math.pi
    M_cr = math.sqrt(((pi**4)*(E**2)*C_w*I_y)/L**4 + ((pi**2)*E*I_y*G*J)/L**2)
    M_c = round((M_cr/1000**2),1)
    if M_c > M_pall:
        M_r = round(1.15*0.9*M_p*(1-(0.28*M_p/M_c)),1)
        expr_M_r = 'M_r = 1.15 \\phi M_p(1-(0.28M_p/M_c))'
    else:
        M_r = round(0.9*M_p,1)
        expr_M_r = 'M_r = \\phi M_p'
    V_r = round(0.55*0.9*A*f_y/1000,0)

    expr_V_r = 'Vr = 0.55 \\phi A f_y'
    expr_Mp = 'M_p = Z_pf_y'
    expr_Mp067 = '0.67M_p'
    expr_Mc = 'M_c = ((\\pi^4E^2C_wI_y)/L^4 + (\\pi^2EI_yGJ)/L^2)^0.5'



    data = {    
                'L':                ['Length of Transom', L, 'mm'],
                'b':                ['Channel Width', b, 'mm'],
                'h':                ['Channel Height', h, 'mm'],
                't_w':              ['Channel Web Thickness', t_w, 'mm'],
                't_f':              ['Channel Flange Thickness', t_f, 'mm'],
                'w':                ['Top and Bottom Plate Width',w, 'mm'],
                't_p':              ['Top and Bottom Plate Thickness', t_p, 'mm'],
                'f_y':              ['Yield Stress', f_y, 'MPa'],
                prop['expr_A']:     ['Channel Cross Sectional Area', prop['A'], 'mm^2'],
                prop['expr_x_c']:   ['Channel Centroid Distance', prop['x_c'], 'mm'],
                prop['expr_I_x']:   ['Channel Second Moment of Area about x-x', prop['I_x'], 'mm^4'],
                prop['expr_I_y']:   ['Channel Second Moment of Area about y-y', prop['I_y'], 'mm^4'],
                prop['expr_J']:     ['Channel Polar Moment', prop['J'], 'mm^4'],
                prop['expr_C_w']:   ['Channel Warping Constant', prop['C_w'], 'mm^6'],
                prop['expr_Z_p']:   ['Channel Plastic Section Modulus', prop['Z_p'], 'mm^3'],
                
                plate['expr_A']:     ['Double Plate Cross Sectional Area', plate['A'], 'mm^2'],
                plate['expr_I_x']:   ['Double Plate Second Moment of Area about x-x', plate['I_x'], 'mm^4'],
                plate['expr_I_y']:   ['Double Plate Second Moment of Area about y-y', plate['I_y'], 'mm^4'],
                plate['expr_J']:     ['Double Plate Polar Moment', plate['J'], 'mm^4'],
                plate['expr_Z_p']:   ['Double Plate Plastic Section Modulus', plate['Z_p'], 'mm^3'],

                'I_x':               ['Combined Second Moment of Area about x-x', I_x, 'mm^3'],
                'I_y':               ['Combined Second Moment of Area about y-y', I_y, 'mm^3'],
                'Z_p':               ['Combined Plastic Section Modulus', Z_p, 'mm^3'],
                
                expr_Mp:            ['Plastic Moment',M_p,'kNm' ],
                expr_Mp067:         ['Adjusted Plastic Moment',M_pall,'kNm' ],
                expr_Mc:            ['Critical Elastic Moment', M_c, 'kNm'],
                expr_M_r:           ['Factored Moment Resistance', M_r, 'kNm'],
                expr_V_r:           ['Factored Shear Resistance', V_r, 'kNm']
    }

    return data, M_r, V_r

#===================================================================================================#
def emergencyloads():
    topt, M_r, V_r = top_transom()
    gen_data = general_data()

    RBF = gen_data['RBF'][1]
    L = topt['L'][1]
    N_beams = 2

    M_u = round(RBF*L/4000,0)
    V_u = round(RBF/2,0)
    IC =  round(M_u/(N_beams*M_r) + V_u/(N_beams*V_r),2)
    if IC < 1:
        text = "Pass"
    else:
        text = "Fail"

    expr_M_u = 'M_u = RBF L/4'
    expr_V_u = 'M_u = RBF/2'
    expr_IC = "M_u/M_r + V_u/V_r < 1"

    data = {
        'RBF':            ['Rope Break Force', RBF, 'kN'],
        'No.':            ['Number of Beams', N_beams, ''],
        'M_r':            ['Combined Bending Resistance', N_beams*M_r, 'kN'],
        'M_r':            ['Combined Shear Resistance', N_beams*V_r, 'kN'],
        expr_M_u:         ['Ultimate Bending Moment', M_u, 'kN'],
        expr_V_u:         ['Ultimate Shear Force', V_u, 'kN'],
        expr_IC:          ['Interaction Check', IC, text]              
    }

    return data

#===================================================================================================#
def operationalloads():
    topt, M_r, V_r = top_transom()
    gen_data = general_data()
    gen_skip = general_skip_loads()
    perm_data = permanent_loads()
    R = gen_data['W_pay'][1]
    g = 9.81
    G_c = perm_data['G_c = (m_1 + m_3 + m_4)g'][1]

    LC = round((1.2*G_c + 1.6*R)/1000,0) # kN
    L = topt['L'][1]
    N_beams = 2

    M_u = round(LC*L/4000,0)
    V_u = round(LC/2,0)
    IC =  round(M_u/(N_beams*M_r) + V_u/(N_beams*V_r),2)
    if IC < 1:
        text = "Pass"
    else:
        text = "Fail"

    expr_M_u = 'M_u = (RBF) L/4'
    expr_V_u = 'M_u = (RBF)/2'
    expr_IC = "M_u/M_r + V_u/V_r < 1"

    data = {
        'LC = 1.2G_c + 1.6R':   ['Operation Force', LC, 'kN'],
        'No.':                  ['Number of Beams', N_beams, ''],
        'M_r':                  ['Combined Bending Resistance', N_beams*M_r, 'kN'],
        'M_r':                  ['Combined Shear Resistance', N_beams*V_r, 'kN'],
        expr_M_u:               ['Ultimate Bending Moment', M_u, 'kN'],
        expr_V_u:               ['Ultimate Shear Force', V_u, 'kN'],
        expr_IC:                ['Interaction Check', IC, text]              
    }

    return data

#===================================================================================================#
def fatigue_load_top():
    gen_data = general_data()
    rock_load = rock_loads()
    perm_data = permanent_loads()
    topt, M_r, V_r = top_transom()
    acc_forces = winder_acceleration_loads()

    R = gen_data['W_pay'][1]
    R_d = rock_load['R_d = (\\alpha_v)(R)'][1]
    G_c = perm_data['G_c = (m_1 + m_3 + m_4)g'][1]
    Cpm = gen_data['Cycles'][1]
    A_o = acc_forces['A_o = (\\alpha_d) a_o (G_c + C_y + T)/g'][1]
    A_t = acc_forces['A_t = (\\alpha_d) a_t (G_c + C_y + T)/g'][1]
    L = topt['L'][1]
    Z_p = topt['Z_p'][1]
    DesignLife = 24 # 24 months
    NoTrips = Cpm*DesignLife
    MCL = R_d + 0.25*G_c
    sigma_a = round(MCL*L/(4*Z_p),1)
    A_o_f = 2*A_o
    sigma_b = round(A_o_f*L/(4*Z_p),1)
    sigma_c = round(0.2*R*L/(4*Z_p),1)



    expr_R_d = 'R_d = (\\alpha_v)(R)'
    expr_G_c = 'G_c = (m_1 + m_3 + m_4)g'
    expr_MCL = 'MCL = R_d + 0.25G_c'
    expr_sigma_a = '\\sigma_a = 0.5 (MCL) L/(4 Z_p))'
    expr_sigma_b = '\\sigma_b = 0.5 (2 A_o L/(4 Z_p))'
    expr_sigma_c = '\\sigma_c = 0.5 (0.2 R L/(4 Z_p))'
    expr_IC = "\\sigma_a/S_e + \\sigma_b/S_e + \\sigma_c/S_e < 1"

    

    N_beams = 2
    S_e = 70 

    IC =  round(sigma_a/(N_beams*S_e) + sigma_b/(N_beams*S_e) + sigma_c/(N_beams*S_e),2)
    if IC < 1:
        text = "Pass"
    else:
        text = "Fail"

    data = {
        'Cycles':     ['Cycles per Month', Cpm, ''],
        'Design':     ['Design Life', DesignLife, 'months'],
        'Trips':      ['Total Number of Trips', NoTrips, ''],
        expr_R_d:     ['Rock during Filling',R_d, 'N'],
        expr_G_c:     ['Permanent Load', G_c, 'N'],
        expr_MCL:     ['Major Cycle Load', MCL, 'N'],
        expr_sigma_a: ['Stress Amplitude', sigma_a/N_beams, 'MPa'],
        '2A_o':       ['Acceleration Cycles Load', 2*A_o, 'N'],
        expr_sigma_b: ['Stress Acceleration Increase', sigma_b, 'MPa'],
        '0.2R':       ['Bounding Load', 0.2*R, 'N'],
        expr_sigma_c: ['Stress Acceleration Increase', sigma_c, 'MPa'],
        'S_e':        ['Steel Endurance Limit', S_e, 'MPa'],
        expr_IC:      ['Interaction Check', IC, text]    
    }

    return data

#===================================================================================================#
def bot_transom():
    gen_data = general_data()
    gen_skip = general_skip_loads()
    perm_data = permanent_loads()

    RBF = gen_data['RBF'][1]
    L = 1700 # Length of transom
    E = 200000 # Modulus of Elastisity MPa
    G = 70000 # Shear Modulus MPa
    f_y = 355 #Yield Stress MPa
    t_w = 7.5 # Web Thickness mm
    t_f = 14 # Flange Thickness mm
    h = 230 # Beam Height mm
    b = 90 # Beam Width mm
    w = 230 # Plate Width mm
    t_p = 20 # Plate Thickness
    
    plate = properties_double_plate(h,w,t_p)
    prop = properties_channel(b,h,t_w, t_f)
    Z_p = prop['Z_p']
    I_x = prop['I_x']
    I_y = prop['I_y']
    A= prop['A']
    J = prop['J']
    C_w = prop['C_w']

    Z_p_p = plate['Z_p']
    I_x_p = plate['I_x']
    I_y_p = plate['I_y']
    # Z_p_p = 0
    # I_x_p = 0
    # I_y_p = 0
    A_p= plate['A']
    J_p = plate['J']
    # A_p = 0
    # J_p = 0


    I_x = I_x + I_x_p
    I_y = I_y + I_y_p
    Z_p = Z_p + Z_p_p
    J = J + J_p
    A = A + A_p

    M_p = round(Z_p*f_y/1000**2,1)
    M_pall = round(0.67*M_p,1)
    pi = math.pi
    M_cr = math.sqrt(((pi**4)*(E**2)*C_w*I_y)/L**4 + ((pi**2)*E*I_y*G*J)/L**2)
    M_c = round((M_cr/1000**2),1)
    if M_c > M_pall:
        M_r = round(1.15*0.9*M_p*(1-(0.28*M_p/M_c)),1)
        expr_M_r = 'M_r = 1.15 \\phi M_p(1-(0.28M_p/M_c))'
    else:
        M_r = round(0.9*M_p,1)
        expr_M_r = 'M_r = \\phi M_p'
    V_r = round(0.55*0.9*A*f_y/1000,0)

    expr_V_r = 'Vr = 0.55 \\phi A f_y'
    expr_Mp = 'M_p = Z_pf_y'
    expr_Mp067 = '0.67M_p'
    expr_Mc = 'M_c = ((\\pi^4E^2C_wI_y)/L^4 + (\\pi^2EI_yGJ)/L^2)^0.5'



    data = {    
                'L':                ['Length of Transom', L, 'mm'],
                'b':                ['Channel Width', b, 'mm'],
                'h':                ['Channel Height', h, 'mm'],
                't_w':              ['Channel Web Thickness', t_w, 'mm'],
                't_f':              ['Channel Flange Thickness', t_f, 'mm'],
                'w':                ['Top and Bottom Plate Width',w, 'mm'],
                't_p':              ['Top and Bottom Plate Thickness', t_p, 'mm'],
                'f_y':              ['Yield Stress', f_y, 'MPa'],
                prop['expr_A']:     ['Channel Cross Sectional Area', prop['A'], 'mm^2'],
                prop['expr_x_c']:   ['Channel Centroid Distance', prop['x_c'], 'mm'],
                prop['expr_I_x']:   ['Channel Second Moment of Area about x-x', prop['I_x'], 'mm^4'],
                prop['expr_I_y']:   ['Channel Second Moment of Area about y-y', prop['I_y'], 'mm^4'],
                prop['expr_J']:     ['Channel Polar Moment', prop['J'], 'mm^4'],
                prop['expr_C_w']:   ['Channel Warping Constant', prop['C_w'], 'mm^6'],
                prop['expr_Z_p']:   ['Channel Plastic Section Modulus', prop['Z_p'], 'mm^3'],
                
                plate['expr_A']:     ['Double Plate Cross Sectional Area', plate['A'], 'mm^2'],
                plate['expr_I_x']:   ['Double Plate Second Moment of Area about x-x', plate['I_x'], 'mm^4'],
                plate['expr_I_y']:   ['Double Plate Second Moment of Area about y-y', plate['I_y'], 'mm^4'],
                plate['expr_J']:     ['Double Plate Polar Moment', plate['J'], 'mm^4'],
                plate['expr_Z_p']:   ['Double Plate Plastic Section Modulus', plate['Z_p'], 'mm^3'],

                'I_x':               ['Combined Second Moment of Area about x-x', I_x, 'mm^3'],
                'I_y':               ['Combined Second Moment of Area about y-y', I_y, 'mm^3'],
                'Z_p':               ['Combined Plastic Section Modulus', Z_p, 'mm^3'],
                
                expr_Mp:            ['Plastic Moment',M_p,'kNm' ],
                expr_Mp067:         ['Adjusted Plastic Moment',M_pall,'kNm' ],
                expr_Mc:            ['Critical Elastic Moment', M_c, 'kNm'],
                expr_M_r:           ['Factored Moment Resistance', M_r, 'kNm'],
                expr_V_r:           ['Factored Shear Resistance', V_r, 'kNm']
    }

    return data, M_r, V_r

#===================================================================================================#
def emergencyloads_bot():
    bott, M_r, V_r = bot_transom()
    gen_data = general_data()

    RBF = gen_data['RBF'][1]
    L = bott['L'][1]
    N_beams = 2

    M_u = round(RBF*L/4000,0)
    V_u = round(RBF/2,0)
    IC =  round(M_u/(N_beams*M_r) + V_u/(N_beams*V_r),2)
    if IC < 1:
        text = "Pass"
    else:
        text = "Fail"

    expr_M_u = 'M_u = RBF L/4'
    expr_V_u = 'M_u = RBF/2'
    expr_IC = "M_u/M_r + V_u/V_r < 1"

    data = {
        'RBF':            ['Rope Break Force', RBF, 'kN'],
        'No.':            ['Number of Beams', N_beams, ''],
        'M_r':            ['Combined Bending Resistance', N_beams*M_r, 'kN'],
        'M_r':            ['Combined Shear Resistance', N_beams*V_r, 'kN'],
        expr_M_u:         ['Ultimate Bending Moment', M_u, 'kN'],
        expr_V_u:         ['Ultimate Shear Force', V_u, 'kN'],
        expr_IC:          ['Interaction Check', IC, text]              
    }

    return data


#===================================================================================================#
def bridle():
    gen_data = general_data()
    gen_skip = general_skip_loads()
    perm_data = permanent_loads()

    RBF = gen_data['RBF'][1]
    E = 200000 # Modulus of Elastisity MPa
    G = 70000 # Shear Modulus MPa
    f_y = 355 #Yield Stress MPa

    A = 2680
    t_w = 7
    bolt_hole = 24
    A_n = A - bolt_hole*t_w
    N_bridles = 4

    T_u = RBF
    T_r = round((0.85*0.9*A_n*f_y)/1000,0)

    IC =  round(T_u/(N_bridles*T_r),2)
    if IC < 1:
        text = "Pass"
    else:
        text = "Fail"

    expr_IC = "T_u/T_r < 1"
    expr_T_r = 'T_r = 0.85 \\phi A f_y'

    data = {    
                'A_t':              ['Total Cross Sectional Bridle Area',round(N_bridles*A,0), 'mm^2'],
                'A_e':              ['Total Net Cross Sectional Bridle Area', round(N_bridles*A_n,0), 'mm'],
                'RBF':              ['Rope Break Force', RBF, 'kN'],
                expr_T_r:           ['Tensile Resistance per Channel',T_r,'N' ],
                'No.':              ['Number of Bridless', N_bridles, ''],
                'T_r':              ['Total Tensile Resistance',round(N_bridles*T_r,0), 'N'],
                expr_IC:            ['Interaction Check', IC, text] 
    }

    return data, T_r

#===================================================================================================#
def fatigue_load_bridle():
    gen_data = general_data()
    rock_load = rock_loads()
    perm_data = permanent_loads()
    topt, M_r, V_r = top_transom()
    acc_forces = winder_acceleration_loads()

    R = gen_data['W_pay'][1]
    R_d = rock_load['R_d = (\\alpha_v)(R)'][1]
    G_c = perm_data['G_c = (m_1 + m_3 + m_4)g'][1]
    Cpm = gen_data['Cycles'][1]
    A_o = acc_forces['A_o = (\\alpha_d) a_o (G_c + C_y + T)/g'][1]
    A_t = acc_forces['A_t = (\\alpha_d) a_t (G_c + C_y + T)/g'][1]

    # 180 x channels
    A = 2680
    t_w = 7
    bolt_hole = 24
    A_n = A - bolt_hole*t_w
    N_bridles = 4

    DesignLife = 24 # 24 months
    NoTrips = Cpm*DesignLife
    MCL = R_d + 0.25*G_c
    sigma_a = round(MCL/A_n,1)
    A_o_f = 2*A_o
    sigma_b = round(A_o_f/(N_bridles*A_n),1)
    sigma_c = round(0.2*R/(N_bridles*A_n),1)

    expr_R_d = 'R_d = (\\alpha_v)(R)'
    expr_G_c = 'G_c = (m_1 + m_3 + m_4)g'
    expr_MCL = 'MCL = R_d + 0.25G_c'
    expr_sigma_a = '\\sigma_a = MCL/(N_b A_n))'
    expr_sigma_b = '\\sigma_b = (2 A_o/(N_b A_n))'
    expr_sigma_c = '\\sigma_c = (0.2 R/(N_b A_n))'
    expr_IC = "\\sigma_a/S_e + \\sigma_b/S_e + \\sigma_c/S_e < 1"

    S_e = 70 

    IC =  round((sigma_a/S_e) + (sigma_b/S_e) + (sigma_c/S_e),2)
    if IC < 1:
        text = "Pass"
    else:
        text = "Fail"

    data = {
        'Cycles':     ['Cycles per Month', Cpm, ''],
        'Design':     ['Design Life', DesignLife, 'months'],
        'Trips':      ['Total Number of Trips', NoTrips, ''],
        'N_b':        ['Number of Bridle Channels', N_bridles, ''],
        expr_R_d:     ['Rock during Filling',R_d, 'N'],
        expr_G_c:     ['Permanent Load', G_c, 'N'],
        expr_MCL:     ['Major Cycle Load', MCL, 'N'],
        expr_sigma_a: ['Stress Amplitude', sigma_a, 'MPa'],
        '2A_o':       ['Acceleration Cycles Load', 2*A_o, 'N'],
        expr_sigma_b: ['Stress Acceleration Increase', sigma_b, 'MPa'],
        '0.2R':       ['Bounding Load', 0.2*R, 'N'],
        expr_sigma_c: ['Stress Acceleration Increase', sigma_c, 'MPa'],
        'S_e':        ['Steel Endurance Limit', S_e, 'MPa'],
        expr_IC:      ['Interaction Check', IC, text]    
    }

    return data

#===================================================================================================#