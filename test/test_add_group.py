# -- author: Igor Nozdrin --
# -- Created by Igor at 11/17/2021 --
# -- coding = "utf-8" ---


# from selenium.webdriver.common.action_chains import ActionChains
import pytest
from model.group import Group
from fixture.group_helper import GroupHelper
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='asdsafd', header='sdgdsaas', footer='asdfaf'))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='', header='', footer=''))
    app.session.logout()
