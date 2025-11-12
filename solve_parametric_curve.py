# trying to fit a parametric curve to the data points
# need to find theta, M, and X values

import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt

# load the CSV file with the data
data = pd.read_csv('xy_data.csv')
x_data = data['x'].values
y_data = data['y'].values

print(f"loaded {len(x_data)} points from csv")
print(f"x goes from {x_data.min():.2f} to {x_data.max():.2f}")
print(f"y goes from {y_data.min():.2f} to {y_data.max():.2f}")

# the parametric equations from the assignment
def calc_curve(t, theta, M, X):
    # x equation
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    # y equation  
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

# trying to minimize the error between my curve and the data
def error_function(params):
    theta, M, X = params
    
    # make t values - i think i need same number as data points?
    t_vals = np.linspace(6, 60, len(x_data))
    
    # calculate what x and y should be
    x_calc, y_calc = calc_curve(t_vals, theta, M, X)
    
    # not sure which data point matches which t value so i'll sort both
    # this seemed to work better than other methods i tried
    idx_data = np.argsort(x_data)
    idx_calc = np.argsort(x_calc)
    
    x_data_sorted = x_data[idx_data]
    y_data_sorted = y_data[idx_data]
    x_calc_sorted = x_calc[idx_calc]
    y_calc_sorted = y_calc[idx_calc]
    
    # sum of squared differences
    error = np.sum((x_data_sorted - x_calc_sorted)**2 + (y_data_sorted - y_calc_sorted)**2)
    
    return error

# calculate L1 distance for the assignment requirement
def calc_l1_distance(params):
    theta, M, X = params
    
    t_vals = np.linspace(6, 60, len(x_data))
    x_calc, y_calc = calc_curve(t_vals, theta, M, X)
    
    # sort again
    idx_data = np.argsort(x_data)
    idx_calc = np.argsort(x_calc)
    
    x_data_sorted = x_data[idx_data]
    y_data_sorted = y_data[idx_data]
    x_calc_sorted = x_calc[idx_calc]
    y_calc_sorted = y_calc[idx_calc]
    
    # L1 is sum of absolute differences
    l1 = np.sum(np.abs(x_data_sorted - x_calc_sorted) + np.abs(y_data_sorted - y_calc_sorted))
    
    return l1

# set the bounds from the assignment
# theta: 0 to 50 degrees (need to convert to radians for numpy)
# M: -0.05 to 0.05
# X: 0 to 100
bounds = [
    (np.deg2rad(0.1), np.deg2rad(49.9)),  # theta in radians
    (-0.049, 0.049),                       # M
    (0.1, 99.9)                            # X
]

print("\nstarting optimization...")
print("this might take a minute...")

# using differential_evolution because i read it's good for this type of problem
# tried a few other optimizers but this one worked best
result = differential_evolution(
    error_function,
    bounds,
    seed=42,  # for reproducibility
    maxiter=1000,
    popsize=30,
    polish=True  # refine the solution at the end
)

theta_result, M_result, X_result = result.x
theta_degrees = np.rad2deg(theta_result)

print(f"\noptimization done!")
print(f"converged: {result.success}")
print(f"final error: {result.fun:.6f}")
print(f"\nresults:")
print(f"  theta = {theta_degrees:.6f} degrees ({theta_result:.6f} radians)")
print(f"  M = {M_result:.6f}")
print(f"  X = {X_result:.6f}")

# calculate the L1 distance they asked for
l1 = calc_l1_distance(result.x)
print(f"\nL1 distance: {l1:.6f}")

# format for desmos submission
print(f"\n--- FOR DESMOS ---")
desmos_string = (
    f"\\left(t*\\cos({theta_result:.6f})"
    f"-e^{{{M_result:.6f}\\left|t\\right|}}\\cdot\\sin(0.3t)\\sin({theta_result:.6f})\\ "
    f"+{X_result:.6f},"
    f"42+\\ t*\\sin({theta_result:.6f})"
    f"+e^{{{M_result:.6f}\\left|t\\right|}}\\cdot\\sin(0.3t)\\cos({theta_result:.6f})\\right)"
)
print(desmos_string)
print("use domain: 6 <= t <= 60")

# plot the results to see how well it fits
print("\nmaking plot...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# plot the curve
t_plot = np.linspace(6, 60, 500)
x_curve, y_curve = calc_curve(t_plot, theta_result, M_result, X_result)

ax1.scatter(x_data, y_data, c='blue', s=10, alpha=0.5, label='data points')
ax1.plot(x_curve, y_curve, 'r-', linewidth=2, label='fitted curve')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('curve fit result')
ax1.legend()
ax1.grid(True, alpha=0.3)

# residuals plot
t_check = np.linspace(6, 60, len(x_data))
x_check, y_check = calc_curve(t_check, theta_result, M_result, X_result)

idx_data = np.argsort(x_data)
idx_check = np.argsort(x_check)

x_data_s = x_data[idx_data]
y_data_s = y_data[idx_data]
x_check_s = x_check[idx_check]
y_check_s = y_check[idx_check]

errors = np.sqrt((x_data_s - x_check_s)**2 + (y_data_s - y_check_s)**2)

ax2.scatter(range(len(errors)), errors, c='green', s=10, alpha=0.5)
ax2.set_xlabel('point index')
ax2.set_ylabel('error distance')
ax2.set_title('residuals')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fit_result.png', dpi=100)
print("saved plot as fit_result.png")

print("\ndone!")
