from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
import pygame

pygame.init()
pygame.mixer.init()

def play_main_theme_sound():
    pygame.mixer.music.load("Midnight_Rendezvous.mp3")
    pygame.mixer.music.play(-1)

def play_eat_sound():
    eat_sound = pygame.mixer.Sound("music_food.wav")
    eat_sound.play()

def play_collision_sound():
    collision_sound = pygame.mixer.Sound("game_over.wav")
    collision_sound.play()

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
apple = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
play_main_theme_sound()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake_off_canvas = ((snake.head.xcor() >= 290 or snake.head.xcor() <= -290) or
                        (snake.head.ycor() >= 290 or snake.head.ycor() <= -290))

    #Detect when the snake eats the apple
    if snake.head.distance(apple) <= 15:
        apple.refresh()
        snake.increase_snake()
        scoreboard.increase_score()
        play_eat_sound()

    #Detect when the snake collides with herself or with the wall
    if snake_off_canvas or snake.collision():
        scoreboard.reset()
        snake.reset()
        play_collision_sound()
        play_main_theme_sound()

screen.exitonclick()