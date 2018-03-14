
"""
behave environment module for testing behave-django
"""


def before_feature(context, feature):
        context.fixtures = ['core-services.json']
