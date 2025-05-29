import subprocess

OLLAMA_PATH = r"C:\Users\HARIANTH\AppData\Local\Programs\Ollama\ollama.exe"  # Full path here


def classify_business(description: str) -> str:
    try:
        command = [
            OLLAMA_PATH, "run", "mistral",
            f"What is the NAICS code for this business: {description}?"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60,
            encoding="utf-8"
        )

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"❌ Classification failed: {result.stderr.strip()}"

    except subprocess.TimeoutExpired:
        return "❌ Classification timed out."
    except FileNotFoundError:
        return "❌ Ollama not found. Please check the path."
    except Exception as e:
        return f"❌ Classification failed: {str(e)}"
