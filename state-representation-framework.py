class State:
    """Represents a single state in the state-space."""
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.transitions = {}

    def add_transition(self, action, next_state):
        """Add a transition to another state."""
        self.transitions[action] = next_state

    def get_next_state(self, action):
        """Get the next state for a given action."""
        return self.transitions.get(action, None)

    def __str__(self):
        return f"State({self.name}): {self.description}"


class StateSpace:
    """Represents the entire state-space."""
    def __init__(self):
        self.states = {}

    def add_state(self, state):
        """Add a state to the state-space."""
        self.states[state.name] = state

    def get_state(self, name):
        """Retrieve a state by its name."""
        return self.states.get(name, None)

    def display(self):
        """Display the state-space with transitions."""
        for state in self.states.values():
            print(f"{state.name} -> {[f'{action} -> {next_state}' for action, next_state in state.transitions.items()]}")

    def simulate(self, start_state_name, actions):
        """Simulate a sequence of actions in the state-space."""
        current_state = self.get_state(start_state_name)
        if not current_state:
            print("Start state not found!")
            return

        print(f"Starting at: {current_state.name}")
        for action in actions:
            next_state_name = current_state.get_next_state(action)
            if not next_state_name:
                print(f"Action '{action}' is invalid from state '{current_state.name}'")
                break
            current_state = self.get_state(next_state_name)
            print(f"Action '{action}' -> Moved to: {current_state.name}")
        print(f"Final State: {current_state.name}")


# Example Usage
if __name__ == "__main__":
    # Define states
    idle = State("Idle", "The system is idle")
    processing = State("Processing", "The system is processing data")
    waiting = State("Waiting", "The system is waiting for input")
    finished = State("Finished", "The system has completed processing")

    # Define transitions
    idle.add_transition("start", "Processing")
    processing.add_transition("wait", "Waiting")
    processing.add_transition("finish", "Finished")
    waiting.add_transition("input", "Processing")
    finished.add_transition("reset", "Idle")

    # Build state-space
    state_space = StateSpace()
    for state in [idle, processing, waiting, finished]:
        state_space.add_state(state)

    # Display state-space
    print("State-Space Representation:")
    state_space.display()

    # Simulate state transitions
    print("\nSimulation:")
    actions = ["start", "wait", "input", "finish", "reset"]
    state_space.simulate("Idle", actions)
