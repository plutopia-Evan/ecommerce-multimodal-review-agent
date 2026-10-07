import os
import sys

import requests
from dotenv import load_dotenv


load_dotenv()

API_BASE_URL = os.getenv("DIFY_API_BASE_URL", "https://api.dify.ai/v1").rstrip("/")
API_KEY = os.getenv("DIFY_API_KEY")

if not API_KEY:
    sys.exit("请先在 .env 中设置 DIFY_API_KEY。")

payload = {
    "inputs": {
        "review_id": "review_demo_001",
        "product_id": "product_001",
        "review_text": (
            "保温杯已经连续使用一周，杯盖旋紧后放在背包里没有漏水，"
            "早上装入热水，到下午仍然保持温热，容量适合日常通勤。"
        ),
        "product_title": "316不锈钢保温杯便携大容量男女通用商务水杯",
        "product_description": (
            "采用316不锈钢内胆，配备旋拧式密封杯盖，"
            "具有保温、便携和防漏功能。"
        ),
        "review_images": [],
    },
    "response_mode": "blocking",
    "user": "github-demo-user",
}

response = requests.post(
    f"{API_BASE_URL}/workflows/run",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json=payload,
    timeout=120,
)
response.raise_for_status()
print(response.json())
