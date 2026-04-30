def analyze_message(message: str):
    print("🔥 ANALYZER RUNNING:", message)

    message = message.lower()
    score = 0
    reasons = []

    # 🪙 GOLD SCAMS
    if "gold" in message:
        score += 40
        reasons.append("gold scam")

    # 💰 MONEY / PAYMENT
    if "pay" in message or "₹" in message or "payment" in message:
        score += 30
        reasons.append("money request")

    # 🏦 BANK / KYC FRAUD
    if "bank" in message or "kyc" in message or "account" in message:
        score += 40
        reasons.append("bank fraud")

    # 🔗 LINKS (PHISHING)
    if "http" in message or "www" in message:
        score += 40
        reasons.append("suspicious link")

    # 📦 COURIER / DELIVERY SCAM
    if "courier" in message or "delivery" in message or "track" in message:
        score += 30
        reasons.append("fake delivery scam")

    # 📱 APK / APP DOWNLOAD
    if ".apk" in message or "download app" in message:
        score += 50
        reasons.append("malicious app")

    # 📲 SOCIAL MEDIA SCAMS
    if "followers" in message or "instagram" in message or "whatsapp" in message:
        score += 30
        reasons.append("social media scam")

    # 🎁 FREE / OFFER / LOTTERY
    if "free" in message or "offer" in message or "won" in message or "prize" in message:
        score += 35
        reasons.append("fake offer")

    # ⚡ URGENCY
    if "urgent" in message or "immediately" in message or "within 24 hours" in message:
        score += 25
        reasons.append("urgency pressure")

    # ⚠️ THREATS
    if "penalty" in message or "blocked" in message:
        score += 25
        reasons.append("threat message")

    score = min(score, 100)

    # 🎯 RISK LEVEL
    if score >= 70:
        risk = "high"
    elif score >= 40:
        risk = "medium"
    else:
        risk = "low"

    # 🌐 FINAL USER MESSAGE (ENGLISH + TELUGU)
    if risk == "high":
        reply = (
            "⚠️ This message is HIGHLY suspicious. Do NOT click any links or make payments.\n"
            "⚠️ ఈ సందేశం ప్రమాదకరంగా ఉంది. లింక్ క్లిక్ చేయవద్దు, డబ్బులు పంపవద్దు."
        )
    elif risk == "medium":
        reply = (
            "⚠️ This message looks suspicious. Verify before trusting.\n"
            "⚠️ ఈ సందేశం అనుమానాస్పదంగా ఉంది. నమ్మే ముందు చెక్ చేయండి."
        )
    else:
        reply = (
            "✅ This message looks safe. You can proceed.\n"
            "✅ ఈ సందేశం సురక్షితం. మీరు కొనసాగవచ్చు."
        )

    return {
        "fake_probability": score,
        "risk_level": risk,
        "reason": ", ".join(reasons),
        "user_warning": reply
    }