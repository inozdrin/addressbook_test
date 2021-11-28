# -- author: Igor Nozdrin --
# -- Created by Igor at 11/20/2021 --
# -- coding = "utf-8" ---
from model.group import Group


def test_delete_first_group(app):
    old_group_list = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    #   *** Delete the first group ***
    app.group.delete_first_group()
    # ******* Delete all groups one-by-one ******
    # while app.group.count() > 0:
    #     app.group.delete_first_group()
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list[0:1] = []
    assert old_group_list == new_group_list
