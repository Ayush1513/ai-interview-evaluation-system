def follow_up_logic(score):

    if score >= 8:
        return "Next Topic"

    elif score >= 5:
        return "Follow-up Level 1"

    else:
        return "Follow-up Level 2"