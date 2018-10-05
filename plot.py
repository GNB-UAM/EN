# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import os

#rojo claro,verde claro, azul claro, azul oscuro, rosa, naranja, amarillo, verde oscuro, verde oliva, negro, marron, violeta, burdeos, aguamarina, gris, rojo palido
colors = ["#FE0000","#25FD00","#00BAFE","#1400FD","#FD00CE","#FD7600","#FEF900","#2D5D0A","#83B62B","#000000","#800000","#87048F","#820624","#08EC81","#827E83","#D96B4E"]
    
map_colors = ["Purples","Greens","Blues","Greys","Oranges","Reds","PuRd","RdPu","copper"]
lst_subplt = [1,2,6,7,11,12,16,14,5,3,9,4,15,10,8,13]

# Hasta ahora, va todo bien

#TO DO
#Poner martinelli


def no_normalizar(x):
    return x

def normalizar(x):
    """
        Normaliza los datos entre 0 y 1.
        Normaliza una serie de numeros, representandolos entre 0 y 1
        Parametros:
            x -- Serie que se quiere normalizar
        Retorno:
            Lista con los valores normalizados
    """
    miin = min(x)
    diff = max(x) - miin
    if diff == 0:
        return [1.0]*len(x)

    return [(value - miin)*1.0/diff for value in x] #Se multiplica por 1.0 para que el valor sea considerado un double.

# Normalizar utilizando el Z_Score
def normalizar_Z_Score(x):
    """
        Normaliza los datos utilizando el método del ZScore.
        Normaliza una serie de numeros, utilizando para ello el método del ZScore.
        Parametros:
            x -- Serie que se quiere normalizar
        Retorno:
            Lista con los valores normalizados
    """
    media,desviacion = mean(x,axis=0),std(x,axis=0)
    return [(value-media)/desviacion for value in x]

def get_files_folder(folder,ext=".dat"):
    """
        Devuelve los ficheros de una carpeta
        Devuelve el nombre de los ficheros de una carpeta, que tengan un formato concreto
        Parametros:
            folder -- Carpeta de donde obtener los ficheros
            ext -- Extensión de los ficheros
        Retorno:
            lstFiles -- Lista con los ficheros obtenidos
    """
    lstFiles = []
    lstDir = os.walk(folder)

    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ext):
                lstFiles.append(folder+'/'+nombreFichero+extension if '/' not in folder else folder+nombreFichero+extension)

    lstFiles.sort()
    return lstFiles

# Imprimir lineas verticales
def plot_vertical_lines(s_ini,switc,n_times,CTE):
    """
        Imprime lineas verticales de separación entre odorantes.
        Imprime lineas verticales de separación entre los distintos odorantes que componen una captura.
        Parametros:
            s_ini -- muestras iniciales del experimento
            switc -- tiempo en segundos que un odorante es analizado
            n_times -- cuanto gases se han analizado
            CTE -- si se ha dejado un tiempo de aire entre odorantes.
        Retorno:
    """    

    cont = 0
    plt.axvline(cont,color="black",linewidth=0.8)
    #cont+=s_ini
    #plt.axvline(cont,color="black",linewidth=0.8)

    for i in range(n_times):
        if CTE > 0:
            cont+=CTE
            plt.axvline(cont,color="black",linewidth=0.8)
        cont+=switc
        plt.axvline(cont,color="black",linewidth=0.8)
        
    if CTE > 0:
        cont+=CTE
        plt.axvline(cont,color="black",linewidth=0.8)

    return

def treat_data(file,norm,columns):
        
    data = np.genfromtxt(file,skip_header=1,delimiter=' ').T
    switch,s_ini,CTE,ntran = np.genfromtxt(file,skip_footer=len(data[0]),delimiter=' ') #Saco la cabecera
    switch,s_ini,CTE,ntran = int(switch),int(s_ini),int(CTE),int(ntran)
    lsts = [norm(data[c]) for c in columns]
    
    return lsts,switch,s_ini,CTE,ntran

def plot_lst(lsts,switch,fig,div_plt,sini,colors=colors):
        """
            Imprime los valores de las sublistas
            Imprime los valores de las sublistas en una gráfica, en varias gráficas o en subgráficas.
            Parametros:
                lsts -- lista de listas con los valores que se van a imprimir
                s_ini -- muestras iniciales de la captura
                switch -- tiempo en que cada gas es analizado
                ntran -- número de odorantes analizados
                CTE -- tiempo en segundos de aire entre gases
                norm -- booleano que indica si los datos están normalizados            
                fig -- booleano para indicar si se van a imprimir todos en la misma gráfica o no

            Retorno:
        """
        
        if fig == True:
            plt.figure(1)

        if div_plt == True:
            lst_subpltdata_xaxisrange = list(zip(*[iter(range(len(lsts[0][sini+switch:])))]*switch))

        for figure,value in enumerate(lsts): #La cosa de delante es para indicar la figura 1 2 ó 3
            #value = norm(value[s_ini:])
            if fig == False:
                plt.figure(figure+1)
            if div_plt == True:
                # Hay que poner el [1:], porque la muestra 0, es la transición de las muestras iniciales al primer odorante
                lst_subpltdata = list(zip(*[iter(value[sini:])]*switch))[1:]
                for subplt,xaxissubpltdata,subpltdata in zip(lst_subplt,lst_subpltdata_xaxisrange,lst_subpltdata):
                    ax = plt.subplot(4,4,subplt)
                    ax.plot(xaxissubpltdata,subpltdata,'-',c=colors[figure%len(colors)])
                    # Lo siguiente reduce el tamaño de los valores de los ejes para que no se solapen
                    ax.tick_params(axis='both', which='major', labelsize=5)
                    ax.tick_params(axis='both', which='minor', labelsize=4) 
            else: 
                plt.plot(value[sini:],'-',c=colors[figure%len(colors)])
        
        return

def save_plot(s_ini,switch,ntran,CTE,n_figs,xaxis,yaxis,titles,image_folder,div_plt,norm,sub_name=''):
        """
            Guarda las gráficas
            Guarda las gráficas en ficheros, en la carpeta que se le indica, poniendo los valores de los ejes y los titulos.
            Parametros:
                lsts -- lista de listas con los valores que se van a imprimir
                s_ini -- muestras iniciales de la captura
                switch -- tiempo en que cada gas es analizado
                ntran -- número de odorantes analizados
                CTE -- tiempo en segundos de aire entre gases
                norm -- booleano que indica si los datos están normalizados            
                fig -- booleano para indicar si se van a imprimir todos en la misma gráfica o no

            Retorno:
                name -- nombre del fichero
        """
        sub_namep = sub_name.split("/")[-1]
        for i,ylabel,title in zip(range(n_figs),yaxis,titles):
            fig = plt.figure(i+1)
            if div_plt == True:
                fig.suptitle(title, fontsize=16)
                fig.text(0.5, 0.04, xaxis, ha='center')
                fig.text(0.04, 0.5, ylabel, va='center', rotation='vertical')
                name = "norm_div_subplots_Plot_sensor_"+sub_namep+"_"+ylabel+".eps" \
                    if norm == True else "div_subplots_Plot_sensor_"+sub_namep+"_"+ylabel+".eps"
            else:
                plot_vertical_lines(s_ini,switch,ntran,CTE)
                plt.xlabel(xaxis,fontsize=23)
                plt.ylabel(ylabel,fontsize=23)
                plt.title(title,fontsize=30)
                name = "norm_Plot_sensor_"+sub_namep+"_"+ylabel+".eps" \
                    if norm == True else "Plot_sensor_"+sub_namep+"_"+ylabel+".eps"

            plt.savefig(image_folder+name,format="eps")
            plt.close(fig)

        return

# Funciona correctamente
def plot_file_columns_together(file,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    lsts,switch,s_ini,CTE,ntran = treat_data(file=file,norm=norm,columns=columns)
    plot_lst(lsts=lsts,switch=switch,fig=True,div_plt=False,colors=colors[:len(lsts)],sini=s_ini)
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=1,
        xaxis=xaxis,yaxis=yaxis,titles=titles,image_folder=image_folder,div_plt=False,norm=norm,sub_name=file)

    return

def plot_file_columns_together_div_subplots(file,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_file_columns_together(file=file,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,
        titles=titles,div_plt=True)
    return

# Funciona correctamente
def plot_files_separately_columns_together(files,columns,image_folder,norm,xaxis,yaxis,titles):

    for file in files:
        plot_file_columns_together(file=file,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles)

    return

def plot_files_separately_columns_together_div_subplots(files,columns,image_folder,norm,xaxis,yaxis,titles):

    for file in files:
        plot_file_columns_together(file=file,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,
            titles=titles,div_plt=True)

    return

# Funciona correctamente
def plot_files_together_columns_together(files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):
    
    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    for pos,file in enumerate(files):
        lsts,switch,s_ini,CTE,ntran = treat_data(file=file,norm=norm,columns=columns)
        plot_lst(lsts=lsts,switch=switch,fig=True,div_plt=div_plt,colors=[colors[pos%len(colors)]],sini=s_ini)
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=1,xaxis=xaxis,yaxis=yaxis,
        titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name=file+"_plot_files_together_columns_together")
    return

def plot_files_together_columns_together_div_subplots(files,columns,image_folder,norm,xaxis,yaxis,titles):
    
    plot_files_together_columns_together(files=files,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,
        titles=titles,div_plt=True)

    return

# Funciona correctamente
def plot_folder_files_separately_columns_together(folder,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    tfiles = get_files_folder(folder)
    for posfile in files:
        plot_file_columns_together(file=tfiles[posfile],columns=columns,image_folder=image_folder,norm=norm,
            xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)

    return

def plot_folder_files_separately_columns_together_div_subplots(folder,files,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folder_files_separately_columns_together(folder=folder,files=files,columns=columns,image_folder=image_folder,
        norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

    return

# Funciona correctamente
def plot_folder_files_together_columns_together(folder,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    tfiles = get_files_folder(folder)
    tfiles = [tfiles[posfile] for posfile in files]
    plot_files_together_columns_together(files=tfiles,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)

def plot_folder_files_together_columns_together_div_subplots(folder,files,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folder_files_together_columns_together(folder=folder,files=files,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_files_separately_columns_together(folders,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    for folder in folders:
        plot_folder_files_separately_columns_together(folder=folder,files=files,columns=columns,
            image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)

    return

def plot_folders_files_separately_columns_together_div_subplots(folders,files,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folders_files_separately_columns_together(folders=folders,files=files,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_files_together_columns_together(folders,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    for folder,posfiles,map_color in zip(folders,files,map_colors):
        tfiles = get_files_folder(folder)
        colors = np.linspace(0.3,1,len(posfiles))
        mymap = plt.get_cmap(map_color)
        my_colors = mymap(colors)
        for posfile,color in zip(posfiles,my_colors):
            lsts,switch,s_ini,CTE,ntran = treat_data(file=tfiles[posfile],norm=norm,columns=columns)
            plot_lst(lsts=lsts,switch=switch,fig=True,div_plt=div_plt,colors=[color],sini=s_ini)
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=1,xaxis=xaxis,yaxis=yaxis,titles=titles,
        image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name=tfiles[-1]+"_plot_folders_files_together_columns_together")
    return

def plot_folders_files_together_columns_together_div_subplots(folders,files,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folders_files_together_columns_together(folders=folders,files=files,columns=columns,image_folder=image_folder,
        norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folder_chunks_together_columns_together(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    tfiles = get_files_folder(folder)
    tfiles = list(zip(*[iter(tfiles)]*chunk_size))
    for pos,map_color in zip(schunks,map_colors):
        mymap = plt.get_cmap(map_color)
        colors = np.linspace(0.3,1,len(tfiles[pos]))
        my_colors = mymap(colors)
        for file,color in zip(tfiles[pos],my_colors):
            lsts,switch,s_ini,CTE,ntran = treat_data(file=file,norm=norm,columns=columns)
            plot_lst(lsts=lsts,switch=switch,fig=True,div_plt=div_plt,colors=[color],sini=s_ini)

    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=1,
        xaxis=xaxis,yaxis=yaxis,titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name="folder_chunks_columns_together")

    return

def plot_folder_chunks_together_columns_together_div_subplots(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folder_chunks_together_columns_together(folder=folder,chunk_size=chunk_size,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folder_chunks_separately_columns_together(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    tfiles = get_files_folder(folder)
    tfiles = list(zip(*[iter(tfiles)]*chunk_size))
    for pos,map_color in zip(schunks,map_colors):
        colors = np.linspace(0.3,1,len(tfiles[pos]))
        mymap = plt.get_cmap(map_color)
        my_colors = mymap(colors)
        for file,color in zip(tfiles[pos],my_colors):
            lsts,switch,s_ini,CTE,ntran = treat_data(file=file,norm=norm,columns=columns)
            plot_lst(lsts=lsts,switch=switch,fig=True,div_plt=div_plt,colors=[color],sini=s_ini)

        save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=1,
            xaxis=xaxis,yaxis=yaxis,titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name="folder_chunks_separately_columns_together_"+str(pos))

    return

def plot_folder_chunks_separately_columns_together_div_subplots(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folder_chunks_separately_columns_together(folder=folder,chunk_size=chunk_size,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_chunks_separately_columns_together(folders,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    for folder in folders:
        plot_folder_chunks_separately_columns_together(folder=folder,chunk_size=chunk_size,schunks=schunks,columns=columns,
            image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)

    return

def plot_folders_chunks_separately_columns_together_div_subplots(folders,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folders_chunks_separately_columns_together(folders=folders,chunk_size=chunk_size,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_chunks_together_columns_together(folders,chunk_sizes,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    for folder,chunk_size,schunk,map_color in zip(folders,chunk_sizes,schunks,map_colors):
        tfiles = get_files_folder(folder)
        tfiles = list(zip(*[iter(tfiles)]*chunk_size))
        colors = np.linspace(0.3,1,len(schunk))
        mymap = plt.get_cmap(map_color)
        my_colors = mymap(colors)
        for pos,color in zip(schunk,my_colors):
            for file in tfiles[pos]:
                lsts,switch,s_ini,CTE,ntran = treat_data(file=file,norm=norm,columns=columns)
                plot_lst(lsts=lsts,switch=switch,fig=True,div_plt=div_plt,colors=[color],sini=s_ini)
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=1,xaxis=xaxis,yaxis=yaxis,titles=titles,
        image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name=file+"_plot_folders_chunks_together_columns_together")
    return

def plot_folders_chunks_together_columns_together_div_subplots(folders,chunk_sizes,schunks,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folders_chunks_together_columns_together(folders=folders,chunk_sizes=chunk_sizes,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

def treat_plot_elems(files,norm,columns,colors=colors,div_plt=False):
        """
            Realiza la lectura de los ficheros, su normalización y su impresión posterior.
            Realiza la lectura de los ficheros, su normalización y su impresión posterior.
            Parametros:
                file -- fichero cuyos valores queremos representar
                image_folder -- carpeta donde guardar las imágenes
            Retorno:
        """
        for pos,file in enumerate(files):
            lsts,switch,s_ini,CTE,ntran = treat_data(file=file,norm=norm,columns=columns)
            plot_lst(lsts=lsts,switch=switch,colors=[colors[pos%len(colors)]],fig=False,div_plt=div_plt,sini=s_ini)

        return switch,s_ini,CTE,ntran

# Funciona correctamente
def plot_file_columns_separately(file,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    switch,s_ini,CTE,ntran = treat_plot_elems(files=[file],norm=norm,div_plt=div_plt,columns=columns,colors=colors)
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=min(len(yaxis),len(titles)),xaxis=xaxis,yaxis=yaxis,
        titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name=file)

    return

def plot_file_columns_separately_div_subplots(file,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_file_columns_separately(file=file,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,
        yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_files_separately_columns_separately(files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    for file in files:
        plot_file_columns_separately(file=file,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,
            titles=titles,div_plt=div_plt)
    return

def plot_files_separately_columns_separately_div_subplots(files,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_files_separately_columns_separately(files=files,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,
        yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_files_together_columns_separately(files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):
    
    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    switch,s_ini,CTE,ntran = treat_plot_elems(files=files,norm=norm,div_plt=div_plt,columns=columns,colors=colors)
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=min(len(yaxis),len(titles)),xaxis=xaxis,yaxis=yaxis,
        titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name=files[-1]+"_plot_files_together_columns_separately")
    return

def plot_files_together_columns_separately_div_subplots(files,columns,image_folder,norm,xaxis,yaxis,titles):
    
    plot_files_together_columns_separately(files=files,columns=columns,image_folder=image_folder,norm=norm,xaxis=xaxis,
        yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folder_files_separately_columns_separately(folder,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    tfiles = get_files_folder(folder)
    for posfile in files:
        plot_file_columns_separately(file=tfiles[posfile],columns=columns,image_folder=image_folder,norm=norm,
            xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)

    return

def plot_folder_files_separately_columns_separately_div_subplots(folder,files,columns,image_folder,norm,xaxis,yaxis,titles):
    plot_folder_files_separately_columns_separately(folder=folder,files=files,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folder_files_together_columns_separately(folder,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    tfiles = get_files_folder(folder)
    tfiles = [tfiles[pos] for pos in files]
    plot_files_together_columns_separately(files=tfiles,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)

    return

def plot_folder_files_together_columns_separately_div_subplots(folder,files,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folder_files_together_columns_separately(folder=folder,files=files,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_files_separately_columns_separately(folders,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    for folder in folders:
        plot_folder_files_separately_columns_separately(folder=folder,files=files,columns=columns,
            image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)
    return

def plot_folders_files_separately_columns_separately_div_subplots(folders,files,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folders_files_separately_columns_separately(folders=folders,files=files,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_files_together_columns_separately(folders,files,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    for folder,posfiles,map_color in zip(folders,files,map_colors):
        lstfiles,tfiles = [],get_files_folder(folder)
        colors = np.linspace(0.3,1,len(posfiles))
        mymap = plt.get_cmap(map_color)
        my_colors = mymap(colors)
        for posfile in posfiles: #treat_plot_elems(file,norm,False,columns,colors=colors)
            lstfiles.append(tfiles[posfile])

        switch,s_ini,CTE,ntran = treat_plot_elems(files=lstfiles,norm=norm,columns=columns,div_plt=div_plt,colors=my_colors)

    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=min(len(yaxis),len(titles)),xaxis=xaxis,yaxis=yaxis,titles=titles,
        image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name=lstfiles[-1]+"_plot_folders_files_together_columns_separately")
    return

def plot_folders_files_together_columns_separately_div_subplots(folders,files,columns,image_folder,norm,xaxis,yaxis,titles):
    
    plot_folders_files_together_columns_separately(folders=folders,files=files,columns=columns,image_folder=image_folder,norm=norm,
        xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folder_chunks_separately_columns_separately(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    tfiles = get_files_folder(folder)
    tfiles = list(zip(*[iter(tfiles)]*chunk_size))
    for pos,map_color in zip(schunks,map_colors):
        colors = np.linspace(0.3,1,len(tfiles[pos]))
        mymap = plt.get_cmap(map_color)
        my_colors = mymap(colors)
        switch,s_ini,CTE,ntran = treat_plot_elems(files=tfiles[pos],norm=norm,columns=columns,div_plt=div_plt,colors=my_colors)
        save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=min(len(yaxis),len(titles)),
            xaxis=xaxis,yaxis=yaxis,titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name="chunk_"+str(pos)+"_plot_folder_chunks_separately_columns_separately")

def plot_folder_chunks_separately_columns_separately_div_subplots(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles):

    plot_folder_chunks_separately_columns_separately(folder=folder,chunk_size=chunk_size,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folder_chunks_together_columns_separately(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    tfiles = get_files_folder(folder)
    tfiles = list(zip(*[iter(tfiles)]*chunk_size))
    for pos,map_color in zip(schunks,map_colors):
        colors = np.linspace(0.3,1,len(tfiles[pos]))
        mymap = plt.get_cmap(map_color)
        my_colors = mymap(colors)
        switch,s_ini,CTE,ntran = treat_plot_elems(files=tfiles[pos],norm=norm,columns=columns,div_plt=div_plt,colors=my_colors)
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=min(len(yaxis),len(titles)),
        xaxis=xaxis,yaxis=yaxis,titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name="chunk_"+str(pos)+"_plot_folder_chunks_together_columns_separately")

def plot_folder_chunks_together_columns_separately_div_subplots(folder,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles):
    
    plot_folder_chunks_together_columns_separately(folder=folder,chunk_size=chunk_size,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_chunks_separately_columns_separately(folders,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    for folder in folders:
        plot_folder_chunks_separately_columns_separately(folder=folder,chunk_size=chunk_size,schunks=schunks,columns=columns,
            image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=div_plt)

    return

def plot_folders_chunks_separately_columns_separately_div_subplots(folders,chunk_size,schunks,columns,image_folder,norm,xaxis,yaxis,titles):
    
    plot_folders_chunks_separately_columns_separately(folders=folders,chunk_size=chunk_size,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)

# Funciona correctamente
def plot_folders_chunks_together_columns_separately(folders,chunk_sizes,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):

    os.makedirs(image_folder, mode=0o755, exist_ok=True)
    for folder,chunk_size,schunk,map_color in zip(folders,chunk_sizes,schunks,map_colors):
        tfiles = get_files_folder(folder)
        tfiles = list(zip(*[iter(tfiles)]*chunk_size))
        colors = np.linspace(0.3,1,len(schunk))
        mymap = plt.get_cmap(map_color)
        my_colors = mymap(colors)
        for pos,color in zip(schunk,my_colors):
            switch,s_ini,CTE,ntran = treat_plot_elems(files=tfiles[pos],norm=norm,columns=columns,div_plt=div_plt,colors=[color])
    
    save_plot(s_ini=s_ini,switch=switch,ntran=ntran,CTE=CTE,n_figs=min(len(yaxis),len(titles)),xaxis=xaxis,yaxis=yaxis,
        titles=titles,image_folder=image_folder,div_plt=div_plt,norm=norm,sub_name=folder+"_plot_folders_chunks_together_columns_separately")
    return

def plot_folders_chunks_together_columns_separately_div_subplots(folders,chunk_sizes,schunks,columns,image_folder,norm,xaxis,yaxis,titles,div_plt=False):
    
    plot_folders_chunks_together_columns_separately(folders=folders,chunk_sizes=chunk_sizes,schunks=schunks,columns=columns,
        image_folder=image_folder,norm=norm,xaxis=xaxis,yaxis=yaxis,titles=titles,div_plt=True)