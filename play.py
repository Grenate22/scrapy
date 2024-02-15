from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/index.html")
    page.get_by_label("Search", exact=True).click()
    page.get_by_label("Search", exact=True).fill("bread")
    page.keyboard.press('Enter')
    page.get_by_role("link", name="Images", exact=True).click()
    page.get_by_role('button', name='bread').nth(0).click()
    time.sleep(5)
    page.get_by_role("button", name="Close").click()
    time.sleep(5)
    page.get_by_role('button', name='bread').nth(1).click()
    time.sleep(5)
    page.get_by_role("button", name="Close").click()
    time.sleep(5)
    page.get_by_role('button', name='bread').nth(2).click()
    time.sleep(5)
    page.get_by_role("button", name="Close").click()
    time.sleep(5)
    page.get_by_role('button', name='bread').nth(3).click()
    # if images:
    #     alt_text = images.get_attribute("alt")
    #     print(alt_text)
    # else:
    #     print("no text")
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
