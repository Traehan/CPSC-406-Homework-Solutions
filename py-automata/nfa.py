# a class for NFAs
# modify as needed
class NFA :

    # init the NFA
    def __init__(self, Q, Sigma, delta, q0, F) : 
        self.Q = Q # set of states
        self.Sigma = Sigma # set of symbols
        self.delta = delta # non-deterministic transition function
        self.q0 = q0 # initial state
        self.F = F # final states
   
   # print the data of the NFA
    def __repr__(self) :
        return f"NFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

    # run the NFA on the word w
    # return if the word is accepted or not
    # modify as needed
    def run(self, w):
        current_states = {self.q0}
        for symbol in w:
            next_states = set()
            for state in current_states:
                next_states.update(self.delta.get((state, symbol), []))
            current_states = next_states
        return any(state in self.F for state in current_states)