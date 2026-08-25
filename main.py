from core.logger import info, success, error
from core.config import USERNAME, ASSISTANT_NAME
from core.agent import agent
from core.speech import speak
from core.voice import voice

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
        error(e)


def get_input():
    """
    Lets the user choose between typing or speaking.
    """

    mode = input("\n(T)ype or (V)oice? ").strip().lower()

    if mode == "v":
        return voice.listen()

    return input(f"{USERNAME}: ").strip()


def main():

    startup()

    while True:

        try:

            prompt = get_input()

            if not prompt:
                continue

            if prompt.lower() in ("exit", "quit"):

                goodbye = "Goodbye."

                print(f"\n{ASSISTANT_NAME}:")
                print(goodbye)

                speak(goodbye)
                break

            plan = planner.create_plan(prompt)

            result = execute(plan)

            if result is not None:

                print()
                print(f"{ASSISTANT_NAME}:")
                print(result)
                print()

                speak(result)
                continue

            reply = agent.handle(prompt)

            print()
            print(f"{ASSISTANT_NAME}:")
            print(reply)
            print()

            speak(reply)

        except KeyboardInterrupt:
            print("\nExiting...")
            break

        except Exception as e:
            error(e)


if __name__ == "__main__":
    main()