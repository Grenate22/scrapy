from playwright.sync_api import sync_playwright, Playwright

def run(playwright:Playwright):
    title_list = []
    context = playwright.request.new_context()
    response = context.get("http://127.0.0.1:8000/store/products/",headers={'Accept': 'application/json'})
    res = response.json()
    for re in res:
        title_list.append(re['title'])
    print(f'we have {len(title_list)} data')
    # print(title_list)

with sync_playwright() as playwright:
    run(playwright)