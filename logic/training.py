from dataclasses import dataclass
import csv

@dataclass
class ExerciseHeaders:
    name: str
    type: str
    level: str
    calories_burnt: int
    

class Training:
    def __init__(self, exercises_file: str) -> None:
        with open(exercises_file, 'rt', encoding='utf-8') as exercises:
            exercises_data_raw = csv.reader(exercises)
            self.exercises = list(exercises_data_raw)
            
    def recommend_exercises(self, weight, height, objective):
        pass