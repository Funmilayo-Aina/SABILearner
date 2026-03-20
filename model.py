import random
#SKILLS
MULTI_SKILL_KNOWLEDGE_COMPONENTS = ['Addition', 'Subtraction', 'Multiplication', 'Division']
skills = {
    skill: 0.5 for skill in MULTI_SKILL_KNOWLEDGE_COMPONENTS
}
  #BKT parameters
BKT_MODEL_PARAMETERS = {
    'prior': 0.5,
    'transit': 0.2,
    'guess': 0.1,
    'slip': 0.1
}  
history ={
    skill:[] for skill in MULTI_SKILL_KNOWLEDGE_COMPONENTS  
} 
#Current state
current_answer = None
current_skill = None

#BKT update function
def update_bkt(skill, correct):
    global skills

    p_L = skills[skill]
    p_T = BKT_MODEL_PARAMETERS['transit']
    p_G = BKT_MODEL_PARAMETERS['guess']
    p_S = BKT_MODEL_PARAMETERS['slip']

    # Bayesian update
    if correct:
        numerator = p_L * (1 - p_S)
        denominator = numerator + (1 - p_L) * p_G
    else:
        numerator = p_L * p_S
        denominator = numerator + (1 - p_L) * (1 - p_G)

    p_L = numerator / denominator

    # Learning transition
    p_L = p_L + (1 - p_L) * p_T

    # Save updated value
    skills[skill] = p_L
    history[skill].append(p_L)

    return p_L
# =========================
# SELECT NEXT SKILL (SMART)
# =========================
def select_skill():
    # Focus on weakest skill
    return min(skills, key=skills.get)


# =========================
# GENERATE QUESTION
# =========================
def generate_question():
    global current_answer, current_skill

    current_skill = select_skill()
    knowledge = skills[current_skill]

    # Adaptive difficulty
    if knowledge < 0.4:
        level = "easy"
        max_val = 5
    elif knowledge < 0.7:
        level = "medium"
        max_val = 10
    else:
        level = "hard"
        max_val = 20

    a = random.randint(1, max_val)
    b = random.randint(1, max_val)

    if current_skill == "Addition":
        current_answer = a + b
        question = f"What is {a} + {b}?"

    elif current_skill == "Subtraction":
        current_answer = a - b
        question = f"What is {a} - {b}?"

    elif current_skill == "Multiplication":
        current_answer = a * b
        question = f"What is {a} × {b}?"

    elif current_skill == "Division":
        b = random.randint(1, max_val)
        current_answer = a
        question = f"What is {a*b} ÷ {b}?"

    return {
        "question": question,
        "skill": current_skill,
        "level": level,
        "knowledge": round(knowledge, 3),
        "all_skills": {k: round(v, 3) for k, v in skills.items()}
    }


# =========================
# CHECK ANSWER
# =========================
def check_answer(user_answer):
    global current_answer, current_skill

    correct = float(user_answer) == float(current_answer)

    updated_knowledge = update_bkt(current_skill, correct)

    if correct:
        feedback = f"✅ Correct! ({current_skill})"
    else:
        feedback = f"❌ Incorrect. Correct answer: {current_answer}"

    return {
        "feedback": feedback,
        "skill": current_skill,
        "updated_knowledge": round(updated_knowledge, 3),
        "all_skills": {k: round(v, 3) for k, v in skills.items()}
    }