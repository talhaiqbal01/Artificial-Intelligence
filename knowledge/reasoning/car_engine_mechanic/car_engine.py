"""
Car Engine Class
"""
from rules import Rules


def display_issues(issues):
    """
    Displays possible issues based on the given symptoms
    :param issues:
    :return:
    """
    if issues:
        print("\nPossible issues based on the symptoms provided:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No issues found for the given symptoms.")


class CarEngine:
    def __init__(self):
        self.rules = Rules()
        self.rules.load_rules()  # Ensure rules are loaded
        self.symptoms_list = [
            "car not starting",
            "battery light on",
            "squeaking noise during braking",
            "engine overheating"
        ]

    def run_diagnostics(self):
        """
        Return the issues in the car based on
        :return:
        """
        print("Welcome to the Car Diagnostic Tool")
        print("Please select the symptoms your car is experiencing from the list below:")
        for idx, symptom in enumerate(self.symptoms_list, 1):
            print(f"{idx}. {symptom}")
        print("Type '0' when you are finished entering symptoms.")

        selected_symptoms = self.get_user_symptoms()

        issues = self.rules.infer_issues(selected_symptoms)
        display_issues(issues)

    def get_user_symptoms(self):
        """
        Takes symptoms from the user
        :return:
        """
        selected_symptoms = []
        while True:
            user_input = input("Enter the number of the symptom: ")
            if user_input.isdigit():
                choice = int(user_input)
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.symptoms_list):
                    selected_symptom = self.symptoms_list[choice - 1]
                    if selected_symptom not in selected_symptoms:
                        selected_symptoms.append(selected_symptom)
                    else:
                        print("Symptom already selected.")
                else:
                    print("Invalid option, please try again.")
            else:
                print("Please enter a valid number.")
        return selected_symptoms
