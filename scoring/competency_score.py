def calculate_competency_score(categories):

    if not categories:
        return 0

    total = sum(
        item.get("score", 0)
        for item in categories
    )

    return round(
        total / len(categories),
        2
    )