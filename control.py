#! /bin/python3

import pygame
from movement import *

pygame.init()
window = pygame.display.set_mode((300, 300))
time = pygame.time.Clock()

left_motor = Motor( 11, 13 )
right_motor = Motor( 19, 15 )
movement = Movement( left_motor, right_motor )

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("left")
                movement.turnLeft()

            if event.key == pygame.K_d:
                print("right")
                movement.turnRight()

            if event.key == pygame.K_w:
                print("forward")
                movement.forward()

            if event.key == pygame.K_s:
                print("backward")
                movement.backward()

        if event.type == pygame.KEYUP:
            if event.key in ( pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s ):
                print("stopping")
                movement.stop()

    time.tick(60)
