import numpy as np
import torch 


sent1 = "hi my name is bob"
sent2 = "hi my what is goof "
sent3 = "what do you want from me???"
sent4 = "this is a good story you should read too"
sent5 = "what do you want now?"

x = torch.Tensor()
x = x.new_zeros([2,2])

print(x)

for row  in x:
    for elem in row: 
        x[row][elem] = 1

print(x)






























