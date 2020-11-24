import turtle
import winsound

# adding the screen and customizing it
win = turtle.Screen()
win.title("Pong by Dipesh")
# win.bgcolor("Red")
win.bgpic("bg.png")
win.setup(800, 600)
win.tracer(0)  # it helps the code to operate quick and accurate

# Paddle A/ Player 1(left player)
player1 = turtle.Turtle()
player1.speed(1)
player1.shape("square")
player1.color("white")
player1.penup()  # removes the line
player1.goto(-380, 0)
player1.shapesize(5, 1)  # default size is (20X20) so now the size is (20X5=100, 20X1=20).....

# Paddle B/ Player 2(right player)
player2 = turtle.Turtle()
player2.speed(1)
player2.shape("square")
player2.penup()
player2.goto(380, 0)
player2.shapesize(5, 1)

# BALL
ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.color("grey")
# for the movement of the ball
ball.dx = 0.4
ball.dy = 0.4


# SCORE
score_1 = 0
score_2 = 0

#TEXT ON THE WINDOW
pen = turtle.Turtle()
pen.speed(0)
pen.color("lightgreen")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player_1 = 0         player_2 = 0", align="center", font=("Courier", 18, "bold"))     #score for player1


# Player1 movement function
def player_1_up():
    y_player1 = player1.ycor()  # returns the y coordinate of the player
    if y_player1 <= (300 - 65):
        y_player1 +=60
    else:
        y_player1 += 0
    player1.sety(y_player1)


def player_1_down():
    y_player1 = player1.ycor()
    if y_player1 >= (-300 + 65):
        y_player1 -= 60
    else:
        y_player1 -= 0
    player1.sety(y_player1)

def player_2_up():
    y_player2 = player2.ycor()
    if y_player2 <= (300-65):
        y_player2 += 60
    else:
        y_player2 += 0
    player2.sety(y_player2)

def player_2_down():
    y_player2 = player2.ycor()
    if y_player2 >= (-300+65):
        y_player2 -= 60
    else:
        y_player2 += 0
    player2.sety(y_player2)

# keyBoard configuration
win.listen()
win.onkeypress(player_1_up, "w")
win.onkeypress(player_1_down, "s")
win.onkeypress(player_2_up, "Up")
win.onkeypress(player_2_down, "Down")

# Game loop
running = True
while (running):

    #  BALL MOVEMENT
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking along with ball movement
    if ball.ycor() > 290:   #UP WALL
        ball.sety(290)
        ball.dy *= -1  #it bounces the ball back and also controls the speed of the ball
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:   #RIGHT WALL
        # ball.goto(0, 0)   -->it will take the ball back to center
        ball.setx(390)
        ball.dx *= -1
        score_1 += 1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player_1 = {}         player_2 = {}".format(score_1, score_2), align="center", font=("Courier", 18, "bold"))

    if ball.ycor() < -280:  #DOWN WALL
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_2 += 1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player_1 = {}         player_2 = {}".format(score_1, score_2), align="center", font=("Courier", 18, "bold"))
    #Collisioin of ball and players
    ballx = ball.xcor()
    bally = ball.ycor()
    player1x = player1.xcor()
    player1y = player1.ycor()
    player2x = player1.xcor()
    player2y = player2.ycor()
    # for player2
    if (ballx > 360 and ballx < 380) and (bally < (player2y + 40) and bally > (player2y - 40)):
        ball.setx(350)
        ball.dx *= -1
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
    # for player1
    if (ballx< -360 and ballx> -380) and (bally > (player1y - 40) and bally < (player1y + 40)):
        ball.setx(-360)
        ball.dx *= -1
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
    # updates game window according to the changes done
    win.update()
