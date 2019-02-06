#pong.py

import text_graphics_engine
import keyboard
import math
import random

screen = text_graphics_engine.screen([80,20]," ")
paddle_one = text_graphics_engine.obj([[0,5],[0,6],[0,7],[0,8],[0,9],[0,10]],"[",0,screen)
paddle_two = text_graphics_engine.obj([[80,5],[80,6],[80,7],[80,8],[80,9],[80,10]],"]",0,screen)
ball = text_graphics_engine.obj([[40,10]],"0",0,screen)
ball_angle = math.radians(45)
ball_speed = 0.5
ball_velo = [0,0]

done = False

while not done:
    try:
        if keyboard.is_pressed('p'):
            done = True
        if keyboard.is_pressed('s'):
            paddle_one + [0,1]
        if keyboard.is_pressed('w'):
            paddle_one + [0,-1]
        if keyboard.is_pressed('down'):
            paddle_two + [0,1]
        if keyboard.is_pressed('up'):
            paddle_two + [0,-1]        
    except:
        pass
    if round(ball.coords[0][1]) == 0 or round(ball.coords[0][1]) == 20:
        ball_angle = math.degrees(ball_angle)
        ball_angle = (180-ball_angle)%360
        ball_angle = math.radians(ball_angle)
    if (round(ball.coords[0][0]) == 0 or round(ball.coords[0][0]) == 80) and (ball == paddle_one or ball == paddle_two):
        ball_angle = math.degrees(ball_angle)
        ball_angle = (360-ball_angle)%360
        ball_angle += random.randrange(-1,2)
        ball_speed += 0
        ball_angle = math.radians(ball_angle)
    if ball.coords[0][0] < 0 or ball.coords[0][0] > 80:
        ball.set_coords([[40,10]])
        
    ball_velo = [(ball_speed*math.sin(ball_angle)),(ball_speed*math.cos(ball_angle)*-1)]
    ball + ball_velo
    screen.clear_screen([ball_speed])