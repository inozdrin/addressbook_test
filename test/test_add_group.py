# -- author: Igor Nozdrin --
# -- Created by Igor at 11/17/2021 --
# -- coding = "utf-8" ---


# from selenium.webdriver.common.action_chains import ActionChains
import pytest
from model.group import Group
from sys import maxsize
from fixture.group_helper import GroupHelper
from fixture.application import Application


def test_add_group(app):
    old_group_list = app.group.get_group_list()
    group = Group(name='asdsafd', header='sdgdsaas', footer='asdfaf')
    app.group.create(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)

    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_group_list = app.group.get_group_list()
#     group = Group(name='', header='', footer='')
#     app.group.create(group)
#     assert len(old_group_list) + 1 == app.group.count()
#     new_group_list = app.group.get_group_list()
#     old_group_list.append(group)
#     assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)



