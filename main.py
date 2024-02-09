from playwright.sync_api import sync_playwright, Playwright
import time

def run(playwright:Playwright):
    title_list = []
    context = playwright.request.new_context()
    response = context.get("http://127.0.0.1:8000/store/products/",headers={'Accept': 'application/json'})
    res = response.json()
    for re in res:
        title_list.append(re['title'])
    print(f'we have {len(title_list)} data')
    # print(title_list)

def main(playwright: Playwright):
    chrome = playwright.chromium
    print('launchinh a browser')
    browser = chrome.launch(headless=False)
    print('launching a new page')
    page = browser.new_page()
    print('visiting a new url')
    page.goto('https://www.google.com/webhp')
    word = 'Hello world'
    page.get_by_title('Search').fill(word)
    page.keyboard.press('Enter')
    # page.locator('div').get_by_text('Images').click()
    page.get_by_role('link', name="Images", exact=True).click()
    time.sleep(5)
    new = word.split( )
    print(new[0])
    page.get_by_role('button', name=new[0]).first.click()
    time.sleep(10)
    print('text successfully sed')
    browser.close()
    print('browser closed successfully')

with sync_playwright() as playwright:
    main(playwright)