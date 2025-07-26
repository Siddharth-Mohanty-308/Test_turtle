import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# Streamlit page setup
st.set_page_config(page_title="Turtle-style Nested Polygons", layout="centered")
st.title("🌀 Turtle-style Nested Polygons (3 to 7 sides)")

placeholder = st.empty()

def generate_polygon(sides, side_length):
    """
    Generate a regular polygon with one base side aligned to the x-axis.
    Returns the vertices and radius used for spacing.
    """
    angle = 2 * np.pi / sides
    R = side_length / (2 * np.sin(np.pi / sides))  # circumradius
    points = []
    for i in range(sides):
        theta = i * angle + np.pi / 2 - angle / 2  # rotation to align base
        x = R * np.cos(theta)
        y = R * np.sin(theta)
        points.append((x, y))
    return np.array(points), R

# Checkbox to start/stop drawing loop
run = st.checkbox("Run Drawing", value=False)

while run:
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis("off")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    side_length = 2.0
    min_sides = 3
    max_sides = 7
    prev_radius = 0
    shift = np.array([0.0, 0.0])

    for sides in range(max_sides, min_sides - 1, -1):
        polygon, radius = generate_polygon(sides, side_length)

        # Shift upward so bottom side aligns with previous shape
        offset_y = prev_radius - (-radius * np.sin(np.pi / sides)) if prev_radius else 0
        shifted = polygon + shift + [0, offset_y]

        # Draw outline with random color
        color = [random.random() for _ in range(3)]
        ax.plot(*shifted.T, color=color, linewidth=2)
        ax.plot([shifted[-1][0], shifted[0][0]],
                [shifted[-1][1], shifted[0][1]], color=color, linewidth=2)

        shift += [0, offset_y]
        prev_radius = radius * np.sin(np.pi / sides)

    placeholder.pyplot(fig)
    time.sleep(2)
else:
    st.info("Check the box above to start the animation.")
