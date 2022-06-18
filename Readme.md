# Archivos

- Modelos de regresión lineal OLS P(Q), __sin atributo Año__
  - $P(Q)=\beta_1Q +\beta_0$
  - $P(Q)=\beta_1Q +\beta_2 Q^2 + \beta_3Q^3  +\beta_0$
  - $P(Q)=\beta_1Q +\beta_2 Q^2 + \beta_3Q^3 +\beta_0$
  - $\ln(P(Q))=\beta_1Q  +\beta_0$
  - $\ln(P(Q))=\beta_1\ln(Q)  +\beta_0$

- Variables:
  - $P:$ Precio Estimado
  - $Q:$ Peso neto Kg.(_Variable discreta_)
  - $A:$ Año el cual se ejecuta la venta.(_Variable discreta_)
  - $w_i$ Semana $i$ del conjunto de semanas $W$

## A_2 (lineal sin Año)) Construccion modelo [Tradicional 1010078]

Se definen las funciones del arrchivp `R_FM_Func.py`, Se estudia el K para R+FM y se evalua los valores de $W_F$ $W_M$.

## R_FM_Func.py

>Archivo importable desde otro codigo, con funciones para ajustar a los datos.

### Funciones

#### Ajuste De Datos

- Estado R
  - `Estado_R(X)` por apply
  - DF_Estado_R(DF) ajusta directamnte el DF ingresado

- __Estandarizado Normalizado__

  - `pd.DataFrame(StandardScaler().fit_transform(X_std),columns=X_std.columns)`

- __Esclaado Min Max__
  
    _No se recomienda cuando existe una amplitud de outlier muy grand, porque el realiza un desajuste muy grande.
 `data_Min_Max(dx,Min_Max_col,drop_columns)`
  > Entrega un df copiado
  >> Ajusta las columnas del arreglo Min_Max_col
$x_{scaled}=\dfrac{x-min(x)}{max(x)-min(x)}$

  - dx dataframe
  - Min_Max_col: (Array) Listado de columnas a escalar
  - drop_columns: (True or False)  Eliminar columnas del listado
- `data_ln(dx,ln_col,drop_columns)`

 > Pasa un listado de columnas a Ln y entrga una copia del dataframe
 > - dx: dataframe
 > - ln_col: (Array) Listado de columnas a escalar
 > - drop_columns: (True or False)  Eliminar columnas del listado

- `Df_Pond_FxM(RFM_df ,  Col_FM , weighted_F,weighted_M):`

   > Entrega una copia del df:
    >>con una nueva columna llamda $(F \times W_F + M \times W_M)$
   >
   > - W_F pond de F
   > - W_M pond de M
   > - Col_FM:(F,M)

#### Ajuste de K-means

- `Curva_kmeans(D_Clientes_Frec,Col,Normal_Standar_Boolean=False):`
    >Permite definir el numero de K segmentos de K-means.

- `Columnas_def(X_std):`
    >Permite definir como disminutye al variancia intra cluster al incorporar más columnas

#### Proceso de Clustering K-means

- `def_Col_cluster(D_Clientes, Col, Numero_de_clusters, ln_Col_tra=False)`

>Entrega(DataFrame):
>>Una copia del dataframe `D_Clientes` Con una columna adicional llamada `identified_clusters` con los el cluster que pertenece cada cliente.(Cada fila).

> - D_Clientes: Dataframe a clusterizar (pd.DataFrame)
> - Col: Columnas utilizadas para el clustering (Array)
> - Numero_de_clusters: K segmentos a generar (int)
> - ln_Col_tra=False: Si las columnas ya fueron ajustadas con Ln (Bulean logical value)

# Procedimiento a realizar

## Clusterings a desarrollar

Tiene sentido aplicar distintos modelos según la actividad del cliente.
Carece de sentido comprar un cliente que posee un comportamiento de compra actualizado los ultimos 90 días, a uno que no realiza una compra hace mas de un año.

La actividad de R, esta segmetnada en la siguiente secuencia:

- 0 a 90 días __Activo__
- 91 a 365 días __Fugandose__
- 366 días en adelante __Fugado__

```python
if(x<=90):
        return('Activo')
    elif(90<x<=365):
        return('Fugandose')
    else:
        return('Fugado')
```

### Modelos a desarrollar

1. [X] ~~Clustering RFM~~
2. [X] Clustering RFM+(FxM)
3. [X] ~~Clustering RF KG~~
4. [X] ~~Clustering RFM KG~~
5. [X] ~~Clustering RF KG Valoración~~
6. [ ] Clustering RFM KG Valoración
7. [ ]~~Clustering RFM KG Sencibilidad Jerarquica~~

## Pasos R+FM

1. [X] Data Customer All
2. [X] Data Facturas All
3. [X] Construcción Caracteristicas a usar
    > Se contruyeron las funciones para ajustar facilmente las columnas de interes
4. [X] Dispersión puntos RFM
   > Es muy simple el resultado y no vale la pena
5. [X] Escalar datos de RFM+
    - [X] Aplicar escala Min_MAX
    - [X] Aplicar escala Normalizado
    - [X] Aplicar escala Ln()
6. [X] Preparación basica, Ajuste de datos
    - [X] Definir FxM, def que requere de $W_f$ $W_m$
    - [X] Definir R Estado de actividad
7. [X] Modelo Clustering de RFM+ Parametros
    - [X] Curva de la cantiadad de cluster
    - [X] Columnas error, cantidad de Variables
8. [X] Estructura iterativa, para dif valores de $W_f$ $W_m$
    - [X] Contruye un grafico de dispersión para los dif valores
    - [X] guardado en PDF del grafico para los dif valores
9. [X] Metricas para comprar modelos
    - [ ] Estudiar publicación de RFM
      - [ ] Cómo se presenta la prueba del K-means, que metricas utiliza, cual es su experimento con los clusters.
    - [X] Definir un objetivo en comun de los tipos de modelos __(PREDICICÓND DEL PRECIO)__
    - [X] Desempeño de un modelo predictivo, Log-Log que considera.
10. [X] Resultado o Descripción del Cluster contruido.
    1. [X] Grafico
    2. [X] Grafico columna que representa los valores e cada cluster

## Trabajo con datos

1. [X] Py que abra archivos de datos facilmente, con poco texto
2. [X] Atributo promedio y coeficiente de variación del ticket o lote de compra Kg del cliente.
3. [X] Atributo incorporación del tipo de semana a los datos de las facturaciones electronicas

## Apuntes

1. [X] Se esta definiendo dispersión de M y F.
2. [X] Escribir que que implica cada numeración.
3. [X] Cambiar a cluster etiquetado
4. [X] Realizar tabla que describa cada cluster.
5. [X] Con la tabla echa es mas facil sirve para describir.

# Falta en R+FM

1. [ ] __Descripción de los atributros__ 
Realizar tabla descriptiva con todos los atributos de los clientes.
   1. [X] Atributos r+fm
      1. rfm descritivo
      2. rfm promedio
   2. [X] atributos valoración
      1. Histograma con graficas
   3. [ ] Aributos kg
      1. [X] kg promedio
      2. [ ] CV del tiket 
3. [ ] Implementar Graficos, del comportamiento de los clientes. 
   1. [X] Copiar graficos presentación
   2. [ ] Ver graficos utilizados en el area de analisis de datos
      1. [X] PRECIO POMEDIO MENSUAL
      2. [x] KG PROMEDIO
         1. [ ] Mensual no es necesario
         2. [ ] ingreso en CLP(Opcional)
      3. [ ] Distribución geografica (Opcional)
4. [ ] 