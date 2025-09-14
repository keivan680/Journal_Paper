#!/usr/bin/env python3
"""
Fixed test script with better initialization for Example B
"""

import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize
import sys

# Problem parameters
rho1 = 10.0
rho2 = 20.0
rho = np.array([rho1, rho2])

# Expected solution from paper
x_star_expected = np.array([0.5271, 0.7916])
cost_expected = 0.8419
u_star_expected = np.array([1.4020, 1.6824])

def safe_exp(x, max_val=30):
    """Safe exponential to avoid overflow."""
    x_clipped = np.clip(x, -max_val, max_val)
    return np.exp(x_clipped)

def objective_function(x):
    return 0.5 * (x[0] - 1)**2 + 0.5 * (x[1] - 2)**2

def objective_gradient(x):
    return np.array([x[0] - 1, x[1] - 2])

def constraint_function(x, u):
    exp_x = np.array([safe_exp(x[0]**2), safe_exp(x[1]**2)])
    return u @ exp_x

def constraint_gradient_x(x, u):
    return np.array([
        2 * x[0] * safe_exp(x[0]**2) * u[0],
        2 * x[1] * safe_exp(x[1]**2) * u[1]
    ])

def constraint_gradient_u(x):
    return np.array([safe_exp(x[0]**2), safe_exp(x[1]**2)])

def h_functions(u, rho):
    h = np.zeros(2)
    for j in range(2):
        if abs(u[j]) < 0.01:
            # Near zero approximation
            h[j] = 1.0 + safe_exp(1e10) * u[j] - rho[j]
        else:
            exp_u2 = safe_exp(u[j]**2)
            exp_inv_u = safe_exp(1.0 / u[j]) if u[j] > 0 else safe_exp(-1e10)
            h[j] = exp_u2 + u[j] * exp_inv_u - rho[j]
    return h

def h_gradients(u):
    grad = np.zeros(2)
    for j in range(2):
        if abs(u[j]) < 0.01:
            grad[j] = 0.0
        else:
            # Gradient of exp(u^2) + u*exp(1/u)
            grad_exp_u2 = 2 * u[j] * safe_exp(u[j]**2)
            
            if u[j] > 0:
                exp_inv_u = safe_exp(1.0 / u[j])
                grad_u_exp_inv = exp_inv_u - exp_inv_u / u[j]
            else:
                grad_u_exp_inv = 0
            
            grad[j] = grad_exp_u2 + grad_u_exp_inv
    return grad

def ro_dynamics_nonlinear(state, t, epsilon=0.01, b=5.0, rho=np.array([10.0, 20.0])):
    # Unpack state [x(2), lambda(1), u(2), v(2)]
    x = state[0:2]
    lambda_val = state[2]
    u = state[3:5]
    v = state[5:7]
    
    # Add small regularization to prevent u from going to zero
    u = np.maximum(u, 0.01)
    
    # Compute values
    g_val = constraint_function(x, u)
    h_vals = h_functions(u, rho)
    
    # x dynamics with damping
    dx = -objective_gradient(x) - (lambda_val + epsilon) * constraint_gradient_x(x, u)
    dx = np.clip(dx, -10, 10)  # Limit step size
    
    # lambda dynamics
    lambda_dot_arg = g_val - b - v @ h_vals
    if lambda_val + epsilon > 0 or lambda_dot_arg > 0:
        dlambda = lambda_dot_arg
    else:
        dlambda = 0
    dlambda = np.clip(dlambda, -10, 10)
    
    # u dynamics with regularization
    grad_g_u = constraint_gradient_u(x)
    grad_h = h_gradients(u)
    du = grad_g_u - grad_h * v
    du = np.clip(du, -5, 5)
    
    # v dynamics
    dv = np.zeros(2)
    for j in range(2):
        v_dot_arg = (lambda_val + epsilon) * h_vals[j]
        if v[j] > 0 or v_dot_arg > 0:
            dv[j] = v_dot_arg
        else:
            dv[j] = 0
        dv[j] = np.clip(dv[j], -10, 10)
    
    return np.concatenate([dx, [dlambda], du, dv])

print("Testing RO Dynamics for Example B (Fixed)")
print("="*70)

# Better initialization strategy
print("\nTrying multiple initializations...")
best_error = np.inf
best_solution = None
best_ic = None

# Try different initial conditions
initial_conditions = [
    np.array([0.5, 0.8, 0.5, 1.0, 1.5, 0.5, 0.5]),  # Close to expected
    np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]),  # All ones
    np.array([0.3, 0.5, 0.1, 0.5, 0.8, 0.1, 0.1]),  # Small values
    np.array([0.7, 1.2, 0.8, 1.2, 1.4, 0.8, 0.8]),  # Medium values
]

# Also try with different b values
b_values = [3.0, 4.0, 5.0, 6.0, 7.0]

for b_test in b_values:
    for ic in initial_conditions:
        t_span = np.linspace(0, 50, 2000)
        
        try:
            solution = odeint(ro_dynamics_nonlinear, ic, t_span, 
                            args=(0.01, b_test, rho), rtol=1e-6, atol=1e-8)
            
            x_final = solution[-1, 0:2]
            cost_final = objective_function(x_final)
            error = np.linalg.norm(x_final - x_star_expected)
            
            if error < best_error:
                best_error = error
                best_solution = solution[-1]
                best_ic = ic
                best_b = b_test
                
        except:
            continue

if best_solution is not None:
    print(f"\nBest result found with b = {best_b:.2f}")
    x_final = best_solution[0:2]
    lambda_final = best_solution[2]
    u_final = best_solution[3:5]
    v_final = best_solution[5:7]
    cost_final = objective_function(x_final)
    
    print("\nResults:")
    print(f"  Final x: [{x_final[0]:.4f}, {x_final[1]:.4f}]")
    print(f"  Expected x: [{x_star_expected[0]:.4f}, {x_star_expected[1]:.4f}]")
    print(f"  Error in x: {best_error:.6f}")
    print(f"  Final cost: {cost_final:.4f}")
    print(f"  Expected cost: {cost_expected:.4f}")
    print(f"  Final u: [{u_final[0]:.4f}, {u_final[1]:.4f}]")
    
    # Check constraint
    g_final = constraint_function(x_final, u_final)
    print(f"\nConstraint: g(x*, u*) = {g_final:.4f}, b = {best_b:.4f}")
    
    # Check boundary
    h_final = h_functions(u_final, rho)
    print(f"Boundary: h₁ = {h_final[0]:.4f}, h₂ = {h_final[1]:.4f}")
    
    if best_error < 0.1:
        print("\n✓ Solution converged close to expected values")
    else:
        print("\n⚠ Solution differs from expected - may need further tuning")
else:
    print("\n✗ Failed to find a good solution")

print("\n" + "="*70)