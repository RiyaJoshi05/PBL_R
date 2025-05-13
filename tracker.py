from nutrition_api import get_nutrition_data
import csv
from datetime import datetime

def log_food(food_data):
    with open('storage.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            food_data['food_name'],
            food_data['nf_calories'],
            food_data['nf_protein'],
            food_data['nf_total_carbohydrate'],
            food_data['nf_total_fat']
        ])

def daily_summary():
    total_calories = 0
    today = datetime.now().strftime('%Y-%m-%d')

    try:
        with open('storage.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                timestamp = row[0]
                if timestamp.startswith(today):
                    total_calories += float(row[2])
        print(f"Total Calories Today: {total_calories} kcal\n")
    except FileNotFoundError:
        print("No data logged yet.\n")

def main():
    print("Welcome to Nutrition Tracker!")
    while True:
        food = input("Enter food (or 'exit'/'summary'): ").strip()
        if food.lower() == 'exit':
            break
        elif food.lower() == 'summary':
            daily_summary()
            continue

        data = get_nutrition_data(food)
        if data:
            print(f"\n{data['food_name'].title()} - {data['nf_calories']} kcal")
            print(f"Protein: {data['nf_protein']}g, Carbs: {data['nf_total_carbohydrate']}g, Fat: {data['nf_total_fat']}g\n")
            log_food(data)
        else:
            print("Could not retrieve data. Try again.")

if __name__ == "__main__":
    main()