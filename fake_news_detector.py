import subprocess
import json

def check_fake_news(text):
    prompt = f"""
    Analyze this news article for credibility. Look for red flags such as:
    - Sensational language
    - Bias
    - Lack of sources
    - Misleading claims

    Return a JSON object with:
    - credibility_score (1-100)
    - explanation

    Text: {text}
    """

    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    try:
        json_start = output.index('{')
        json_data = json.loads(output[json_start:])
        return json_data
    except:
        return {
            "credibility_score": 50,
            "explanation": "Could not parse output. Possibly malformed response."
        }
