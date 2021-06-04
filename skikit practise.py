

import os

path = '/Users/lewis/AppData/Local/Programs/Python/Python39/test images'

files = os.listdir(path)

originalImages = []
brightened = []
filtered = []

for f in files:
    originalImages.append(f)
    print(f)

print(originalImages)

def brightImages(x):
    from skimage import exposure
    image_bright = exposure.adjust_gamma(x,gamma=0.5,gain=1)
    brightenened.append(image_bright)

def filterImage(x):
    from skimage.io import imread
    from skimage.filters import sobel_h
    image = imread(x,as_gray=True)
    img_sobel = sobel_h(image)
    filtered.append(img_sobel)

def displayImages(x):
    from skimage.io import imread, imshow
    import matplotlib.pyplot as plt
    
    for f in originalImages:
        filterImage(x)
        brightImage(x)
        
    for f in originalImages:
        
        plt.subplot(plot), imshow(originalImage[int(f)])
        plt.title('Original Photo')
        
        plt.subplot(plot), imshow(brightened[int(f)])
        plt.title('Brightened Photo')
        
        plt.subplot(plot), imshow(filtered[int(f)])
        plt.title('Filtered Photo')

        plt.show()     

displayImages(originalImages)
