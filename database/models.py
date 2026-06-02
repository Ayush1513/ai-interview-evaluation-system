from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Text

from database.connection import Base


class Interview(Base):

    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(Text)

    answer = Column(Text)

    answer_accuracy = Column(Float)
    
    depth = Column(Float)

    clarity = Column(Float)

    problem_solving = Column(Float)

    confidence = Column(Float)

    communication = Column(Float)

    final_score = Column(Float)

    competency_score = Column(Float)

    recommendation = Column(String)

    feedback = Column(Text)

    summary = Column(Text)

    follow_up_question = Column(Text)

    strengths = Column(Text)

    weaknesses = Column(Text)

    evaluation_category = Column(Text)

    timestamp = Column(String)