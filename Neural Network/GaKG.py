#Librerías
import tensorflow as tf
import numpy as np

#Entradas
gramos=np.array([1,139,492,235,1294], dtype=float)

#Salidas
kilogramo=np.array([0.001,0.139,0.492,0.235,1.294], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1]) #units es la cantidad de neuronas de la capa / autoregistra la capa de entrada con nuestros datos
modelo = tf.keras.Sequential([capa])


modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1), # es lo que le permite a la red ajustar los pesos de manera eficiente para que aprenda poco a p0co / el 0.1 es la tasa de aprendizaje(no hay que abusarse ni tan poco)
    loss='mean_squared_error' 
)

print("Comenzando entrenamiento...")
historial = modelo.fit(gramos, kilogramo, epochs=10000, verbose=False) #epochs es la cantidad de vuelta que quiero que lo intente / verbose=False es para sacar mugre miegra se entrena
print("Modelo entrenado!")

#veamos los resultados de la función de pérdida
#nos va a decir que tan mal están los resultados en cada vuelta dada
import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])

print("Hagamos una predicción!")
resultado = modelo.predict([100])
print("El resultado es " + str(resultado) + " kilogramo!")


#Podemos ver los valores internos, como el peso y el sesgo
print("Variables internas del modelo")
print(capa.get_weights())

