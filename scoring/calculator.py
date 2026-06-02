from scoring.config import SCORING_CONFIG


def calculate_score(scores, question_type):


    weights = SCORING_CONFIG[question_type]


    final_score = 0


    for key,value in weights.items():

        final_score += (
            scores.get(key,0)
            *
            value
        )


    return round(
        final_score,
        2
    )