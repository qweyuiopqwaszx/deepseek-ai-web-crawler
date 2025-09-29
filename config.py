# config.py

BASE_URL = "https://www.etsy.com/search?q=nail&ref=pagination"
CSS_SELECTOR = "[class^='v2-listing-card__info']"
REQUIRED_KEYS = [
    "name",
    "merchantname",
    "discountedprice",
    "originalprice",
    "rating",
    "numberofreviews",
    "freeshipping",
    "description",
]
