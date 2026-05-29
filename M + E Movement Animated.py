
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Orbital radii (AU)
R_EARTH_AU = 1.0
R_MARS_AU = 1.821

# Orbital periods (Earth years) — sidereal, real-world
T_EARTH_YEARS = 1.0
T_MARS_YEARS = 1.821  # ~686.98 Earth days

# Simulation: how much time (in years) advances each frame
YEARS_PER_FRAME = 0.005

# Animation
INTERVAL_MS = 10
N_FRAMES = 1200  # ~5 simulated years total

# --- Static circular orbit paths ---
theta = np.linspace(0, 2 * np.pi, 600)

orbit_x_earth = R_EARTH_AU * np.cos(theta)
orbit_y_earth = R_EARTH_AU * np.sin(theta)
orbit_x_mars = R_MARS_AU * np.cos(theta)
orbit_y_mars = R_MARS_AU * np.sin(theta)

# --- Figure ---
fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(0, 0, "o", color="pink", markersize=17, label="Sun", zorder=3)
ax.plot(orbit_x_earth, orbit_y_earth, color="blue", linewidth=2, label="Earth orbit")
ax.plot(orbit_x_mars, orbit_y_mars, color="red", linewidth=2, label="Mars orbit")

(earth_dot,) = ax.plot([], [], "o", color="blue", markersize=10, label="Earth", zorder=4)
(mars_dot,) = ax.plot([], [], "o", color="red", markersize=10, label="Mars", zorder=4)

time_text = ax.text(
    0.02, 0.98, "", transform=ax.transAxes, va="top", fontsize=11,
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
)

ax.set_aspect("equal")
ax.set_xlabel("Distance from Sun (AU)")
ax.set_ylabel("Distance from Sun (AU)")
ax.set_title("Earth and Mars — independent orbital periods")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="upper right")

margin = 0.12
ax.set_xlim(-R_MARS_AU - margin, R_MARS_AU + margin)
ax.set_ylim(-R_MARS_AU - margin, R_MARS_AU + margin)

plt.tight_layout()


def init():
    earth_dot.set_data([], [])
    mars_dot.set_data([], [])
    time_text.set_text("")
    return earth_dot, mars_dot, time_text


def update(frame):
    t_years = frame * YEARS_PER_FRAME

    theta_earth = 2 * np.pi * t_years / T_EARTH_YEARS
    theta_mars = 2 * np.pi * t_years / T_MARS_YEARS

    earth_dot.set_data(
        [R_EARTH_AU * np.cos(theta_earth)],
        [R_EARTH_AU * np.sin(theta_earth)],
    )
    mars_dot.set_data(
        [R_MARS_AU * np.cos(theta_mars)],
        [R_MARS_AU * np.sin(theta_mars)],
    )

    time_text.set_text(
        f"Sim time: {t_years:.2f} yr\n"
        f"Earth: {t_years / T_EARTH_YEARS:.2f} orbits\n"
        f"Mars:  {t_years / T_MARS_YEARS:.2f} orbits"
    )

    return earth_dot, mars_dot, time_text


ani = FuncAnimation(
    fig,
    update,
    frames=N_FRAMES,
    init_func=init,
    blit=True,
    interval=INTERVAL_MS,
    repeat=True,
)

plt.show()