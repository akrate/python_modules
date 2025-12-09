#!/usr/bin/env python3

"""
Helper file for Growing Code.
"""

import importlib


def test_exercise(folder, module_name, func_name):
    """
    Loads and tests an exercise from a folder like ex00.ft_hello_garden
    """
    full_path = f"{folder}.{module_name}"

    print(f"\n=== Testing {module_name} ===")

    try:
        module = importlib.import_module(full_path)
        func = getattr(module, func_name)

        # Special case for exercise 7 (it needs parameters)
        if func_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")
            func("tomato", 15, "packets")
            func("carrot", 8, "grams")
            func("lettuce", 12, "area")
            print("\nTesting with unknown unit:")
            func("basil", 5, "unknown")
        else:
            func()

    except ModuleNotFoundError:
        print(f"❌ Could not find {full_path}.py")
        print("   Make sure the file exists inside its folder.")

    except AttributeError:
        print(f"❌ Function {func_name}() not found in {full_path}.py")

    except Exception as error:
        print(f"❌ Error running function: {error}")


def main():
    print("🌱 Welcome to Growing Code! 🌱")
    print("Which exercise would you like to test?\n")

    print("0 - ft_hello_garden")
    print("1 - ft_plot_area")
    print("2 - ft_harvest_total")
    print("3 - ft_plant_age")
    print("4 - ft_water_reminder")
    print("5 - ft_count_harvest (iter + rec)")
    print("6 - ft_garden_summary")
    print("7 - ft_seed_inventory")
    print("a - test all\n")

    choice = input("Enter your choice: ")

    if choice == "0":
        test_exercise("ex00", "ft_hello_garden", "ft_hello_garden")
    elif choice == "1":
        test_exercise("ex01", "ft_plot_area", "ft_plot_area")
    elif choice == "2":
        test_exercise("ex02", "ft_harvest_total", "ft_harvest_total")
    elif choice == "3":
        test_exercise("ex03", "ft_plant_age", "ft_plant_age")
    elif choice == "4":
        test_exercise("ex04", "ft_water_reminder", "ft_water_reminder")
    elif choice == "5":
        test_exercise("ex05", "ft_count_harvest_iterative", "ft_count_harvest_iterative")
        test_exercise("ex05", "ft_count_harvest_recursive", "ft_count_harvest_recursive")
    elif choice == "6":
        test_exercise("ex06", "ft_garden_summary", "ft_garden_summary")
    elif choice == "7":
        test_exercise("ex07", "ft_seed_inventory", "ft_seed_inventory")
    elif choice == "a":
        test_exercise("ex00", "ft_hello_garden", "ft_hello_garden")
        test_exercise("ex01", "ft_plot_area", "ft_plot_area")
        test_exercise("ex02", "ft_harvest_total", "ft_harvest_total")
        test_exercise("ex03", "ft_plant_age", "ft_plant_age")
        test_exercise("ex04", "ft_water_reminder", "ft_water_reminder")
        test_exercise("ex05", "ft_count_harvest_iterative", "ft_count_harvest_iterative")
        test_exercise("ex05", "ft_count_harvest_recursive", "ft_count_harvest_recursive")
        test_exercise("ex06", "ft_garden_summary", "ft_garden_summary")
        test_exercise("ex07", "ft_seed_inventory", "ft_seed_inventory")
    else:
        print("❌ Invalid choice! Choose 0–7 or 'a'.")


if __name__ == "__main__":
    main()
