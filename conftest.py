# -- author: Igor Nozdrin --
# -- Created by Igor at 11/20/2021 --
# -- coding = "utf-8" ---
import pytest
from fixture.application import Application

fixture = None  # declare global variable fixture for future checks


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.check_tabs()
        fixture.session.login(username='admin', password='secret')
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.check_tabs()
            fixture.session.login(username='admin', password='secret')
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
