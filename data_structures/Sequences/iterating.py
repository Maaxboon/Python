# Iterating: iterating through items in a sequence

# item
x = [7, 8, 3]

for item in x:
    print(item)

# index and item
y = [7, 8, 3]
for index, item in enumerate(y): # enumerate returns both index and item
    print(index, item)
