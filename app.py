import turtle
import time

# Set up the screen
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=600, height=400)

# Initial scores
score_a = 0
score_b = 0

# 30-second timer
start_time = time.time()
game_duration = 30  # in seconds

# Input player names
player_a_name = win.textinput("Player A", "Enter name for Player A:")
player_b_name = win.textinput("Player B", "Enter name for Player B:")
if not player_a_name:
    player_a_name = "Player A"
if not player_b_name:
    player_b_name = "Player B"

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 7  # Decreased value to slow down the ball in the x-direction
ball.dy = -7  # Decreased value to slow down the ball in the y-direction

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 160)
score_display.write("{}: {}  {}: {}".format(player_a_name, score_a, player_b_name, score_b), align="center",
                     font=("Courier", 24, "normal"))

# Timer display
timer_display = turtle.Turtle()
timer_display.speed(0)
timer_display.color("white")
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(0, -180)

# Functions
def update_score():
    score_display.clear()
    score_display.write("{}: {}  {}: {}".format(player_a_name, score_a, player_b_name, score_b), align="center",
                        font=("Courier", 24, "normal"))

def update_timer():
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(game_duration - elapsed_time, 0)
    timer_display.clear()
    timer_display.write("Time: {}".format(remaining_time), align="center", font=("Courier", 24, "normal"))
    if remaining_time == 0:
        end_game()

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 180:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -180:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 180:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -180:
        y -= 20
    paddle_b.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
def move():
    global score_a, score_b
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        update_score()

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        update_score()

    # Paddle and ball collisions
    if (ball.dx > 0) and (250 > ball.xcor() > 240) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(240)
        ball.dx *= -1

    if (ball.dx < 0) and (-250 < ball.xcor() < -240) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-240)
        ball.dx *= -1

    update_timer()
    win.update()
    win.ontimer(move, 10)  # Call move function after 10 milliseconds

# Start the game loop
move()

# Function to end the game
def end_game():
    global score_a, score_b
    if score_a == score_b:
        message = "Game Over! It's a tie!"
    else:
        winner = player_a_name if score_a > score_b else player_b_name
        message = "Game Over! {} wins!".format(winner)
    timer_display.clear()
    timer_display.write(message, align="center", font=("Courier", 24, "normal"))
    time.sleep(5)
    win.bye()  # Close the game window

# Main loop
win.mainloop()
