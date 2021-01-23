"""
run a Monte-Carlo Markov-Chain (MCMC) simulation for planes.

recap on the essentials of MCMC (maybe using the supermarket and plane crash examples)

* our model contains a Markov Chain: defined states S0..S2 and transition probs P
* randomly sample steps:
  1. create an agent in initial state (plane, customer or random choice, x/y)
  2. randomly perform a move (choose the next state with P|S, go left/right/up/down/fire)
  3. store the current state somewhere
  4. have a stop condition
* repeat the above step N times
* store the results (CSV? JSON?)
"""
from random import choices

STATES = ['airport', 'air', 'crashed']

def mcmc(state, transition_probs):
    """runs a Monte-Carlo Markov-Chain simulation of a plane. Returns a list of states passed."""
    history = [state]
    while state != 'crashed':
        probs = transition_probs[state]
        state = choices(STATES, probs)[0]
        history.append(state)
    return history

P = {
    #          airport  air      crashed
    'airport': [0.4,    0.6    , 0.0    ],
    'air':     [0.8,    0.19999, 0.00001],
    # crashed   0       0        1.0
}

result = mcmc(state='airport', P)
print(f"crashed after {len(result)} days of service")
