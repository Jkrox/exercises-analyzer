from dataclasses import dataclass
import csv

@dataclass
class MealHeaders:
    food: str
    calories: int
    carbohydrates: int
    fats: int
    

class Nutrition:
    def __init__(self, nutrition_file: str) -> None:
        with open(nutrition_file, 'rt', encoding='utf-8') as nutrition:
            nutrition_data_raw = csv.reader(nutrition)
            self.nutrition = list(nutrition_data_raw)
    
    def imc(self):
        pass