import torch
def tensor_ops():
    a = torch.tensor([1,2,3])
    b = torch.tensor([4,5,6])
    return torch.dot(a,b), a * b
if __name__ == '__main__':
    print('Dot Product:', tensor_ops()[0])
    print('Element-wise Multiplication:', tensor_ops()[1])
