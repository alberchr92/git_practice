cars = ['bmw', 'audi', 'toyota']
cars.sort()
print(cars)

#sortieren in umgekehrter Reihenfolge
cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)

print(len(cars), "\n")

#if-Anweisungen
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())