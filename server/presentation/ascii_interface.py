from prettytable import PrettyTable
from utils import get_user_info, clean_display, load_data

def get_user_info() -> list:
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
        
        goal_option = input("Select an option from above: ").lower()
        general_info = get_user_info()
        gender = general_info['gender']
        weight = general_info['weight']
        height = general_info['height']
        age = general_info['age']
        activity_level = general_info['activity_level']
        
        
        if goal_option not in ["l", "g"]:
            raise ValueError('Invalid option selected.')     
        else:
            clean_display()
            if goal_option == 'l':
                print("You chose: Lose weight. Let's get started!")
            else:
                print("You chose: Gain muscle. Let's get started!")
            return (goal_option, gender, weight, height, age, activity_level)    
    
def show_data_exercises(exercise_file: str) -> str:
    """Show a table with some exercises contaning the name of the exercise,
        type, level and burned calories.

    Args:
        exercise_file (str): Path name of the exercise file to open

    Returns:
        str: return the table with all the data in an organized format.
    """
    exercises = load_data(file=exercise_file)
    
    # Object to store the data in the table with a colorful representation.
    table_exercises = PrettyTable()
    table_exercises.field_names = exercises[0] # Headers
    for row_exercises in exercises[1:]:
        table_exercises.add_row(row_exercises)
    return str(table_exercises)    

def show_data_meals(meals_file: str) -> str:
    """Show a table with some meals contaning the name of the meal,
        calories per 100g, and the same grames containing for Proteins, Carbohydrates, Fats.

    Args:
        meals_file (str): Path name of the meals file to open

    Returns:
        str: return the table with all the data in an organized format.
    """
    meals = load_data(file=meals_file)
    
    # Object to store the data in the table with a colorful representation.
    table_meals = PrettyTable()
    table_meals.field_names = meals[0] # Headers
    for row_meals in meals[1:]:
        table_meals.add_row(row_meals)
    return str(table_meals)    



if __name__ == "__main__":
    print(show_data_exercises('data/exercises.csv'))