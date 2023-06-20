"""
Project: 
Given a specific training goal (whether to gain muscle or lose fat), a person's weight and height, 
and a budget for one month's food, what would be the best combination of exercises and foods to 
achieve that goal and stay within the budget?
"""   
from logic.nutrition import MealHeaders, Nutrition
from logic.training import ExerciseHeaders, Training
from presentation.ascii_interface import get_user_input, show_data_exercises, show_data_meals     

def main():
    get_user_input()

     
if __name__ == "__main__":
    main()
