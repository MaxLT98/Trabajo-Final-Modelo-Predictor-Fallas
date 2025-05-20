# Trabajo-Final-Modelo-Predictor-Fallas

Predictor de fallas para motor de induccion a partir de sus valores de funcionamiento - Trabajo Final del Curso Data Science Grupo 3

El Modelo fue elaborado a partir de una base de datos de parámetros de funcionamiento de motores de induccion de una empresa industrial, que según sus valores se tiene registro de su estado cuando falla

Por tanto, realizando un análisis de clasificacion de los valores de funcionamiento con el estado de la máquina, se seleccionó las variables de proceso que se mide de forma continua segun el procedimiento de mantenimiento predictivo para lograr predecir si la máquina fallará. Estas variables resultaron:

## ~ Temperatura del motor [K°]
## ~ Temperatura del Proceso [K°]
## ~ Velocidad de rotacion de motor [RPM]
## ~ Torque [Nm]

## El mejor modelo de clasificacion para predecir la falla es el RamdomForest.
