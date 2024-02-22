class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol, None)


class FiniteAutomaton:
    def __init__(self):
        self.start_state = State("start")
        self.end_state = State("end")

        # Define transitions
        self.start_state.add_transition('a', self.end_state)
        self.end_state.add_transition('b', self.end_state)

        # Current state
        self.current_state = self.start_state

    def reset(self):
        self.current_state = self.start_state

    def process_input(self, input_string):
        for symbol in input_string:
            next_state = self.current_state.get_next_state(symbol)
            if next_state:
                self.current_state = next_state
            else:
                return False

        return self.current_state == self.end_state


# Example usage:
if __name__ == "__main__":
    automaton = FiniteAutomaton()

    # Test cases
    test_strings = ['ab', 'aab', 'abb', 'abc', 'ba', 'abab']

    for test_string in test_strings:
        automaton.reset()
        result = automaton.process_input(test_string)
        print(f"String '{test_string}' ends with 'ab': {result}")
