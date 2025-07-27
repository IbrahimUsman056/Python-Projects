import turtle
import time
import random

delay=0.2
score=0
highscore=0

#set up the screen
wn=turtle.Screen()
wn.title("SNAKE GAME BY IBRAHIM")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shapesize(0.5)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0,100)

#snake body empty at start
segments=[]

#scoreboard
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Ariel",24,"normal"))


#functions
def go_up():
    if(head.direction!="down"):
        head.direction="up"

def go_down():
    if(head.direction!="up"):
        head.direction="down"

def go_right():
    if(head.direction!="left"):
        head.direction="right"    

def go_left():
    if(head.direction!="right"):
        head.direction="left"

def move():
    if(head.direction=="up"):
        y=head.ycor()
        head.sety(y+20)
    
    if(head.direction=="down"):
        y=head.ycor()
        head.sety(y-20)

    if(head.direction=="right"):
        x=head.xcor()
        head.setx(x+20)

    if(head.direction=="left"):
        x=head.xcor()
        head.setx(x-20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")

#main game loop
while True:
    wn.update()

    #check for a collision with border
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        #hide the segments
        for seg in segments:
            seg.goto(1000,1000)
        #clear the segments list
        segments.clear()
        #reset score
        score=0
        #reset delay
        delay=0.2
        #update score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,highscore), align="center", font=("Ariel",24,"normal"))

    #check for collision with food
    if(head.distance(food)<20):
        #move food to random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a segment
        newsegment=turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape("circle")
        newsegment.color("lightgreen")
        newsegment.penup()
        segments.append(newsegment)
        #shorten the delay
        delay-=0.002
        #increase score
        score+=1
        if(score>highscore):
            highscore=score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,highscore), align="center", font=("Ariel",24,"normal"))

    #move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where head is
    if (len(segments)>0):
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision between head and segments
    for seg in segments:
        if(seg.distance(head)<20):
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide segments
            for seg in segments:
                seg.goto(1000,1000)
            #clear the segments list
            segments.clear()
            #reset score
            score=0
            #reset delay
            delay=0.2
            #update score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,highscore), align="center", font=("Ariel",24,"normal"))


    time.sleep(delay)
wn.mainloop()