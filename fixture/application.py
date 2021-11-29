# -- author: Igor Nozdrin --
# -- Created by Igor at 11/19/2021 --
# -- coding = "utf-8" ---
from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper

import time


class Application:

    def __init__(self):
        self.wd = WebDriver()
        # self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def check_tabs(self):  # Checking if Chrome Settings  Tab opens when browser starts
        if len(self.wd.window_handles) > 1:
            current_window = self.wd.window_handles[1]
            chrome_sett_tab = self.wd.window_handles[0]
            self.wd.switch_to.window(chrome_sett_tab)
            self.wd.close()
            self.wd.switch_to.window(current_window)
        else:
            pass

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/addressbook/')


    def destroy(self):
        self.wd.quit()
