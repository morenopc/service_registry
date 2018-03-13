from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt import utils


class ServicesAPITestCase(APITestCase):

    fixtures = ['core-services.json', ]

    def setUp(self):

        user = User.objects.create_superuser(username='tester',
                                             email='tester@mail.com',
                                             password='t&s3TEr3')

        payload = utils.jwt_payload_handler(user)
        token = utils.jwt_encode_handler(payload)

        self.auth = 'JWT {0}'.format(token)

    def test_get_services(self):
        """GET /api/v1/registries/ must return status code 200"""
        
        resp = self.client.get(reverse('service-list'), HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        self.assertEqual(len(resp.data), 6)

    def test_add_service(self):
        """
            POST /api/v1/registries/ must return status code 201
            JSON response {"service":"test3","version":"0.0.1","change":"created"}"""

        resp = self.client.post(reverse('service-list'),
                               {"service":"test3", "version":"0.0.1"},
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content,
            {"service":"test3","version":"0.0.1","change":"created"})

    def test_find_service(self):
        """
            GET /api/v1/search/ must return status code 200 and
            JSON response {"service":"test","version":"0.0.1","count":2}
        """

        resp = self.client.get(reverse('search'),
                               {"service":"test", "version":"0.0.1"},
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content,
            {"service":"test","version":"0.0.1","count":2})

    def test_find_non_existing_service(self):
        """
            GET /api/v1/search/ must return status code 404 and
            JSON response {"service":"test","version":"0.0.4","count":0}
        """

        resp = self.client.get(reverse('search'),
                               {"service":"test", "version":"0.0.4"},
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_404_NOT_FOUND, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content,
            {"service":"test","version":"0.0.4","count":0})

    def test_find_service_without_version(self):
        """
            GET /api/v1/search/ must return status code 200 and
            JSON response {"service":"test","count":4}
        """

        resp = self.client.get(reverse('search'),
                               {"service":"test"},
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content, {"service":"test","count":4})

    def test_search_without_parameter(self):
        """GET /api/v1/search/ must return status code 500"""

        resp = self.client.get(reverse('search'),
                               {"version":"0.0.1"},
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_500_INTERNAL_SERVER_ERROR, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content,
            {"detail":"Search parameter (service) could not be found"})

    def test_search_without_service(self):
        """GET /api/v1/search/ must return status code 500"""

        resp = self.client.get(reverse('search'),
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_500_INTERNAL_SERVER_ERROR, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content,
            {"detail":"Search parameters (service or version) could not be found"})

    def test_update_service(self):
        """
            PUT /api/v1/search/ must return status code 200 and
            JSON response {"change":"changed"}
        """

        resp = self.client.put(reverse('update', args=[12]),
                               {"service":"test", "version":"0.0.4"},
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content, {"change":"changed"})

    def test_remove_service(self):
        """
            DELETE /api/v1/search/ must return status code 200 and
            JSON response {"service":"test2","change":"removed"}
        """

        resp = self.client.delete(reverse('remove', args=[16]),
                               HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)
        # JSON Response
        self.assertJSONEqual(resp.content, {"service":"test2","change":"removed"})
