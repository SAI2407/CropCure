import torch.nn as nn
import torch
import os

class TinyVGG(nn.Module):
  """ TinyVGG model architecture """
  def __init__(self , input_shape : int , hidden_units : int , output_shape : int) -> None :
    super().__init__()
    self.conv_block_1 = nn.Sequential(nn.Conv2d(in_channels = input_shape , out_channels = hidden_units , kernel_size = 3 , stride = 1 , padding = 1),
                                      nn.ReLU(),
                                      nn.Conv2d(in_channels = hidden_units , out_channels = hidden_units , kernel_size = 3 , stride = 1 , padding = 1),
                                      nn.ReLU(),
                                      nn.MaxPool2d(kernel_size = 2 , stride = 2)

                                      )
    self.conv_block_2 = nn.Sequential(nn.Conv2d(in_channels = hidden_units , out_channels = hidden_units , kernel_size = 3 , stride = 1 , padding = 1),
                                      nn.ReLU(),
                                      nn.Conv2d(in_channels = hidden_units , out_channels = hidden_units , kernel_size = 3 , stride = 1 , padding = 1),
                                      nn.ReLU(),
                                      nn.MaxPool2d(kernel_size = 2 , stride = 2)

                                      )
    self.classifier = nn.Sequential(nn.Flatten() ,
                                    nn.Linear(in_features = hidden_units*16*16,
                                              out_features = output_shape))
  def forward(self , x):
    x = self.conv_block_1(x)
    #print(x.shape)
    x = self.conv_block_2(x)
    #print(x.shape)
    x = self.classifier(x)
    #print(x.shape)
    return x
  

device = "cpu"
model = TinyVGG(input_shape=3, # number of color channels (3 for RGB)
                        hidden_units=10,
                        output_shape= 3).to(device)
leaf_model = TinyVGG(input_shape=3, # number of color channels (3 for RGB)
                        hidden_units=10,
                        output_shape= 2).to(device)


model.load_state_dict(torch.load(os.path.join("TinyVGG", "best_VGG_model_state_dict.pth")))
leaf_model.load_state_dict(torch.load(os.path.join("leaf-non-leaf", "best_leaf-not-leaf_model_state_dict.pth")))

