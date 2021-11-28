# -- author: Igor Nozdrin --
# -- Created by Igor at 11/19/2021 --
# -- coding = "utf-8" ---
from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, 'span.group'):
                txt = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=txt, id=id))
        return list(self.group_cache)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, 'new').click()
        self.fill_group_form(group)
        wd.find_element(By.NAME, 'submit').click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, field_value):
        wd = self.app.wd
        if field_value is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(field_value)

    def modify(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element(By.NAME, 'update').click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME, 'delete').click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))
