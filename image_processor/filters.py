from PIL import ImageFilter

def apply_blur(image):
    return image.filter(ImageFilter.BLUR)

def apply_contour(image):
    return image.filter(ImageFilter.CONTOUR)
