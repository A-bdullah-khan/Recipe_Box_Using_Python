# Importing Libraries
import shutil
import os
from pathlib import Path

# Getting the full path till Recipes folder
BASE_DIR = Path(__file__).resolve().parent
full_path = BASE_DIR / "Recipes"


# Function to count recipes
def count_recipes():
    counter = 0
    for category_folder in full_path.iterdir():
        for file in category_folder.iterdir():
            if file.is_file():
                counter += 1
    return counter


# Function to list categories
def list_categories():
    categories = []
    for folder in full_path.iterdir():
        if folder.is_dir():
            categories.append(folder.name)
    return categories


# Function to show the menu
def show_menu(total_recipes):
    print("Welcome to Recipes Box")
    print(f"You have {total_recipes} recipes")
    print(f"Your recipes are stored in {full_path}")
    print("Choose an option:")
    print("[1] Read Recipe")
    print("[2] Create Recipe")
    print("[3] Create Category")
    print("[4] Delete Recipe")
    print("[5] Delete Category")
    print("[6] Exit Program")
    choice = int(input("Enter your choice: "))
    return choice


# Function to read a recipe
def read_recipe(all_categories):
    print(f"The categories of recipes are: {all_categories}")
    index = int(input("Choose a category by number (starting from 1): ")) - 1
    chosen_category = all_categories[index]
    selected_category_path = full_path / chosen_category

    recipes = [file.name for file in selected_category_path.iterdir() if file.is_file() and file.name.endswith('.txt')]

    for i, recipe in enumerate(recipes, start=1):
        print(f"[{i}] {recipe}")

    recipe_index = int(input("Choose a recipe by number: ")) - 1
    chosen_recipe = recipes[recipe_index]

    recipe_path = selected_category_path / chosen_recipe
    with open(recipe_path, "r") as file:
        content = file.read()
        print("\n" + content)


# Function to create a recipe
def create_recipe(all_categories):
    print("Categories:")
    for i, category in enumerate(all_categories, start=1):
        print(f"[{i}] {category}")

    index = int(input("Choose a category by number: ")) - 1
    chosen_category = all_categories[index]
    selected_category_path = full_path / chosen_category

    recipe_name = input("Enter the name of your new recipe: ").strip()
    recipe_path = selected_category_path / f"{recipe_name}.txt"

    recipe_content = input("Enter the content of your new recipe: ")
    with open(recipe_path, 'w') as file:
        file.write(recipe_content)

    print(f"Recipe '{recipe_name}' has been created in category '{chosen_category}'.")


# Function to create a category
def create_category():
    new_category = input("Enter the name of your new category: ").strip()
    new_category_path = full_path / new_category
    new_category_path.mkdir()
    print(f"New category '{new_category}' has been created at {new_category_path}")


# Function to delete a recipe
def delete_recipe(all_categories):
    print("Categories:")
    for i, category in enumerate(all_categories, start=1):
        print(f"[{i}] {category}")

    category_index = int(input("Choose a category by number: ")) - 1
    chosen_category = all_categories[category_index]
    category_path = full_path / chosen_category

    recipes = [file.name for file in category_path.iterdir() if file.is_file() and file.name.endswith('.txt')]

    for i, recipe in enumerate(recipes, start=1):
        print(f"[{i}] {recipe}")

    recipe_index = int(input("Which recipe would you like to delete? ")) - 1
    chosen_recipe = recipes[recipe_index]
    recipe_path = category_path / chosen_recipe

    recipe_path.unlink()
    print(f"Recipe '{chosen_recipe}' has been deleted.")


# Function to delete a category
def delete_category(all_categories):
    print("Categories:")
    for i, category in enumerate(all_categories, start=1):
        print(f"[{i}] {category}")

    category_index = int(input("Choose a category you want to delete: ")) - 1
    chosen_category = all_categories[category_index]
    category_path = full_path / chosen_category

    shutil.rmtree(category_path)
    print(f"Category '{chosen_category}' has been deleted successfully.")


#  Main Program

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    total_recipes = count_recipes()
    all_categories = list_categories()

    choice = show_menu(total_recipes)

    if choice == 1:
        read_recipe(all_categories)
    elif choice == 2:
        create_recipe(all_categories)
    elif choice == 3:
        create_category()
    elif choice == 4:
        delete_recipe(all_categories)
    elif choice == 5:
        delete_category(all_categories)
    elif choice == 6:
        print("Ending the program! Take care.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

    input("\nPress Enter to continue...")
