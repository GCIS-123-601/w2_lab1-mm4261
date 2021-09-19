import turtle

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.goto(50,40)
    turtle.down()
    turtle.home()
    turtle.circle(25)
def turtle_state():
    print(turtle.isdown())
    print(turtle.heading())
    print(turtle.xcor(),turtle.ycor())
def main():
    turtle_state()
    test_drive()
    input("Press ENTER Key to Continue..")
    turtle_state()
main()