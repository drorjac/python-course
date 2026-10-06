# ============================================================
#  S1_solar_system_pycharm.py
#  Part 1 Showcase - "AI builds a solar system"
#
#  The circles version of the solar system, as one standalone
#  script: the Sun, Mercury, Venus, Earth, Mars and the Moon.
#  This is what we ran in PyCharm: open this file and press Run.
#  A window opens with the animation. Close the window to stop.
#
#  You will meet lists (Lecture 5), loops (Lecture 6),
#  functions (Lecture 7) and plots (Lecture 10) later.
#  For now: read the comments, run it, and change numbers!
#  Needs matplotlib (PyCharm can install it for you).
# ============================================================
import math                                       # pi, cos, sin
import matplotlib.pyplot as plt                   # the drawing tool
from matplotlib.animation import FuncAnimation    # turns drawings into a movie

# ---- the planets: one list per property (item 0 = Mercury, 1 = Venus, ...) ----
names     = ["Mercury", "Venus", "Earth", "Mars"]
distances = [0.39, 0.72, 1.00, 1.52]       # distance from the Sun, in AU
periods   = [0.24, 0.62, 1.00, 1.88]       # time for one circle, in years
colors    = ["gray", "#C98A2B", "#1E3A8A", "#E8554E"]

moon_distance = 0.15     # NOT to scale (the real one: about 0.0026 AU)
moon_period = 0.0748     # 27.3 days, written in years
step = 0.01              # years per frame (about 4 days)


def position(distance, period, time):
    angle = 2 * math.pi * time / period      # how far around the circle
    return distance * math.cos(angle), distance * math.sin(angle)


def draw_solar_system(axes, time):
    axes.clear()                                       # wipe the old picture
    axes.set_xlim(-1.8, 1.8)
    axes.set_ylim(-1.8, 1.8)
    axes.set_aspect("equal")                           # circles look like circles
    axes.axis("off")                                   # no axis lines
    axes.plot(0, 0, "o", color="#F6B800", markersize=20)    # the Sun
    for i in range(len(names)):                        # for every planet...
        axes.add_patch(plt.Circle((0, 0), distances[i], fill=False, color="lightgray"))
        x, y = position(distances[i], periods[i], time)
        axes.plot(x, y, "o", color=colors[i], markersize=9)
        axes.text(x + 0.08, y + 0.08, names[i], fontsize=9)
    earth_x, earth_y = position(1.0, 1.0, time)        # the Moon rides along with Earth
    moon_x, moon_y = position(moon_distance, moon_period, time)
    axes.plot(earth_x + moon_x, earth_y + moon_y, "o", color="dimgray", markersize=4)
    axes.set_title(f"Our solar system - day {time * 365:.0f}")


def update(frame):                 # frame = 0, 1, 2, ...
    draw_solar_system(axes, frame * step)


fig, axes = plt.subplots(figsize=(6, 6))
anim = FuncAnimation(fig, update, frames=400, interval=40)   # 400 frames = about 4 years
plt.show()                                                   # opens the window
print("Window closed. Bye from Pip!")
