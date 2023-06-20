import os, csv

def clean_display():
    os.system('cls')
    
def load_data(file: str) -> list:
    with open(file, newline='') as f:
        data = csv.reader(f)
        return list(data)

def get_user_info() -> dict:
    gender = input('Gender (male/female): ')
    weight = float(input('Weight (in kg): '))
    height = float(input('Height (in cm): '))
    age = int(input('Age: '))
    activity_level = int(input('Activity level (1-5): '))
    return {
        'gender': gender,
        'weight': weight,
        'height': height,
        'age': age,
        'activity_level': activity_level,
    }
    