# coding: utf-8
#!/usr/bin/python

from datetime import datetime, date
import sys,os
import modulaciones as modulacion
import tratamiento_cadenas as tc
import signal

# Valores límite para la ejecucion
MAXSUCCION = 100
MINSUCCION = 30
MAXHEAT = 100
MINHEAT = 1
MINSWICHT = 1
MINTENDENCIA = 0
MINTIEMPO = 0
MINSAMPLESINIO = 10

tipos_modulacion = {1:modulacion.Puro,2:modulacion.Regresion,3:modulacion.Martinelli,4:modulacion.MPID}
#tipos_representacion = {1:graficas.plot_grafs_diccionary,2:graficas.plot_elems_grafs_diccionary,3:graficas.plot_elems_div_grafs_diccionary}
#tipos_representacion_martinelli = {1:graficas.plot_martinelli,2:graficas.plot_martinelli_time_pulses,3:graficas.plot_martinelli_div_graf}

#Se comprueba que los datos introducidos estén acotados entre los valores deseados
def comprobacion_datos_introducidos(mod,experiment_data_dict):
    
    #Caso base, opciones comunes
    for suc,sw,sini in zip(experiment_data_dict[tc.SSUCCION],experiment_data_dict[tc.SSWESTIM],experiment_data_dict[tc.SSINICIO]):
        if suc > MAXSUCCION or suc < MINSUCCION or sw < MINSWICHT or (mod != 3 and sini < MINSAMPLESINIO):
            print ('PARAMETROS(S) INCORRECTO(S).\n Por favor revise los parametros introducidos y vuelva a empezar')
            exit(1)

    #Caso de regresion
    if mod == 2:
        for tend,he in zip(experiment_data_dict[tc.STEND],experiment_data_dict[tc.SHTSENSOR]):
            if he < MINHEAT or he > MAXHEAT or tend < MINTENDENCIA:
                print ('PARAMETROS(S) INCORRECTO(S).\n Por favor revise los parametros introducidos y vuelva a empezar')
                exit(1)

def help():
    print("Ayuda para la ejecucion de PyHuele")
    print("Forma para la ejecucion: sudo python3 PyHuele arg1 arg2")
    print("arg1:\n\t1: para la captura desde PyHuele\n\t2: para la captura desde GPyHuele\n\t3: para el envio de la senal para pausar/continuar la captura de odorantes")
    print("arg2: Fichero de configuracion para la ejecucion")

def main():

    if sys.argv[1] == "help" or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help()
        exit()

    # Opcion de enviar una senial al programa en ejecucion
    #print("Argumentos pasados: ",sys.argv,len(sys.argv),int(sys.argv[1]))
    if len(sys.argv) == 2 and sys.argv[1] == '3':
        try:
            f = open("file_daemon.txt","r")
        except FileNotFoundError:
            print("El programa no se encuentra capturando datos actualmente")
            exit()
            
        pid = int(f.readline())
        os.kill(pid,signal.SIGUSR1)
        f.close()
        exit()
    
    path_config_experiment = sys.argv[1]
    
    if sys.argv[1] == 1:
        mod,experiment_data_dict,platform_data_dict = tc.leer_ficheros_graphicPyHuele(path_config_experiment,path_config_platform)
    else:
        try:
                mod,experiment_data_dict = tc.tratamiento_fichero_configuracion(
                        tc.leer_fichero_configuracion(path_config_experiment))
        except:
                print ("Se encontro un error al procesar los datos, compruebe que el fichero este bien escrito")
                return exit(1)
                
    comprobacion_datos_introducidos(mod,experiment_data_dict)
    modul = tipos_modulacion[mod](experiment_data_dict)
    path = modul.iniciar_captura_datos()

    return

if __name__ == '__main__':
        main()
