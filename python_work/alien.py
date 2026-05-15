alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0 ['color'] = 'green'
alien_0 ['points'] = 5
print(alien_0)
alien_0['color'] = 'orange'
print(alien_0)

alien_0 = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x-position']}")
#Bewege das Raumschiff nach rechts.
#Bestimme die Entfernung, die das Raumschiff basierend auf seiner Geschwindigkeit bewegen soll.
#verschoben werden muss
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #Dies muss ein schnelles Schiff sein
    x_increment = 3

alien_0['x-position'] = alien_0['x-position'] + x_increment
print(f"New position: {alien_0['x-position']}")

alien_0['speed'] = 'fast'
print(f"New position: {alien_0['x-position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)