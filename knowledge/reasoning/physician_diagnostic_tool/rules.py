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
            {"symptoms": ["fever", "cough", "shortness of breath", ],
             "possible_issues": ["COVID-19", "flu", "common cold", ],
             },
            {"symptoms": ["headache", "nausea", "sensitivity to light", ],
             "possible_issues": ["migraine", "tension headache", "cluster headache", ],
             },
            {"symptoms": ["stomach pain", "diarrhea", "vomiting", ],
             "possible_issues": ["food poisoning", "stomach flu", "appendicitis", ],
             },
            {"symptoms": ["chest pain", "shortness of breath", "sweating", ],
             "possible_issues": ["heart attack", "angina", "panic attack", ],
             },
        ]

    def infer_issues(self, symptoms):
        """
        Identifies possible issues based on set of rules
        :param symptoms:
        :return:
        """
        matched_issues = []
        for rule in self.rules:
            if any(symptom in symptoms for symptom in rule["symptoms"]):
                for issue in rule["possible_issues"]:
                    if issue not in matched_issues:
                        matched_issues.append(issue)
        return matched_issues
