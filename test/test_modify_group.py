# -- author: Igor Nozdrin --
# -- Created by Igor at 11/20/2021 --
# -- coding = "utf-8" ---

from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    group = Group(name="New name")
    group.id = old_group_list[index].id
    app.group.modify_group_by_index(index, group)
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

# def test_modify_group_header(app):
#     old_group_list = app.group.get_group_list()
#     app.group.modify(Group(header='New group Header'))
#     new_group_list = app.group.get_group_list()
#     assert len(old_group_list) == len(new_group_list)
