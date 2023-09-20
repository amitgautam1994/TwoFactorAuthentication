import requests
import random
import os, dotenv

dotenv.load_dotenv()


def send_otp_to_phone(mobile_no):
    # try:
    otp = random.randint(1000, 9999)
    api_key = os.environ['API_KEY_2F']
    url = 'https://2factor.in/API/V1/%s/SMS/%s/%s/' % (api_key, mobile_no, otp)
    print(url)

    response = requests.get(url)
    print(response)
    return otp

    # except Exception as e:
    #     return None

