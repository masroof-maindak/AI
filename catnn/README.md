# Setup

```
# 1. Download
wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz

# 2. Extract
tar xzvf images.tar.gz

# 3. Keep images for only 5 cat classes
find images/* -type f ! -regex  '\(.*Abyssinian.*\|.*Bengal.*\|.*Bombay.*\|.*Egyptian_Mau.*\|.*Russian_Blue.*\)$' -delete

# 4. Install Python packages
uv sync
```

# Usage

```
uv run main.py
```

# Acknowledgements

## Dataset

- [Oxford-IIIT Pets Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)

## Convolutional Neural Networks

- [Ujjwal Karn's Blog - An Intuitive Explanation of Convolutional Neural Networks](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)
- [IBM Technology - What are Convolutional Neural Networks (CNNs)?](https://youtu.be/QzY57FaENXg?feature=shared)
- [DeepLearningBook - ConvNets](https://www.deeplearningbook.org/contents/convnets.html)
- [Alescontrela/Numpy-CNN](https://github.com/Alescontrela/Numpy-CNN)
- [Stanford CS231n - Lecture Slides](https://cs231n.stanford.edu/slides/2016/winter1516_lecture7.pdf)

### Convolution

- [Explained Visually - Image Kernels](https://setosa.io/ev/image-kernels/)
- [Better Explained - Convolution](https://betterexplained.com/articles/intuitive-convolution/)
- [Wikipedia - Kernel (Image Processing)](https://en.wikipedia.org/wiki/Kernel_(image_processing))
