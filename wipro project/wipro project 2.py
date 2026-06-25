#project 2
a= 0.51
b=a*24 #cost per day
c=b*7 #cost per week
d=c*30 #cost per month assuming 30 days in a month
budget= 918
e=budget/b #cost to operate on a budget
print(f"cost to operate one server per day: ${b:.2f}")
print(f"cost to operate one server per week: ${c:.2f}")
print(f"cost to operate one server per month: ${d:.2f}")
print(f"with ${budget}, uou can operate {e:.2f} days.")
