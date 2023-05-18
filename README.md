## Completing Data Collection and Cleansing, as well as with resize data onto same size
## Completing Model Buiding and Tuning

- Data Collection has done using web scraping method through Google Images.
- Data Cleansing has done on images that is not relevant with the real traditional music instruments.
- Data Resize has done by converting various different size of images onto the same size of 256x256 px.
- Data Detail:
  - Bonang: 127 images
  - Burdah: 31 images
  - Kolintang: 101 images
  - Rebab: 68 images
  - Saluang: 107 images
  - Sape: 147 images
  - Sasando: 98 images
  - Talindo: 9 images
  - Tifa: 88 images
  - Yi: 15 images

- Model has been builded using InceptionV3 pre-trained model and adapted by custom datasets and model architecture.
- Model still has very low precision such that it can't even predict other music instruments other than just Bonang and Saluang.