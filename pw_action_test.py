from playwright.sync_api import Page, expect

def test_pw_action(page: Page):
    page.goto(url="http://www.自动化测试.com")


def test_pw_notification_message(page: Page):
    page.goto("/demo/button", wait_until="networkidle")
    page.get_by_text("点击我试试1").click()
    expect(page.get_by_text("点击成功1")).to_be_visible()


def test_pw_new_page(page: Page):
    page.goto("/demo/link", wait_until="networkidle")
    page.get_by_text("本页跳转到百度").click()
    expect(page.get_by_text("百度一下", exact=True)).to_be_visible()
    page.goto("/demo/link", wait_until="networkidle")

    with page.expect_popup() as new_page:
        # with 可以定义一些操作的起止，固定用法
        # 监听下面的click操作，打开新的页面后，给这个页面定义个名字为new_page
        page.get_by_text("新页面跳转到淘宝").click()

    page_new = new_page.value
    expect(page_new.locator(".search-button")).to_be_attached()
    # 只要DOM能找到，断言就能成功


def test_pw_hover(page: Page):
    page.goto("/demo/hover", wait_until="networkidle")
    page.locator("#c4").hover()
    expect(page.get_by_text("你已经成功悬浮")).to_be_visible()
    # hover操作，容易被打断


def test_pw_dropdown(page: Page):
    page.goto("/demo/dropdown", wait_until="networkidle")
    page.get_by_text("点击选择").click()
    page.get_by_text("playwright").click()
    expect(page.get_by_text("你选择了websocket"))
    page.get_by_text("点击选择").click()
    page.get_by_text("selenium").click()
    expect(page.get_by_text("你选择了websocket"))
