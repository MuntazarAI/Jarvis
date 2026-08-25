import argparse
from execution.agent import agent

# Register every tool
import tools

from core.chat import retrieve_relevant_memory


def main(auto_tasks: str | None = None, smart: bool = True):

    def run_task(task: str):
        print("\n" + "-" * 60)
        print("Task:", task)

        if smart:
            memory_text = retrieve_relevant_memory(task)
            print("\nRelevant memories:")
            print(memory_text)

        response = agent.run(task)

        print("\nPLAN")
        print(response.get("plan"))

        print("\nRESULT")
        print(response.get("formatted_result"))

        print("\nJarvis:")
        print(response.get("answer"))

        return response

    if auto_tasks is None:
        print("=" * 60)
        print("Jarvis AI")
        print("Type 'exit' to quit. Use Ctrl+C to stop.")
        print("=" * 60)

        try:
            while True:
                user = input("\nYou: ").strip()

                if user.lower() in ("exit", "quit"):
                    print("\nJarvis: Goodbye!")
                    break

                run_task(user)

        except KeyboardInterrupt:
            print("\nJarvis: Interrupted. Goodbye!")

    else:
        try:
            with open(auto_tasks, encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"Tasks file not found: {auto_tasks}")
            return

        tasks = [line for line in lines if line and not line.startswith("#")]

        print(f"Running {len(tasks)} automated tasks from {auto_tasks} (smart={smart})")

        for task in tasks:
            response = run_task(task)
            answer = response.get("answer", "")
            if isinstance(answer, str) and "failed" in answer.lower():
                print("Retrying failed task once...")
                run_task(task)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jarvis AI - interactive and automated modes")
    parser.add_argument("--tasks", "-t", help="Path to a tasks file (one task per line). If omitted, runs interactively.")
    parser.add_argument("--no-smart", dest="smart", action="store_false", help="Disable retrieval of relevant memories before running tasks.")

    args = parser.parse_args()
    main(auto_tasks=args.tasks, smart=args.smart)
