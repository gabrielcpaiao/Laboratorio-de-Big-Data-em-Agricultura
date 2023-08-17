values = [10, 20, 30, 40, 50, 60, 70]
min_value = 20
max_value = 50
clipped_values = [min(max(value, min_value), max_value) for value in values]
print(clipped_values)