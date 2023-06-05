## Completing Data Collection and Cleansing, as well as with resize data onto same size
## Completing Model Buiding and Tuning

- Data Collection has done using web scraping method through Google Images.
- Data Cleansing has done on images that is not relevant with the real traditional music instruments.
- Data Resize has done by converting various different size of images onto the same size of 256x256 px.
- Data Detail:
  - Bonang: 127 images
  - Kolintang: 101 images
  - Rebab: 68 images
  - Saluang: 107 images
  - Sape: 147 images
  - Sasando: 98 images
  - Tifa: 88 images

- Model has been builded using custom model and adapted by custom datasets and model architecture.
- Model have better performance and precision than the previous model by converting all training images into grayscale

## Completing Model Deployment Setup

- Model is saved in HDF5 format
- Model is deployed with Flask
- Model is deployed in Google Cloud Platform
- Model is deployed using CI/CD cycle and Docker