'''
epoch = 1 forward and backward pass of ALL training samples
batch_size = number of training samples in one forward & backward pass
number of iterations = number of passes, each pass using [batch_size] number of samples
e.g. 100 samples, batch_size=20 --> 100/20 = 5 iterations for 1 epoch
'''

import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math

import torchvision.datasets

class WineDataset(Dataset):
    def __init__(self):
        # data loading
        xy = np.loadtxt('/Users/tarawutchaisri/Desktop/pytorch/data/wine.csv', delimiter=",", dtype=np.float32, skiprows=1)
        self.x = torch.from_numpy(xy[:, 1:])
        self.y = torch.from_numpy(xy[:, [0]])
        self.n_samples = xy.shape[0]

    def __getitem__(self,index):
        # dataset[0]
        return self.x[index], self.y[index]
    
    def __len__(self):
        # len(dataset)
        return self.n_samples
    
dataset = WineDataset()
# first_data = dataset[0]
# features, labels = first_data
# print(features, labels)
dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True)
# datatiter = iter(dataloader)
# data = next(datatiter)
# features, labels = data
# print(features, labels)
num_epochs = 2
total_samples = len(dataset)
n_iterations = math.ceil(total_samples / 4)
print(total_samples,n_iterations)
for epoch in range(num_epochs):
    for i, (inputs, labels) in enumerate(dataloader):
        # forward backward, update
        if (i+1) % 5 == 0:
            print(f'epoch {epoch+1}/{num_epochs}, step {i+1}/{n_iterations}, inputs {inputs.shape}')

# fashion-mnist,, cifar, coco
train_dataset = torchvision.datasets.MNIST(root='./data',
                                           train=True,
                                           transform=torchvision.transforms.ToTensor(),
                                           download=True
                                           )
train_loader = DataLoader(dataset=train_dataset,
                          batch_size=3,
                          shuffle=True
                          )

dataiter = iter(train_loader)
data = next(dataiter)
inputs, targets = data
print(inputs.shape, targets.shape)