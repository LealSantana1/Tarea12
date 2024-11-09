#EJERCICIO 6
media <- 50
desviacion_estandar <- 12
set.seed(123) 
muestra <- rnorm(1000, mean = media, sd = desviacion_estandar)
prob_menor_70 <- pnorm(70, mean = media, sd = desviacion_estandar)
prob_mayor_70 <- 1 - prob_menor_70
cat("La probabilidad de que un valor sea mayor que 70 es:", prob_mayor_70, "\n")
hist(muestra, breaks = 30, col = rgb(0.2, 0.6, 1, 0.5), 
     xlim = c(min(muestra), max(muestra)), 
     main = "Histograma de la distribución normal",
     xlab = "Valores", ylab = "Frecuencia", border = "black")
abline(v = 70, col = "red", lwd = 2, lty = 2)
text(75, 50, labels = paste("P(X > 70) =", round(prob_mayor_70, 4)), col = "black")
x_values <- seq(70, max(muestra), length.out = 100)
y_values <- dnorm(x_values, mean = media, sd = desviacion_estandar)
polygon(c(x_values, max(muestra)), c(y_values, 0), col = rgb(1, 0, 0, 0.3), border = NA)
box()
