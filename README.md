# Nutrition Tracker

A simple Python-based command-line Nutrition Tracker that allows users to:

- Enter food items and get nutritional information.
- Log meals to a local CSV file.
- View a daily calorie summary.

## Features

- Uses Nutritionix API to fetch nutrition data.
- Logs data with timestamp to `storage.csv`.
- Provides daily calorie summary.

## Setup

1. Clone the repository or download the files.
2. Get an App ID and API Key from [Nutritionix](https://developer.nutritionix.com/).
3. Replace `your_app_id` and `your_api_key` in `nutrition_api.py`.
4. Install the required packages:
   ```
   pip install requests
   ```
5. Run the tracker:
   ```
   python tracker.py
   ```

## Example

```
Welcome to Nutrition Tracker!
Enter food (or 'exit'/'summary'): banana

Banana - 105 kcal
Protein: 1.3g, Carbs: 27g, Fat: 0.4g
```

## Notes

- Data is stored in `storage.csv`.
- Use `summary` command to view total calories consumed today.