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

# Procedimiento a realizar:

## Clusterings a desarrollar
Tiene sentido aplicar distintos modelos según la actividad del cliente. 
Carece de sentido comprar un cliente que posee un comportamiento de compra actualizado los ultimos 90 días, a uno que no realiza una compra hace mas de un año.

La actividad de R, esta segmetnada en la siguiente secuencia:
- 0 a 90 días __Activo__
- 90 a 364 días __Fugandose__
- 365 días en adelante __Fugado__

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