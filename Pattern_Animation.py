import numpy as np
import turtle as turtle
import random

def spiral(M, N):
    k = 0  # Starting row index
    l = 0  # Starting column index
    f = 0
    tur.color("green")
    while k < M and l < N:
        if f == 1:
            tur.right(90)
        # Print the first row from the remaining rows
        for i in range(l, N):
            tur.forward(dot_distance)
        k += 1
        f = 1
        tur.right(90)
        # Print the last column from the remaining columns
        for i in range(k, M):
            tur.forward(dot_distance)
        N -= 1
        tur.right(90)
        # Print the last row from the remaining rows in reverse order
        if k < M:
            for i in range(N - 1, l - 1, -1):
                tur.forward(dot_distance)
            M -= 1
            tur.right(90)
        # Print the first column from the remaining columns in reverse order
        if l < N:
            for i in range(M - 1, k - 1, -1):
                tur.forward(dot_distance)
            l += 1


tur = turtle.Turtle()
turtle.bgcolor("black")
dot_distance = 25
tur.setpos(-250,250) #to top left. 0,0 to centre
spiral(20, 20)
turtle.done()
