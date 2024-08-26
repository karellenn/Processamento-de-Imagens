import unittest
from PIL import Image
from image_processor.filters import apply_blur, apply_contour

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.image = Image.new('RGB', (100, 100), color = 'red')

    def test_apply_blur(self):
        blurred_image = apply_blur(self.image)
        self.assertIsNotNone(blurred_image)

    def test_apply_contour(self):
        contoured_image = apply_contour(self.image)
        self.assertIsNotNone(contoured_image)

if __name__ == "__main__":
    unittest.main()
