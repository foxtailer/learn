from urllib import response
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from . import views


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