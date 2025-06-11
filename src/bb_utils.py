def validate_card_value(value):
    if isinstance(value, int) and 1 <= value <= 11:
        return True
    return False

def extract_numbers_from_text(text):
    return [int(s) for s in text.split() if validate_card_value(int(s))]

def format_advice(advice):
    return f"💡 Advice: {advice}"