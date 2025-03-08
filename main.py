0

#Copiot generated code based off simple prompt explaining the calculation of macronutrients based on goal weight
# def main():
#     goal_weight_lbs = float(input("Enter your goal weight (in lbs): "))
#     total_daily_calories = goal_weight_lbs * 12  # Total daily calories based on goal weight in lbs
#     protein = goal_weight_lbs  # Protein in grams, 1g per lb of goal weight
#     protein_calories = protein * 4  # Calories from protein
#     calories_left = total_daily_calories - protein_calories
#     fat_calories = total_daily_calories * 0.25  # 25% of total daily calories from fat
#     fat = fat_calories / 9  # Fat in grams
#     calories_left -= fat_calories
#     carbohydrates = calories_left / 4  # Remaining calories from carbohydrates, converted to grams
    
#     print(f"Total Daily Calories: {total_daily_calories:.2f} kcal")
#     print(f"Protein: {protein:.2f} g")
#     print(f"Fat: {fat:.2f} g")
#     print(f"Carbohydrates: {carbohydrates:.2f} g")

#Refactored code with Gemini replacing multiple functions with a single function that returns a dataclass object
import dataclasses

@dataclasses.dataclass
class Macronutrients:
    """Represents the macronutrient breakdown (protein, fat, carbs) in grams."""
    protein: float
    fat: float
    carbohydrates: float

    def __post_init__(self):
        """Validate that all macronutrient values are non-negative."""
        if self.protein < 0:
            raise ValueError("Protein must be non-negative.")
        if self.fat < 0:
            raise ValueError("Fat must be non-negative.")
        if self.carbohydrates < 0:
            raise ValueError("Carbohydrates must be non-negative.")

def calculate_macronutrients(goal_weight_lbs: float, calorie_multiplier: float = 12, protein_multiplier: float = 1, fat_percentage: float = 0.25) -> Macronutrients:
    """Calculates macronutrients (protein, fat, carbs) based on goal weight.

    Args:
        goal_weight_lbs: The target weight in pounds.
        calorie_multiplier:  Multiplier to calculate total daily calories.
        protein_multiplier: Multiplier to calculate daily protein intake.
        fat_percentage: Percentage of total calories from fat.

    Returns:
        A Macronutrients object containing the calculated protein, fat, and
        carbohydrate amounts in grams.

    Raises:
        ValueError: If goal_weight_lbs is not positive.
    """
    if goal_weight_lbs <= 0:
        raise ValueError("Goal weight must be greater than 0")

    total_daily_calories = goal_weight_lbs * calorie_multiplier
    protein_grams = goal_weight_lbs * protein_multiplier
    protein_calories = protein_grams * 4  # 4 calories per gram of protein

    fat_calories = total_daily_calories * fat_percentage
    fat_grams = fat_calories / 9  # 9 calories per gram of fat

    calories_left = total_daily_calories - protein_calories - fat_calories
    carbohydrate_grams = calories_left / 4  # 4 calories per gram of carb

    return Macronutrients(protein_grams, fat_grams, carbohydrate_grams)


def main():
    """Gets the user's goal weight and prints the calculated macronutrients."""

    try:
        goal_weight_lbs = float(input("Enter your goal weight in lbs: "))
        macros = calculate_macronutrients(goal_weight_lbs)

        print(f"Total Daily Calories: {goal_weight_lbs * 12:.2f} kcal")  # Calculate directly
        print(f"Protein: {macros.protein:.2f} g")
        print(f"Fat: {macros.fat:.2f} g")
        print(f"Carbohydrates: {macros.carbohydrates:.2f} g")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print("An unexpected error occurred")
        print(e)



if __name__ == "__main__":
    main()