# quick check to make sure the answer is right
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# the values i got
theta = 0.525193  # radians
M = 0.029880
X = 55.013785

# load the real data
data = pd.read_csv('xy_data.csv')
x_data = data['x'].values
y_data = data['y'].values

# calculate my curve
t_vals = np.linspace(6, 60, 1000)
x_calc = t_vals * np.cos(theta) - np.exp(M * np.abs(t_vals)) * np.sin(0.3 * t_vals) * np.sin(theta) + X
y_calc = 42 + t_vals * np.sin(theta) + np.exp(M * np.abs(t_vals)) * np.sin(0.3 * t_vals) * np.cos(theta)

print(f"t range: 6 to 60")
print(f"calculated x range: {x_calc.min():.2f} to {x_calc.max():.2f}")
print(f"calculated y range: {y_calc.min():.2f} to {y_calc.max():.2f}")
print(f"actual data x range: {x_data.min():.2f} to {x_data.max():.2f}")
print(f"actual data y range: {y_data.min():.2f} to {y_data.max():.2f}")

# plot to visually check
plt.figure(figsize=(10, 8))
plt.scatter(x_data, y_data, c='blue', s=20, alpha=0.5, label='actual data', zorder=1)
plt.plot(x_calc, y_calc, 'r-', linewidth=3, label='my curve (t=6 to 60)', zorder=2)

# mark start and end points
plt.plot(x_calc[0], y_calc[0], 'go', markersize=12, label=f't=6 start', zorder=3)
plt.plot(x_calc[-1], y_calc[-1], 'mo', markersize=12, label=f't=60 end', zorder=3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('verification: does my curve match the data?')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.tight_layout()
plt.savefig('verification_check.png', dpi=100)
print("\nsaved verification_check.png")

# check a few specific t values
print("\nChecking specific t values:")
for t_test in [6, 15, 30, 45, 60]:
    x_t = t_test * np.cos(theta) - np.exp(M * abs(t_test)) * np.sin(0.3 * t_test) * np.sin(theta) + X
    y_t = 42 + t_test * np.sin(theta) + np.exp(M * abs(t_test)) * np.sin(0.3 * t_test) * np.cos(theta)
    print(f"  t={t_test:2d}: x={x_t:.2f}, y={y_t:.2f}")

plt.show()
