# -- author: Igor Nozdrin --
# -- Created by Igor at 11/20/2021 --
# -- coding = "utf-8" ---

from model.group import Group


def test_modify_group_name(app):

    app.group.modify(Group(name='New group'))



def test_modify_group_header(app):

    app.group.modify(Group(header='New group Header'))

