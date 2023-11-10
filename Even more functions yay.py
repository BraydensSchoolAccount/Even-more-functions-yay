# too many functions... yay
# Brayden Towner
# 11/10/2023

import os
exercise_int=1

# Just to keep it in one file, I'll use headers and cls to clarify exercises.
# This code repeats a lot
def next_exercise(exercise_name):
    # It tries to grab the local variable with this name which doesn't exist...
    # I knew of this keyword already
    global exercise_int
    # Only pause pre-exercise if this isn't the first
    if exercise_int > 1:
        os.system("pause")
    os.system("cls")
    print(f"Exercise {exercise_int}: {exercise_name}\n")
    exercise_int+=1

def make_shirt(size, message):
    """Prints the info of the shirt given

    Args:
        size (str): The Size of the shirt
        message (str): What the shirt should say
    No return
    """
    print(f"Your shirt size is {size} with the great message of '{message}'")

def describe_city(city, country="America"):
    """Relies on user trust to say that a specific city is in a country

    Args:
        city (str): Name of the city you're describing
        country (str, optional): Country the city is in. Defaults to "America".
    """
    print(f"{city} is in {country}")

def math_stuff(starting_number):
    """Divides by 2, then multiplies by 4. Not efficient at all

    Args:
        starting_number (int): The number to divide and multiply
    Returns int: The solution
    """
    def divide_by_2(number):
        """Divides a number by 2

        Args:
            number (int): The number to divide

        Returns:
            float: The number divided
        """
        return number/2
    def multiply_by_4(number):
        """multiply a number by 44

        Args:
            number (float): The number to multiply

        Returns:
            float: The number multiplied
        """
        return number*4
    small = divide_by_2(starting_number)
    bigger = multiply_by_4(small)
    return bigger

def spawn_enemy(enemy_type, x, y, weapon="*use random weapon function here*", has_medkit=False):
    """A fake function to spawn enemies

    Args:
        enemy_type (str): The type of enemy you want to spawn based off name
        x (int): Grid x position of enemy in level
        y (int): Grid y position of enemy in level
        weapon (str, optional): Force enemy to have specific weapon. Defaults to "*use random weapon function here*".
        has_medkit (bool, optional): Should they drop a medkit when they die?. Defaults to False.
    """
    print(f"enemy_type: {enemy_type},\nx: {x},\ny: {y},\n(Optional) weapon: {weapon},\n(Optional) has_medkit: {has_medkit}")


def pizza(*toppings):
    """Makes a very real pizza with any toppings the user wants! Any topping

    Args:
        toppings (str, multiple): The list of toppings the user wants
    """
    print("Making a pizza with the following toppings: ")
    for topping in toppings:
        print("\t-",topping)


next_exercise("Shirts")