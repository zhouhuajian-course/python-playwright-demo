import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://baike.baidu.com/")
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("python")
    page.get_by_role("textbox").press("Enter")
    # role name value
    expect(page.get_by_role("heading", name="Python")).to_be_visible()
    expect(page.locator("#lemmaDesc")).to_contain_text("计算机编程语言")
    expect(page.locator("h1")).to_contain_text("Python")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
