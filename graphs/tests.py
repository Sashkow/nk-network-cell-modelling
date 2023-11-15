from django.test import TestCase
from django.test.client import RequestFactory

from django.apps import apps
from django.apps import AppConfig

from graphs.models import Cell, Like
from django.contrib.auth.models import User

from django.urls import reverse


from django.http import HttpResponse, HttpResponseRedirect, HttpRequest


class MainViewTestCase(TestCase):
    fixtures = ["test_data.json"]

    def test_unauthed_user_auths_as_admin_by_default(self):
        """
        test unauthenticated user authenticates as 'admin' by default
        """
        self.assertTrue(True)
        self.assertEqual(self.client.session, {})
        response = self.client.get(reverse("index"))
        admin_pk = User.objects.get(username="admin").pk
        self.assertEqual(self.client.session["_auth_user_id"], admin_pk)


class AppConfigTestCase(TestCase):
    def test_graph_models_in_app_config(self):
        """
        check whether :model:`Cell` and :model:`Like` are in app_config models
        """
        graphs_app_config = apps.get_app_config("graphs")
        self.assertTrue(Cell in list(graphs_app_config.get_models()))
        self.assertTrue(Like in list(graphs_app_config.get_models()))


from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.cache import get_cache_key

from graphs.views import dynamic_image


class ImageCachingTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_cache_invalidation_with_no_cache(self):
        """
        test get_cache_key returns None for request with no cache
        """
        url = reverse("dynamic-image", args=("simplified_cell_states_graph",))
        request = self.factory.get(url)

        cache_key = get_cache_key(request)
        self.assertEqual(cache_key, None)

    # def test_cache_invalidation_with_cache(self):
    #     """
    #     same as :test:`test_cache_invalidation_with_no_cache` but with cache
    #     """
    #     url = reverse('dynamic-image', args=('simplified_cell_states_graph',))
    #     request = self.factory.get(url)
    #     response = self.client.get(url)
    #     cache_key = get_cache_key(request)
    #     self.assertFalse(cache_key == None)

    #     cache.delete(cache_key)


#         cache_key = get_cache_key(request)
#         self.assertEquals(cache_key, None) # fails


#     def test(self):
#         from graphs.views import expire_page_cache
#         expire_page_cache('dynamic-image', args=('simplified_cell_states_graph',))
