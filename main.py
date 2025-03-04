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
