from adafruit_circuitplayground import cp
import time

num_pixels = 10
black = (0,0,0)
Forward =(0,100,0)
Backward = (0,0,100)
Delay = .1

while True:
    for x in range(num_pixels):
        cp.pixels[x] = Forward
        time.sleep(Delay)
        cp.pixels[x] = black



    for x in range(num_pixels - 1, -1, -1) :
        cp.pixels[x]=Backward
        time.sleep(Delay)
        cp.pixels[x]= black

