import os
import json
import re

from dotenv import load_dotenv
from anthropic import Anthropic


# ==========================
# Load ENV
# ==========================

load_dotenv()


# ==========================
# Claude Client
# ==========================

client = Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)


# ==================================
# Claude AI Answer Evaluation Service
# ==================================

def ai_evaluate_answer(question, answer):

    prompt = f"""

You are an expert AI interview evaluator.

Evaluate the candidate answer.


QUESTION:
{question}


CANDIDATE ANSWER:
{answer}



Evaluate using these parameters:

1. answer_accuracy
- Correctness of answer
- Concept understanding

2. depth
- Explanation detail
- Examples
- Practical knowledge

3. clarity
- Structure
- Easy understanding

4. problem_solving
- Logical thinking
- Approach

5. confidence
- Certainty in explanation

6. communication
- Language quality
- Presentation


IMPORTANT:

If question is technical:
focus more on correctness and depth.

If question is HR / behavioral:
focus more on communication,
confidence and relevance.


Also generate:

1. Short interview summary

2. Dynamic competency analysis

Choose 3-5 competencies dynamically
based on the answer.

Examples:

Software Candidate:
- Domain Knowledge
- Problem Solving
- Communication

Sales Candidate:
- Customer Handling
- Persuasion
- Communication

Management Candidate:
- Leadership
- Decision Making
- Communication


Generate follow-up question:

Rules:

Average score >= 8
→ No follow-up required

Average score between 5 and 7
→ Ask medium difficulty follow-up

Average score below 5
→ Ask basic follow-up



Return ONLY valid JSON.

JSON FORMAT:

{{
    "answer_accuracy":8,

    "depth":7,

    "clarity":8,

    "problem_solving":7,

    "confidence":8,

    "communication":8,

    "feedback":"short feedback",

    "summary":"overall candidate summary",

    "strengths":[
        "strength point"
    ],

    "weaknesses":[
        "weakness point"
    ],

    "evaluation_category":[

        {{
            "name":"Domain Knowledge",
            "score":8
        }},

        {{
            "name":"Communication",
            "score":9
        }},

        {{
            "name":"Critical Thinking",
            "score":7
        }}

    ],

    "follow_up_question":
    "dynamic follow up question"
}}

"""

    try:

        response = client.messages.create(

            model="claude-haiku-4-5-20251001",

            max_tokens=800,

            temperature=0,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        result = (
            response
            .content[0]
            .text
            .strip()
        )

        print(
            "\n========== CLAUDE RESPONSE =========="
        )

        print(result)

        print(
            "====================================\n"
        )



        # ==========================
        # Extract JSON safely
        # ==========================

        json_match = re.search(
            r"\{[\s\S]*\}",
            result
        )

        if not json_match:

            raise Exception(
                "Claude JSON not found"
            )

        data = json.loads(
            json_match.group()
        )



        return {

            "answer_accuracy":
                data.get(
                    "answer_accuracy",
                    5
                ),

            "depth":
                data.get(
                    "depth",
                    5
                ),

            "clarity":
                data.get(
                    "clarity",
                    5
                ),

            "problem_solving":
                data.get(
                    "problem_solving",
                    5
                ),

            "confidence":
                data.get(
                    "confidence",
                    5
                ),

            "communication":
                data.get(
                    "communication",
                    5
                ),

            "feedback":
                data.get(
                    "feedback",
                    "No feedback"
                ),

            "summary":
                data.get(
                    "summary",
                    ""
                ),

            "strengths":
                data.get(
                    "strengths",
                    []
                ),

            "weaknesses":
                data.get(
                    "weaknesses",
                    []
                ),

            "evaluation_category":
                data.get(
                    "evaluation_category",
                    []
                ),

            "follow_up_question":
                data.get(
                    "follow_up_question",
                    "No follow-up required"
                )

        }

    except Exception as e:

        print(
            "Claude Error:",
            e
        )



        # ==========================
        # Fallback Response
        # ==========================

        return {

            "answer_accuracy": 5,

            "depth": 5,

            "clarity": 5,

            "problem_solving": 5,

            "confidence": 5,

            "communication": 5,

            "feedback":
            "Claude evaluation failed",

            "summary":
            "AI summary unavailable",

            "strengths": [
                "Evaluation unavailable"
            ],

            "weaknesses": [
                "AI response unavailable"
            ],

            "evaluation_category": [
                

                {
                    "name": "Communication",
                    "score": 5
                },

                {
                    "name": "Problem Solving",
                    "score": 5
                }

            ],

            "follow_up_question":
            "Can you explain your answer in more detail?"

        }