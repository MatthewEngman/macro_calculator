import dataclasses


def main():
    goal_weight_lbs = float(input("Enter your goal weight (in lbs): "))
    total_daily_calories = goal_weight_lbs * 12  # Total daily calories based on goal weight in lbs
    protein = goal_weight_lbs  # Protein in grams, 1g per lb of goal weight
    protein_calories = protein * 4  # Calories from protein
    calories_left = total_daily_calories - protein_calories
    fat_calories = total_daily_calories * 0.25  # 25% of total daily calories from fat
    fat = fat_calories / 9  # Fat in grams
    calories_left -= fat_calories
    carbohydrates = calories_left / 4  # Remaining calories from carbohydrates, converted to grams
    
    print(f"Total Daily Calories: {total_daily_calories:.2f} kcal")
    print(f"Protein: {protein:.2f} g")
    print(f"Fat: {fat:.2f} g")
    print(f"Carbohydrates: {carbohydrates:.2f} g")

if __name__ == "__main__":
    main()

@dataclasses
class GoalWeight:
    goal_weight_lbs: float
    
@dataclasses
class TotalDailyCalories:
    total_daily_calories: float
    def calculate_total_daily_calories(goal_weight):
        return goal_weight * 12

@dataclasses
class Protein:
    protein: float
    def calculate_protein(goal_weight):
        return goal_weight

@dataclasses
class Fat:
    fat: float
    def calculate_fat(total_daily_calories):
        fat_calories = total_daily_calories * 0.25
        return fat_calories / 9

@dataclasses
class Carbohydrates:
    carbohydrates: float
    def calculate_carbohydrates(calories_left):
        return calories_left / 4

@dataclasses
class CaloriesLeft:
    calories_left: float
    def calculate_calories_left(total_daily_calories, protein_calories):
        return total_daily_calories - protein_calories

@dataclasses
class CaloriesFromProtein:
    calories_from_protein: float
    def calculate_calories_from_protein(protein):
        return protein * 4

@dataclasses
class CaloriesFromFat:
    calories_from_fat: float
    def calculate_calories_from_fat(total_daily_calories):
        fat_calories = total_daily_calories * 0.25
        return fat_calories / 9

@dataclasses
class CaloriesFromCarbohydrates:
    calories_from_carbohydrates: float
    def calculate_calories_from_carbohydrates(calories_left):
        return calories_left / 4


