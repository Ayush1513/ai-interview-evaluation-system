# metrics.py

from scoring.session_store import get_interview_history


def get_metrics():

    history = get_interview_history()

    interviews = history["interviews"]

    total = len(interviews)


    # If no interviews available
    if total == 0:

        return {

            "total_interviews": 0,

            "average_score": 0,

            "recommended_count": 0

        }


    # Sum all scores
    total_score = sum(

        item["final_score"]

        for item in interviews

    )


    # Average score
    average_score = round(

        total_score / total,

        2

    )


    # Count recommended candidates
    recommended_count = len(

        [

            item for item in interviews

            if item["recommendation"] == "Recommended"

        ]

    )


    return {

        "total_interviews": total,

        "average_score": average_score,

        "recommended_count": recommended_count

    }