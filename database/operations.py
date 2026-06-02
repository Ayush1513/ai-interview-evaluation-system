from sqlalchemy.orm import Session
from database.models import Interview
import json


def save_interview_data(db: Session, data):

    interview = Interview(

        question=data["question"],

        answer=data["answer"],

        answer_accuracy=data["answer_accuracy"],

        depth=data["depth"],

        clarity=data["clarity"],

        problem_solving=data["problem_solving"],

        confidence=data["confidence"],

        communication=data["communication"],

        final_score=data["final_score"],

        competency_score=data["competency_score"],

        recommendation=data["recommendation"],

        feedback=data["feedback"],

        summary=data.get(
            "summary",
            ""
        ),

        follow_up_question=data.get(
            "follow_up_question",
            ""
        ),

        strengths=json.dumps(
            data.get(
                "strengths",
                []
            )
        ),

        weaknesses=json.dumps(
            data.get(
                "weaknesses",
                []
            )
        ),

        evaluation_category=json.dumps(
            data.get(
                "evaluation_category",
                []
            )
        ),

        timestamp=data["timestamp"]

    )

    db.add(interview)

    db.commit()

    db.refresh(interview)

    return interview


def get_all_interviews(db: Session):

    return db.query(
        Interview
    ).all()