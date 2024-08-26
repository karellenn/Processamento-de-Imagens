import unittest
from image_processor.io import load_image, save_image

class TestIO(unittest.TestCase):
    def test_load_image(self):
        image = load_image("tests/imagem1.jpg")
        self.assertIsNotNone(image)

    def test_save_image(self):
        image = load_image("tests/imagem1.jpg")
        save_image(image, "tests/test_output.jpg")
        output_image = load_image("tests/test_output.jpg")
        self.assertIsNotNone(output_image)

if __name__ == "__main__":
    unittest.main()
