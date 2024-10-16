import pandas as pd
import numpy as np
import random

# Constants
num_records = 100000
age_range = (18, 65)

# Height and weight ranges
height_range_male = (145, 190)  # Height in cm for males
height_range_female = (135, 180)  # Height in cm for females
weight_range_male = (50, 120)  # Weight in kg for males
weight_range_female = (45, 120)  # Weight in kg for females

# Diseases and their calorie intake ranges (in calories)
disease_calories = {
    "PCOD": (1300, 1900),
    "Heart Attack": (1200, 1800),
    "Kidney Stone": (1500, 2000),
    "Diabetes": (1400, 1900),
    "Healthy": (1600, 2500)
}

# Gender options
genders = ["Male", "Female"]
diseases = list(disease_calories.keys())

data = []

for _ in range(num_records):
    # Randomly generate gender, age, height, weight
    gender = random.choice(genders)
    age = random.randint(age_range[0], age_range[1])
    
    if gender == "Male":
        height = random.randint(height_range_male[0], height_range_male[1])
        weight = random.randint(weight_range_male[0], weight_range_male[1])
    else:
        height = random.randint(height_range_female[0], height_range_female[1])
        weight = random.randint(weight_range_female[0], weight_range_female[1])
    
    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)
    
    # Randomly choose a disease (no PCOD for males)
    if gender == "Male":
        disease = random.choice([d for d in diseases if d != "PCOD"])
    else:
        disease = random.choice(diseases)
    
    # Get calorie range for the disease
    calorie_min, calorie_max = disease_calories[disease]

    # Generate random calories within the disease range
    calories = random.randint(calorie_min, calorie_max)

    # Assign status based on calorie intake
    if 1300 <= calories <= 1600:
        status = "Low"
    elif 1601 <= calories <= 1900:
        status = "Medium"
    elif 1901 <= calories <= 2100:
        status = "High"
    else:
        status = "Above High"

    # Append the record
    data.append({
        "Gender": gender,
        "Age": age,
        "Height (cm)": height,
        "Weight (kg)": weight,
        "BMI": round(bmi, 2),
        "Disease": disease,
        "Calories": calories,
        "Status": status
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("health_data.csv", index=False)
