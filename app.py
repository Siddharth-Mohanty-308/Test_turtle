import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# Set page config
st.set_page_config(page_title="Nested Polygons", layout="centered")

st.title("🎨 Nested Polygons with Random Colors")

placeholder = st.empty()

def regular_polygon(sides, radius, center=(0, 0)):
    angle = 2 * np.pi / sides
    return [
        (
            center[0] + radius * np.cos(i * angle - np.pi / 2),
            center[1] + radius * np.sin(i * angle - np.pi / 2)
        )
        for i in range(sides)
    ]

# Infinite loop
run = st.checkbox("Start Drawing", value=False)

while run:
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis("off")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    radius = 1.2
    for sides in range(3, 8):
        color = [random.random() for _ in range(3)]
        polygon = regular_polygon(sides, radius)
        x, y = zip(*polygon)
        ax.fill(x, y, color=color, edgecolor="white", linewidth=2)
        radius *= 0.75  # shrink for next shape

    placeholder.pyplot(fig)
    time.sleep(1.5)
else:
    st.info("Click the checkbox to start the drawing loop.")
