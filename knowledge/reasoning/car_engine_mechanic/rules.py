"""
Rules Class
"""


class Rules:
    def __init__(self):
        self.rules = []

    def load_rules(self):
        """
        Set possible symptoms dictionary into rules list
        :return:
        """
        self.rules = [
            {"symptoms": ["car not starting", "battery light on"],
             "possible_issues": ["dead battery", "faulty alternator", ],
             },
            {"symptoms": ["squeaking noise during braking"],
             "possible_issues": ["worn brake pads", "damaged brake rotors", ],
             },
            {"symptoms": ["engine overheating"],
             "possible_issues": ["low coolant", "faulty thermostat", "clogged radiator", ],
             },
            {"symptoms": ["battery light on"],
             "possible_issues": ["dead battery", "bad alternator", ],
             }
        ]

    def infer_issues(self, symptoms):
        """
        Identifies possible issues based on set of rules
        :param symptoms:
        :return:
        """
        matched_issues = []
        for rule in self.rules:
            if all(symptom in symptoms for symptom in rule["symptoms"]):
                for issue in rule["possible_issues"]:
                    if issue not in matched_issues:
                        matched_issues.append(issue)
        return matched_issues
