import turtle

window = turtle.Screen()
window.bgcolor("sky blue")

turtle.done()
tree = turtle.Turtle()
tree.color("forest green")

tree.setposition(50, -50)
tree.setposition(-50, -50)
tree.setposition(0, 0)

tree.begin_fill()
tree.setposition(50, -50)
tree.setposition(-50, -50)
tree.setposition(0, 0)
tree.end_fill()
