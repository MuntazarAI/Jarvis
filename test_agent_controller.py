from agent.controller import agent_controller

def main():
    print("=" * 80)
    print("TESTING AGENT CONTROLLER")
    print("=" * 80)

    try:
        state = agent_controller.run("Fix every NameError")

        print()
        print("=" * 80)
        print("FINAL STATE")
        print("=" * 80)

        print(state.summary())

        print()
        print("SUCCESS")

    except Exception as e:
        print()
        print("=" * 80)
        print("FAILED")
        print("=" * 80)

        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()