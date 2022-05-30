# Function import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Requiere
import sklearn
import statsmodels.api as sm
from sklearn.linear_model import Ridge

#============================================
# Curva K-means Regla del codo
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler



#=========================================
# Actividad según R+
#=========================================


def Estado_R(x):
    """
    Cortes 0-89|90-364|365-
    Uso:
    RFM_Customers['Actividad del cliente']=\
    RFM_Customers['Recency Actual'].apply(lambda r: Estado_R(r)  )
    
    O por DF_Estado_R(DF)
    """
    if(x<=90):
        return('Activo')
    elif(90<x<=365):
        return('Fugandose')
    else:
        return('Fugado')
     
def DF_Estado_R(DF):
    """
    Cortes 0-90|91-365|366-
    Uso: Estado_R
    Requiere columna: 'Recency Actual'

    DF_Estado_R(RFM_Customers)
    RFM_Customers.head()
        """
    DF['Actividad del cliente']=\
    DF['Recency Actual'].apply(lambda r: Estado_R(r) )
    return(DF)


#=========================================
# Ajuste de columnas 
#=========================================
def data_Norm_satandar(dx,Normalizad_col,drop_columns):
    """
    Pasa un listado de columnas a Ln
    
        dx: dataframe
        Normalizad_col: (Array) Listado de columnas a escalar 
        drop_columns: (True or False)  Eliminar columnas del listado
    """
    df_x=dx.copy()
    for s in Normalizad_col:
        if(s in df_x.columns):
            mean_df=df_x[s].mean()
            std_df_s=df_x[s].std()
            df_x[s + ' (Normalizado)']=\
            df_x[s].apply(lambda x: (x-mean_df)/(std_df_s))
        else:
            print('No se pudo transformar ',s)
    if(drop_columns):
        df_x=df_x.drop(columns = Normalizad_col)
    return(df_x)



def data_Min_Max(dx,Min_Max_col,drop_columns):
    """
    Pasa un listado de columnas a Ln
    No se recimienda usar cuando se presenta outliers
        dx: dataframe
        Min_Max_col: (Array) Listado de columnas a escalar 
        drop_columns: (True or False)  Eliminar columnas del listado
    """
    df_x=dx.copy()
    for s in Min_Max_col:
        if(s in df_x.columns):
            Min_df_s=df_x[s].min()
            Max_df_s=df_x[s].max()
            df_x[s + ' (Escala Min Max)']=\
            df_x[s].apply(lambda x: (x-Min_df_s)/(Max_df_s -Min_df_s))
        else:
            print('No se pudo transformar ',s)
    if(drop_columns):
        df_x=df_x.drop(columns = Min_Max_col)
    return(df_x)



def data_ln(dx,ln_col,drop_columns):
    """
    Pasa un listado de columnas a Ln
    
        dx: dataframe
        ln_col: (Array) Listado de columnas a escalar 
        drop_columns: (True or False)  Eliminar columnas del listado

    import numpy as np
    """
    df_x=dx.copy()
    for s in ln_col:
        if(s in df_x.columns):
            df_x[s + ' (Escala ln)']=\
            df_x[s].apply(lambda x: np.log(x))
        else:
            print('No se pudo transformar ',s)
    if(drop_columns):
        df_x=df_x.drop(columns = ln_col)
    return(df_x)



def Df_Pond_FxM(RFM_df ,  Col_FM , weighted_F,weighted_M):
    """
    Entrega un df:
    Df_Pond_FxM(RFM_df,W_F,W_M):
    W_F pond de F
    W_M pond de M
    Col_FM:(F,M)
    """
    df=RFM_df.copy()

    if((Col_FM[0] in df.columns)&(Col_FM[1] in df.columns)):
        df['$(F \times W_F + M \times W_M)$']=df.apply(lambda x:
            x[Col_FM[0]]* weighted_F +\
            x[Col_FM[1]]*weighted_M,axis=1 )
    else:
        print('Col_FM entregado no corresponde con las oclumnas de df',Col_FM)
    return df




#====================================================================================
# Curva K-means definición del K Cluster  
#=========================================



def Curva_kmeans(D_Clientes_Frec,Col,Normal_Standar_Boolean=False):
    
    """
    Entrega una curva 


    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import StandardScaler

    
    Col=['Frecuency Actual del Cliente','Monetary Actual',
    '$(F \times W_F + M \times W_M)$'
    ]

    """

    X=D_Clientes_Frec.fillna(0)
    X_std=X[Col].copy()


    if(Normal_Standar_Boolean):
        X_std =\
        pd.DataFrame(StandardScaler().fit_transform(X_std),columns=X_std.columns)


    #kmeans = KMeans(n_clusters=6)



    #la suma del error cuadrático para diferentes valores de k
    SSE = []
    for i in range(1, 21):
      km = KMeans(n_clusters=i)
      km.fit(X_std)
      SSE.append(km.inertia_)

    # plot

    plt.plot(range(1, 21), SSE,'-o', color='black')
    plt.xlabel('Número of clusters')
    plt.ylabel('SSE')
    plt.show()
    return(X_std)



#=========================================
# Modelo Kmenas
#=========================================
def def_Col_cluster(D_Clientes, Col 
                    ,Numero_de_clusters
                    ,ln_Col_tra=False
                    ,Normal_Standar_Boolean =False
                    ):
    """
    Este modelo no considera variables categoricas
    D_Clientes:DataFrame con las columnas a utilizar
    Col: Atributos a utilizar para el clustering, 
        Array con listado de columnas a usar.
    ,ln_Col_tra=False, True if se requiere hacer escalado Ln
    ,Max_Min_Bul=True, True if  se requiere hacer escalado Min Max
    
    Utiliza:
    data_ln()
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    import pandas as pd
    """ 
    X=D_Clientes.fillna(0).copy()
    
    #if requiere estandarización Ln
    if(ln_Col_tra):
        X_std =data_ln(X[Col],Col,True).copy()
    X_std=X[Col].copy()

    #if requiere estandarización 
    if(Normal_Standar_Boolean):
        X_std = pd.DataFrame(
                #Array, con la Estandarización
                StandardScaler()\
                .fit_transform(X_std)
                ,columns=X_std.columns)
    
    #=========================================
    # Modelo Kmenas
    #=========================================
    
    kmeans = KMeans(n_clusters=Numero_de_clusters)
    kfit = kmeans.fit(X_std)
    identified_clusters = kfit.predict(X_std)
    X['identified_clusters']=identified_clusters
    X['identified_clusters']=X['identified_clusters'].astype('category')
    
    if( 'Frecuency Actual del Cliente' in X.columns ):
        X['F-1']= X['Frecuency Actual del Cliente'].apply(lambda x: x**(-1))
    return(X) 

#==================================================================================
# Función de desempeño del Cluster
#
# Modelo Predictivo R2
#
#
#
#=================================================================================
    

def X_set(X,Ridge_mod):
    """
    X_set(X= Data frame con las columnas de X
    ,Ridge_mod= Variabel True si se usará ridge
                False si se desea incorporar el intercepto
    )
    """
    
    X_Set_Def=X.copy()

    #=======================================================
    # Ajuste Log Kilos de Venta
    X_Set_Def['Kilos Venta KG']=X_Set_Def['Kilos Venta KG']\
                                    .apply(lambda x: np.log(x))
    #----------------------------------------------------------
    # Ajuste Categorico a dif Variables
    if('Año' in X_Set_Def.columns):
        X_Set_Def['Año']=X_Set_Def['Año'].astype('int64')
        X_Set_Def['Año']= X_Set_Def['Año']-X_Set_Def['Año'].min() #2018
    
    if('Semana' in X_Set_Def.columns):
        X_Set_Def['Semana']=X_Set_Def['Semana'].astype('category')

    if('Tipo de Semana' in X_Set_Def.columns):
        X_Set_Def['Tipo de Semana']=X_Set_Def['Tipo de Semana']\
                .astype('category')
    if('identified_clusters' in X_Set_Def.columns):
        X_Set_Def['identified_clusters']=X_Set_Def['identified_clusters']\
                .astype('category')
    #-----------------------------------------------------------------
#     print(X_Set_Def.dtypes,'\n'+'='*50)

    # Dummies
    X_Set_Def=pd.get_dummies(X_Set_Def, drop_first=True)
    
#      OLS requiere de un intercepto
    if(Ridge_mod==False):
        X_Set_Def['Intecepto']=[1 for i in range(X_Set_Def.shape[0])]
    
    return(X_Set_Def)

def Func_log_log_Tip_ind_cluster(Data_F,Ridge_mod):
    """
    Entrega el (R train ,R Test)
    Columnas obligatorias:['Kilos Venta KG','Año','identified_clusters','Tipo de Semana']

    Data_F; DF de las caturaciones a utilizar
    Ridge_mod; True or False, si se desea Ridge o OLS

    # Requiere
    import sklearn
    import statsmodels.api as sm
    from sklearn.linear_model import Ridge

    """
    
    #===================================
    #Ajuste de los datos
    #-----------------------------------
#     
    X_Columnas=['Kilos Venta KG','Año','identified_clusters','Tipo de Semana']
    y_pred_Columna='Precio'

    y=Data_F[y_pred_Columna].copy()
    X=X_set(Data_F[ X_Columnas ].copy(),Ridge_mod)


    #Aplico Ln a y
    y=y.apply(lambda x: np.log(x))


    #Calculo de la correlación entre variables
    
#     print('Correlación Variables sobre la Variable ', y_pred_Columna,
#         '\n'+'-'*50+'\n' ,pd.merge(y.reset_index(),X.reset_index()).corr()[y_pred_Columna])

    #===================================
    # Entrenamiento
    #-----------------------------------
    #SPLIT TEST OR TRAIN
    X_train, X_test, y_train, y_test = \
            train_test_split(X, y, random_state=0)
    #-----------------------------------
    # TRAIN MODEL
    if(Ridge_mod):
        #Entraniemnto
        ridge = Ridge(alpha=0.23272024789604073).fit(X_train, y_train)
        #R Score 
        R_test=ridge.score(X_test, y_test)
        R_test=ridge.score(X_test, y_test)
#         print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
#         print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))
#         return(ridge)
#         return(str("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
#                +'  '
#                 +str("Test set score: {:.2f}".format(ridge.score(X_test, y_test))))
        return(
                (ridge.score(X_train, y_train).round(3)),
                (ridge.score(X_test, y_test).round(3))
        )
        
    else:
        mod = sm.OLS(y_train,X_train)
        fii = mod.fit()
#         print('$R^2$ Data Train'  ,sklearn.metrics.r2_score(y_train,fii.predict()).round(3) )
#         print('$R^2$ Data Test'  ,sklearn.metrics.r2_score(y_test,fii.predict(exog=X_test)).round(3))
        return( #'$R^2$ Data Train' + 
               (sklearn.metrics.r2_score(y_train,fii.predict()).round(3) )
#                 '$R^2$ Data Test'   + 
                ,(sklearn.metrics.r2_score(y_test,fii.predict(exog=X_test)).round(3))
                )

        #==========================================
        # Todos los datos, desde ell 2018
        # $R^2$ Data Train 0.4378602682377155
        # $R^2$ Data Test 0.43860226392178925
#         return(fii)

