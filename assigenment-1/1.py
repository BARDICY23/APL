###assignments/1

products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]

clean_products = list(map(lambda p: p.strip().title(), products))

print(clean_products)
