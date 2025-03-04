def calculate_total_daily_calories(goal_weight):
    return goal_weight * 12

def calculate_protein(goal_weight):
    return goal_weight

def calculate_fat(total_daily_calories):
    fat_calories = total_daily_calories * 0.25
    return fat_calories / 9

def calculate_carbohydrates(calories_left):
    return calories_left / 4
