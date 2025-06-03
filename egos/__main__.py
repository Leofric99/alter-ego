import os
import importlib

def list_ego_options(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.py') and f != '__main__.py']
    options = [os.path.splitext(f)[0] for f in files]
    display_options = [name.capitalize() for name in options]
    return options, display_options

def main():

    print("=" * 50)
    print("🦸  Alter-Ego Selector  🦸".center(50))
    print("=" * 50)

    directory = os.path.dirname(os.path.abspath(__file__))
    module_names, display_options = list_ego_options(directory)
    if not module_names:
        print("No alter-egos found.")
        return

    print("Which alter-ego would you like to interact with?\n")
    for idx, option in enumerate(display_options, 1):
        print(f"{idx}. {option}")

    choice = input("\nEnter the number of your choice: ")
    print("-" * 50)
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(module_names):
            chosen_module = module_names[choice_idx]
            module = importlib.import_module(f"egos.{chosen_module}")
            if hasattr(module, "handle_conversation"):
                module.handle_conversation()
            else:
                print(f"{display_options[choice_idx]} does not have a handle_conversation() function.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()