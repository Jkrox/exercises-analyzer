"""
Proyecto: 
Dada una meta de entrenamiento específica (ya sea aumentar músculo o perder grasa), el peso y altura de una persona,
y un presupuesto para la alimentación de un mes, ¿cuál sería la mejor combinación de ejercicios y alimentos para
lograr esa meta y ajustarse al presupuesto?
"""

import csv, os
from prettytable import PrettyTable
from dataclasses import dataclass

def user_input() -> list:
    preview: str = """
    ----------------------------------------------------
|                                                  |
|      Bienvenido al planificador de entrenamiento  |
|                                                  |
----------------------------------------------------
|                                                  |
|        ¿Cuál es tu objetivo de entrenamiento?     |
|                                                  |
|             [P] Perder peso                        |
|             [S] Subir masa muscular               |
|                                                  |
----------------------------------------------------
    """
    while True:
        print(preview)
        
        option = input("Seleccionar la opción que aparece en pantalla: ").lower()
        weight = float(input("Cuál es su peso en kilogramos: "))
        height = int(input("Cuál es su altura en centimetros: "))
        
        if option != "p" and option != 's':
            raise ValueError('Opción no válida')     
        elif option == 'p' or option == 's':
            os.system("cls")
            if option == 'p':
                print("Elegiste: Perder peso. Bien, comencemos!")
                
            else:
                print("Elegiste: Subir masa muscular. Bien, comencemos!")
                
            return [option, weight, height]    
            
@dataclass
class ExercisesHeaders:
    name: str
    tipo: str
    nivel: str
    calorias_quemadas: int
    
@dataclass
class MealsHeaders:
    alimento: str
    calorias: int
    carbohidratos: int
    grasas: int
    
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
            print(self.meals) 
            
    def show_data(self) -> str:
        """We print out the exercises and meals in a pretty way and colorful.

        Returns:
            str: Table representing our data more organised for the view.
        """
        table, table2 = PrettyTable(), PrettyTable()
        table.field_names, table2.field_names = self.exercises[0], self.meals[0]
        rows = list(zip(self.exercises[1:], self.meals[1:]))
        for row, row2 in rows:
            table.add_row(row)
            table2.add_row(row2)
        return str(table), str(table2) # table = Exercises, table2 = Meals
             
    
    def is_food(self):
        meal1 = MealsHeaders(alimento=self.meals[0])
    
        

def main():
    perder_grasa = Calculator(exercises_file="exercises.csv", meals_file='meals.csv')
    user_input()
    print(perder_grasa.show_data()[1], '\n')
    print(perder_grasa.show_data()[0])
    
if __name__ == "__main__":
    main()