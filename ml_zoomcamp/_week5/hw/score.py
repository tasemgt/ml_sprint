import requests

url = 'http://localhost:9696/predict'

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)
predictions = response.json()

print(predictions)

if predictions['converted']:
    print('customer is likely to convert')
else:
    print('customer is not likely to convert, send more offers')