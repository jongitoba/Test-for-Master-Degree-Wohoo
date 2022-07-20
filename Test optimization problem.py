from docplex.mp.model import Model

m = Model(name = "Phone production")

# Variables
# -Phone production
phone1Prod = m.continuous_var(name = "Production og phone 1")
phone2Prod = m.continuous_var(name = "Production og phone 2")

# -Time
phone1Time = 1.5
phone2Time = 2

# -Price
phone1Price = 900
phone2Price = 1100



# Constraints
# -Prod
phone1Cons = m.add_constraint(phone1Prod >=500)
phone2Cons = m.add_constraint(phone2Prod >=200)

# -Time
totProdCons = m.add_constraint(m.sum((phone1Prod * phone1Time, phone2Prod * phone2Time)) <= 2999.5)



# Goal / Objective
m.maximize(phone1Prod * phone1Price + phone2Prod * phone2Price)



# Solving the problem
sol = m.solve()
sol.display()

