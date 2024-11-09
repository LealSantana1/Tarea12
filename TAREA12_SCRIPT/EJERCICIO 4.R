#ejercicio 4 
muestra_A <- rnorm(1000, mean = 55, sd = 10) 
muestra_B <- rnorm(1000, mean = 65, sd = 15)  
hist(muestra_A, 
     col = rgb(0, 0, 1, 0.5), 
     xlim = c(min(c(muestra_A, muestra_B)), max(c(muestra_A, muestra_B))),
     main = "Comparación de Muestras A y B", 
     xlab = "Valores", 
     ylab = "Frecuencia", 
     border = "black", 
     breaks = 20)

hist(muestra_B, 
     col = rgb(1, 0, 0, 0.5),  
     add = TRUE,  
     breaks = 20)


legend("topright", 
       legend = c("Muestra A", "Muestra B"), 
       fill = c(rgb(0, 0, 1, 0.5), rgb(1, 0, 0, 0.5)), 
       title = "Distribuciones", 
       border = "black")
media_A <- mean(muestra_A)
desviacion_A <- sd(muestra_A)

media_B <- mean(muestra_B)
desviacion_B <- sd(muestra_B)
cat("Muestra A - Media: ", media_A, " Desviación estándar: ", desviacion_A, "\n")
cat("Muestra B - Media: ", media_B, " Desviación estándar: ", desviacion_B, "\n")
