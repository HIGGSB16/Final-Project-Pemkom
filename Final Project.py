import pygame, sys, math, time
from pygame.locals import *
from math import pi, sin, cos

pygame.init()

# Variable

WHITE = (255,255,255)
BLACK = (0,0,0)
Theta = pi/2
a = 0
v = 0
u = float(
    input(
        "Friction Coefficient: "
        )
    )
c = 1 - u

# Window

BG = pygame.display.set_mode(
    (500, 400), 0, 32
    )
BG.fill(
    WHITE
    )
Capt = pygame.display.set_caption(
    "Simulation"
    )

# Clock

Clock = pygame.time.Clock()

# Initial Time

t = 0
dt = time.time()
T = True

# Using Font

font2 = pygame.font.SysFont(
    "Calibri", 26
    )

# Track

Track = pygame.draw.arc(
    BG, BLACK, (50, 0, 400, 400),pi, pi*2, 2
    )
Wall1 = pygame.draw.line(
    BG, (BLACK), (0, 200), (50, 200)
    )
Wall2 = pygame.draw.line(
    BG, (BLACK), (450, 210), (500, 210)
    )

# Main Program

while True:
    Clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # STOP TIMER
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                T = not True

    # TIMER
    if True:
        t = time.time() - dt

    Txt = font2.render(
        str(
            round(t, 2)
            ),
        True, BLACK
        )
    BG.blit(
        Txt, (0, 50)
        )
    
    x = int(
        sin(Theta)
        * 200) + 250
    y = int(
        cos(Theta)
        * 200) + 190
    print(
        round(
            v,5
            )
        )
    a = -0.01*sin(Theta)
    v += a
    v *= c
    Theta += v
    
    Ball = pygame.draw.circle(
        BG, BLACK, (x,y), 10
        )
    pygame.display.flip()





    

