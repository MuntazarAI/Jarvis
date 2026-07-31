from ollama import chat
from core.config import MODEL
import traceback

SYSTEM_PROMPT = """
You are Jarvis, an AI assistant created by Muntazar.

Never claim to be the real Marvel JARVIS.
Never claim Tony Stark built you.

If someone asks who created you, answer that you were built by Muntazar and powered by Ollama running locally.

Be:
- Helpful
- Professional
- Honest
- Concise

If you don't know something, admit it instead of inventing facts.
"""


def ask_llm(messages: list) -> str:
    """Send messages to the configured LLM and return the assistant reply.

    This function wraps the underlying client call and returns a helpful
    error message instead of raising when the configured model or endpoint
    is not available. That makes the CLI-friendly and automated modes
    fail more clearly and gives actionable next steps.
    """

    try:
        response = chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                *messages,
            ],
        )

        print("\n======================")
        print("MESSAGES SENT TO OLLAMA")
        print("======================")

        for m in messages:
            print(f"{m['role']}: {m['content']}")

        print("======================\n")

        # Ollama returns a dict with message content
        return response.get("message", {}).get("content", "")

    except Exception as e:
        # Build helpful diagnostics for common failure modes
        err_text = str(e)
        tb = traceback.format_exc()

        suggestion_lines = [
            "LLM error while calling Ollama:",
            f"  {err_text}",
            "",
            "Possible causes and fixes:",
            "- The MODEL configured may not be available to Ollama or the API endpoint.",
            "  Check core/config.py or your environment/.env for MODEL and ensure Ollama has that model pulled.",
            "  Example to pull a model for Ollama: `ollama pull qwen2.5:3b`",
            "- Ollama daemon may not be running locally. Start it according to your Ollama installation instructions.",
            "- If you intended to use a cloud provider (OpenAI), set up the appropriate client and MODEL that the cloud supports.",
            "- If the error mentions a model not accessible on /chat/completions (e.g., 'mai-code-1-flash'), that model may not be available on the chat endpoint or requires account access.",
            "",
            "To continue quickly, either:",
            "- Set MODEL in core/config.py to a local model you have (default: qwen2.5:3b), or",
            "- Install and run Ollama and pull the desired model, or",
            "- Configure the repo to use a supported cloud model and credentials.",
            "",
            "Full traceback (for debugging):",
            tb,
        ]

        return "\n".join(suggestion_lines)
