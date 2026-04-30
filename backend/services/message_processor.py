from services.language_detector import detect_language
from services.translator import translate_to_english, translate_to_original
from services.ai_analyzer import analyze_message
from services.risk_detect_engine import calculate_risk


def process_message(message: str):

    # Step 1: Language detect
    lang = detect_language(message)

    # Step 2: Translate to English
    if lang != "en":
        message_en = translate_to_english(message)
    else:
        message_en = message

    # Step 3: AI analysis
    print("👉 MESSAGE RECEIVED:", message_en)

    analysis = analyze_message(message_en)

    print("👉 ANALYSIS RESULT:", analysis)

    # Step 4: Risk calculation
    score, risk = calculate_risk(analysis)

    # ✅ Step 5: Use bilingual warning directly
    reply = analysis["user_warning"]

    return {
        "score": score,
        "risk": risk,
        "message": reply
    }