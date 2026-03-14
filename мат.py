import numpy as np
from scipy.optimize import linprog

supply = np.array([90, 40, 70])
demand = np.array([50, 50, 100])

cost_matrix = np.array([
    [3, 4, 2],
    [5, 6, 1],
    [8, 3, 5]
])

num_variables = supply.size * demand.size
costs = cost_matrix.flatten()

A_eq_supply = np.zeros((supply.size, num_variables))
for i in range(supply.size):
    A_eq_supply[i, i * demand.size:(i + 1) * demand.size] = 1

b_eq_supply = supply

A_eq_demand = np.zeros((demand.size, num_variables))
for j in range(demand.size):
    for i in range(supply.size):
        A_eq_demand[j, i * demand.size + j] = 1

b_eq_demand = demand

A_eq = np.vstack([A_eq_supply, A_eq_demand])
b_eq = np.concatenate([b_eq_supply, b_eq_demand])

result = linprog(c=costs, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')

if result.success:
    shipment_plan = result.x.reshape(supply.size, demand.size)
    print("Оптимальный план перевозок (по количеству):")
    print(shipment_plan)
    total_cost = np.sum(shipment_plan * cost_matrix)
    print(f"Общие затраты: {total_cost}")
else:
    print("Решение не найдено.")