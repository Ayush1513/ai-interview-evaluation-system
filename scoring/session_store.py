# session_store.py

from datetime import datetime

interview_history=[]


def save_interview(data):

    entry={

        "question":
        data["question"],

        "answer":
        data["answer"],

        "final_score":
        data["final_score"],

        "recommendation":
        data["dynamic_action"],

        "time":
        datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
        )

    }

    interview_history.append(
    entry
    )



def get_interview_history():

    return {

        "total_interviews":
        len(interview_history),

        "interviews":
        interview_history

    }