def detect_question_type(question):

    question = question.lower()


    technical_keywords = [
        "algorithm",
        "database",
        "stack",
        "queue",
        "api",
        "sql",
        "python",
        "java",
        "code",
        "program"
    ]


    hr_keywords = [
        "yourself",
        "strength",
        "weakness",
        "career",
        "goal",
        "motivation"
    ]


    behavioral_keywords = [
        "challenge",
        "conflict",
        "team",
        "pressure",
        "failure",
        "experience"
    ]


    for word in technical_keywords:

        if word in question:
            return "technical"


    for word in hr_keywords:

        if word in question:
            return "hr"


    for word in behavioral_keywords:

        if word in question:
            return "behavioral"


    return "general"
