import unittest

from src.http_helper.http_meta import parser_http_referer


class ReviewTest(unittest.TestCase):

    def test_parser_http_referer(self):
        http_referer = 'http://localhost:8000/edit_page/2/'
        result = parser_http_referer(http_referer)
        self.assertEqual(result['path'], 'edit_page')
        self.assertEqual(result['id'], '2')

    def test_parser_http_referer_app_url(self):
        http_referer = 'http://localhost:8000/articles/write_article'
        result = parser_http_referer(http_referer)
        self.assertEqual(result['path'], 'articles')
        self.assertEqual(result['id'], 'write_article')
