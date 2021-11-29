# -- author: Igor Nozdrin --
# -- Created by Igor at 11/19/2021 --
# -- coding = "utf-8" ---
# from fixture.application import Application
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').click()
        wd.find_element(By.NAME, 'user').clear()
        wd.find_element(By.NAME, 'user').send_keys(username)
        wd.find_element(By.NAME, 'pass').click()
        wd.find_element(By.NAME, 'pass').clear()
        wd.find_element(By.NAME, 'pass').send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def get_logged_user(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    # return wd.find_elements_by_xpath("//div/div[1]/form/b").text == "(" + username + ")"

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()
        else:
            pass

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
