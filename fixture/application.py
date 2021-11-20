# -- author: Igor Nozdrin --
# -- Created by Igor at 11/19/2021 --
# -- coding = "utf-8" ---
from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.group_helper import GroupHelper
import time


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/addressbook/')
        time.sleep(3)


    def destroy(self):
        self.wd.quit()
