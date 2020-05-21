toppings = ['pepperoni','cheese','barbeque','chicken']

for topping in toppings:
	print("I like " , topping , " pizza!\n")

print("I like all pizza!")	

one_mill = list(range(1,1000001))
for i in one_mill:
	print(i)

max_million = max(one_mill)
min_million = min(one_mill)
sum_million = sum(one_mill)

print("max: ", max_million)
print("min: ", min_million)
print("sum: ", sum_million)

odd_nums = [num+2 for num in range(-1,18)]
print("odd numbers less than 20:", odd_nums)

multiplesOfThree = [num*3 for num in range(3,31)]
print("\nmultiples of 3: ", multiplesOfThree)

cubedUnderTen = [num**3 for num in range(1,11)]
for i in cubedUnderTen:
	print(i)