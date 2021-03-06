#===============================
# Import
#===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#from geopandas import *

# from plotnine import *

#para ajustar las fechas
import datetime


#===================================
# Dicionario de columnas
#===================================
Dic_col={'Base':
                             ['Material (Nombre)', 'Kilos Venta KG', 'Precio','Cliente'],
        'Fecha':
                             ['Día natural','Día Semana','Semana', 'Mes', 'Año'],
        'Ubicacion':
                             ['Centro','Población'],
        'Cliente Categoria':
                             ['Cluster','Segmento.1', 'Categoría Cliente'],
        'Cliente Atributos':
                             ['Año Creación', 'Material Favorito','Frecuencia Historica'] 
         ,'RFM Row':
                 ['Recency días','Frecuency_Row','Monetary']
        ,'RFM Customers':
                 ['Recency Actual','Frecuency Actual del Cliente','Monetary Actual']
        ,'Ticket Row':
                 ['Ticket Promedio','Ticket CV']
        ,'Ticket Customers':
                 ['Ticket Promedio Actual','Ticket CV Actual']
        }



#=========================================
#Abre y junta los datos referidos a la facuraciones electronicas
# file_direct_O: Dirección de donde se ubican los DataFrames
#=========================================

def RFM_Data_func(file_direct_O):
	"""
	Abre y junta los datos referidos a la facuraciones electronicas
	file_direct_O: Dirección de donde se ubican los DataFrames

	"""

	#======================================================================
	# CSV Rread
	#=====================================================================


	#======================================================================
	# R
	#=====================================================================

	file_direct=file_direct_O+'data_1010078_CT R'+'.csv'
	print(file_direct)
	col_names=pd.read_csv(file_direct,
	                      encoding="utf-8",sep=";",nrows=0).columns

	types_dict = {col: str for col in list(col_names)}

	data_i_R = pd.read_csv(file_direct,
	                   encoding="utf-8",sep=";",dtype=types_dict
	                      ,index_col='Unnamed: 0'
	                      )

	# Se debe agregar el parametro ,index_col='Unnamed: 0' 
	# de esta froma tal vez se pueda hacer un merge en base al indice

	#elimina una columna en especifico
	#DF_FULL.drop('Año natural', inplace=True, axis=1)
	print('R',data_i_R.shape)


	#======================================================================
	# F
	#=====================================================================

	file_direct=file_direct_O+'data_1010078_CT F'+'.csv'
	col_names=pd.read_csv(file_direct,
	                      encoding="utf-8",sep=";",nrows=0).columns

	types_dict = {col: str for col in list(col_names)}

	data_i_F = pd.read_csv(file_direct,
	                   encoding="utf-8",sep=";",dtype=types_dict
	                      ,index_col='Unnamed: 0'
	                      )

	# Se debe agregar el parametro ,index_col='Unnamed: 0' 
	# de esta froma tal vez se pueda hacer un merge en base al indice

	#elimina una columna en especifico
	#DF_FULL.drop('Año natural', inplace=True, axis=1)
	print(file_direct)
	print('F',data_i_F.shape)
	#======================================================================
	# M
	#=====================================================================

	file_direct=file_direct_O+'data_1010078_CT M'+'.csv'
	col_names=pd.read_csv(file_direct,
	                      encoding="utf-8",sep=";",nrows=0).columns

	types_dict = {col: str for col in list(col_names)}

	data_i_M = pd.read_csv(file_direct,
	                   encoding="utf-8",sep=";",dtype=types_dict
	                      ,index_col='Unnamed: 0'
	                      )

	# Se debe agregar el parametro ,index_col='Unnamed: 0' 
	# de esta froma tal vez se pueda hacer un merge en base al indice

	#elimina una columna en especifico
	#DF_FULL.drop('Año natural', inplace=True, axis=1)
	print(file_direct)
	print('M',data_i_M.shape)

	# ===================================================================
	# Merge
	# RFM
	#=====================================================================
	print('------------------------------------------------')
	print('Merge')
	print('RF',(pd.merge(data_i_R,data_i_F )).shape)
	print('RFM',pd.merge(pd.merge(data_i_R,
	                              data_i_F ) ,
	                    data_i_M).shape)
	DATA_i_RFM = pd.merge(pd.merge(data_i_R,data_i_F ),data_i_M)

	# del (data_i_R,data_i_F,data_i_M)
	return(DATA_i_RFM)


# =============================================================================
# Ajustar la data RFM_Data_func
# =============================================================================
def Ajuste_data_RFM(data):
    """
    Destinado a ajustar los valores de la funcion RFM_Data_func

    columnas como 
    for i in ['Kilos Venta KG'
        ,'Precio'
        ,'Recency días'
        ,'Frecuency_Row'
        ,'Monetary'
        ,'Ingreso de Venta CLP'
        
    """
    # data_f=data.copy()
    df = data.copy()
    # df=data_f
    # =================================
    # ELiminare dodos los valores Nan
    # =================================
    #for i in df.columns.to_list():
    #    df=df[df[i].notna()]



    #=================================
    # Proceso Recency a Int 
    #=================================


    df['Recency días']=df['Recency'].apply( lambda x:  x.split(' ')[0])

    #=================================
    # Proceso iterativo Pasar a numero
    #=================================

    for i in ['Kilos Venta KG'
        # ,'Venta Neta'
        ,'Precio'
        # RFM
        ,'Recency días'
        ,'Frecuency_Row'
        ,'Monetary'
        ,'Ingreso de Venta CLP'
        ]:

        df[i]=df[i].astype('float64').astype('int64')

    for i in ['Kilos Venta KG'
        # ,'Venta Neta'
        ,'Precio'
        # RFM
        ,'Recency días'
        # ,'Frecuency_Row'
        # ,'Monetary'
        ,'Ingreso de Venta CLP'
        ]:
        df[i]=df[i].astype('int64')     



    # ==========================================================================================
    # Ajuste de las fechas
    #-----------------------------------------------------------------------------------------
    df["Día natural"] = df["Día natural"].apply(lambda x: 
                                            datetime.datetime.strptime(str(x),
                                                                    '%Y-%m-%d').date())

    #Separacion fecha

    #ELiminado de DF_FULL
    #df['Semana']=df["Día natural"].apply(lambda x: x.isocalendar()[1] )
    #df['Mes']=df["Día natural"].apply(lambda x: x.month)
    #df['Año']=df["Día natural"].apply(lambda x: x.year)
    #df['Semana']=df['Semana'].astype('int64')

    # df['Año']=df['Año'].astype('int64')
    # D_W=['Lunes','Martes','Miércoles','Jueves', 'Viernes','Sábado','Domingo']
    # df['Día Semana']=df["Día natural"].apply(lambda x: D_W[x.isocalendar()[2] -1])
    # df=df[df['Día Semana']!='Domingo']

    print(df.dtypes)

    return(df)

#========================================================
# Funciones destinadas a los atributos del Cliente
#========================================================

def Customers_csv_RFM(file_direct_O):
	"""
	# Se Cargan los datos de ventas con las caracteristicas de los clientes
	requiere para ajustar los valores a Ajuste_Clientes_RFM(data)
	"""

	file_direct=file_direct_O+'Clientes_1010078_CT RFM'+'.csv'
	col_names=pd.read_csv(file_direct,
	                      encoding="utf-8",sep=";",nrows=0).columns

	types_dict = {col: str for col in list(col_names)}

	Clientes_i_RFM= pd.read_csv(file_direct,
	                   encoding="utf-8",sep=";",dtype=types_dict
	                      ,index_col='Unnamed: 0'
	                      )

	# Se debe agregar el parametro ,index_col='Unnamed: 0' 
	# de esta froma tal vez se pueda hacer un merge en base al indice

	#elimina una columna en especifico
	#DF_FULL.drop('Año natural', inplace=True, axis=1)
	return Clientes_i_RFM

# =============================================================================
# Ajustar la data
# =============================================================================
def Ajuste_Clientes_RFM(data):
 
    df=data.copy()

	# =============================================================================
	# Proceso iterativo Pasar a numero
	# ------------------------------------------------------------------------------

	# ----------------------------------------------------------------------
	# Float
    for i in [
            #RFM
            'Recency Actual'
            ,'Frecuency Actual del Cliente'
            ,'Ingreso de Venta Promedio'
              
            #Val Fact
            ,'Kilos Venta KG Promedio'
            ,'Precio Promedio'
            
            # Val historicos (ind del producto)
            ,'Año Creación Promedio'
            ,'Frecuencia Historica Promedio'
             ]:
        df[i]=df[i].astype('float64')
        #.astype('int64')
        
        
	# ------------------------------------------------------------------------ 
    # Int
    for i in [
                #RFM
                'Recency Actual'
                # ,'Frecuency Actual del Cliente'
                # ,'Ingreso de Venta Promedio'

                # Val Fact
                # ,'Kilos Venta KG Promedio'
                # ,'Precio Promedio'

                # Val historicos (ind del producto)
                ,'Año Creación Promedio'
                ,'Frecuencia Historica Promedio'
                ]:
        df[i]=df[i].astype('int64')
        


	#==========================================================================================
	# Ajuste de las fechas
	#-----------------------------------------------------------------------------------------
    for date in ['Fecha ultima Compra','Fecha Creacion']:
        df[date] = df[date].apply(lambda x: 
                                            datetime.datetime.strptime(str(x),
                                                                           '%Y-%m-%d').date())
    
    print(df.dtypes)
 
    return    df.rename(columns={'Ingreso de Venta Promedio':'Monetary Actual'})
#====================================================================================================
# Val_Customers_Weeks_1010078_CT 2018_2021
#======================================================================

def Val_Clientes_weeks(file_direct_O):
	# Se Cargan los datos de ventas con las caracteristicas de los clientes
	#=====================================================================

	file_direct=file_direct_O+'Val_Customers_Weeks_1010078_CT 2018_2021'+'.csv'
	col_names=pd.read_csv(file_direct,
	                      encoding="utf-8",sep=";",nrows=0).columns

	types_dict = {col: str for col in list(col_names)}

	Clientes_Valor_Week= pd.read_csv(file_direct,
	                   encoding="utf-8",sep=";",dtype=types_dict
	                      ,index_col='Unnamed: 0'
	                      )

	# Se debe agregar el parametro ,index_col='Unnamed: 0' 
	# de esta froma tal vez se pueda hacer un merge en base al indice

	#elimina una columna en especifico
	#DF_FULL.drop('Año natural', inplace=True, axis=1)
	# Clientes_Valor_Week.head()

	for c in Clientes_Valor_Week.columns:
		if(c!='Cliente'):
			Clientes_Valor_Week[c]=\
				Clientes_Valor_Week[c].astype('float64')
	print(Clientes_Valor_Week.dtypes)
	return Clientes_Valor_Week
#==============================================================
#  Agrego a la data CLiente_iRFM los atributos relacionados al Ticket
#==============================================================
def Customer_KG_Mean(data_i_RFM, Clientes_i_RFM, Clientes_Valor_Week):
	"""
	data_i_RFM: Facturas
	Clientes_i_RFM: Atributos RFM
	Clientes_Valor_Week: Valoracion de los clientes
	"""
	df= data_i_RFM
	#----------------------------------------------------------------------------
	#Promedio
	df_g=df[['Cliente','Kilos Venta KG']].groupby('Cliente')\
        .mean().reset_index()\
        .rename(columns={'Kilos Venta KG':Dic_col['Ticket Customers'][0]})
	# df_g
	#----------------------------------------------------------------------------
	#Desviación estandar
	df_G=df[['Cliente','Kilos Venta KG']].groupby('Cliente')\
        .std().reset_index()\
        .rename(columns={'Kilos Venta KG':'Ticket std Actual'})

	print(
	df_G.isnull().sum()
	)
	df_G=df_G.fillna(0)
	#----------------------------------------------------------------------------
	# Merge Coeficiente de variación
	df_group=pd.merge(df_g,df_G,how='right')

	df_group[Dic_col['Ticket Customers'][1]]=\
	df_group.apply(lambda x: 
				x['Ticket std Actual']/
				x[Dic_col['Ticket Customers'][0]] ,axis=1)
	#----------------------------------------------------------------------------
	Clientes_i=pd.merge(Clientes_i_RFM,df_group)
	print(Clientes_i.shape)
	
	Clientes_i=pd.merge(Clientes_Valor_Week,Clientes_i)
	print(Clientes_i.shape)
	Clientes_i['$F^{-1}$ Actual']=\
		Clientes_i[Dic_col['RFM Customers'][1]].apply( lambda x: x**(-1))
	print(Clientes_i.shape)
	return(Clientes_i)

#======================================================================
# Tipo de semana 
#======================================================================

def Tipo_de_semana_Model(file_direct_O):
	#======================================================================
	# Se Cargan los datos de ventas con las caracteristicas de los clientes
	#=====================================================================

	file_direct=\
	file_direct_O+'Weeks_clusters_1010078_CT_2018_2021 Other val 2020_2021'+'.csv'

	col_names=pd.read_csv(file_direct,
						encoding="utf-8",sep=";",nrows=0).columns

	types_dict = {col: str for col in list(col_names)}

	Df_Week= pd.read_csv(file_direct,
					encoding="utf-8",sep=";",dtype=types_dict
						,index_col='Unnamed: 0'
						)

	# Se debe agregar el parametro ,index_col='Unnamed: 0' 
	# de esta froma tal vez se pueda hacer un merge en base al indice

	#elimina una columna en especifico
	#DF_FULL.drop('Año natural', inplace=True, axis=1)
	# Df_Week.head(1)
	for c in Df_Week.columns:
		if(
		(c!='Variable')&(c!='Atributo')&(c!='Semana')&(c!='Tipo de Semana')
		):
			Df_Week[c]=\
				Df_Week[c].astype('float64')

	print(Df_Week.dtypes)
	return(Df_Week)
def Merge_Week(file_direct_O,data_i_RFM):
	"""
	file_direct_O: Dirección o ubicacion del dt week
	data_i_RFM: Data Facturas, con columna Semana a incoorporar Tipo de semana
	"""
	Df_Week=Tipo_de_semana_Model(file_direct_O)
	data_i_RFM_week=pd.merge(
	Df_Week[['Semana','Tipo de Semana']]
	,data_i_RFM#[['Semana','Año']]
	,how='inner')
	print(data_i_RFM.shape[0] - data_i_RFM_week.shape[0])
	return(data_i_RFM_week)

"""
Falta:
1. [ ] Atributo promedio y coeficiente de variación del ticket o lote de compra Kg del cliente.
2. [ ] Atributo incorporación del tipo de semana a los datos de las facturaciones electronicas

"""