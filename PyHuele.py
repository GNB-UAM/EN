# coding: utf-8
#!/usr/bin/python

from datetime import datetime, date
import sys
import modulaciones as modulacion
import tratamiento_cadenas as tc

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

def main():
	
	path_config_experiment = sys.argv[1]
	path_config_platform = sys.argv[2]
	execution = int(sys.argv[3]) if len(sys.argv) == 4 else 0

	if execution == 1:
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
