from playwright.sync_api import Page, expect

def test_baidu(page: Page):
    # test_baidu(page: Page):
    # 这里指定一下page是一个Page类，这样用page.  才能.出来方法
    page.goto(url="https://www.baidu.com")
    # page.wait_for_timeout(5_000)
    # 相当于sleep但有所不同，单位ms
    # sleep会阻碍一些异步、协程的执行
    page.locator("//input[@name='wd']").fill("playwright")
    # page.locator("//input[@type='submit']").click()
    # page.get_by_text("百度一下").count()   --- 看一下梳理
    page.get_by_text("百度一下").click()
    expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()
    # 该断言时间默认为5s




