from django.test import TestCase
from .forms import BlogPostForm

class TestBlogPostForm(TestCase):
    
    def test_can_create_a_post_with_a_name(self):
        form = BlogPostForm(
            {
                "title":"test system",
                "cpu":"i5 Gen-8",
                "gpu":"GTX 1080",
                "ram":"8GB",
                "psu":"750W",
                "mainboard": "ASUS TEST",
                "primary_storage": "SSD TEST"
            }
        )
        self.assertTrue(form.is_valid())
        
        
    def test_correct_message_for_missing_required_field(self):
        form = BlogPostForm(
            {
                "title":"test system",
                "cpu":"i5 Gen-8",
                "gpu":"GTX 1080",
                "ram":"",
                "psu":"750W",
                "mainboard": "ASUS TEST",
                "primary_storage": "SSD TEST"
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['ram'], [u'This field is required.'])
        