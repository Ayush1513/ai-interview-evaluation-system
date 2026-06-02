# AI Interview Evaluation System

## Overview

AI Interview Evaluation System is an AI-powered interview assessment platform that evaluates candidate responses, generates detailed competency scores, provides hiring recommendations, and creates professional PDF reports.

The system leverages Claude AI to analyze interview answers and assess candidates across multiple evaluation criteria such as accuracy, technical depth, communication skills, confidence, and problem-solving ability.

---

## Features

* AI-powered answer evaluation using Claude API
* Automated scoring system
* Competency analysis
* Hiring recommendation generation
* Follow-up question generation
* PDF report generation
* SQLite database integration
* REST APIs using FastAPI
* Interview history tracking
* Technical and non-technical interview support

---

## Evaluation Parameters

The system evaluates candidates on:

| Parameter       | Description                  |
| --------------- | ---------------------------- |
| Answer Accuracy | Correctness of response      |
| Technical Depth | Understanding of concepts    |
| Clarity         | Quality of explanation       |
| Communication   | Ability to express ideas     |
| Problem Solving | Analytical thinking          |
| Confidence      | Confidence level in response |

---

## Competency Analysis

The system generates competency scores for:

* Domain Knowledge
* Communication Skills
* Technical Depth

---

## Technology Stack

### Backend

* Python
* FastAPI

### Database

* SQLite

### AI Model

* Claude API (Anthropic)

### Report Generation

* ReportLab

### API Testing

* Swagger UI

---

## Project Structure

```text
backend/
│
├── database/
│   ├── connection.py
│   ├── models.py
│   └── operations.py
│
├── models/
│   └── score_model.py
│
├── notifications/
│
├── reports/
│   ├── generator.py
│   └── template.html
│
├── routes/
│   └── scoring_routes.py
│
├── scoring/
│   ├── ai_scoring.py
│   ├── competency_score.py
│   ├── followup.py
│   ├── metrics.py
│   ├── recommendation.py
│   └── scoring_service.py
│
└── app.py
```

---

## Workflow

1. Candidate submits an interview answer.
2. Claude AI evaluates the response.
3. Individual parameter scores are generated.
4. Competency scores are calculated.
5. Hiring recommendation is determined.
6. Strengths and weaknesses are identified.
7. Follow-up questions are generated if needed.
8. Results are stored in the database.
9. A PDF interview report is generated.

---

## Scoring Process

### Individual Scores

The AI evaluates:

* Accuracy
* Technical Depth
* Clarity
* Communication
* Problem Solving
* Confidence

### Composite Score

The Final Composite Score is calculated by combining all individual evaluation metrics.

### Competency Score

Competency scores are derived from:

* Domain Knowledge
* Communication Skills
* Technical Understanding

### Recommendation Logic

| Score Range | Recommendation             |
| ----------- | -------------------------- |
| 8 - 10      | Strongly Recommended       |
| 6 - 7.9     | Recommended                |
| 4 - 5.9     | Consider with Reservations |
| Below 4     | Not Recommended            |

---

## API Endpoints

### Evaluate Candidate

```http
POST /score
```

Evaluates candidate answer and generates complete assessment.

### Interview History

```http
GET /interviews
```

Returns all interview records.

### Get Interview

```http
GET /interview/{id}
```

Returns interview details by ID.

---

## Output Generated

The system generates:

* Individual Scores
* Competency Analysis
* Strengths
* Weaknesses
* Follow-Up Questions
* Hiring Recommendation
* Final Composite Score
* PDF Interview Report

---

## Future Enhancements

* Speech-to-Text Integration
* Video Interview Analysis
* Real-Time Interview Evaluation
* Candidate Ranking Dashboard
* Email Report Delivery

---

## Author

**Ayush Kumar**

B.Tech Computer Science Engineering

AI Interview Evaluation System Project
