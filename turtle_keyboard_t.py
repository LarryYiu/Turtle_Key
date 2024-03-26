from turtle import *
pensize(4)
speed('fast')

h_white = 500
w_white = h_white/5
h_black = 0.6 * h_white
w_black = 0.5 * w_white
RIGHT_ANGLE = 90
#1st
forward(w_white)
right(RIGHT_ANGLE)

pensize(w_black)
forward(h_black)
pensize(4)
forward(h_white - h_black)
right(RIGHT_ANGLE)

forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)
forward(w_white)

#2nd
forward(w_white)
right(RIGHT_ANGLE)

pensize(w_black)
forward(h_black)
pensize(4)
forward(h_white - h_black)
right(RIGHT_ANGLE)

forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)
forward(w_white)

#3rd
forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)

forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)
forward(w_white)

#4th
forward(w_white)
right(RIGHT_ANGLE)

pensize(w_black)
forward(h_black)
pensize(4)
forward(h_white - h_black)
right(RIGHT_ANGLE)

forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)
forward(w_white)

#5th
forward(w_white)
right(RIGHT_ANGLE)

pensize(w_black)
forward(h_black)
pensize(4)
forward(h_white - h_black)
right(RIGHT_ANGLE)

forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)
forward(w_white)

#6th
forward(w_white)
right(RIGHT_ANGLE)

pensize(w_black)
forward(h_black)
pensize(4)
forward(h_white - h_black)
right(RIGHT_ANGLE)

forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)
forward(w_white)

#7th
forward(w_white)
right(RIGHT_ANGLE)


forward(h_white)
right(RIGHT_ANGLE)

forward(w_white)
right(RIGHT_ANGLE)

forward(h_white)
right(RIGHT_ANGLE)

mainloop()