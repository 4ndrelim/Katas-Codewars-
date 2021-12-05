# Description #
# The outcome of this exercise will be to return the correct state of the TCP FSM based on the array of events given.
# The input will be an array of events. Your job is to traverse the FSM as determined by the events, and return the proper state as a string, all caps.

# If an event is not applicable to the current state, your code will return "ERROR".
# Action of each event upon each state: (the format is INITIAL_STATE: EVENT -> NEW_STATE)


knowledge ={"CLOSED":       {"APP_PASSIVE_OPEN": "LISTEN", "APP_ACTIVE_OPEN": "SYN_SENT"},
            "LISTEN":       {"RCV_SYN": "SYN_RCVD", "APP_SEND": "SYN_SENT", "APP_CLOSE": "CLOSED"},
            "SYN_RCVD":     {"APP_CLOSE": "FIN_WAIT_1", "RCV_ACK": "ESTABLISHED"},
            "SYN_SENT":     {"RCV_SYN": "SYN_RCVD", "RCV_SYN_ACK": "ESTABLISHED", "APP_CLOSE": "CLOSED"},
            "ESTABLISHED":  {"APP_CLOSE": "FIN_WAIT_1", "RCV_FIN": "CLOSE_WAIT"},
            "FIN_WAIT_1":   {"RCV_FIN": "CLOSING", "RCV_FIN_ACK": "TIME_WAIT", "RCV_ACK": "FIN_WAIT_2"},
            "CLOSING":      {"RCV_ACK": "TIME_WAIT"},
            "FIN_WAIT_2":   {"RCV_FIN": "TIME_WAIT"},
            "TIME_WAIT":    {"APP_TIMEOUT": "CLOSED"},
            "CLOSE_WAIT":   {"APP_CLOSE": "LAST_ACK"},
            "LAST_ACK":     {"RCV_ACK": "CLOSED"}}
def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    while events:
        try: 
          state = knowledge[state][events.pop(0)]
        except KeyError: 
          return "ERROR"
    return state
