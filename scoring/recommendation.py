# recommendation.py


def get_recommendation(score):

    """
    Final hiring recommendation
    based on overall interview score.
    """

    if score >= 8:
        return "Strongly Recommended"

    elif score >= 6:
        return "Recommended"

    elif score >= 4:
        return "Needs Improvement"

    else:
        return "Not Recommended"


# =====================================
# FALLBACK METHODS
# Used only if Claude fails
# =====================================

def get_fallback_follow_up(score):

    if score >= 8:
        return (
            "Can you explain this with a real-world example?"
        )

    elif score >= 6:
        return (
            "Can you explain the internal working in more detail?"
        )

    else:
        return (
            "Please explain the concept in more detail."
        )


def get_fallback_feedback(score):

    if score >= 8:
        return (
            "Strong answer with good understanding and communication."
        )

    elif score >= 6:
        return (
            "Good answer but needs more depth and examples."
        )

    else:
        return (
            "Answer needs significant improvement in understanding and explanation."
        )


def get_fallback_strengths(score):

    if score >= 8:
        return [
            "Strong understanding",
            "Clear communication",
            "Good confidence"
        ]

    elif score >= 6:
        return [
            "Basic understanding",
            "Reasonable explanation"
        ]

    else:
        return [
            "Attempted the question"
        ]


def get_fallback_weaknesses(score):

    if score >= 8:
        return [
            "Minor improvements possible"
        ]

    elif score >= 6:
        return [
            "Needs more examples",
            "Needs deeper explanation"
        ]

    else:
        return [
            "Insufficient understanding",
            "Needs better explanation"
        ]