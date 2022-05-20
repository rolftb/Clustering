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
1. [ ] Data Customer All
2. [ ] Data Facturas All
3. [ ] Construcción Caracteristicas a usar
    - [ ] Un modelo por cada week tipe
    - [X] Modelo que reemplza W por $C_W$
3. [ ] Dispersión puntos RFM
4. [ ] Modelo Clustering de RFM+
    - [ ] Defionir R, aparte
    - [ ] Defionir FxM
    - [ ] Calcular Clustering FxM