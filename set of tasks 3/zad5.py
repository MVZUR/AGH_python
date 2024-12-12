class State:
    """
    Represents a single state in the state machine.
    """
    def __init__(self, name, output=None):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        """Adds a transition to another state based on input_symbol."""
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        """Gets the next state based on the input_symbol."""
        return self.transitions.get(input_symbol)

    def get_output(self):
        """Gets the output associated with the current state (Moore machine)."""
        return self.output

class StateMachine:
    """
    Represents a state machine (Mealy or Moore).
    """
    def __init__(self, initial_state):
        self.current_state = initial_state

    def process_input(self, input_symbol):
        """
        Processes an input symbol and transitions to the next state.
        """
        next_state = self.current_state.get_next_state(input_symbol)
        if next_state is None:
            raise ValueError(f"No transition defined for input '{input_symbol}' in state '{self.current_state.name}'.")

        self.current_state = next_state

    def get_current_state(self):
        """Returns the name of the current state."""
        return self.current_state.name

    def get_current_output(self):
        """Returns the output of the current state (for Moore machines)."""
        return self.current_state.get_output()

# implementacja
def main():
    # definicja stanów
    state_a = State("A", output="Output_A")
    state_b = State("B", output="Output_B")
    state_c = State("C", output="Output_C")

    # dodanie przejść
    state_a.add_transition("0", state_b)
    state_a.add_transition("1", state_c)
    state_b.add_transition("0", state_a)
    state_b.add_transition("1", state_c)
    state_c.add_transition("0", state_c)
    state_c.add_transition("1", state_a)

    # Inicjalizacja ze stanem początkowym
    sm = StateMachine(initial_state=state_a)

    # Przykład użycia
    input_sequence = "011001"

    print(f"Initial State: {sm.get_current_state()}, Output: {sm.get_current_output()}")

    for symbol in input_sequence:
        sm.process_input(symbol)
        print(f"After input '{symbol}': State: {sm.get_current_state()}, Output: {sm.get_current_output()}")

if __name__ == "__main__":
    main()
