from brain.brain import brain
from execution.multiexecutor import multiexecutor
from intelligence.reflection import reflection
from brain.formatter import format_tool_result
from brain.validator import validator
from brain.router import router


class Agent:

    def run(self, user_input):

        # ----------------------------
        # Router first
        # ----------------------------

        plans = router.route(user_input)

        # ----------------------------
        # Otherwise ask the Brain
        # ----------------------------

        if plans is None:
            plans = brain.think(user_input)

        # ----------------------------
        # Always work with a list
        # ----------------------------

        if not isinstance(plans, list):
            plans = [plans]

        # ----------------------------
        # Validate every step
        # ----------------------------

        for plan in plans:

            valid, error = validator.validate(plan)

            if not valid:
                return {
                    "plan": plans,
                    "result": error,
                    "formatted_result": error,
                    "answer": error,
                }

        # ----------------------------
        # Execute
        # ----------------------------

        result = multiexecutor.execute(plans)

        # ----------------------------
        # Reflection
        # ----------------------------

        answer = reflection.reply(user_input, result)

        return {
            "plan": plans,
            "result": result,
            "formatted_result": format_tool_result(result),
            "answer": answer,
        }


agent = Agent()