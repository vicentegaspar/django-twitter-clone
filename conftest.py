import pytest

from pytest_factoryboy import register

from social.tests.factories import UserFactory, ProfileFactory

register(UserFactory)
register(ProfileFactory)
