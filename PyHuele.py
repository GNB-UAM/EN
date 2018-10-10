# coding: utf-8
#!/usr/bin/python

from datetime import datetime, date
import sys
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

def help():
    print("Ayuda para la ejecución de PyHuele")
    print("Forma para la ejecución: sudo PyHuele arg1 arg2")
    print("arg1:\n\t1: para la captura desde PyHuele\n\t2: para la captura desde GPyHuele\n\t3: para el envio de la señal para pausar/continuar la captura de odorantes")
    print("arg2: Fichero de configuración para la ejecución")

def main():

    if sys.argv[1] == "help" or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help()
        exit()

    # Opcion de enviar una senial al programa en ejecucion
    if sys.argv[1] == 3:
        try:
            f = open("file_daemon","r")
        except FileNotFoundError:
            print("No se encuentra ejecutando el programa de captura\n")
            exit()
            
        pid = int(f.readline())
        signal.pthread_kill(pid,signal.SIGUSR1)
        f.close()
    
    path_config_experiment = sys.argv[2]
    path_config_platform = sys.argv[3]

    if sys.argv[1] == 1:
    	mod,experiment_data_dict,platform_data_dict = tc.leer_ficheros_graphicPyHuele(path_config_experiment,path_config_platform)
    else:
	try:
        	mod,experiment_data_dict,platform_data_dict = tc.tratamiento_datos(tc.leer_fichero_experimento(path_config_experiment),tc.leer_fichero_conf_plataforma(path_config_platform))
	except:
		print ("Se encontro un error al procesar los datos, compruebe que el fichero este bien escrito")
		return exit(1)
		
        for suc,sw,sini in zip(experiment_data_dict[tc.SSUCCION],experiment_data_dict[tc.SSWESTIM],experiment_data_dict[tc.SSINICIO]):
            if suc > MAXSUCCION or suc < MINSUCCION or sw < MINSWICHT or (mod != 3 and sini < MINSAMPLESINIO):
	        print ('PARAMETROS(S) INCORRECTO(S).\n Por favor revise los parametros introducidos y vuelva a empezar')
	        exit(1)

        if mod == 2:
            for tend,he in zip(experiment_data_dict[tc.STEND],experiment_data_dict[tc.SHTSENSOR]):
	        if he < MINHEAT or he > MAXHEAT or tend < MINTENDENCIA:
	            print ('PARAMETROS(S) INCORRECTO(S).\n Por favor revise los parametros introducidos y vuelva a empezar')
		    exit(1)

    modul = tipos_modulacion[mod](experiment_data_dict,platform_data_dict)
    path = modul.iniciar_captura_datos()

    return

if __name__ == '__main__':
	main()
