import pytest
from playwright.sync_api import sync_playwright, Page
from config.settings import BASE_URL
from pages.login_page import LoginPage
from utils.logger import logger


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        yield page
        browser.close()

@pytest.fixture
def valid_login(page):
    login_page = LoginPage(page)
    page.goto(BASE_URL)
    login_page.enter_username()
    login_page.enter_password()
    login_page.click_submit()
    logger.info("Logged in successfully")
    print(page.title())
    yield page