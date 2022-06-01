from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        self.category=Category.objects.create(category='testing')
        self.location=Location.objects.create(location='testing')
        self.image=Image.objects.create(image='testing',image_name='testing',image_caption='testing',category=self.category,location=self.location)
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_save_image(self):
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_delete_image(self):
        self.image.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images)==0)
    def test_update_image(self):
        self.image.update_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_get_image_by_id(self):
        self.image.get_image_by_id()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_search_image(self):
        self.image.search_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_filter_by_location(self):
        self.image.filter_by_location()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_filter_by_category(self):
        self.image.filter_by_category()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_get_images_by_id(self):
        self.image.get_images_by_id()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

class LocationTestCase(TestCase):
    def setUp(self):
        self.location=Location.objects.create(location='testing')
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
    def test_save_location(self):
        self.location.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_delete_location(self):
        self.location.delete_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)
    def test_update_location(self):
        self.location.update_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_get_location_by_id(self):
        self.location.get_location_by_id()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_search_location(self):
        self.location.search_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_filter_by_location(self):
        self.location.filter_by_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_filter_by_category(self):
        self.location.filter_by_category()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_get_locations_by_id(self):
        self.location.get_locations_by_id()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category=Category.objects.create(category='testing')
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
    def test_save_category(self):
        self.category.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_delete_category(self):
        self.category.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)==0)
    def test_update_category(self):
        self.category.update_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_get_category_by_id(self):
        self.category.get_category_by_id()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_search_category(self):
        self.category.search_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_filter_by_location(self):
        self.category.filter_by_location()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_filter_by_category(self):
        self.category.filter_by_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)
    def test_get_categories_by_id(self):
        self.category.get_categories_by_id()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)