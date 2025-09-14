#!/usr/bin/env python3
"""
Test script to validate the RO dynamics implementation for Example A
"""

import numpy as np
from scipy.integrate import odeint
import sys

# Problem parameters
a = np.array([1.0, 1.0])
P = np.eye(2)
b = 5.0

# Q matrices for ellipsoids
Q1 = np.array([[2.0, 0.0], [0.0, 2.0]])
Q2 = np.array([[5.0, -2.0], [-2.0, 4.0]])
Q3 = np.array([[4.0, 4.0], [4.0, 6.0]])
Q4 = np.array([[3.0, 0.0], [0.0, 8.0]])
Q5 = np.array([[5.0, 2.0], [2.0, 4.0]])
Q_matrices = [Q1, Q2, Q3, Q4, Q5]

# Expected solution from paper
x_star_expected = np.array([2.2674, 1.6636])
cost_expected = -28.5452

def objective_function(x):
    return -8*x[0] - 16*x[1] + x[0]**2 + 4*x[1]**2

def objective_gradient(x):
    return np.array([2*x[0] - 8, 8*x[1] - 16])

def h_functions(u, Q_matrices):
    h = np.zeros(len(Q_matrices))
    for j, Q in enumerate(Q_matrices):
        h[j] = u @ Q @ u - 1.0
    return h

def ro_dynamics(state, t, epsilon=0.0):
    # Unpack state [x(2), lambda(1), u(2), v(5)]
    x = state[0:2]
    lambda_val = state[2]
    u = state[3:5]
    v = state[5:10]
    
    # x dynamics
    dx = -objective_gradient(x) - (lambda_val + epsilon) * (a + P @ u)
    
    # lambda dynamics
    h_vals = h_functions(u, Q_matrices)
    lambda_dot_arg = (a + P @ u) @ x - b - v @ h_vals
    
    if lambda_val + epsilon > 0 or lambda_dot_arg > 0:
        dlambda = lambda_dot_arg
    else:
        dlambda = 0
    
    # u dynamics
    du = P.T @ x
    for j, Q in enumerate(Q_matrices):
        du -= 2 * v[j] * Q @ u
    
    # v dynamics
    dv = np.zeros(5)
    for j in range(5):
        v_dot_arg = (lambda_val + epsilon) * h_vals[j]
        if v[j] > 0 or v_dot_arg > 0:
            dv[j] = v_dot_arg
        else:
            dv[j] = 0
    
    return np.concatenate([dx, [dlambda], du, dv])

# Test the dynamics
print("Testing RO Dynamics for Example A")
print("="*50)

# Initial conditions
initial_state = np.zeros(10)
t_span = np.linspace(0, 50, 2000)

# Solve ODE
print("Solving ODE system...")
try:
    solution = odeint(ro_dynamics, initial_state, t_span, args=(0.0,))
    print("✓ ODE integration successful")
except Exception as e:
    print(f"✗ ODE integration failed: {e}")
    sys.exit(1)

# Extract final values
x_final = solution[-1, 0:2]
lambda_final = solution[-1, 2]
u_final = solution[-1, 3:5]
v_final = solution[-1, 5:10]
cost_final = objective_function(x_final)

# Check convergence
print("\nResults:")
print(f"  Final x: [{x_final[0]:.4f}, {x_final[1]:.4f}]")
print(f"  Expected x: [{x_star_expected[0]:.4f}, {x_star_expected[1]:.4f}]")
print(f"  Error in x: {np.linalg.norm(x_final - x_star_expected):.6f}")
print(f"  Final cost: {cost_final:.4f}")
print(f"  Expected cost: {cost_expected:.4f}")
print(f"  Error in cost: {abs(cost_final - cost_expected):.6f}")

# Validate results
tolerance = 1e-2
if np.linalg.norm(x_final - x_star_expected) < tolerance:
    print("\n✓ Solution matches expected values within tolerance")
else:
    print("\n✗ Solution does not match expected values")
    
# Check constraint satisfaction
constraint_value = (a + P @ u_final) @ x_final
print(f"\nConstraint check: (a + Pu)^T x = {constraint_value:.4f} <= {b}")
if constraint_value <= b + 1e-6:
    print("✓ Constraint satisfied")
else:
    print("✗ Constraint violated")

# Check which ellipsoids are active
h_final = h_functions(u_final, Q_matrices)
active_ellipsoids = []
for j, h_val in enumerate(h_final):
    if abs(h_val) < 1e-3:
        active_ellipsoids.append(j+1)
        
print(f"\nActive ellipsoids: {active_ellipsoids}")
print(f"Final u: [{u_final[0]:.4f}, {u_final[1]:.4f}]")

print("\n" + "="*50)
print("Test completed successfully!")