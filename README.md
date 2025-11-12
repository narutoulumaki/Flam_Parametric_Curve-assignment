# Parametric Curve Fitting Assignment

## The Problem

I need to find three unknown values (θ, M, X) that make this parametric curve match the data points in `xy_data.csv`.

The equations are:
- x(t) = t*cos(θ) - e^(M|t|)*sin(0.3t)*sin(θ) + X
- y(t) = 42 + t*sin(θ) + e^(M|t|)*sin(0.3t)*cos(θ)

Where:
- 0° < θ < 50°
- -0.05 < M < 0.05  
- 0 < X < 100
- 6 < t < 60

## My Solution

After trying a bunch of different things, I found:

**θ = 30.091366°**  
**M = 0.029880**  
**X = 55.013786**

**L1 Distance: 457.913020**

## How I Did It

### What I Tried First

1. First I tried just guessing values and plotting them - that obviously didn't work well
2. Then I tried using scipy.optimize.minimize() but it kept getting stuck in local minima
3. Finally found differential_evolution which is apparently better for this kind of problem

### The Actual Approach

The main challenge was that I have 1500 data points but I don't know which point corresponds to which t value. 


I used `differential_evolution` from scipy because:
- It's good at finding global minima (not getting stuck)
- Doesn't need gradients
- Handles the weird oscillating exponential function better than other methods I tried

### Code Structure

```python
# Main function that calculates the curve
def calc_curve(t, theta, M, X):
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y


## Files

- `solve_parametric_curve.py` - main script
- `xy_data.csv` - the data points (1500 points)
- `fit_result.png` - plot showing how well it fits
- `README.md` - this file

## To Run

```bash
pip install numpy pandas scipy matplotlib
python solve_parametric_curve.py
```

## Issues I Ran Into

1. First tried with wrong t range (0 to 60 instead of 6 to 60) - that took forever to debug
2. Forgot to convert degrees to radians initially
3. The sorting trick wasn't obvious - spent a while trying other matching methods
4. Had to adjust population size and iterations to get good convergence
