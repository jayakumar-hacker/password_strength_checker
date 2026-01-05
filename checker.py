from rules import (
    contains_user_data,
    is_common_password,
    check_length,
    check_charset,
    has_repetition,
    has_sequence
)

def evaluate_password(password,user_data,common_passwords):
    reasons=[]
    
    personal_issue = contains_user_data(password,user_data)
    # HARD FAIL: personal data
    if personal_issue:
        reasons.append(personal_issue)
        return {
            "status": "UNSAFE",
            "reasons": reasons,
            "score": None
        }
    
    common_word = is_common_password(password, common_passwords)
    if common_word:
        reasons.append(common_word)
        # HARD FAIL: common password
        return {
            "status": "UNSAFE",
            "reasons": [common_word],
            "score": None
        }
    # SCORING
    score = 0
    len_score,len_issue = check_length(password)
    if len_issue:
        reasons.append(len_issue)
    charset_score,char_issue = check_charset(password)
    score+=len_score
    score+=charset_score
    reasons.extend(char_issue)
    
    
    has_repeated = has_repetition(password)
    if has_repeated:
        reasons.append(has_repeated)
        score -= 20

    if has_sequence(password):
        reasons.append("Sequential pattern detected")
        score -= 20

    score = max(0, min(score, 100))
    # STRENGTH LABEL
    if score < 30:
        strength = "WEAK"
    elif score < 60:
        strength = "MEDIUM"
    elif score < 80:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return {
        "status": "SAFE",
        "strength": strength,
        "score": score,
        "notes": reasons
    }
    