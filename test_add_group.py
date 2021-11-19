# -- author: Igor Nozdrin --
# -- Created by Igor at 11/17/2021 --
# -- coding = "utf-8" ---


# from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username='admin', password='secret')
    app.create_group(Group(name='asdsafd', header='sdgdsaas', footer='asdfaf'))
    app.logout()


def test_add_empty_group(app):
    app.login(username='admin', password='secret')
    app.create_group(Group(name='', header='', footer=''))
    app.logout()
