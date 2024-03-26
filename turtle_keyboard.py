from turtle import *

h = 200
w = h/5
RIGHT_ANGLE = 90
black_key_ratio = 0.6
speed('fast')
i = 1
while(i < 8):
    #Right
    forward(w*i)
    right(RIGHT_ANGLE)
    #Down
    if(i%7 == 3 or i%7 == 0):
        forward(h)
    else:
        pensize(15)
        forward(h*black_key_ratio)
        pensize(1)
        forward(h*(1-black_key_ratio))
    right(RIGHT_ANGLE)
    #Left
    forward(w*i)
    right(RIGHT_ANGLE)
    #Up
    forward(h)
    right(RIGHT_ANGLE)
    i = i + 1

mainloop()
