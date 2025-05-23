from urllib import response
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from . import views, models


"""
class SmokeTest(TestCase):
	def test_bad_maths(self):
		self.assertEqual(1+1, 3)
"""

class HomePageTest(TestCase):
	# def test_root_url_resolves_to_home_page_view(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, views.home_page)

	def test_only_saves_items_when_necessary(self):
		self.client.get('/')
		self.assertEqual(models.Item.objects.count(), 0)

	def test_home_page_returns_correct_html(self):
		# request = HttpRequest()
		# response = views.home_page(request)
		response = self.client.get('/')

		# html = response.content.decode('utf8')
		# self.assertTrue(html.startswith('<!DOCTYPE html>'))
		# self.assertIn('lists', html)
		# self.assertTrue(html.endswith('</html>'))

		# expected_html = render_to_string('lists/home.html')
		# self.assertEqual(expected_html, html)

		self.assertTemplateUsed(response, 'lists/home.html')

	def test_can_save_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})

		self.assertEqual(models.Item.objects.count(), 1)
		new_item = models.Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

	def test_redirects_after_POST(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
		# self.assertIn('A new list item', response.content.decode())
		# self.assertTemplateUsed(response, 'lists/home.html')

	def test_displays_all_list_items(self):
		models.Item.objects.create(text='itemey 1')
		models.Item.objects.create(text='itemey 2')

		response = self.client.get('/')

		self.assertIn('itemey 1', response.content.decode())
		self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		first_item = models.Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = models.Item()
		second_item.text = 'Item the second'
		second_item.save()

		saved_items = models.Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewTest(TestCase):
	def test_uses_list_template(self):
		response = self.client.get('/lists/the-only-list-in-the-world/')
		self.assertTemplateUsed(response, 'lists/list.html')

	def test_displays_all_items(self):
		models.Item.objects.create(text='itemey 1')
		models.Item.objects.create(text='itemey 2')

		response = self.client.get('/lists/the-only-list-in-the-world/')

		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2')