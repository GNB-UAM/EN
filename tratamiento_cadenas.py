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

# MODULACION 1 -> PURO, MODULACION 2 -> REGRESION, MODULACION 3 -> MARTINELLI, MODULACION 4 -> PID

ERR,OK = 0,1
MODULACION,GRAFICAR,NEXPERIMENTOS = 'modulation','plot_mode','number_experiments'
SUCCION,NMUESTRAS,SWESTIM,SINICIO,SBESTIM,NFILE,NFOLDER,SLEEP,VECOPVAL,VECOPODR,TEND,HTSENSOR,VEXPE,MMEXE,MMTEM,MTMIN,MTMAX = 'suction','random_number_samples','duration_stimulus','initial_samples','time_between_stimulus','name_file','name_folder','sleep','opening_valves','vector_analy_odor','tendency','sensor_temperature','experiment_version','execution_mode','temperature_mode','minimum_temperature','maximum_temperature'
PIDPERIOD,MAXLIMITUPPERBOUND,MINLIMITUPPERBOUND,MAXLIMITLOWERBOUND,MINLIMITLOWERBOUND,ALPHA,MAXPKVAL,MINPKVAL = 'reference_signal_period','upper_maximum_limit','upper_minimum_limit','lower_maximum_limit','lower_minimum_limit','alpha_value','maximum_value','minimum_value'
RDPORT,HTPORT,MTPORT,RSTCE,SDFOLDER,VALPOS,NMUETS,SLEEPM,SLEEPTYH,VCC,TEMPPORT,TYHSENSOR,ELECPORTS,SENTYPE,RDTIME = 'reading_tgs_port','heating_port','engines_pin','resistance','storage','valves_position','number_samples','frecuency_samples','frecuency_tyh_samples','vcc','reading_tyh_port','model_tyh_sensor','electrovalves_port','model_tgs_sensor','reading_time'
ALL_TRANSITIONS,ALEATORY,USER_TRANSITIONS = 1,2,3

# Power, ground and reset ports
PGRPORTS = ['P9_1','P9_2','P9_3','P9_4','P9_5','P9_6','P9_7','P9_8','P9_9','P9_10','P9_32','P9_34','P9_43','P9_44','P9_45','P9_46','P8_1','P8_2']
ADCS = ['P9_33','P9_35','P9_36','P9_37','P9_38','P9_39','P9_40']
PWMS = ['P8_13','P8_19','P9_14','P9_16','P9_21','P9_22','P9_42']

experiment_keywords = [[MODULACION,NMUESTRAS,NEXPERIMENTOS,SUCCION,SWESTIM,SINICIO,SBESTIM,NFILE,NFOLDER,VECOPVAL,VEXPE,SLEEP],
    [TEND,HTSENSOR],[MMEXE,MMTEM,MTMIN,MTMAX],[PIDPERIOD,MAXLIMITUPPERBOUND,MINLIMITUPPERBOUND,MAXLIMITLOWERBOUND,MINLIMITLOWERBOUND,ALPHA,HTSENSOR,MAXPKVAL,MINPKVAL]]
platform_keywords = [RDPORT,HTPORT,MTPORT,RSTCE,SDFOLDER,VALPOS,NMUETS,SLEEPM,SLEEPTYH,VCC,TEMPPORT,TYHSENSOR,ELECPORTS,SENTYPE,RDTIME]

lista_errores = ["El numero de elementos de la expresion: %s no coincide con el numero de experimentos introducidos",
        "La expresion %s esta mal formada","El identificador %s no existe","La version del experimento: %d no es correcta",
        "El puerto de lectura de datos debe ser un puerto ADC, revise la configuracion",
        "El puerto de lectura de datos debe ser un puerto GPIO para martinelli, revise la configuracion",
        "El puerto de calentamiento del sensor y el de control del motor deben ser puertos PWM, revise la configuracion"]



############################ NUEVO ############################
def tratar_elemento(expresion,valvulas=False):
    lst = []
    for elem in expresion.split(','):
        if ':' in elem:
            ini,fin,salto = elem.split(':') if elem.count(':') == 2 else (elem+':1').split(':')
            lst+=list(range(int(ini),int(fin)+int(salto),int(salto))) if valvulas == False else [[[int(i)]] for i in range(int(ini),int(fin)+int(salto),int(salto))]
        elif '+' in elem or '-' in elem:
            lst.append([tratar_elemento(value) if '+' not in value else [tratar_elemento(value2)[0] for value2 in value.split('+')] for value in elem.split('-')])
        elif '(' in elem:
            elem,rept = re.split("[()]",elem)[:2] # Take the two first elements
            for e in range(int(rept)):
                try:
                    lst.append(literal_eval(elem) if valvulas == False else [[literal_eval(elem)]])
                except:
                    lst.append(elem)
        elif elem == '':
            continue
        else:
            try:
                lst.append(literal_eval(elem) if valvulas == False else [[literal_eval(elem)]])
            except:
                lst.append(elem)
    return lst

def tratamiento_expresion(expresion,repeticiones,valvulas=False):
    expresion,lst,rept = re.split('(\{|\}\([0-9]+\)|\})',expresion)[::-1],[[]],[]
   
    try:
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
                lst.append(tratar_elemento(elem,valvulas)+lst.pop())
    except:
        print(lista_errores[1]%(expresion))
        return exit(1)

    lst = lst.pop()
    if isinstance(lst[-1],str) and '*' in lst[-1]:
        try:
            value = literal_eval(lst[-1][:-1])
        except:
            value = lst[-1][:-1]
        lst.pop()
        lst+=[value for i in range(repeticiones-len(lst))]

    if len(lst) != repeticiones:
        print(lista_errores[0]%(''.join(expresion[::-1]))) # Se reconstruye la cadena inicial
        return exit(1)
        
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
    dict[keyword_mod] = mod
    keywords_modulation = list(set(experiment_keywords[0]+experiment_keywords[mod]))

    ### CARGO VALORES POR DEFECTO ###
    dict[VALPOS] = 'P'
    dict[SENTYPE] = 3
    dict[RDTIME] = 0.1
    dict[ELECPORTS] = ['P8_10','P8_12','P8_14','P8_16']

    for keyword,val_keyword in zip(lst_keywords,lst_values):
        if keyword not in platform_keywords and keyword not in keywords_modulation:
            print (lista_errores[2]%(keyword))
            return -1
        else:
            dict[keyword] = val_keyword

    rest_keywords_modulation = list(set(experiment_keywords[0]+experiment_keywords[mod])-set(lst_keywords))
    for elem in rest_keywords_modulation:
        dict[elem] = '0*'

    rest_keywords_platform = list(set(platform_keywords)-set(lst_keywords)-set([VALPOS,SENTYPE,RDTIME,ELECPORTS]))
    for elem in rest_keywords_platform:
        dict[elem] = ''

    return dict

def tratamiento_fichero_configuracion(dict):

    rept,mod = int(dict.pop(NEXPERIMENTOS)),int(dict.pop(MODULACION))
    versiones = tratamiento_expresion(dict.pop(VEXPE),rept)

    # Guardamos los datos en el diccionario, los guardo todos primero, porque puede haber datos necesarios para tratar que reciba al final
    for key,value in dict.items():
        #print(key,value)
        if key in conf_values:
            dict[key] = tratamiento_plataforma(key,value,mod)
        else:
            dict[key] = tratamiento_experimento(key,value,versiones,rept)
            
    
    #print("MUESTRAS",dict[SVECOPODR])
    # Creamos las series de odorantes que se van a analizar
    vecs_open_valves_ret,vector_open_valves,muestras,pos_valvulas,valvulas_seleccionadas,nombre_valvulas_abrir = [],dict[VECOPVAL],dict.pop(NMUESTRAS),dict[VALPOS],dict[ELECPORTS],[]
    for version in versiones:
        if version == ALL_TRANSITIONS:
            valvulas_abrir = todas_transiciones(valvulas_seleccionadas)
        elif version == ALEATORY:
            valvulas_abrir = crear_transiciones(muestras.pop(0),valvulas_seleccionadas)
        elif version == USER_TRANSITIONS:
            valvulas_abrir = vector_open_valves.pop(0)
        else:
            print (lista_errores[3]%(version))
            return exit(1)

        vecs_open_valves_ret.append(valvulas_abrir
            if pos_valvulas == 'P' else [list(set(range(1,len(valvulas_seleccionadas)+1))-set(lst)) for lst in valvulas_abrir])
        nombre_valvulas_abrir.append(valvulas_abrir)

    dict[VECOPVAL] = vecs_open_valves_ret
    dict[VECOPODR] = nombre_valvulas_abrir

    return mod,dict

def tratamiento_experimento(key,value,versiones,repeticiones):

    if key == NMUESTRAS:
        expr = tratamiento_expresion(value,versiones.count(2))
    elif key == VECOPVAL:
        expr = tratamiento_expresion(value,versiones.count(3),True)
    else:
        expr = tratamiento_expresion(value,repeticiones)
    
    return expr

def tratamiento_plataforma(key,value,mod):
    
    if key == RDPORT:
        if value not in ADCS and mod != 3:
            print (lista_errores[4])
            return exit(1)
        elif  mod == 3 and (value in ADCS or value in PWMS or value in PGRPORTS):
            print (lista_errores[5])
            return exit(1)
        else:
            return value
    elif (key == HTPORT or key == MTPORT) and value not in PWMS:
        print (lista_errores[6])
        return exit(1)
    elif key == ELECPORTS:
        expr = value.split(",") if isinstance(value,list) == False else value
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

    return [[rn.randint(1,len(total_valvulas))] for i in range(switch)]

def todas_transiciones(set_total_vales):
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
    #print("CACA DE VACA",x,d1)
    ret = []
    for v in x:
         #print(v,d1)
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