import unittest
from image_processor.transformation import resize_image, convert_to_grayscale
from image_processor.io import load_image

class TestTransformation(unittest.TestCase):

    def setUp(self):
        self.image = load_image("tests/imagem1.jpg")

    def test_resize_image(self):
        resized_image = resize_image(self.image, (100, 100))
        self.assertEqual(resized_image.size, (100, 100))

    def test_convert_to_grayscale(self):
        grayscale_image = convert_to_grayscale(self.image)
        self.assertEqual(grayscale_image.mode, "L")

if __name__ == "__main__":
    unittest.main()
