import RPi.GPIO as GPIO
import neopixel
import time
import board

NEO = 18
numNEO = 1
# GPIO.setmode(GPIO.BCM)
GPIO.setup(NEO, GPIO.OUT)
pixels = neopixel.NeoPixel(board.D18, numNEO)

# def show_neo(r, g, b):
#     inc_r=int(r/9)
#     inc_g=int(g/9)
#     inc_b=int(b/9)

#     pixels.fill((0, 0, 0))
#     pixels.show()
#     for j in range(0, 4) :
#         for i in range(0, numNEO) :
#             pixels[i]=(inc_r*(i+1), inc_g*(i+1), inc_b*(i+1))
#             time.sleep(0.1)
#         pixels.fill((r, g, b))
#         pixels.show()
#         time.sleep(0.5)
#         #for i in range(7, 0, -1):
#         pixels[i]=(0, 0, 0)
#         time.sleep(0.5)
#     time.sleep(3)

# while True:
#     show_neo(255, 255, 0)
#     show_neo(255, 0, 255)
#     show_neo(0, 0, 255)


while True:
    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)
    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(1)