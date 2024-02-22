class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol, None)


class PluralFiniteStateMachine:
    def __init__(self):
        self.start_state = State("start")
        self.end_state = State("end")

        # Define transitions
        self.start_state.add_transition('noun', self.end_state)

        self.end_state.add_transition('s', self.end_state)
        self.end_state.add_transition('es', self.end_state)

        # Current state
        self.current_state = self.start_state

    def reset(self):
        self.current_state = self.start_state

    def pluralize_noun(self, noun):
        for letter in noun[::-1]:
            next_state = self.current_state.get_next_state(letter)
            if next_state:
                self.current_state = next_state
            else:
                return noun + 's'  # default plural form if no rule matches
        return noun


# Example usage:
if __name__ == "__main__":
    fsm = PluralFiniteStateMachine()

    # Test cases
    nouns = ['cat', 'dog', 'church', 'watch', 'bus', 'box']

    for noun in nouns:
        fsm.reset()
        plural_form = fsm.pluralize_noun(noun)
        print(f"The plural form of '{noun}' is '{plural_form}'")
