import os
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.utils import save_image

import config
from dataset import MyDataset
from discriminator_model import Discriminator
from generator_model import Generator


if not os.path.exists('./model/'):
    os.mkdir('./model/')
if not os.path.exists('./model/generator/'):
    os.mkdir('./model/generator/')
if not os.path.exists('./model/discriminator/'):
    os.mkdir('./model/discriminator/')
if not os.path.exists('./saved_img/'):
    os.mkdir('./saved_img/')

D_photo = Discriminator(in_channels=3).to(config.DEVICE)
D_monet = Discriminator(in_channels=3).to(config.DEVICE)
G_photo = Generator(img_channels=3, num_residuals=9).to(config.DEVICE)
G_monet = Generator(img_channels=3, num_residuals=9).to(config.DEVICE)
opt_D = optim.Adam(
    params=list(D_photo.parameters()) + list(D_monet.parameters()),
    lr=config.LEARNING_RATE,
    betas=(0.5, 0.999)
)
opt_G = optim.Adam(
    params=list(G_photo.parameters()) + list(G_monet.parameters()),
    lr=config.LEARNING_RATE,
    betas=(0.5, 0.999)
)
L1 = nn.L1Loss()
MSE = nn.MSELoss()

train_dataset = MyDataset(
    root_photo='./photo_jpg/',
    root_monet='./monet_jpg/',
    transform=config.TRANSFORM
)
val_dataset = MyDataset(
    root_photo='./photo_jpg/',
    root_monet='./monet_jpg/',
    transform=config.TRANSFORM
)
train_loader = DataLoader(train_dataset, batch_size=config.BATCH_SIZE, shuffle=True)

for epoch in range(1, config.EPOCH + 1):
    monet_reals = 0
    monet_fakes = 0
    loop = tqdm(train_loader, leave=True)
    for idx, (photo, monet) in enumerate(loop):
        photo = photo.to(config.DEVICE)
        monet = monet.to(config.DEVICE)

        # train discriminators
        fake_monet = G_monet(photo)
        D_monet_real = D_monet(monet)
        D_monet_fake = D_monet(fake_monet.detach())
        monet_reals += D_monet_real.mean().item()
        monet_fakes += D_monet_fake.mean().item()
        D_monet_real_loss = MSE(D_monet_real, torch.ones_like(D_monet_real))
        D_monet_fake_loss = MSE(D_monet_fake, torch.zeros_like(D_monet_fake))
        D_monet_loss = D_monet_real_loss + D_monet_fake_loss

        fake_photo = G_photo(monet)
        D_photo_real = D_photo(photo)
        D_photo_fake = D_photo(fake_photo.detach())
        D_photo_real_loss = MSE(D_photo_real, torch.ones_like(D_photo_real))
        D_photo_fake_loss = MSE(D_photo_fake, torch.zeros_like(D_photo_fake))
        D_photo_loss = D_photo_real_loss + D_photo_fake_loss

        D_loss = (D_photo_loss + D_monet_loss) / 2

        opt_D.zero_grad()
        D_loss.backward()
        opt_D.step()

        # train generators
        D_monet_fake = D_monet(fake_monet)
        D_photo_fake = D_photo(fake_photo)
        G_monet_loss = MSE(D_monet_fake, torch.ones_like(D_monet_fake))
        G_photo_loss = MSE(D_photo_fake, torch.zeros_like(D_photo_fake))

        cycle_photo = G_photo(fake_monet)
        cycle_monet = G_monet(fake_photo)
        cycle_photo_loss = L1(photo, cycle_photo)
        cycle_monet_loss = L1(monet, cycle_monet)

        identity_photo = G_photo(photo)
        identity_monet = G_monet(monet)
        identity_photo_loss = L1(photo, identity_photo)
        identity_monet_loss = L1(monet, identity_monet)

        G_loss = (
                G_monet_loss
                + G_photo_loss
                + cycle_monet_loss * config.LAMBDA_CYCLE
                + cycle_photo_loss * config.LAMBDA_CYCLE
                + identity_monet_loss * config.LAMBDA_IDENTITY
                + identity_photo_loss * config.LAMBDA_IDENTITY
        )

        opt_G.zero_grad()
        G_loss.backward()
        opt_G.step()

        if idx % 200 == 0:
            save_image(fake_monet * 0.5 + 0.5, f'./saved_img/monet{idx}.jpg')
            save_image(fake_photo * 0.5 + 0.5, f'./saved_img/photo{idx}.jpg')

        loop.set_postfix(monet_reals=monet_reals / (idx + 1), monet_fakes=monet_fakes / (idx + 1))

    print('[{:2d}/{:2d}] Generator Loss: {:8.6f} | Discriminator Loss: {:8.6f}'
          .format(epoch, config.EPOCH, G_loss, D_loss))

    # save models
    torch.save(G_photo.state_dict(), f'./model/generator/G_photo_epoch{epoch}.pth')
    torch.save(G_monet.state_dict(), f'./model/generator/G_monet_epoch{epoch}.pth')
    torch.save(D_photo.state_dict(), f'./model/discriminator/D_photo_epoch{epoch}.pth')
    torch.save(D_monet.state_dict(), f'./model/discriminator/D_monet_epoch{epoch}.pth')
