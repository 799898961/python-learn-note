# 8.8科赫雪花.py

import turtle as tr

def koch(size, n):
    if n==0 :
        tr.fd(size)
    else :
        for angle in [0, 60, -120, 60]:
            tr.left(angle)
            koch(size/3, n-1)
def main():
    tr.setup(600,720)
    tr.penup()
    tr.goto(-200,100)
    tr.pendown()
    tr.pencolor("red")
    tr.ht()
    tr.speed(0)
    tr.pensize(2) 
    level = 3
    for i in range(3):
        koch(400, level)
        tr.right(120)
    
    tr.done()

main()