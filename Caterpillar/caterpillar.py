#importing libraries
import random
import turtle as t

t.bgcolor('yellow')

#Create a caterpillar
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
#caterpillar.hideturtle()

#Create a leaf turtle
leaf = t.Turtle()
leaf_shape = ((0,0), (14,2), (18,6), (20,20),\
    (6,18), (2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed(0)

#Adding text
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align = 'center',\
    font = ('Arial', 16, 'bold'))
text_turtle.hideturtle()
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#Placeholder Function
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x,y) = caterpillar.pos()
    outside = \
        x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside 

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align = 'center', font = ('Arial', 30, 'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align = 'right', font = ('Arial', 40, 'bold'))

def place_leaf():
    leaf.ht() #ht = hideturtle
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st() #st = showturtle

def start_game():
    global game_started
    if game_started:  # if the game already starts
        return
    game_started = True

    score = 0
    text_turtle.clear()  # this is to clear the text from the screen

    caterpillar_speed = 10
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    def move():
        nonlocal caterpillar_speed, caterpillar_length, score
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 1
            score += 10
            display_score(score)

        if outside_window():
            game_over()
            return
        t.ontimer(move, 100)  # Call move() function every 100 milliseconds

    move()  # Start the movement loop

def move_up():
    if caterpillar.heading() != 270:  # Ensure the caterpillar doesn't move directly down
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() != 90:  # Ensure the caterpillar doesn't move directly up
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() != 0:  # Ensure the caterpillar doesn't move directly right
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() != 180:  # Ensure the caterpillar doesn't move directly left
        caterpillar.setheading(0)
        

#Listening keys     
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
t.listen()
t.mainloop()