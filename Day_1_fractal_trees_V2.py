import turtle as tu
import random
from PIL import Image

# setup screen
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Random Fractal Trees 🌳")

# setup turtle
roo = tu.Turtle()
roo.hideturtle()
roo.speed(0)   # fastest
roo.penup()
roo.setpos(0, -250)
roo.setheading(90) #grow Upwards
roo.pendown()

def depth_color (depth, max_depth):
    """Return  a color that shifts with depth"""
    r = int(139 + (34-139) * (depth/max_depth))
    g = int(69 + (139-69)*(depth/max_depth))
    b = int(19 + (34-19)*(depth/max_depth))
    return f"#{r:02x}{g:02x}{b:02x}"


def draw(l, shrink_factor, depth=0, max_depth=8):
    """Recursive fractal tree drawer with random colors."""
    if l < 5 or depth > max_depth:
        return

    roo.pensize(max(1, (max_depth - depth) // 2))   # thinner as depth increases
    roo.pencolor(depth_color(depth, max_depth))     #gradient color
    roo.forward(l)
    pos = roo.pos()       # save state
    ang = roo.heading()

    # left branch
    roo.left(30+ random.randint(-5,5)) #Wind effect 
    draw(l * shrink_factor, shrink_factor, depth+1, max_depth)
   #reset 
    roo.penup(); roo.setpos(pos); roo.setheading(ang); roo.pendown()

    # right branch
    roo.right(30 + random.randint(-5,5) )
    draw(l * shrink_factor, shrink_factor, depth+1, max_depth)

    # back to trunk
    roo.penup(); roo.setpos(pos); roo.setheading(ang); roo.pendown()

    roo.backward(l)

# --- Draw multiple trees in different positions ---
positions = [(-200, -250), (-60, -250), (80, -250), (220, -250)]
lengths = [80, 100, 90, 70]
shrink_factors = [0.75, 0.8, 0.7, 0.78]

for (x, y), L, sf in zip(positions, lengths, shrink_factors):
    roo.penup()
    roo.setpos(x, y)
    roo.setheading(90)  # grow upwards
    roo.pendown()
    draw(L, sf)

wn.exitonclick()

# --- Draw Tree ---
draw(100, 0.75, max_depth=10)

# --- Save to PNG ---
ts = roo.getscreen().getcanvas()
ts.postscript(file="fractal_tree.eps")   # save as EPS
img = Image.open("fractal_tree.eps")
img.save("fractal_tree.png", "png", dpi=(300,300))  # high-res PNG

print("✅ Fractal Tree saved as fractal_tree.png")
wn.exitonclick()