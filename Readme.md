# Archivos

Variables:

- $P:$ Precio Estimado
- $Q:$ Peso neto Kg.(_Variable discreta_)
- $A:$ Año el cual se ejecuta la venta.(_Variable discreta_)
- $w_i$ Semana $i$ del conjunto de semanas $W$

## A_1 (lineal sin Año)) Construccion modelo [Tradicional 1010078]

Modelos de regresión lineal OLS P(Q), __sin atributo Año__

- $P(Q)=\beta_1Q +\beta_0$
- $P(Q)=\beta_1Q +\beta_2 Q^2 + \beta_3Q^3  +\beta_0$
- $P(Q)=\beta_1Q +\beta_2 Q^2 + \beta_3Q^3 +\beta_0$
- $\ln(P(Q))=\beta_1Q  +\beta_0$
- $\ln(P(Q))=\beta_1\ln(Q)  +\beta_0$

### Funciones

#### Ajuste De Datos

- Estado R
  - `Estado\_R(X)` por apply
  - DF_Estado_R(DF) ajusta directamnte el DF ingresado
- `data_Min_Max(dx,Min_Max_col,drop_columns)`
  - Ajusta las columnas del arreglo Min_Max_col
  - Entrega un df copiado
  - dx dataframe
  - Min_Max_col: (Array) Listado de columnas a escalar
  - drop_columns: (True or False)  Eliminar columnas del listado
- `data_ln(dx,ln_col,drop_columns)`
  
  Pasa un listado de columnas a Ln y entrga una copia del dataframe
      - dx: dataframe
      - ln_col: (Array) Listado de columnas a escalar 
      - drop_columns: (True or False)  Eliminar columnas del listado
- `Df_Pond_FxM(RFM_df ,  Col_FM , weighted_F,weighted_M):`
    
    Entrega una copia del df:
    con una nueva columna llamda $(F \times W_F + M \times W_M)$
    
  - W_F pond de F
  - W_M pond de M
  - Col_FM:(F,M)

#### Ajuste de K-means

- `Curva_kmeans(D_Clientes_Frec,Col)`
  
    Permite definir el numero de K segmentos de K-means.

- `Columnas_def(X_std):`

    Permite definir como disminutye al variancia intra cluster al incorporar más columnas

#### Proceso de Clustering K-means

- `def_Col_cluster(D_Clientes, Col, Numero_de_clusters, ln_Col_tra=False)`

>Entrega(DataFrame):
Una copia del dataframe `D_Clientes` Con una columna adicional llamada `identified_clusters` con los el cluster que pertenece cada cliente.(Cada fila).

> - D_Clientes: Dataframe a clusterizar (pd.DataFrame)
> - Col: Columnas utilizadas para el clustering (Array)
> - Numero_de_clusters: K segmentos a generar (int)
> - ln_Col_tra=False: Si las columnas ya fueron ajustadas con Ln (Bulean logical value)



# Procedimiento a realizar:

## Clusterings a desarrollar

Tiene sentido aplicar distintos modelos según la actividad del cliente. 
Carece de sentido comprar un cliente que posee un comportamiento de compra actualizado los ultimos 90 días, a uno que no realiza una compra hace mas de un año.

La actividad de R, esta segmetnada en la siguiente secuencia:

- 0 a 90 días __Activo__
- 90 a 364 días __Fugandose__
- 365 días en adelante __Fugado__

```python
if(x<=90):
        return('Activo')
    elif(90<x<=365):
        return('Fugandose')
    else:
        return('Fugado')
```

__Modelos a desarrollar__

1. [ ] Clustering RFM+
2. [ ] Clustering RFM+(FxM)
3. [ ] Clustering RF KG 
4. [ ] Clustering RFM KG 
5. [ ] Clustering RF KG Valoración
6. [ ] Clustering RFM KG Valoración
7. [ ] Clustering RFM KG Sencibilidad Jerarquica





## Pasos RFM

1. [X] Data Customer All
2. [X] Data Facturas All
3. [X] Construcción Caracteristicas a usar
4. [ ] Dispersión puntos RFM
5. [X] Escalar datos de RFM+
    - [X] Aplicar escala Min_MAX
    - [X] Aplicar escala Ln()
6. [ ] Preparación basica, Ajuste de datos
    - [X] Definir FxM, def que requere de $W_f$ $W_m$
    - [X] Definir R Estado de actividad
7. [ ] Modelo Clustering de RFM+ Parametros
    - [ ] Curva de la cantiadad de cluster
    - [ ] Columnas error, cantidad de Variables
8. [ ] Estructura iterativa, para dif valores de $W_f$ $W_m$
    - [ ] Contruye un grafico de dispersión para los dif valores
    - [ ] guardado en PDF del grafico para los dif valores
9. [ ] Metricas para comprar modelos
    - [ ] Estudiar publicación de RFM
    - [ ] Definir un objetivo en comun de los tipos de modelos
    - [ ] Desempeño de un modelo predictivo, Log-Log que considera 