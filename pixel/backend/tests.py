import tempfile

from django.test import TestCase, Client, override_settings
from django.urls import reverse
from PIL import Image

from .models import ImageModel, PixelCount


class TestBackend(TestCase):
    """Тест доступности главной страницы \
        и 404 ошибку на еще не существующей '/result/1'"""
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    @override_settings(DEBUG=False)
    def test_page_not_found(self):
        not_found_url = '/result/1'
        with self.subTest("Not found (404)"):
            response = self.client.get(not_found_url, follow=True)
            self.assertEqual(response.status_code, 404)


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class TestUploadImage(TestCase):
    """Тест загрузки изображения \
        и последующего добавления записей в модели ImageModel и PixelCount"""
    def setUp(self):
        self.client = Client()
        self.img = self.create_image()

    def tearDown(self):
        self.img.close()

    @staticmethod
    def create_image():
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            image = Image.new('RGB', (200, 200), 'white')
            image.save(f, 'PNG')

        return open(f.name, mode='rb')

    def test_upload_image(self):
        self.post = self.client.post('/', {
                'image': self.img
            }, follow=True)
        with self.subTest("upload image"):
            self.assertEqual(self.post.status_code, 200)
            self.assertEqual(ImageModel.objects.count(), 1)
            self.assertEqual(PixelCount.objects.count(), 1)

        response = self.client.get(reverse('result', args=[1]))
        self.assertEqual(response.status_code, 200)


@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class TestPixelCount(TestCase):
    """Тест обработки изображения"""
    @staticmethod
    def create_image():
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            image = Image.new('RGB', (200, 200), 'red')
            image.save(f, 'PNG')

        return open(f.name, mode='rb')

    def setUp(self):
        self.client = Client()
        self.img = self.create_image()
        self.post = self.client.post('/', {
            'image': self.img
        }, follow=True)

    def tearDown(self):
        self.img.close()

    def test_black_or_white(self):
        black_or_white = PixelCount.objects.filter(id=1)[0].black_or_white
        self.assertEqual(black_or_white, 'equal')

    def test_json_field(self):
        json_field = PixelCount.objects.filter(id=1)[0].hex_colors
        self.assertIn('#ff0000', json_field.keys())
