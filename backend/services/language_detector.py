from langdetect import detect

def detect_language(text: str):
    try:
        lang = detect(text)
        return lang
    except:
        return "unknown"