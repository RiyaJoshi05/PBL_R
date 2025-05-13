import requests
APP_ID = 'cc73aa80'  
API_KEY = 'df84ac079f13b8042f0e6a0cdaada361'  

def get_nutrition_data(food_item):
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
        'Content-Type': 'application/json',
    }
    body = {
        'query': food_item
    }

    response = requests.post(url, json=body, headers=headers)
    data = response.json()
    if 'foods' in data:
        return data['foods'][0]  # return first result
    else:
        return None