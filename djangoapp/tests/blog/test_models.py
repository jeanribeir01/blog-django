from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Post, Category


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='123')
        cls.category = Category.objects.create(name='Tecnologia')
        dummy_image = SimpleUploadedFile(
            name='test_image.gif',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
            content_type='image/gif'
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title='Um Título Bem Grande Para o Post',
            slug='um-titulo-bem-grande',
            body='Este é o corpo do nosso post de teste.',
            image=dummy_image
        )
        cls.post.categories.add(cls.category)

    def test_title_content(self):
        self.assertEqual(self.post.title, 'Um Título Bem Grande Para o Post')

    def test_string_representation(self):
        self.assertEqual(str(self.post), 'Um Título Bem Grande Para o Post')

    def test_post_is_related_to_user_and_category(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.categories.count(), 1)
        self.assertEqual(self.post.categories.first().name, 'Tecnologia')

    def test_image_is_assigned_correctly(self):
        self.assertIsNotNone(self.post.image)
        self.assertTrue(self.post.image.name.startswith('blog-post-image/'))