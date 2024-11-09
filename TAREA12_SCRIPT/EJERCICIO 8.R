#EJERCICIO 8
set.seed(123)
muestra <- rnorm(200, mean = 30, sd = 5)

hist(muestra, 
     breaks = 20, 
     col = rgb(0.2, 0.6, 1, 0.5), 
     main = "Histograma de la muestra con media = 30 y sd = 5", 
     xlab = "Valores", 
     ylab = "Frecuencia", 
     border = "black")

curve(dnorm(x, mean = mean(muestra), sd = sd(muestra)), 
      col = "red", 
      lwd = 2, 
      add = TRUE)

prueba_normalidad <- shapiro.test(muestra)

print(prueba_normalidad)

if (prueba_normalidad$p.value > 0.05) {
  cat("La muestra parece seguir una distribución normal (p-valor > 0.05).\n")
} else {
  cat("La muestra no sigue una distribución normal (p-valor <= 0.05).\n")
}

