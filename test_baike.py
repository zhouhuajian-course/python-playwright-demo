import re

import pytest
from playwright.sync_api import Page, expect


# fixture
def test_example(page: Page) -> None:
    page.goto("https://baike.baidu.com/")
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("python")
    page.get_by_role("textbox").press("Enter")
    expect(page.get_by_role("heading", name="Python")).to_be_visible()
    expect(page.locator("#lemmaDesc")).to_contain_text("计算机编程语言")
    expect(page.locator("h1")).to_contain_text("Python")
    page.get_by_role("heading", name="Python").click(button="right")


