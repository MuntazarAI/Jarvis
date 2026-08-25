from jarvis.core.statemachine.machine import StateMachine

def test_state_machine():
    sm = StateMachine("start")
    sm.add_state("end")
    sm.add_transition("start", "end", "go")
    sm.trigger("go")
    assert sm.get_current_state() == "end"
