import requests

url = "https://virtual-tds-ta.vercel.app/query"
data = {
    "question": "What is the purpose of the TDS Virtual TA?",
    "image": None
}

response = requests.post(url, json=data)
print(response.json())
