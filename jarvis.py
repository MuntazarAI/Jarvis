from brain.agent import agent

# Register every tool
import tools


def main():

    print("=" * 60)
    print("Jarvis AI")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        user = input("\nYou: ").strip()

        if user.lower() in ("exit", "quit"):
            print("\nJarvis: Goodbye!")
            break

        response = agent.run(user)

        print("\nPLAN")
        print(response["plan"])

        print("\nRESULT")
        print(response["formatted_result"])

        print("\nJarvis:")
        print(response["answer"])


if __name__ == "__main__":
    main()