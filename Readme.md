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
1. [ ] Clustering RFM+
2. [ ] Clustering RF KG Valoración
3. [ ] Clustering RFM KG Valoración
4. [ ] Clustering RFM KG Valoración





## Pasos RFM
1. [X] Data Customer All
2. [X] Data Facturas All
3. [X] Construcción Caracteristicas a usar
4. [ ] Dispersión puntos RFM
5. [X] Escalar datos de RFM+
    - [X] Aplicar escala Min_MAX
    - [X] Aplicar escala Ln()
6. [ ] Preparación basica
    - [X] Definir FxM, def que requere de $W_f$ $W_m$
    - [X] Definir R Estado de actividad
7. [ ] Modelo Clustering de RFM+ Parametros
    - [ ] Curva de la cantiadad de cluster
    - [ ] Columnas error, cantidad de atributos
    - [ ] 
