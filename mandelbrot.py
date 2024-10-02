import pygame
import math
import cmath

pygame.init()
pygame.display.set_caption("mandelbrot")
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0,0,0))

def Mandelbrot(c):
    z =  complex(0,0)
    counter = 0
    while abs(z) <2 and counter <80:
        z = z*z+c
        counter +=1
    return counter


t = -.03
while t<.04:
    t+=.001

    m = .07
    while m<.9:
        m+=.001
        c = complex(t, m)
        num = Mandelbrot(c)
        if num < 20:
            screen.set_at((int(t*1000+400), int(m*1000-400)), (num*7, num*3, num*10))

        #print("num is ", num, " at ", t, m)
        pygame.display.flip()

pygame.time.wait(10000)
pygame.quit
