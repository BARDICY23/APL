numbers = [10, 20, 30, 40, 50]

min_num = min(numbers)
max_num = max(numbers)

normalized = list(map(lambda x: (x - min_num) / (max_num - min_num), numbers))

print(normalized)
