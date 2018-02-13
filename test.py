import pulp as p

print('Hello world!')

obj = p.LpProblem('Get Wasted', p.LpMaximize)

b = p.LpVariable('beer', lowBound = 0)
w = p.LpVariable('wine', lowBound = 0)

obj += 0.05*b + 0.12*w

obj += 0.2*b + 1.2*w <= 30
obj += 15*b + 30*w <= 1500

print(obj)

obj.solve()

p.LpStatus[obj.status]

for var in obj.variables():
	print(var.name, "=", var.varValue)

print(p.value(obj.objective))
