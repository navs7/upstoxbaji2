from urllib.parse import parse_qs, urlparse
import requests
from playwright.sync_api import Playwright, sync_playwright, expect
import pyotp
from config import MOBILE_NO, PIN, TOTP_KEY

api_key_file = r"C:\Users\07nav\Downloads\upstoxbaji2\api_key.txt"
api_key = open(api_key_file, "r").read().strip()
rurl = "https://account.upstox.com/developer/apps"
uri = f"https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={ api_key }&redirect_uri={rurl}"
print(uri)
code=""

def run(playwright: Playwright) -> str:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    with page.expect_request(f"*{rurl}?code*") as request:
        page.goto(uri)
        page.locator("#mobileNum").click()
        page.locator("#mobileNum").fill(MOBILE_NO)
        page.get_by_role("button", name="Get OTP").click()
        page.locator("#otpNum").click()
        otp = pyotp.TOTP(TOTP_KEY).now()
        page.locator("#otpNum").fill(otp)
        page.get_by_role("button", name="Continue").click()
        page.get_by_label("Enter 6-digit PIN").click()
        page.get_by_label("Enter 6-digit PIN").fill(PIN)
        res = page.get_by_role("button", name="Continue").click()
        page.wait_for_load_state()
    url = request.value.url
    print("Redirect Url with code{url}")
    parsed = urlparse(url)
    code = parse_qs(parsed.query)["code"][0]
    context.close()
    browser.close()
    return code


with sync_playwright() as playwright:
    code = run(playwright)

api_secret_file = r"C:\Users\07nav\Downloads\upstoxbaji2\api_secret.txt"
api_key = open(api_key_file, "r").read().strip()
api_secret = open(api_secret_file, "r").read().strip()
uri = "https://account.upstox.com/developer/apps"
url = "https://api-v2.upstox.com/login/authorization/token"
# url = "https://api.upstox.com/v2/login/authorization/token"

headers = {
    "Accept": "application/json",
    "Api-Version": "2.0",
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {
    "code": code,
    "client_id": api_key,
    "client_secret": api_secret,
    "redirect_uri": uri,
    "grant_type": "authorization_code",
}
response = requests.post(url, headers=headers, data=data)
access_token = response.json()["access_token"]
access_token_file = r"C:\Users\07nav\Downloads\upstoxbaji2\access_token.txt"
print(
    access_token, file=open(access_token_file, "w")
)  # write 'access-token' to txt file
print("token: " + access_token)