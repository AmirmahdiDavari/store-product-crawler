import csv
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

# Set up the Firefox WebDriver
# service = Service(GeckoDriverManager().install())
options = Options()

options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
# صبر کردن برای مشاهده نتایج
time.sleep(5)


def scroll_to_bottom():
    """Scroll to the bottom of the page incrementally."""
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new content to load
        time.sleep(4)  # Adjust as necessary

        # Calculate new scroll height and compare with last height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Exit the loop if no new content is loaded
        last_height = new_height


def get_top_brand_list():
    result = []
    # # Open the target URL
    # driver.get("https://www.digistyle.com/pages/brand/")
    #
    # # Wait for the page to load
    # time.sleep(5)  # You can adjust the sleep time as needed
    #
    # # Find the elements containing the brand names
    # top_brands_div = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[4]/div[2]/div[2]")
    #
    # # Click the div element
    # top_brands_div.click()
    # # Find all <a> tags with the specified class
    # brand_links = driver.find_elements(By.CSS_SELECTOR, ".c-brands-letters__brand-link.js-filter-tag-superior")
    #
    # # Extract the href attributes and append to a list
    # href_list = [link.get_attribute('href') for link in brand_links]
    #
    # # Print the extracted hrefs
    # print("Brand Links:")
    # for href in href_list:
    #     print(href)
    # print(len(href_list))
    result = [
        # "https://www.digistyle.com/adamak-brand/",
        #       "https://www.digistyle.com/ador-brand/",
        #       "https://www.digistyle.com/rns-brand/",
        #       "https://www.digistyle.com/arian-nakh-baf-brand/",
              "https://www.digistyle.com/analia-brand/",
              "https://www.digistyle.com/styx-brand/",
              "https://www.digistyle.com/aspest-brand/",
              "https://www.digistyle.com/sclaree-brand/",
              "https://www.digistyle.com/afratin-brand/",
              "https://www.digistyle.com/elswan-brand/",
              "https://www.digistyle.com/elsana-brand/",
              "https://www.digistyle.com/encino-brand/",
              "https://www.digistyle.com/active-brand/",
              "https://www.digistyle.com/easydo-brand/",
              "https://www.digistyle.com/inlay-brand/",
              "https://www.digistyle.com/baynet-brand/",
              "https://www.digistyle.com/borhan-tan-posh-brand/",
              "https://www.digistyle.com/biol-brand/",
              "https://www.digistyle.com/pa-ara-brand/",
              "https://www.digistyle.com/patan-jameh-brand/",
              "https://www.digistyle.com/paloote-brand/",
              "https://www.digistyle.com/paniz-fa-brand/",
              "https://www.digistyle.com/panil-brand/",
              "https://www.digistyle.com/papa-brand/",
              "https://www.digistyle.com/paytakht-fa-brand/",
              "https://www.digistyle.com/prime-brand/",
              "https://www.digistyle.com/top-shop-brand/",
              "https://www.digistyle.com/tan-posh-henghameh-brand/",
              "https://www.digistyle.com/twin-brand/",
              "https://www.digistyle.com/teeteesh-brand/",
              "https://www.digistyle.com/dorsa-brand/",
              "https://www.digistyle.com/atarod-leather-brand/",
              "https://www.digistyle.com/mashad-leather-brand/",
              "https://www.digistyle.com/chindka-brand/",
              "https://www.digistyle.com/dermalift-brand/",
              "https://www.digistyle.com/digistyle-essentials-brand/",
              "https://www.digistyle.com/ranj-brand/",
              "https://www.digistyle.com/renuzit-brand/",
              "https://www.digistyle.com/zantos-brand/",
              "https://www.digistyle.com/zi-brand/",
              "https://www.digistyle.com/sarzi-brand/",
              "https://www.digistyle.com/sarook-brand/",
              "https://www.digistyle.com/serge-brand/",
              "https://www.digistyle.com/sevda-brand/",
              "https://www.digistyle.com/seven-poon-brand/",
              "https://www.digistyle.com/sepidpoosh-brand/",
              "https://www.digistyle.com/cinere-brand/",
              "https://www.digistyle.com/shahpar-brand/",
              "https://www.digistyle.com/schon-brand/",
              "https://www.digistyle.com/fulica-brand/",
              "https://www.digistyle.com/fiorella-brand/",
              "https://www.digistyle.com/callista-brand/",
              "https://www.digistyle.com/corum-brand/",
              "https://www.digistyle.com/kromaki-b-brand/",
              "https://www.digistyle.com/saeedi-shoe-brand/",
              "https://www.digistyle.com/gordye-brand/",
              "https://www.digistyle.com/lafarrerr-brand/",
              "https://www.digistyle.com/lord-archer-brand/",
              "https://www.digistyle.com/lupilu-brand/",
              "https://www.digistyle.com/madar-brand/",
              "https://www.digistyle.com/maral-brand/",
              "https://www.digistyle.com/masarm-brand/",
              "https://www.digistyle.com/maldini-brand/",
              "https://www.digistyle.com/my-brand/",
              "https://www.digistyle.com/maya-maahak-brand/",
              "https://www.digistyle.com/myilda-brand/",
              "https://www.digistyle.com/miscellaneous-brand/",
              "https://www.digistyle.com/moringa-emo-brand/",
              "https://www.digistyle.com/narbon-brand/",
              "https://www.digistyle.com/nizel-brand/",
              "https://www.digistyle.com/nil-kouk-brand/",
              "https://www.digistyle.com/nikta-brand/",
              "https://www.digistyle.com/hydroderm-brand/",
              "https://www.digistyle.com/sw-1991-brand/",
              "https://www.digistyle.com/casio-brand/",
              "https://www.digistyle.com/comeon-brand/",
              "https://www.digistyle.com/collezione-brand/",
              "https://www.digistyle.com/defacto-brand/",
              "https://www.digistyle.com/ellaro-brand/",
              "https://www.digistyle.com/esmara-brand/",
              "https://www.digistyle.com/indigo-brand/",
              "https://www.digistyle.com/koza-brand/",
              "https://www.digistyle.com/mango-brand/",
              "https://www.digistyle.com/nbb-brand/",
              "https://www.digistyle.com/naviforce-brand/",
              "https://www.digistyle.com/oral-b-brand/",
              "https://www.digistyle.com/pepperts-brand/",
              "https://www.digistyle.com/prestige-brand/",
              "https://www.digistyle.com/ray-ban-brand/",
              "https://www.digistyle.com/skmei-brand/",
              "https://www.digistyle.com/valancy-brand/",
              "https://www.digistyle.com/woody-sence-brand/"]
    return result


def get_product_brands(brand_url):
    product_ids = []
    driver.get(f"{brand_url}?pageno=1&sortby=7")
    scroll_to_bottom()
    product_divs = driver.find_elements(By.CSS_SELECTOR, ".cp-card.cp-card--product-card.js-cro-product")
    product_ids = [div.get_attribute('data-product-id') for div in product_divs]

    return product_ids


def get_product_detail(product_id):
    pass


def get_comment_detail(html_content, product_id):
    soup = BeautifulSoup(html_content, "html.parser")

    comments_detail = []
    comments = []
    for comment in soup.find_all("div", class_="c-product-page__comment"):
        rating = comment.find("div", class_="c-product-page__comment-rate").text.strip()
        title_tag = comment.find("div", class_="c-product-page__comment-title")
        title = title_tag.text.strip() if title_tag else "بدون عنوان"

        author_name = comment.find("span", class_="c-product-page__comment-author-name").text.strip()
        date = comment.find("span", class_="c-product-page__comment-date").text.strip()
        buyer_status = "خریدار" if comment.find("span", class_="c-product-page__comment-customer") else "غیر خریدار"

        comment_text = comment.find("p", class_="c-product-page__comment-text").text.strip()

        recommendation_tag = comment.find("div", class_="c-product-page__comment-recom")
        recommendation = recommendation_tag.text.strip() if recommendation_tag else "نامشخص"

        seller_tag = comment.find("div", class_="c-product-page__comment-seller")
        seller = seller_tag.find("a").text.strip() if seller_tag else "نامشخص"

        size_tag = comment.find("div", class_="c-product-page__comment-variant")
        size = size_tag.find("span",
                             class_="c-product-page__comment-variant-value").text.strip() if size_tag else "نامشخص"

        comments.append([
            product_id,  # شناسه محصول
            rating,  # امتیاز
            title,  # عنوان کامنت
            author_name,  # نام کاربر
            date,  # تاریخ ثبت نظر
            buyer_status,  # وضعیت خریدار
            comment_text,  # متن کامنت
            recommendation,  # پیشنهاد خرید
            seller,  # فروشنده
            size  # سایز محصول
        ])

        comments_detail.append({
            "product_id": product_id,
            "rating": rating,
            "title": title,
            "author": author_name,
            "date": date,
            "buyer_status": buyer_status,
            "comment_text": comment_text,
            "recommendation": recommendation,
            "seller": seller,
            "size": size
        })

    # نام فایل CSV
    csv_file = "commentsDigistyle1.csv"

    # بررسی اینکه آیا فایل وجود دارد یا نه، برای جلوگیری از تکرار هدرها
    file_exists = os.path.isfile(csv_file)

    # ذخیره داده‌ها در CSV (افزودن داده‌های جدید بدون حذف داده‌های قبلی)
    with open(csv_file, mode="a", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)

        # اگر فایل تازه ساخته شده، عنوان ستون‌ها را اضافه کنیم
        if not file_exists:
            writer.writerow(
                ["شناسه محصول", "امتیاز", "عنوان", "نام کاربر", "تاریخ", "وضعیت خریدار", "متن کامنت", "پیشنهاد خرید",
                 "فروشنده", "سایز محصول"])

        # نوشتن اطلاعات کامنت‌ها در فایل
        writer.writerows(comments)

    print(f"✅ داده‌های جدید با موفقیت به '{csv_file}' اضافه شدند.")
    for comment in comments:
        print(comment)


def get_product_comments(product_id):
    last_comments = ''
    for page in range(1, 1000):
        # Define the base URL
        url = f"https://www.digistyle.com/ajax/product/comments/list/{product_id}/"

        # Prepare the parameters
        params = {"page": page}
        params["mode"] = None

        # Send the GET request
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            # Process the response
            if page > 1:
                # Append response to existing comments (you would handle this in your UI)
                print("Appending comments...")
            else:
                # Load new comments (you would handle this in your UI)
                print("Loading comments...")

            if last_comments == response.text:
                break
            last_comments = response.text
            get_comment_detail(response.text, product_id)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        time.sleep(10)


brands = get_top_brand_list()
for brand_url in brands:
    product_ids = get_product_brands(brand_url)
    for product_id in product_ids:
        while True:
            try:
                driver.get(f"https://www.digistyle.com/product/{product_id}")
                get_product_detail(product_id)
                get_product_comments(product_id)
                break
            except Exception as e:
                print(f"Exception in get_product_detail {e}")
