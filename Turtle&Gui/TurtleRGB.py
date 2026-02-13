

tim = t.Turtle()
t.colormode(255)

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(38)
    tim.setheading(random.choice(directions))