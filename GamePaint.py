from turtle import Turtle, Screen

# Le decimos que wn será screen, para abreviar, y el color de fondo sera azul.
wn = Screen()
wn.bgcolor('blue')

# Le decimos que arrow será turtle, y el color de la flecha sera white
arrow = Turtle()
arrow.color('white')

# Le decimos la velocidad min:0(quieto) max:10 
jordi = 3

# Le decimos que se mueva con arrow.forward
def travel():
    arrow.speed(1)
    arrow.forward(jordi)
    wn.ontimer(travel, 10)


# Le decimos que en una tecla se use la funcion lambda=flecha posicion (grados) 'tecla'
wn.onkey(lambda: arrow.setheading(90), 'Up')
wn.onkey(lambda: arrow.setheading(180), 'Left')
wn.onkey(lambda: arrow.setheading(0), 'Right')
wn.onkey(lambda: arrow.setheading(270), 'Down')

# Le decimos que este siempre escuchando para poder mover el cursor
wn.listen()

# Empezamos el viaje.
travel()

wn.mainloop()