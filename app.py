from flask import Flask, render_template, request
import requests

app = Flask(__name__)

APP_ID = 'cc73aa80'  
API_KEY = 'df84ac079f13b8042f0e6a0cdaada361'  

def suggest_recipe(nutrient):
    """
    Suggests recipes based on the given macronutrient.

    Args:
        nutrient (str): The type of nutrient ("protein", "fat", "carbohydrate").

    Returns:
        list: A list of recipe suggestions with names and YouTube links.
    """
    suggestions = {
        "protein": [
            {"name": "Grilled Chicken Salad", "link": "https://www.youtube.com/watch?v=QUY_IUq5BzU"},
            {"name": "Greek Yogurt Parfait", "link": "https://www.youtube.com/watch?v=wu5mlLHVzXQ"},
            {"name": "Lentil Soup", "link": "https://www.youtube.com/watch?v=hfL7CPhku2I"}
        ],
        "fat": [
            {"name": "Avocado Toast", "link": "https://www.youtube.com/watch?v=0R5km8AQGlI"},
            {"name": "Nuts Mix", "link": "https://www.youtube.com/watch?v=xcz2LIvpMwI"},
            {"name": "Salmon Fillet", "link": "https://www.youtube.com/watch?v=mxa-4hN1-qM"}
        ],
        "carbohydrate": [
            {"name": "Brown Rice Bowl", "link": "https://www.youtube.com/watch?v=T5Rbf-4XEBE"},
            {"name": "Whole Wheat Pasta", "link": "https://www.youtube.com/watch?v=ZyJgGr70Gj8"},
            {"name": "Fruit Smoothie", "link": "https://www.youtube.com/watch?v=2CzMagqdjko"}
        ]
    }
    return suggestions.get(nutrient.lower(), [])


def get_nutrition_data(food_item):
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
        'Content-Type': 'application/json',
    }
    body = { 'query': food_item }

    response = requests.post(url, json=body, headers=headers)
    data = response.json()
    if 'foods' in data:
        return data['foods'][0]
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    nutrition_data = None
    recommendations = []
    if request.method == "POST":
        food = request.form.get("food")
        data = get_nutrition_data(food)
        if data:
            nutrition_data = {
                "name": data["food_name"].title(),
                "calories": data["nf_calories"],
                "protein": data["nf_protein"],
                "carbs": data["nf_total_carbohydrate"],
                "fat": data["nf_total_fat"]
            }
            if data["nf_protein"] < 5:
                recommendations.extend(suggest_recipe("protein"))
            if data["nf_total_fat"] < 3:
                recommendations.extend(suggest_recipe("fat"))
            if data["nf_total_carbohydrate"] < 10:
                recommendations.extend(suggest_recipe("carbohydrate"))

    return render_template("index.html", nutrition=nutrition_data, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
