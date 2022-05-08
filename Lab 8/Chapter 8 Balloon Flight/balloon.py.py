# -*- coding: utf-8 -*-

import pgzrun
from pgzero.builtins import Actor
from random import randint

WIDTH = 800
HEIGHT = 600
GRAVITY_STRENGTH = 1

# define actors
balloon = Actor('balloon')
balloon.pos = 400, 300

bird = Actor('bird-up')
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor('house')
house.pos = randint(800, 1600), 460

tree = Actor('tree')
tree.pos = randint(800, 1600), 450

# define flags
bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0

# for score keeping
scores = []

# to flag midpoints for incrementing score
birdPassedMidpoint = False
housePassedMidpoint = False
treePassedMidpoint = False

def update_high_scores():
    global score, scores
    filename = (r'C:\Users\lingt\OneDrive\Documents\EE104\Lab 8\Chapter 8 Balloon Flight\high-scores.txt')
    scores = []
    with open(filename, 'r') as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + ' ')
                score = int(high_score)
            else:
                scores.append(str(high_score) + ' ')
    with open(filename, 'w') as file:
        for high_score in scores:
            file.write(high_score)


def display_high_scores():
    screen.draw.text('HIGH SCORES', (350, 150), color='black')
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + '.  ' + high_score, (350, y),
                         color='black')
        y += 25
        position += 1


def draw():
    screen.blit('background', (0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text('Score: ' + str(score), (700, 5), color='black')
    else:
        display_high_scores()


def on_mouse_down():
    global up, game_over
    up = True
    balloon.y -= 50


def on_mouse_up():
    global up
    up = False


def flap():
    global bird_up
    if bird_up:
        bird.image = 'bird-down'
        bird_up = False
    else:
        bird.image = 'bird-up'
        bird_up = True


def update():
    global game_over, score, number_of_updates
    # flags for objects passing the balloon/midpoint
    global birdPassedMidpoint, housePassedMidpoint, treePassedMidpoint
    if not game_over:
        if not up:
            balloon.y += GRAVITY_STRENGTH  # gravity
        if bird.x > 0:
            # case statement to incrment score if balloon passes bird
            if bird.x < 400 and birdPassedMidpoint == False:
                score += 1
                birdPassedMidpoint = True #flags midpoint
            bird.x -= 6 # + 2 speed
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            birdPassedMidpoint = False #resets midpoint flag
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            number_of_updates = 0

        if house.right > 0:
            # case statement to incrment score if balloon passes house
            if house.x < 400 and housePassedMidpoint == False:
                score += 1
                housePassedMidpoint = True #flags midpoint
            house.x -= 2
        else:
            housePassedMidpoint = False #resets midpoint flag
            house.x = randint(800, 1600)

        if tree.right > 0:
            # case statement to incrment score if balloon passes tree
            if tree.x < 400 and treePassedMidpoint == False:
                score += 1
                treePassedMidpoint = True #flags midpoint
            tree.x -= 2
        else:
            treePassedMidpoint = False #resets midpoint flag
            tree.x = randint(800, 1600)
            # if tree is within 200 from house
            if (tree.x < (house.x + 200) and tree.x > (house.x - 200)):
                tree.x = house.x + 500 # space out tree from house by 500

        #adjusted so top of balloon can go off screen a little for more mobility
        if balloon.top < -100 or balloon.bottom > 560:
            game_over = True
            update_high_scores()

        if (balloon.collidepoint(bird.x, bird.y) or
                balloon.collidepoint(house.x, house.y) or
                balloon.collidepoint(tree.x, tree.y)):
            game_over = True
            update_high_scores()


pgzrun.go()