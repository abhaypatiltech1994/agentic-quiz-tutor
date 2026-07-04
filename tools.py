import random
from data.quiz_data import QUIZ_BANK

# Keeps track of which question was last asked, so check_answer can reference it
_current_question = {}

def get_question(topic: str = "") -> str:
    """Fetch a random quiz question, optionally filtered by topic keyword."""
    global _current_question
    candidates = QUIZ_BANK
    if topic:
        candidates = [q for q in QUIZ_BANK if topic.lower() in q["question"].lower()]
        if not candidates:
            candidates = QUIZ_BANK
    _current_question = random.choice(candidates)
    return _current_question["question"]

def check_answer(user_answer: str) -> str:
    """Check the user's answer against the last question asked."""
    if not _current_question:
        return "No question has been asked yet. Please request a question first."
    correct = _current_question["answer"]
    if user_answer.strip().lower() in correct.lower() or correct.lower() in user_answer.strip().lower():
        return f"Correct! The answer is '{correct}'."
    else:
        return f"Not quite. The correct answer is '{correct}'."