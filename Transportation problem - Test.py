from pulp import *

# Problem formulation
warehouses = ['A', 'B', 'C']

supply = {'A': 300, 
          'B': 600, 
          'C': 600}

projects = ['1', '2', '3']

demand = {'1': 150,
          '2': 450,
          '3': 900}

costs = [ # Project (col) x Warehouse (row)
         [5,1,9],
         [4,2,8],
         [8,7,2]
    ]

costs = makeDict([warehouses, projects], costs, 0)

# Initialize problem
prob = LpProblem("Material Supply Problem", LpMinimize)

# List of routes
Routes = [(w,p) for w in warehouses for p in projects]

vars = LpVariable.dicts("Route", (warehouses, projects), 0, None, LpInteger)

# Obj. func
prob += (
    lpSum([vars[w][p] * costs[w][p] for (w,p) in Routes]),
    "Sum of transporting costs", 
)

# Constraints

for w in warehouses:
    prob += (
        lpSum([vars[w][p] for p in projects]) <= supply[w],
        "Sum product out of warehouse %s" % w,
        )

for p in projects:
    prob += (
        lpSum([vars[w][p] for w in warehouses]) >= demand[p],
        "Sum products in to project %s" %p,
        )
    
# Solving model
prob.solve()

for v in prob.variables():
    print(v.name, " = ", v.varValue)
    
print("Value of Obj.Func = ", value(prob.objective))
    
    