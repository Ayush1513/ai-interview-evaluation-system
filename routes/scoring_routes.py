from fastapi import APIRouter
from fastapi.responses import FileResponse

from models.score_model import ScoreRequest

from scoring.ai_scoring import ai_evaluate_answer
from scoring.calculator import calculate_score
from scoring.question_classifier import detect_question_type
from database.operations import get_all_interviews

from scoring.recommendation import (
    get_recommendation,
    get_fallback_follow_up
)
from scoring.audit_log import (
    save_log,
    get_logs
)

from reports.generator import generate_report


# DATABASE IMPORTS

from database.connection import SessionLocal

from database.operations import (
    save_interview_data,
    get_all_interviews
)

from database.models import Interview


from datetime import datetime


router = APIRouter()


db = SessionLocal()



# ===================================
# SCORE API
# ===================================
@router.post("/score")
def score(data: ScoreRequest):

    question_type = detect_question_type(
        data.question
    )

    scores = ai_evaluate_answer(
        data.question,
        data.answer
    )

    scores.setdefault("answer_accuracy", 5)
    scores.setdefault("depth", 5)
    scores.setdefault("clarity", 5)
    scores.setdefault("problem_solving", 5)
    scores.setdefault("confidence", 5)
    scores.setdefault("communication", 5)

    # STEP 4
    final_score = calculate_score(
    scores,
    question_type
    )
    decision = get_recommendation(
    final_score
)

    summary = scores.get(
        "summary",
        ""
    )

    evaluation_category = scores.get(
        "evaluation_category",
        []
    )

    competency_score = 0

    if evaluation_category:

        competency_score = round(
            sum(
                item.get("score", 0)
                for item in evaluation_category
            )
            / len(evaluation_category),
            2
        )

    # DYNAMIC FOLLOW-UP

    if final_score >= 8:

        follow_up = "No follow-up required"

    else:

        follow_up = scores.get(
    "follow_up_question",
    get_fallback_follow_up(
        final_score
    )
   )

    feedback = scores.get(
        "feedback",
        "Candidate evaluation completed."
    )

    strengths = scores.get(
        "strengths",
        []
    )

    weaknesses = scores.get(
        "weaknesses",
        []
    )

    response = {

        "question": data.question,
        "answer": data.answer,
        "question_type": question_type,

        "answer_accuracy":
         scores["answer_accuracy"],

        "depth":
        scores["depth"],

        "clarity":
        scores["clarity"],

        "problem_solving":
        scores["problem_solving"],

        "confidence":
        scores["confidence"],

        "communication":
        scores["communication"],

        "final_score":
        final_score,

        "competency_score":
        competency_score,

        "summary":
        summary,

        "evaluation_category":
        evaluation_category,

        "dynamic_action":
        decision,

        "recommendation":
        decision,

        "follow_up_question":
        follow_up,

        "feedback":
        feedback,

        "strengths":
        strengths,

        "weaknesses":
        weaknesses,

        "timestamp":
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    }

    # DATABASE SAVE

    save_interview_data(
        db,
        response
    )

    # AUDIT LOG

    save_log(
        "Interview Evaluated",
        {
            "question": data.question,
            "question_type": question_type,
            "score": final_score,
            "competency_score": competency_score,
            "recommendation": decision
        }
    )

    # PDF

    generate_report(response)
    response["notification"] = (
    "Candidate report generated successfully and is ready for HR download."
    )
    
    response["report"] = "candidate_report.pdf"

    return response



# ===================================
# DOWNLOAD REPORT
# ===================================


@router.get("/report")
def download_report():

    return FileResponse(

        path="candidate_report.pdf",

        filename="candidate_report.pdf",

        media_type="application/pdf"

    )




# ===================================
# HISTORY
# ===================================


@router.get("/history")
def history():


    interviews = get_all_interviews(
        db
    )


    formatted=[]


    for item in interviews:


        formatted.append({

            "question":
            item.question,


            "answer":
            item.answer,


            "score":
            item.final_score,


            "recommendation":
            item.recommendation,


            "time":
            item.timestamp

        })


    return {


        "total_interviews":
        len(formatted),


        "interviews":
        formatted

    }




# ===================================
# METRICS
# ===================================


@router.get("/metrics")
def metrics():


    interviews = get_all_interviews(
        db
    )


    total=len(interviews)


    if total==0:


        return {

            "total_interviews":0,

            "average_score":0,

            "recommended_count":0

        }


    average=round(

        sum(

            i.final_score

            for i in interviews

        )

        /

        total,

        2

    )


    recommended=len(

        [

            i for i in interviews

           if i.recommendation in [
                    "Recommended",
                    "Strongly Recommended"
              ]

        ]

    )


    return {


        "total_interviews":
        total,


        "average_score":
        average,


        "recommended_count":
        recommended

    }




# ===================================
# LOGS
# ===================================


@router.get("/logs")
def logs():

    return get_logs()




# ===================================
# CLEAR HISTORY
# ===================================


@router.delete("/clear-history")
def clear_history():


    db.query(
        Interview
    ).delete()


    db.commit()


    return {

        "message":
        "History Cleared Successfully"

    }

@router.get("/interviews")
def get_interview_history():

    db = SessionLocal()

    interviews = get_all_interviews(db)

    return interviews


# ==========================
# GET SINGLE INTERVIEW
# ==========================

@router.get("/interview/{id}")
def get_interview(id: int):

    db = SessionLocal()

    interviews = get_all_interviews(db)

    for item in interviews:
        if item.id == id:
            return item

    return {
        "error": "Interview not found"
    }