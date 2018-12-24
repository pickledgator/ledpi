import time
import random
import board
import adafruit_dotstar as dotstar

num_pixels = 240
dots = dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=0.2)

head = 0
tail = -30
color = 0xFF0000

while True:
    dots[head] = color
    dots[tail] = 0
    dots.show()
    time.sleep(1.0 / 50)
    print("head: {}, tail: {}".format(head, tail))

    head += 1
    if(head >= num_pixels):
        head = 0
        color >>= 8
        if(color == 0):
            color = 0xFF0000

    tail += 1
    if(tail >= num_pixels):
        tail = 0
    

