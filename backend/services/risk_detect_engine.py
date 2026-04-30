# import json

# def format_response(ai_output):
#     data = json.loads(ai_output)

#     percentage = data["fake_probability"]
#     risk = data["risk_level"]
#     reason = data["reason"]

#     if risk == "high":
#         warning = "⚠️ This message looks dangerous. Do NOT click any links."
#     elif risk == "medium":
#         warning = "⚠️ This message may be misleading. Verify before trusting."
#     else:
#         warning = "✅ This message seems relatively safe."

#     return f"""
# Fake Probability: {percentage}%

# Risk Level: {risk.upper()}

# Reason: {reason}

# {warning}
# # """
def calculate_risk(analysis):
    """
    Convert AI output into usable score + risk level
    """

    # If AI returns string JSON, we assume it's already parsed in future
    score = analysis.get("fake_probability", 0)

    if score >= 70:
        level = "high"
    elif score >= 40:
        level = "medium"
    else:
        level = "low"

    return score, level