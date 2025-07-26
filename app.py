import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

st.set_page_config(page_title="Nested Edge-Sharing Polygons", layout="centered")
st.title("🌀 Nested Edge-Sharing Polygons (3 to 7 sides)")

placeholder = st.empty()

def generate_polygon(sides, side_length):
    """
    Generate coordinates of a regular polygon starting from bottom center,
    oriented such that one side lies flat on the x-axis.
    """
    angle = 2 * np.pi / sides
    R = side_length / (2 * np.sin(np.pi / sides))  # circumradius
    points = []
    for i in range(sides):
        theta = angle * i + np.pi / 2 - angle / 2  # rotate so one side is flat
        x = R * np.cos(theta)
        y = R * np.sin(theta)
        points.append((x, y))
    return np.array(points), R

# Infinite loop
run = st.checkbox("Start Drawing", value=False)

while run:
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis("off")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    side_length = 2.0  # constant side length for all shapes
    min_sides = 3
    max_sides = 7
    previous_radius = 0
    center_shift = np.array([0.0, 0.0])

    for sides in range(max_sides, min_sides - 1, -1):
        polygon, radius = generate_polygon(sides, side_length)

        # Translate the polygon upward so that the bottom edge aligns with previous shape's bottom
        shift_y = previous_radius - (-radius * np.sin(np.pi / sides)) if previous_radius else 0
        shifted_polygon = polygon + center_shift + [0, shift_y]

        color = [random.random() for _ in range(3)]
        ax.plot(*shifted_polygon.T, color=color, linewidth=2, marker='o')
        # Close the shape
        ax.plot([shifted_polygon[-1][0], shifted_polygon[0][0]],
                [shifted_polygon[-1][1], shifted_polygon[0][1]], color=color, linewidth=2)

        # Update center shift and radius
        center_shift = center_shift + [0, shift_y]
        previous_radius = radius * np.sin(np.pi / sides)

    placeholder.pyplot(fig)
    time.sleep(2)
else:
    st.info("Click the checkbox to start the drawing loop.")
