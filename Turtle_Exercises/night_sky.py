from shapes import *

bgcolor('black')

fillcolor('blue')
begin_fill()
star(50)
end_fill()
goto(100,200)

fillcolor('purple')
pensize(5)
begin_fill()
star(100)
end_fill()
goto(-200, 150)

fillcolor('yellow')
pensize(5)
pencolor('blue')
begin_fill()
star(85)
end_fill()
penup()
goto(-250, -75)

pendown()
fillcolor('yellow')
pencolor('white')
begin_fill()
star(300)
end_fill()


mainloop()
