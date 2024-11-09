#EJERCICIO 10

set.seed(123) 
X <- rnorm(100, mean = 10, sd = 3)
Y <- rnorm(100, mean = 15, sd = 4)

Z <- X + Y

media_Z <- mean(Z)
desviacion_Z <- sd(Z)

media_teorica <- mean(X) + mean(Y)
desviacion_teorica <- sqrt(sd(X)^2 + sd(Y)^2)

cat("Media calculada de Z: ", media_Z, "\n")
cat("Desviación estándar calculada de Z: ", desviacion_Z, "\n")
cat("Media teórica de Z: ", media_teorica, "\n")
cat("Desviación estándar teórica de Z: ", desviacion_teorica, "\n")
par(mfrow = c(1, 3), mar = c(4, 4, 2, 1))
hist(X, breaks = 15, col = rgb(0.2, 0.6, 1, 0.5), main = "Histograma de X", 
     xlab = "Valores", ylab = "Frecuencia", border = "black")
hist(Y, breaks = 15, col = rgb(1, 0.6, 0.2, 0.5), main = "Histograma de Y", 
     xlab = "Valores", ylab = "Frecuencia", border = "black")
hist(Z, breaks = 15, col = rgb(0.6, 0.2, 0.6, 0.5), main = "Histograma de Z", 
     xlab = "Valores", ylab = "Frecuencia", border = "black")

