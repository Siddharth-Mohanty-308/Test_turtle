import streamlit as st
import turtle
import random
import time
import os

# Hide streamlit deprecation warnings
st.set_option('deprecation.showPyplotGlobalUse', False)

# Function to draw polygon inside polygon recursively
def draw_nested_polygons(t, sides=3, max_sides=7, length=100):
    if sides > max_sides:
        return
    t.color(random.random(), random.random(), random.random())
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    # Move to center of current shape
    t.forward(length / 3)
    draw_nested_polygons(t, sides + 1, max_sides, length / 1.5)

# Function to clear the screen and draw again
def draw_once(screen):
    screen.clear()
    t = turtle.Turtle()
    t.speed(0)
    screen.bgcolor("black")
    t.pensize(2)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_nested_polygons(t)
    screen.update()

# Streamlit app
st.title("Recursive Turtle Drawing in Streamlit")

# Canvas rendering using turtle (infinite loop simulation)
placeholder = st.empty()

run = st.checkbox("Run Drawing", value=False)

if run:
    screen = turtle.Screen()
    screen.tracer(0)

    while True:
        draw_once(screen)
        time.sleep(2)
else:
    st.write("Check the box above to start drawing.")
