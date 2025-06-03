import subprocess
import re

OLLAMA_PATH = r"C:\Users\HARIANTH\AppData\Local\Programs\Ollama\ollama.exe"  # Full path here


def classify_business(description: str) -> str:
    try:
        command = [
            OLLAMA_PATH, "run", "mistral",
            # Prompt for ollama to get the naics for the given description
            f"Give me the NAICS code for this business: {description}?"
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


def infer_zip_and_census(city: str, state: str) -> tuple[str, str]:
    try:
        command = [
            OLLAMA_PATH, "run", "mistral",
            # Prompt for ollama to get the naics for the given description
            f"Only respond with ZIP code and Census Tract separated by a space for city '{city}' in state '{state}'."
        ]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            # Can increase or decrease this depending on the machine.
            timeout=30,
            encoding="utf-8",        # Forcing UTF-8
            errors="replace"         # Replacing bad characters instead of crashing
        )
        if result.returncode != 0:
            return "N/A", "N/A"

        output = result.stdout.strip()
        parts = output.split()
        if len(parts) >= 2:
            return parts[0], parts[1]
        elif len(parts) == 1:
            return parts[0], "N/A"
        else:
            return "N/A", "N/A"
    except:
        return "N/A", "N/A"
