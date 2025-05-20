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
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'lists/home.html')


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