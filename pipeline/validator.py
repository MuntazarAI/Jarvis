import subprocess


class EngineeringValidatorStage:
    """
    Validates the execution results.

    This stage checks whether the engineering process
    completed successfully.
    """

    def validate(self, context):

        print("[Validator] Validating engineering results...")

        context.validation = {
            "steps": len(context.history),
            "successful_steps": 0,
            "failed_steps": 0,
            "syntax_ok": True,
            "tests_ok": True,
        }

        for item in context.history:

            if item.get("success"):
                context.validation["successful_steps"] += 1
            else:
                context.validation["failed_steps"] += 1

        #
        # Optional syntax validation
        #

        try:

            subprocess.run(
                [
                    "python",
                    "-m",
                    "compileall",
                    ".",
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )

        except subprocess.CalledProcessError:

            context.validation["syntax_ok"] = False

        context.success = (
            context.validation["failed_steps"] == 0
            and context.validation["syntax_ok"]
        )

        return context


engineering_validator_stage = EngineeringValidatorStage()