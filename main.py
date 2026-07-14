from core.logger import info, success, error
from core.config import USERNAME, ASSISTANT_NAME
from core.chat import ask


def startup():
    print("=" * 45)
    print(f"          {ASSISTANT_NAME.upper()} AI")
    print("=" * 45)

    info("Loading configuration...")
    success("Configuration loaded.")

    print()
    print(f"{ASSISTANT_NAME}:")
    print(f"Hello, {USERNAME}.")
    print("Systems online.\n")


def main():
    startup()

    while True:
        prompt = input(f"{USERNAME}: ")

        if prompt.lower() in ["exit", "quit"]:
            print(f"\n{ASSISTANT_NAME}: Goodbye.")
            break

        try:
            reply = ask(prompt)

            print()
            print(f"{ASSISTANT_NAME}:")
            print(reply)
            print()

        except Exception as e:
            error(e)


if __name__ == "__main__":
    main()
    