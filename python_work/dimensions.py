dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# Tupel sind unveränderlich, daher führt der folgende Code zu einem Fehler
# dimensions[0] = 250
for dimension in dimensions:
    print(dimension)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)