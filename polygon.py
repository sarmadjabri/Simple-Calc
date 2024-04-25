import turtle

def draw(sides, length):
    for _ in range(int(sides)):
        turtle.forward(int(length))
        turtle.right(360 / int(sides))
