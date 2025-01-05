import turtle

window = turtle.Screen()

#generar una istancia
tortuga = turtle.Turtle()

colores = ['green', 'yellow', 'red', 'blue']

# Dibujar el cuadrado con un bucle
for color in colores:
    tortuga.color(color)
    tortuga.forward(100)
    tortuga.right(90)

window.mainloop()