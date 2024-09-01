from playwright.sync_api import Page, expect

def test_pw_action(page: Page):
    page.goto(url="http://www.自动化测试.com")
