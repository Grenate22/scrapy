from playwright.async_api import Playwright, expect,async_playwright
import asyncio
import requests
import io
import time
from PIL import Image


async   def run(playwright: Playwright) -> None:
    browser =await playwright.chromium.launch(headless=False)
    context =await browser.new_context()
    page =await context.new_page()
    await page.goto("https://www.google.com/index.html")
    await page.get_by_label("Search", exact=True).click()
    await page.get_by_label("Search", exact=True).fill("bread")
    await page.keyboard.press('Enter')
    await page.get_by_role("link", name="Images", exact=True).click()
   
    await page.get_by_role('button', name='bread').nth(0).click()
    img_element =await page.wait_for_selector("#Sva75c > div.A8mJGd.NDuZHe.CMiV2d.OGftbe-N7Eqid-H9tDt > div.dFMRD > div.AQyBn > div.tvh9oe.BIB1wf.hVa2Fd > c-wiz > div > div > div > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.pT0Scc.iPVvYb")
    if img_element:
        src_va =await img_element.get_attribute("src")
        print(src_va)
        response = requests.get(src_va,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
        image_buffer = io.BytesIO(response.content)
        with open("newImg.jpg", "wb") as f:
            f.write(image_buffer.getvalue())
        
    await page.get_by_role("button", name="Close").click()

    await page.get_by_role('button', name='bread').nth(1).click()
    img_element =await page.wait_for_selector("#Sva75c > div.A8mJGd.NDuZHe.CMiV2d.OGftbe-N7Eqid-H9tDt > div.dFMRD > div.AQyBn > div.tvh9oe.BIB1wf.hVa2Fd > c-wiz > div > div > div > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.pT0Scc.iPVvYb")
    if img_element:
        src_va =await img_element.get_attribute("src")
        print(src_va)
        response = requests.get(src_va,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
        print(response)
        image = Image.open(io.BytesIO(response.content))
        image.show()
   
    await page.get_by_role("button", name="Close").click()

    await page.get_by_role('button', name='bread').nth(2).click()
    img_element =await page.wait_for_selector("#Sva75c > div.A8mJGd.NDuZHe.CMiV2d.OGftbe-N7Eqid-H9tDt > div.dFMRD > div.AQyBn > div.tvh9oe.BIB1wf.hVa2Fd > c-wiz > div > div > div > div > div.v6bUne > div.p7sI2.PUxBg > a > img.sFlh5c.pT0Scc.iPVvYb")
    if img_element:
        src_va =await img_element.get_attribute("src")
        print(src_va)
        response = requests.get(src_va,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
        print(response)
        image = Image.open(io.BytesIO(response.content))
        image.show()
   
    await page.get_by_role("button", name="Close").click()
  
    # await page.get_by_role('button', name='bread').nth(3).click()
    # current_url = page.url
    # print(current_url)
    # if images:
    #     alt_text = images.get_attribute("alt")
    #     print(alt_text)
    # else:
    #     print("no text")
    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())