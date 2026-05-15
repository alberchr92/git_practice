motorcycles = ['harley', 'kawasaki', 'yamaha']
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'bmw')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('kawasaki')
print(motorcycles)