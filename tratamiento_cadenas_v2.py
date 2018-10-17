# coding: utf-8
#!/usr/bin/python

#COMPROBAR QUE CUANDO NO HAY UNA PALABRA FUNCIONE TODO, COMPROBAR EL +

import os
import re
#import numpy as np
import random as rn
from ast import literal_eval
import pickle
import numpy as np
import itertools

# MODULACION 1 -> PURO, MODULACION 2 -> REGRESION, MODULACION 3 -> MARTINELLI

ERR,OK = 0,1
MODULACION,GRAFICAR,NEXPERIMENTOS = 'modulation','plot_mode','number_experiments'
SUCCION,NMUESTRAS,SWESTIM,SINICIO,SBESTIM,NFILE,NFOLDER,SLEEP,VECOPVAL,VECOPODR,TEND,HTSENSOR,VEXPE,MMEXE,MMTEM,MTMIN,MTMAX = 'suction','number_samples','duration_stimulation','initial_samples','time_between_stimulus','name_file','name_folder','sleep','vector_open_valves','vector_analy_odor','tendency','heat_sensor','experiment_version','martinelli_execution_mode','martinelli_temperature_mode','minimun_temperature_martinelli','maximun_temperature_martinelli'
PIDPERIOD,MAXLIMITUPPERBOUND,MINLIMITUPPERBOUND,MAXLIMITLOWERBOUND,MINLIMITLOWERBOUND,ALPHA,MAXPKVAL,MINPKVAL = 'period','upper_limit_max','upper_limit_min','lower_limit_max','lower_limit_min','alpha','max_peak_value','min_peak_value'
RDPORT,HTPORT,MTPORT,RSTCE,SDFOLDER,VALPOS,NMUETS,SLEEPM,SLEEPTYH,VCC,TEMPPORT,TYHSENSOR,ELECPORTS,SENTYPE,RDTIME = 'reading_port','heating_port','motor_pin','resistance','sd_folder','valve_position','number_samples','sleep_time','sleep_time_th','vcc','th_reading_port','sensor_tyh_type','electrovalves_port','type_sensor','reading_time'
ALL_TRANSITIONS,ALEATORY,USER_TRANSITIONS = 1,2,3

# Power, ground and reset ports
PGRPORTS = ['P9_1','P9_2','P9_3','P9_4','P9_5','P9_6','P9_7','P9_8','P9_9','P9_10','P9_32','P9_34','P9_43','P9_44','P9_45','P9_46','P8_1','P8_2']
ADCS = ['P9_33','P9_35','P9_36','P9_37','P9_38','P9_39','P9_40']
PWMS = ['P8_13','P8_19','P9_14','P9_16','P9_21','P9_22','P9_42']

experiment_keywords = [[MODULACION,NMUESTRAS,NEXPERIMENTOS,SUCCION,SWESTIM,SINICIO,SBESTIM,NFILE,NFOLDER,VECOPVAL,VEXPE,SLEEP],
    [TEND,HTSENSOR],[MMEXE,MMTEM,MTMIN,MTMAX],[PIDPERIOD,MAXLIMITUPPERBOUND,MINLIMITUPPERBOUND,MAXLIMITLOWERBOUND,MINLIMITLOWERBOUND,ALPHA,HTSENSOR,MAXPKVAL,MINPKVAL]]
platform_keywords = [RDPORT,HTPORT,MTPORT,RSTCE,SDFOLDER,VALPOS,NMUETS,SLEEPM,SLEEPTYH,VCC,TEMPPORT,TYHSENSOR,ELECPORTS,SENTYPE,RDTIME]

# VERSION CORTA
SMODULACION,SGRAFICAR,SNEXPERIMENTOS = MODULACION[:2]+MODULACION[-2:],GRAFICAR[:2]+GRAFICAR[-2:],NEXPERIMENTOS[:2]+NEXPERIMENTOS[-2:]

SSUCCION = SUCCION[:2]+SUCCION[-2:]
SNMUESTRAS = NMUESTRAS[:2]+NMUESTRAS[-2:]
SSWESTIM = SWESTIM[:2]+SWESTIM[-2:]
SSINICIO = SINICIO[:2]+SINICIO[-2:]
SSBESTIM = SBESTIM[:2]+SBESTIM[-2:]
SNFILE = NFILE[:2]+NFILE[-2:]
SNFOLDER = NFOLDER[:2]+NFOLDER[-2:]
SSLEEP = SLEEP[:2]+SLEEP[-2:]
SVECOPVAL = VECOPVAL[:2]+VECOPVAL[-2:]
SVECOPODR = VECOPODR[:2]+VECOPODR[-2:]
STEND = TEND[:2]+TEND[-2:]
SHTSENSOR = HTSENSOR[:2]+HTSENSOR[-2:]
SVEXPE = VEXPE[:2]+VEXPE[-2:]
SMMEXE = MMEXE[11:13]+MMEXE[-8:-6] # Cojo una mas para evitar errores
SMMTEM = MMTEM[11:13]+MMTEM[-8:-6] # Cojo una mas para evitar errores
SMTMIN = MTMIN[:2]+MTMIN[-2:]
SMTMAX = MTMAX[:2]+MTMAX[-2:]
SPIDPERIOD = PIDPERIOD[:2]+PIDPERIOD[-2:]
SMAXLIMITUPPERBOUND = MAXLIMITUPPERBOUND[:2]+MAXLIMITUPPERBOUND[-2:]
SMINLIMITUPPERBOUND = MINLIMITUPPERBOUND[:2]+MINLIMITUPPERBOUND[-2:]
SMAXLIMITLOWERBOUND = MAXLIMITLOWERBOUND[:2]+MAXLIMITLOWERBOUND[-2:]
SMINLIMITLOWERBOUND = MINLIMITLOWERBOUND[:2]+MINLIMITLOWERBOUND[-2:]
SALPHA = ALPHA[:2]+ALPHA[-2:]
SMAXPKVAL = MAXPKVAL[:2] + MAXPKVAL[-2:]
SMINPKVAL = MINPKVAL[:2] + MINPKVAL[-2:]

SRDPORT = RDPORT[:2]+RDPORT[-2:]
SHTPORT = HTPORT[:2]+HTPORT[-2:]
SMTPORT = MTPORT[:2]+MTPORT[-2:]
SRSTCE = RSTCE[:2]+RSTCE[-2:]
SSDFOLDER = SDFOLDER[:2]+SDFOLDER[-2:]
SVALPOS = VALPOS[:2]+VALPOS[-2:]
SNMUETS = NMUETS[:2]+NMUETS[-2:]
SSLEEPM = SLEEPM[:2]+SLEEPM[-2:]
SSLEEPTYH = SLEEPTYH[:2]+SLEEPTYH[-2:]
SVCC = VCC[:2]+VCC[-2:]
STEMPPORT = TEMPPORT[:2]+TEMPPORT[-2:]
STYHSENSOR = TYHSENSOR[:2]+TYHSENSOR[-2:]
SELECPORTS = ELECPORTS[:2]+ELECPORTS[-2:]
SSENTYPE = SENTYPE[:2]+SENTYPE[-2:]
SRDTIME = RDTIME[:2]+RDTIME[-2:]

values = [[SNEXPERIMENTOS,SSUCCION,SNMUESTRAS,SSWESTIM,SSINICIO,SSBESTIM,SNFILE,SNFOLDER,SSLEEP,SVECOPVAL,SVEXPE],
    [STEND,SHTSENSOR],
    [SMMEXE,SMMTEM,SMTMIN,SMTMAX],
    [SPIDPERIOD,SMAXLIMITUPPERBOUND,SMINLIMITUPPERBOUND,SMAXLIMITLOWERBOUND,SMINLIMITLOWERBOUND,SALPHA,SHTSENSOR,SMAXPKVAL,SMINPKVAL]]

conf_values = [SRDPORT,SHTPORT,SMTPORT,SRSTCE,SSDFOLDER,SVALPOS,SNMUETS,SSLEEPM,SSLEEPTYH,SVCC,STEMPPORT,STYHSENSOR,SELECPORTS,SSENTYPE,SRDTIME]

############################ NUEVO ############################
def tratar_elemento(expresion):

    lst = []
    for elem in expresion.split(','):
        if ':' in elem:
            elem = elem.split(':')
            lst+=list(range(literal_eval(elem[0]),literal_eval(elem[1])+1,1)) if len(elem) == 2 else list(range(literal_eval(elem[0]),literal_eval(elem[1])+1,literal_eval(elem[2])))
        elif '+' in elem or '-' in elem or '-' in expresion or '+' in expresion:
            lst.append([[literal_eval(value)] if '+' not in value else [literal_eval(value2) for value2 in value.split('+')] for value in elem.split('-')])
        elif '(' in elem:
            elem,rept = re.split("[()]",elem)[:2] # Take the two first elements

            for e in range(int(rept)):
                try:
                    lst.append(literal_eval(elem))
                except:
                    lst.append(elem)
        elif elem == '':
            continue
        else:
            try:
                lst.append(literal_eval(elem))
            except:
                lst.append(elem)
    return lst

def tratamiento_expresion(expresion,repeticiones):
    expresion,lst,rept = re.split('(\{|\}\([0-9]+\)|\})',expresion)[::-1],[[]],[]
    
    for elem in expresion:
        if '}(' in elem:
            rept.append(int(re.split('\}\(|\)',elem)[1]))
            lst.append([])
        elif '}' in elem:
            lst.append([])
            rept.append(1)
        elif '{' in elem:
            lst.append(lst.pop()*rept.pop()+lst.pop())
        elif elem == '' or elem == ',':
            continue
        else:
            lst.append(tratar_elemento(elem)+lst.pop())

    if len(lst) != 1:
        return ERR
    else:
        lst = lst.pop()
        if isinstance(lst[-1],str) and '*' in lst[-1]:
            try:
                value = literal_eval(lst[-1][:-1])
            except:
                value = lst[-1][:-1]
            lst.pop()
            lst+=[value for i in range(repeticiones-len(lst))]

    return lst

def leer_fichero(path):

    lst,lstval = [],[]

    with open(path) as f:
        for line in f.readlines():
            line = re.sub('[\s]+','',line)
            line = re.split(':|//',line)
            if line[0] == '':
                continue
            else:
                if line[0].lower() == MODULACION: # CASO ESPECIAL PONER EN POS. 0 PARA ACCESO RAPIDO
                    lst.insert(0,line[0].lower())
                    lstval.insert(0,line[1]) 
                lst.append(line[0].lower())
                lstval.append(line[1])
                
    return lst,lstval

def leer_fichero_configuracion(path):

    lst_keywords,lst_values = leer_fichero(path)
    dict,mod,keyword_mod = {},int(lst_values.pop(0))-1,lst_keywords.pop(0)
    dict[keyword_mod[:2]+keyword_mod[-2:]] = mod
    keywords_modulation = list(set(experiment_keywords[0]+experiment_keywords[mod]))

    ### CARGO VALORES POR DEFECTO ###
    dict[SVALPOS] = 'P'
    dict[SSENTYPE] = 3
    dict[SRDTIME] = 0.1

    for keyword,val_keyword in zip(lst_keywords,lst_values):
        if keyword not in platform_keywords and keyword not in keywords_modulation:
            print ("The identificator " + keyword + " doesn't exits, please check the identificator is the correct")
            return -1
        elif keyword == 'martinelli_execution_mode' or keyword == 'martinelli_temperature_mode': 
                dict[keyword[11:13]+keyword[-8:-6]] = val_keyword
        else:
            dict[keyword[:2]+keyword[-2:]] = val_keyword

    rest_keywords_modulation = list(set(experiment_keywords[0]+experiment_keywords[mod])-set(lst_keywords))
    for elem in rest_keywords_modulation:
        dict[elem[:2]+elem[-2:]] = '0*'

    rest_keywords_platform = list(set(platform_keywords)-set(lst_keywords)-set([VALPOS,SENTYPE,RDTIME]))
    for elem in rest_keywords_platform:
        dict[elem[:2]+elem[-2:]] = ''

    return dict

def tratamiento_fichero_configuracion(dict):

    rept,mod = int(dict.pop(SNEXPERIMENTOS)),int(dict.pop(SMODULACION))
    versiones = tratamiento_expresion(dict.pop(SVEXPE),rept)
    print(versiones)
    if versiones == ERR:
        print ("Error in the element: " + VEXPE + ", check the number of repeticions from this element")
        return exit(1)

    # Guardamos los datos en el diccionario, los guardo todos primero, porque puede haber datos necesarios para tratar que reciba al final
    for key,value in dict.items():
        print(key,value)
        if key in conf_values:
            dict[key] = tratamiento_plataforma(key,value,mod)
        else:
            dict[key] = tratamiento_experimento(key,value,versiones,rept)
            
    dict[SVECOPODR] = dict[SVECOPVAL].copy()
    # Creamos las series de odorantes que se van a analizar
    vecs_open_valves_ret,vector_open_valves,muestras,pos_valvulas,valvulas_seleccionadas = [],dict[SVECOPVAL],dict.pop(SNMUESTRAS),dict[SVALPOS],dict[SELECPORTS]
    for version in versiones:
        print("version: ",version)
        if version == ALL_TRANSITIONS:
            vecs_open_valves_ret.append(todas_transiciones())
        elif version == ALEATORY:
            vecs_open_valves_ret.append(crear_transiciones(muestras.pop(0),valvulas_seleccionadas))
        elif version == USER_TRANSITIONS:
            vecs_open_valves_ret.append(vector_open_valves.pop(0)
                if pos_valvulas == 'P' else [list(set(range(1,len(valvulas_seleccionadas)+1))-set(lst)) for lst in vector_open_valves.pop(0)])
        else:
            print (versiones,"Error in version introduced, it does not exits")
            return exit(1)

    dict[SVECOPVAL] = vecs_open_valves_ret

    return dict

def tratamiento_experimento(key,value,versiones,repeticiones):

    if key == SNMUESTRAS:
        expr = tratamiento_expresion(value,versiones.count(2))
    elif key == SVECOPVAL:
        expr = tratamiento_expresion(value,versiones.count(3))
    else:
        expr = tratamiento_expresion(value,repeticiones)
    
    if expr == ERR:
        print ("Error in the element: " + key + ", check the number of repeticions from the element")
        return exit(1)

    return expr

def tratamiento_plataforma(key,value,mod):
    
    if key == SRDPORT:
        if value not in ADCS and mod != 3:
            print ('El puerto de lectura de datos debe ser un puerto ADC, revise la configuracion')
            return exit(1)
        elif  mod == 3 and (value in ADCS or value in PWMS or value in PGRPORTS):
            print ('El puerto de lectura de datos debe ser un puerto GPIO para martinelli, revise la configuracion')
            return exit(1)
        else:
            return value
    elif (key == SHTPORT or key == SMTPORT) and value not in PWMS:
        print ('El puerto de calentamiento del sensor y el de control del motor deben ser puertos PWM, revise la configuracion')
        return exit(1)
    elif key == SELECPORTS:
        expr = value.split(",")
        #set_total_vales = set(range(1,len(value.split(","))+1))
    else:   
        expr = value

    return expr

def crear_transiciones(switch,total_valvulas):
    """
    Crea transiciones entre gases

    Creamos transiciones entre gases, aleatoriamente, de forma que nunca se repita la misma secuencia de apertura.
    Que no entre dos veces al sensor el mismo gas.

    Parámetros:
    switch -- numero de gases que van a entrar al sensor
    
    Retorno:
    devolver -- array con los gases que van a entrar al sensor

    """

    return [rn.randint(1,len(total_valvulas)) for i in range(switch)]

def todas_transiciones():
    """
    Crea transiciones entre gases

    Creamos transiciones entre gases, sin poner aire entre los gases
    
    Retorno:
    devolver -- array con los gases que van a entrar al sensor

    """
    # Movida rara, dejo así, aunque se podrá mejorar
    n_sensor = len(set_total_vales)
    a_n_sensor = np.arange(1,n_sensor+1)
    lst = np.array(list(itertools.product(a_n_sensor,a_n_sensor)))
    m = np.arange(n_sensor**2).reshape(n_sensor,n_sensor)
    d0 = m.diagonal().copy()
    np.fill_diagonal(m,0) 
    m = np.triu(m)
    x = lst[m[m!=0]]
    d1 = lst[m.diagonal(1)].tolist()
    print("CACA DE VACA",x,d1)
    ret = []
    for v in x:
         print(v,d1)
         if v.tolist() not in d1:
              ret.append([v[0]])
              ret.append([v[1]])
         else:
              ret.append([v[1]])

    for v in lst[d0]:
        ret.append([v[0]])
        ret.append([v[1]])
          
    ret.pop()
    ret.append(ret[0])
    
    return ret

# Problema al pasar de string al tipo correspondiente
def leer_ficheros_graphicPyHuele(path_experiment_config,path_platform_config):

    experiment_data_dict,platform_data_dict = {},{}

    for path,dict in zip([path_experiment_config,path_platform_config],[experiment_data_dict,platform_data_dict]):
        fil = open(path,'rb')
        #print(pickle.load())
        while 1:
            try:
                line,lst = pickle.load(fil)
                #print(line,lst)
                if line == 'moon':
                    mod = lst
                    continue
                #if lst == '':
                #    continue
                    #try:
                    #lst.append(data)
                    #except:
                    #    lst.append(data)
                try:
                    dict[line] = literal_eval(lst)
                except:
                    dict[line] = lst
            except (EOFError, pickle.UnpicklingError):
                break
        fil.close()

    return mod,experiment_data_dict,platform_data_dict

###############################################################