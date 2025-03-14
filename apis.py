import time

import requests


def get_all_brands():
    result = []
    retry = 0
    while retry <= 4:
        try:
            for page_number in range(1, 300):
                url = f"https://www.khanoumi.com/api/ntl/v1/catalog/brands?page_size=300&page_number={page_number}"

                payload = {}
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
                    'baggage': 'sentry-environment=production,sentry-release=toad%404.80.6,sentry-public_key=e595bcb6ea5861276e2684c5af938d07,sentry-trace_id=218afc1f948e4181a2424ede625136fb,sentry-sample_rate=0.0001,sentry-sampled=false',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/json; charset=utf-8',
                    'priority': 'u=1, i',
                    'referer': 'https://www.khanoumi.com/products/121-pomegranate-hair-care-mask-750ml-33903',
                    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'sentry-trace': '218afc1f948e4181a2424ede625136fb-b57ccd88a923bd16-0',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
                    'Cookie': 'user_i=true; x-maria-ust=467a6aa3-27d9-47b8-85a2-fdb8387ab1ad'
                }

                response = requests.request("GET", url, headers=headers, data=payload)

                print(response.text)

                if response.json()['isSuccess']:
                    if not response.json()["data"]["items"]:
                        return result
                    for brand in response.json()["data"]["items"]:
                        result.append(brand)
                time.sleep(10)
        except Exception as e:
            retry += 1
            print(f" Exception  in  get   all brand {e}")
            time.sleep(15)
    return result


def get_all_product_brand(brand_id):
    result = []
    retry = 0
    while retry <= 4:
        try:
            for page_number in range(1, 10000000):
                url = f"https://www.khanoumi.com/api/ntl/v1/products?brand_id={brand_id}&page_number={page_number}&page_size=240"

                payload = {}
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
                    'baggage': 'sentry-environment=production,sentry-release=toad%404.80.6,sentry-public_key=e595bcb6ea5861276e2684c5af938d07,sentry-trace_id=3830dd215de24a189ef7fa67db94b7fd,sentry-sample_rate=0.0001,sentry-sampled=false',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/json; charset=utf-8',
                    'priority': 'u=1, i',
                    'referer': 'https://www.khanoumi.com/products/lafarrerr-anti-spot-spf50-sunscreen-cream-for-oily-and-acne-prone-skin-25318',
                    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'sentry-trace': '3830dd215de24a189ef7fa67db94b7fd-b5488d0a55ac03d4-0',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
                    'Cookie': 'user_i=true; x-maria-ust=467a6aa3-27d9-47b8-85a2-fdb8387ab1ad'
                }
                response = requests.request("GET", url, headers=headers, data=payload)
                print(response.text)
                if not response.json()["data"]["products"]["items"]:
                    return result
                if response.json()['isSuccess']:
                    for brand in response.json()["data"]["products"]["items"]:
                        result.append(brand)
                time.sleep(10)
        except Exception as e:
            retry += 1
            print(f" Exception  in  get   all brand {e}")
            time.sleep(15)
    return result


def get_product_comment(product_id):
    result = []
    retry = 0
    while retry <= 4:
        try:
            for page_number in range(1, 10000000):
                url = f"https://www.khanoumi.com/api/cml/v1/products/id/{product_id}/comments?page_number={page_number}&page_size=4"

                payload = {}
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
                    'baggage': 'sentry-environment=production,sentry-release=toad%404.80.6,sentry-public_key=e595bcb6ea5861276e2684c5af938d07,sentry-trace_id=3830dd215de24a189ef7fa67db94b7fd,sentry-sample_rate=0.0001,sentry-sampled=false',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/json; charset=utf-8',
                    'priority': 'u=1, i',
                    'referer': 'https://www.khanoumi.com/products/lafarrerr-anti-spot-spf50-sunscreen-cream-for-oily-and-acne-prone-skin-25318',
                    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'sentry-trace': '3830dd215de24a189ef7fa67db94b7fd-b5488d0a55ac03d4-0',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
                    'Cookie': 'user_i=true; x-maria-ust=467a6aa3-27d9-47b8-85a2-fdb8387ab1ad'
                }
                response = requests.request("GET", url, headers=headers, data=payload)
                print(response.text)
                if not response.json()["data"]["items"]:
                    return result
                if response.json()['isSuccess']:
                    for brand in response.json()["data"]["items"]:
                        result.append(brand)
                time.sleep(10)
        except Exception as e:
            retry += 1
            print(f" Exception  in  get   all brand {e}")
            time.sleep(15)
    return result
