import ast

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(data):

    file_name = "candidate_report.pdf"

    pdf = SimpleDocTemplate(
        file_name
    )

    styles = getSampleStyleSheet()

    content = []

    # =================================
    # TITLE
    # =================================

    content.append(
    Paragraph(
        "AI Interview Evaluation Report",
        styles["Title"]
    )
    )

    content.append(
    Spacer(1, 10)
    )


    # =================================
    # QUESTION
    # =================================

    content.append(
        Paragraph(
            f"<b>Question:</b> {data.get('question', '')}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # =================================
    # ANSWER
    # =================================

    content.append(
        Paragraph(
            f"<b>Candidate Answer:</b> {data.get('answer', '')}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 8)
    )

    # =================================
    # SCORES
    # =================================

    score_data = f"""
    <b>Answer Accuracy:</b> {data.get('answer_accuracy', 0)}/10
    <br/>
    <b>Depth:</b> {data.get('depth', 0)}/10
    <br/>
    <b>Clarity:</b> {data.get('clarity', 0)}/10
    <br/>
    <b>Problem Solving:</b> {data.get('problem_solving', 0)}/10
    <br/>
    <b>Confidence:</b> {data.get('confidence', 0)}/10
    <br/>
    <b>Communication:</b> {data.get('communication', 0)}/10
    <br/>
    <b>Final Composite Score:</b> {data.get('final_score', 0)}/10
    <br/>
    <b>Competency Score:</b> {data.get('competency_score', 0)}/10
    """

    content.append(
        Paragraph(
            score_data,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 8)
    )

    # =================================
    # RECOMMENDATION
    # =================================

    content.append(
    Paragraph(
        f"<b>Hiring Recommendation:</b> {data.get('recommendation','N/A')}",
        styles["Heading2"]
    )
    )

    content.append(
        Spacer(1, 5)
    )

    # =================================
    # SUMMARY
    # =================================
    content.append(
    Paragraph(
        "________________________________________________",
        styles["Normal"]
    )
    )
    content.append(
        Paragraph(
            "Candidate Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            data.get("summary", ""),
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 5)
    )

    # =================================
    # COMPETENCY ANALYSIS
    # =================================

    categories = data.get(
        "evaluation_category",
        []
    )

    content.append(
        Paragraph(
            "Competency Analysis",
            styles["Heading2"]
        )
    )

    for item in categories:

     content.append(
        Paragraph(
            f"• {item.get('name')} : {item.get('score')}/10",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 5)
    )

    # =================================
    # FOLLOW UP QUESTION
    # =================================

    content.append(
        Paragraph(
            "Follow Up Question",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            data.get(
                "follow_up_question",
                "No follow-up question generated"
            ),
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 5)
    )

    
    # =================================
    # STRENGTHS
    # =================================

    strengths_data = data.get(
        "strengths",
        []
    )

    if isinstance(strengths_data, str):

        try:
            strengths_data = ast.literal_eval(
                strengths_data
            )
        except:
            strengths_data = [strengths_data]

    strengths = "<br/>".join(
        [
            f"✓ {item}"
            for item in strengths_data
        ]
    )

    content.append(
        Paragraph(
            f"""
            <b>Strengths:</b>
            <br/>
            {strengths}
            """,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 5)
    )

    # =================================
    # IMPROVEMENT AREAS
    # =================================

    weakness_data = data.get(
        "weaknesses",
        []
    )

    if isinstance(weakness_data, str):

        try:
            weakness_data = ast.literal_eval(
                weakness_data
            )
        except:
            weakness_data = [weakness_data]

    weakness = "<br/>".join(
        [
            f"• {item}"
            for item in weakness_data
        ]
    )

    content.append(
        Paragraph(
            f"""
            <b>Improvement Areas:</b>
            <br/>
            {weakness}
            """,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 8)
    )

    content.append(
    Spacer(1,10)
    )

    content.append(
    Paragraph(
        "<b>AI Feedback</b>",
        styles["Heading2"]
    )
    )

    content.append(
    Paragraph(
        data.get("feedback",""),
        styles["Normal"]
    )
    )

    # =================================
    # TIMESTAMP
    # =================================

    content.append(
        Paragraph(
            f"<b>Generated:</b> {data.get('timestamp', '')}",
            styles["Normal"]
        )
    )

    # =================================
    # BUILD PDF
    # =================================
    content.append(
    Spacer(1, 5)
    )

    content.append(
    Paragraph(
        "<i>Generated by AI Interview Evaluation System</i>",
        styles["Normal"]
    )
    )
    pdf.build(content)

    return file_name