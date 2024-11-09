#EJERCICIO 2
media <- 40
desviacion_estandar <- 5
muestra <- rnorm(1000, mean = media, sd = desviacion_estandar)

hist(muestra, breaks = 30, col = "red", border = "black", 
     main = "Histograma de la distribución normal", 
     xlab = "Valores", 
     ylab = "Frecuencia")
probabilidad <- pnorm(45, mean = media, sd = desviacion_estandar) - pnorm(35, mean = media, sd = desviacion_estandar)
print(paste("La probabilidad de que un valor esté entre 35 y 45 es:", probabilidad))
 