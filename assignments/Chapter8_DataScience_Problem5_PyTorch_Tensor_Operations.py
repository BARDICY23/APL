import torch

t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([4, 5, 6])

dot_product = torch.dot(t1, t2)
element_wise = t1 * t2

print(f"Dot Product: {dot_product}")
print(f"Element-wise Multiplication: {element_wise}")
