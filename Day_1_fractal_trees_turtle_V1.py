# fractal_trees_turtle.py
import turtle, random, math
from PIL import Image

# Window
wn = turtle.Screen()
wn.setup(900, 700)
wn.bgcolor('#07101a')
wn.title("Fractal Trees — Turtle")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)
t.penup()
t.goto(-250, -250)
t.pendown()

# parameters
random.seed()
max_depth = 7

def draw_branch(turtle_obj, length, depth, max_depth):
    if depth > max_depth or length < 6:
        return
    # color varies with depth
    r = 0.2 + 0.6*(depth/max_depth)
    g = 0.1 + 0.8*(1-depth/max_depth)
    b = 0.05 + 0.2*(1-depth/max_depth)
    turtle_obj.pencolor(r, g, b)

    turtle_obj.pensize(max(1, (max_depth - depth) * 0.9))
    turtle_obj.forward(length)

    # position for branches
    pos = turtle_obj.position()
    heading = turtle_obj.heading()

    # left branch
    turtle_obj.left(20 + random.uniform(0, 12))
    draw_branch(turtle_obj, length * (0.68 + random.uniform(-0.05, 0.08)), depth+1, max_depth)

    # restore and right branch
    turtle_obj.penup()
    turtle_obj.setposition(pos)
    turtle_obj.setheading(heading)
    turtle_obj.pendown()

    turtle_obj.right(20 + random.uniform(0, 12))
    draw_branch(turtle_obj, length * (0.68 + random.uniform(-0.05, 0.08)), depth+1, max_depth)

    # restore to original after drawing both sides
    turtle_obj.penup()
    turtle_obj.setposition(pos)
    turtle_obj.setheading(heading)
    turtle_obj.pendown()

# draw several trees across the screen
bases = [(-250, -250), (-90, -250), (70, -250), (230, -250)]
lengths = [120, 95, 110, 100]
depths = [6, 5, 6, 5]

for (bx, by), L, D in zip(bases, lengths, depths):
    t.penup()
    t.setposition(bx, by)
    t.setheading(90)  # upwards
    t.pendown()
    draw_branch(t, L, 0, D)

# Save the turtle canvas as PostScript and convert to PNG:
canvas = wn.getcanvas()
ps_file = "fractal_trees_turtle.ps"
canvas.postscript(file=ps_file, colormode='color')

# Convert to PNG (requires Pillow)
img = Image.open(ps_file)
img.save("fractal_trees_turtle.png", 'png')
print("Saved: fractal_trees_turtle.png")

# Keep the window until closed
wn.mainloop()
