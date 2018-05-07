from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = [240,0, 0]
Blue=[0,255,240]
Pink=[240,0,250]
Yellow=[240,255,0]

sense.show_message("Atrapa", text_colour=Blue)
sense.show_message("la", text_colour=Yellow)
sense.show_message("bola", text_colour=Pink)

x = 0
y = 0

matrix = [[BLACK for column in range(8)] for row in range(8)]

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened


def gen_pipes(matrix):
    for row in matrix:
        row[1] = BLACK
    gap = randint(1, 6)
    matrix[gap][1] = RED
    return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i +1]
        row[-1] = BLACK
    return matrix

def draw_astronaut(event):
    global y
    global x
    sense.set_pixel(x, y, BLACK)
    if event.action == "pressed":
        if event.direction == "up" and y > 0:
            y -= 1
        elif event.direction == "down" and y < 7:
            y += 1
        elif event.direction == "right" and x < 7:
            x += 1
        elif event.direction == "left" and x > 0:
            x -= 1
    if sense.get_pixel(x, y)==RED:
      print("Atrapada")
      #puntos++ o reset timer
    sense.set_pixel(x, y, GREEN)
  
  
  
def check_collision(matrix):
    if matrix[y][x] == GREEN:
        return True
    else:
        return False


sense.stick.direction_any = draw_astronaut

while True:
    matrix = gen_pipes(matrix)
    if check_collision(matrix):
        break
    for i in range(3):
        matrix = move_pipes(matrix)
        sense.set_pixels(flatten(matrix))
        sense.set_pixel(x, y, GREEN) 
        if check_collision(matrix):
            break
        sleep(1)
