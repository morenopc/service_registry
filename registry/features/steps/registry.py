from behave import given, when, then
from core.models import Service as ServiceRegistry
from django.contrib.auth.models import User
from rest_framework_jwt import utils
from rest_framework.test import APIClient

api_client = APIClient()


@given('there is an empty ServiceRegistry')
def an_empty_service_registry(context):
    pass


@given('there is a superuser with a JWtoken')
def a_superuser_with_a_jwtoken(context):

    user = User.objects.create_superuser(username='tester',
                                         email='tester@mail.com',
                                         password='t&s3TEr3')

    payload = utils.jwt_payload_handler(user)
    token = utils.jwt_encode_handler(payload)
    context.auth = 'JWT {0}'.format(token)


@when('I add a service "{service}" with version "{version}"')
def add_a_service(context, service, version):
    context.response = context.test.client.post(
        context.get_url('service-list'),
        {"service": service, "version": version},
        HTTP_AUTHORIZATION=context.auth)


@then('I should be notified with a change "{change}"')
def i_should_be_notified(context, change):
    context.test.assertEqual(context.response.data.get('change'), change)


@when('I search for a service "{service}" with version "{version}"')
def search_for_a_service_with_version(context, service, version):
    context.response = context.test.client.get(
        context.get_url('search'),
        {"service": service, "version": version},
        HTTP_AUTHORIZATION=context.auth)


@then('I should find count "{count:d}" instances of service')
def i_find_number_of_instances_service(context, count):
    context.test.assertEqual(context.response.data.get('count'), count)


@then('the service "{service}" should have the correct type')
def the_service_should_have_the_correct_type(context, service):
    context.test.assertEqual(context.response.data.get('service'), service)


@then('the service "{service}" should have the correct version "{version}"')
def the_service_should_have_the_correct_version(context, service, version):
    context.test.assertEqual(context.response.data.get('service'), service)
    context.test.assertEqual(context.response.data.get('version'), version)


@when('I search for a non existing service '
      '"{service}" with version "{version}"')
def search_for_a_service_with_version(context, service, version):
    context.response = context.test.client.get(
        context.get_url('search'),
        {"service": service, "version": version},
        HTTP_AUTHORIZATION=context.auth)


@then('I should find count "{count:d}" services')
def i_find_number_of_services(context, count):
    context.test.assertEqual(context.response.data.get('count'), count)


@when('I search for a service "{service}" without version')
def search_for_a_service_without_version(context, service):
    context.response = context.test.client.get(
        context.get_url('search'),
        {"service": service},
        HTTP_AUTHORIZATION=context.auth)


@then('I should find count "{count:d}" services')
def i_find_number_of_services(context, count):
    context.test.assertEqual(context.response.data.get('count'), count)


@then('the service without version "{service}" should have the correct type')
def the_service_should_have_the_correct_type(context, service):
    context.test.assertEqual(context.response.data.get('service'), service)


@when('I update a service')
def i_update_a_service(context):
    context.response = api_client.put(
        context.get_url('update', pk=12),
        {"service": "test", "version": "0.0.4"},
        HTTP_AUTHORIZATION=context.auth)


@then('I should be notified with an update change "{change}"')
def should_be_notified_with_an_update_change(context, change):
    context.test.assertEqual(context.response.data.get('change'), change)


@when(u'I remove a service')
def i_remote_a_service(context):
    context.response = api_client.delete(
        context.get_url('remove', pk=16),
        HTTP_AUTHORIZATION=context.auth)
    context.test.assertEqual(context.response.data.get('change'), 'removed')


@then(u'the service should be removed')
def service_should_br_removed(context):
    context.test.assertEqual(
        ServiceRegistry.objects.filter(pk=16).exists(), False)


@then('I should be notified with a delete change "{change}"')
def should_notified_with_a_delete_change(context, change):
    context.test.assertEqual(context.response.data.get('change'), change)
