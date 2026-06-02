def evaluate_answer(question, answer):

    technical = 4
    depth = 4
    clarity = 4
    problem_solving = 4

    answer_lower = answer.lower()

    keywords = [
        "fifo",
        "lifo",
        "queue",
        "stack",
        "tree",
        "binary",
        "node",
        "algorithm",
        "array",
        "linked list"
    ]

    keyword_score = 0

    for word in keywords:

        if word in answer_lower:
            keyword_score += 1

    technical += min(keyword_score,4)


    answer_length = len(
        answer.split()
    )

    # Depth score

    if answer_length > 10:
        depth += 1

    if answer_length > 20:
        depth += 2

    if answer_length > 35:
        depth += 1


    # Clarity score

    if "." in answer:
        clarity += 2

    if "," in answer:
        clarity += 1


    # Problem solving score

    if "example" in answer_lower:
        problem_solving += 2

    if "used" in answer_lower:
        problem_solving += 2

    if "application" in answer_lower:
        problem_solving += 1


    return {

        "technical": min(technical,10),

        "depth": min(depth,10),

        "clarity": min(clarity,10),

        "problem_solving": min(problem_solving,10)

    }