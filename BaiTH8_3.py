import turtle, random
colors = ['red','green','blue','orange','purple','pink','yellow','aqua','navy','teal','coral',
          'tan','tomato','seashell','skyblue','violet','wheat','thistle','orchid']
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.speed(200)
    painter.right(30)
    painter.left(120)
    painter.setposition(9, 2)
