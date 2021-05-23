import albumentations as A
from albumentations.pytorch import ToTensorV2
import torch


BATCH_SIZE = 1
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
EPOCH = 10
LAMBDA_CYCLE = 10
LAMBDA_IDENTITY = 0.0
LEARNING_RATE = 2e-4
TRANSFORM = A.Compose([
    A.Resize(height=256, width=256),
    A.HorizontalFlip(p=0.5),
    A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255),
    ToTensorV2()
], additional_targets={'image0': 'image'})
