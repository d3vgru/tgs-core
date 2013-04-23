import logging
logger = logging.getLogger(__name__)

class State(object):
    def __init__(self, previous_state):
        logging.debug("state %s -> %s", previous_state, self)

class DummyState(State):
    def __init__(self):
        pass

class UnknownState(State):
    pass

class SquareState(State):
    pass

class TaskGroupState(State):
    pass
