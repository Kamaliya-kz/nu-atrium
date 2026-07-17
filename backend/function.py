def get_temperature_recommendation(temperature: float) -> str:
    if temperature < 18:
        return "🥶 Too cold. Studying may be uncomfortable."

    elif 18 <= temperature <= 22:
        return "😊 Excellent temperature for studying."

    elif 22 < temperature <= 26:
        return "🙂 Comfortable for studying."

    elif 26 < temperature <= 30:
        return "😓 A bit warm. Long study sessions may be tiring."

    else:
        return "🥵 Too hot. Consider finding a cooler place."
    

def study_score(reading):

    score = 0

    if 20 <= reading.temperature <= 24:
        score += 3
    elif 24 < reading.temperature <= 27:
        score += 2

    if reading.brightness in ["Bright", "Normal brightness"]:
        score += 2

    if reading.noise == "Quiet":
        score += 3
    elif reading.noise == "Mild noise":
        score += 1

    return score