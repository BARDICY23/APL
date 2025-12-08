words = ["python", "lambda", "programming", "map", "function"]

first_last_chars = list(map(lambda w: (w[0], w[-1]), words))

print(first_last_chars)
