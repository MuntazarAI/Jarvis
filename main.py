from core.logger import info, success, error
from core.config import USERNAME, ASSISTANT_NAME
from core.chat import ask
from core.speech import speak

from core.planner import planner
from core.commands import execute


def startup():
    print("=" * 45)
    print(f"          {ASSISTANT_NAME.upper()} AI")
    print("=" * 45)

    info("Loading configuration...")
    success("Configuration loaded.")

    greeting = f"Hello, {USERNAME}. Systems online."

    print()
    print(f"{ASSISTANT_NAME}:")
    print(greeting)
    print()

    try:
        speak(greeting)
    except Exception as e:
        error(f"Speech error: {e}")


def main():

    startup()

    while True:

        try:

            prompt = input(f"{USERNAME}: ").strip()

            if not prompt:
                continue

            if prompt.lower() in ("exit", "quit"):

                goodbye = "Goodbye."

                print(f"\n{ASSISTANT_NAME}:")
                print(goodbye)

                try:
                    speak(goodbye)
                except Exception as e:
                    error(e)

                break

            # ------------------------
            # Planner
            # ------------------------

            plan = planner.create_plan(prompt)

            # ------------------------
            # Execute commands
            # ------------------------

            result = execute(plan)

            if result is not None:

                print()
                print(f"{ASSISTANT_NAME}:")
                print(result)
                print()

                try:
                    speak(result)
                except Exception as e:
                    error(e)

                continue

            # ------------------------
            # Chat with Ollama
            # ------------------------

            reply = ask(prompt)

            print()
            print(f"{ASSISTANT_NAME}:")
            print(reply)
            print()

            try:
                speak(reply)
            except Exception as e:
                error(e)

        except KeyboardInterrupt:
            print("\nExiting...")
            break

        except Exception as e:
            error(e)


if __name__ == "__main__":
    main()
