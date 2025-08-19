from PIL import Image
import torch
from torchvision import transforms

test_transform = transforms.Compose([transforms.Resize(size = (64 , 64)) , transforms.ToTensor()])

def transformation(img_path , device) :
    img = Image.open(img_path).convert("RGB")
    # Apply transform and show transformed image
    img_transform = test_transform(img).to(torch.float32)  # ensure correct dtype
    # Prepare image for model
    img_model = img_transform.unsqueeze(0).to(device)  # shape: (1, C, H, W)
    return img_model