"""
Project: 
Given a specific training goal (whether to gain muscle or lose fat), a person's weight and height, 
and a budget for one month's food, what would be the best combination of exercises and foods to 
achieve that goal and stay within the budget?
"""

import csv
import os
from prettytable import PrettyTable
from dataclasses import dataclass


def get_user_input() -> list:
    preview: str = """
    ----------------------------------------------------
|                                                  |
|          Welcome to the training planner          |
|                                                  |
----------------------------------------------------
|                                                  |
|        What is your training goal?                |
|                                                  |
|             [L] Lose weight                        |
|             [G] Gain muscle                       |
|                                                  |
---------------------------------------------------- """
    while True:
        print(preview)
        
        option = input("Select an option from above: ").lower()
        weight = float(input("What is your weight in kilograms? "))
        height = int(input("What is your height in centimeters? "))
        
        if option not in ["l", "g"]:
            raise ValueError('Invalid option selected.')     
        else:
            os.system("cls")
            if option == 'l':
                print("You chose: Lose weight. Let's get started!")
            else:
                print("You chose: Gain muscle. Let's get started!")
            return [option, weight, height]    
            

@dataclass
class ExerciseHeaders:
    name: str
    type_: str
    level: str
    calories_burnt: int
    
@dataclass
class MealHeaders:
    food: str
    calories: int
    carbohydrates: int
    fats: int
    
class Calculator:
    def __init__(self, exercises_file: str, meals_file: str) -> None:
        """First off we need to bring in csv files and open them. 

        Args:
            exercises_file (str): CSV file which contains calories burnt for each exercise.
            meals_file (str): meals with its nutritional content for each one.
        """
        with open(exercises_file, 'rt', encoding='utf-8') as exercises:
            exercises_data_raw = csv.reader(exercises)
            self.exercises = list(exercises_data_raw)
            
        with open(meals_file, 'rt', encoding='utf-8') as meals:
            meals_data_raw = csv.reader(meals)
            self.meals = list(meals_data_raw) 
            
    def show_data(self) -> str:
        """We print out the exercises and meals in a pretty way and colorful.

        Returns:
            str: Table representing our data more organized for the view.
        """
        table_exercises, table_meals = PrettyTable(), PrettyTable()
        table_exercises.field_names, table_meals.field_names = self.exercises[0], self.meals[0]
        rows = list(zip(self.exercises[1:], self.meals[1:]))
        for row_exercises, row_meals in rows:
            table_exercises.add_row(row_exercises)
            table_meals.add_row(row_meals)
        return str(table_meals), str(table_exercises) # table_meals = Meals, table_exercises = Exercises
             
    
    def is_food(self):
        meal1 = MealHeaders(food=self.meals[0])
    
        

def main():
    lose_weight = Calculator(exercises_file="exercises.csv", meals_file='meals.csv')
    get_user_input()
    print(lose_weight.show_data()[0], '\n')
    print(lose_weight.show_data()[1])
    
if __name__ == "__main__":
    main()
