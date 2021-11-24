# -- author: Igor Nozdrin --
# -- Created by Igor at 11/17/2021 --
# -- coding = "utf-8" ---


# from selenium.webdriver.common.action_chains import ActionChains
import pytest
from model.group import Group
from fixture.group_helper import GroupHelper
from fixture.application import Application


def test_add_group(app):
    app.group.create(Group(name='asdsafd', header='sdgdsaas', footer='asdfaf'))


def test_add_empty_group(app):
    app.group.create(Group(name='', header='', footer=''))
