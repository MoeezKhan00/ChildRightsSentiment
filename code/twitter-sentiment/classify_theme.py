# classify_theme.py
def classify_themes(df):
    def classify(text):
        text = text.lower()
        if "school" in text or "education" in text or "learning" in text:
            return "Education"
        elif "child labor" in text or "labour" in text:
            return "Child Labor"
        elif "abuse" in text or "violence" in text:
            return "Abuse"
        elif "health" in text or "hospital" in text:
            return "Health"
        elif "rights" in text or "justice" in text:
            return "Child Rights"
        elif "vaccination" in text or "vaccine" in text:
            return "Vaccination"
        elif "child" in text or "children" in text:
            return "General Child Topic"
        else:
            return "Other"

    df['theme'] = df['text'].apply(classify)
    return df
