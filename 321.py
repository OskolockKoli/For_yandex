import shutil
import sys
import os.path
import pyomo.environ as pyo

from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, maximize, minimize, Constraint
from pyomo.opt import SolverFactory
import matplotlib.pyplot as plt
import numpy as np

a = 4
b = 5

a1 = 4
a2 = 2
a3 = 1
b1 = 4
b2 = 2
b3 = 1
n1 = 8
n2 = 8
n3 = 18

model = pyo.ConcreteModel()

model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

model.profit = Objective(
    expr = a*model.x + b*model.y,
    sense = minimize)

model.laborA = Constraint(expr = a1 * model.x + b1 * model.y <= n1)
model.laborB = Constraint(expr = a2 * model.x + b2 * model.y <= n2)
model.laborC = Constraint(expr = a3 * model.x + b3 * model.y >= n3)

fig, ax = plt.subplots(1, 1, figsize=(4, 4))
ax.set_aspect('equal')

ax.axis([0, 8, 0, 20])
ax.set_xlabel('X')
ax.set_ylabel('Y')

x1 = np.array([0, 8])
ax.plot(x1, (n1 - a1*x1) / b1, 'r', lw=2)
ax.plot(x1, (n2 - a2*x1) / b2, 'g', lw=2)
ax.plot(x1, (n3 - a3*x1) / b3, 'b', lw=2)

ax.fill_between([0, 0, 2], [0, 0, 0], [0, 2, 0], color='r', alpha=0.10)
ax.fill_between([0, 0, 4], [2, 4, 0], [2, 0, 0], color='g', alpha=0.10)
ax.fill_between([0, 0, 8], [0, 20, 20], [0, 18, 10], color='b', alpha=0.10)

plt.savefig(fname='plot', bbox_inches='tight')
