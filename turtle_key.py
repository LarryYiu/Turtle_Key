# bring in turtle
from turtle import *

# set default pen size to 4 px
pensize(4)

# vaiables
h_white = 500
w_white = h_white/5
w_black = w_white/2
h_black = 0.6 * h_white
RIGHT_ANGLE = 90

## right
# foward 
forward(w_white)
# turn right
right(RIGHT_ANGLE)

## down
# black key
pensize(w_black)
forward(h_black)
# rest
pensize(4)
forward(h_white - h_black)
right(RIGHT_ANGLE)

## left
forward(w_white)
right(RIGHT_ANGLE)

## up
forward(h_white)
right(RIGHT_ANGLE)

# keep the window running
mainloop()