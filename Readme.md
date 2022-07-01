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
2. [ ] Clustering RFM+(FxM)
3. [ ] ~~Clustering RF KG~~
4. [ ] ~~Clustering RFM KG~~
5. [ ] ~~Clustering RF KG Valoración~~
6. [X] Clustering RFM KG Valoración
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

1. [X] __Descripción de los atributros__ 
Realizar tabla descriptiva con todos los atributos de los clientes.
   1. [X] Atributos r+fm
      1. rfm descritivo
      2. rfm promedio
   2. [X]  Valoración \% atributos
      1. [X] Histograma con graficas
      2. [X] Tabla descriptiva
   3. [X] Aributos kg
      1. [X] kg promedio (Tabla e Histograma)
      2. [X] CV del tiket (Tabla descriptiva)
2. [X] Implementar Graficos, del __comportamiento de los clientes.__ 
   1. [X] Copiar graficos presentación
   2. [X] Ver graficos utilizados en el area de analisis de datos
      1. [X] PRECIO POMEDIO MENSUAL
      2. [x] ~~KG PROMEDIO~~
         1. [X] ~~Mensual no es necesario~~
      3. [X] ~~ingreso en CLP(Opcional)~~
      4. [X] ~~Distribución geografica (Opcional)~~
3. [ ] __Puntajes__
   1. [x] $R^2$ valores predictivos
      1. [x] T test
      2. [x] T Train
      3. [ ] Intervalo de confianza bajo una muestra iterativa
   2. [x] Sklearn para validar el K, de k means
      1. [x] Silhouette Coefficient
      2. [x] Calinski-Harabasz Index
      3. [x] Índice Davies-Bouldin

# Falta en Full

1. [x] Estandarizar datos a utilizar, recorgerlos del apartado final.
2. [x] sobreescribir el codig
3. [ ] ~~Estudiar los valores de W_f y W_M~~
   1. [ ] ~~probar los diferentes valores posibles para  W_f y W_M como se hizo en A2)~~
4. [x] Estudiar el valor de K
   1. [x] Con la forma clasica
   2. [x] con otras metricas de error
5. [x] realizar estructura para analizar el comportamiento de los clusters
6. [x] correr descripción de los graficos
7. [x] Etiquetado de los clusters

## Estudio del modelo OLS para cada cluster

1. [ ] Montruir una muestra de $R^2$
2. [ ] Extraer coeficientes y partes del modelo de regresión
3. [ ] Estudiar porcentualmente el error de las predicciones realizadas
   1. [ ] Error promedio
   2. [ ] Intervalod e confianza
   3. [ ] Margen de error
   4. [ ] Comparar con el contenido visto en simulación para realizar comparación de medias.

## Metricas de Clustering de desempeño

[Link Sklearn](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index)

1. [SEE](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html):
   > Suma de las distancias al cuadrado de las muestras a su centro de conglomerado más cercano, ponderada por los pesos de la muestra, si se proporcionan.
   >> Sum of squared distances of samples to their closest cluster center, weighted by the sample weights if provided.
2. [silhouette_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html):
   > The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.

   >If the ground truth labels are not known, evaluation must be performed using the model itself. The Silhouette Coefficient (sklearn.metrics.silhouette_score) is an example of such an evaluation, where a higher Silhouette Coefficient score relates to a model with better defined clusters. The Silhouette Coefficient is defined for each sample and is composed of two scores:
   
   >a: The mean distance between a sample and all other points in the same class.

   >b: The mean distance between a sample and all other points in the next nearest cluster.

   >The Silhouette Coefficient s for a single sample is then given as:
   
   >> $s = \frac{b - a}{max(a, b)}$
   
   >  The Silhouette Coefficient for a set of samples is given as the mean of the Silhouette Coefficient for each sample.

   >Advantages
      >> - The score is bounded between -1 for incorrect clustering and +1 for highly dense clustering. Scores around zero indicate overlapping clusters.
      >> - The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.

   >Drawbacks
   >>The Silhouette Coefficient is generally higher for convex clusters than other concepts of clusters, such as density based clusters like those obtained through DBSCAN.
4. calinski_harabasz_score:
   >If the ground truth labels are not known, the Calinski-Harabasz index (sklearn.metrics.calinski_harabasz_score) - also known as the Variance Ratio Criterion - can be used to evaluate the model, where a higher Calinski-Harabasz score relates to a model with better defined clusters.

   >The index is the ratio of the sum of between-clusters dispersion and of within-cluster dispersion for all clusters (where dispersion is defined as the sum of distances squared):
   
   >Advantages
      >>The score is higher when clusters are dense and well separated, which relates to a standard concept of a cluster.
   >Drawbacks
      >>The Calinski-Harabasz index is generally higher for convex clusters than other concepts of clusters, such as density based clusters like those obtained through DBSCAN. The score is fast to compute.
5. davies_bouldin_score:

   >If the ground truth labels are not known, the Davies-Bouldin index (sklearn.metrics.davies_bouldin_score) can be used to evaluate the model, where a lower Davies-Bouldin index relates to a model with better separation between the clusters.

   >This index signifies the average ‘similarity’ between clusters, where the similarity is a measure that compares the distance between clusters with the size of the clusters themselves.

   >Zero is the lowest possible score. Values closer to zero indicate a better partition.

   >In normal usage, the Davies-Bouldin index is applied to the results of a cluster analysis as follows:

   >Advantages
      >>The computation of Davies-Bouldin is simpler than that of Silhouette scores.

      >>The index is solely based on quantities and features inherent to the dataset as its computation only uses point-wise distances.
   >Drawbacks
      >>The Davies-Boulding index is generally higher for convex clusters than other concepts of clusters, such as density based clusters like those obtained from DBSCAN.

      >>The usage of centroid distance limits the distance metric to Euclidean space.