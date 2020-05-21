places_to_visit = ['New York', 'Paris', 'Hollywood', 'Iceland', 'Egypt']


print("original order: ", places_to_visit)

print("\nalphabetical list: ", sorted(places_to_visit))

print("\nmy list has not changed: ", places_to_visit)

print("\nreverse alphabetical order: ", sorted(places_to_visit, reverse=True))

places_to_visit.reverse()
print("\nreverse order: ", places_to_visit)

places_to_visit.reverse()
print("\nback to beginning: ", places_to_visit)

places_to_visit.sort()
print("\nthe list is now sorted: ", places_to_visit)

places_to_visit.sort(reverse=True)
print("\nthe list is now sorted in reverse!: ", places_to_visit)