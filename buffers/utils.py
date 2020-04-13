from collections import deque


class Experience(object):
    """
    Contains all information contained in an Experience
    """
    def __init__(self, state, action, reward, next_state, done, priority=2.0):
        self.state = state
        self.action = action
        self.reward = reward
        self.next_state = next_state
        self.done = done
        self.priority = priority

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)


class ExperienceDeque(deque):
    """
    Container for processing, sorting Experience objects
    """

    def sort(self, *args, **kwargs):
        items = [self.pop() for x in range(len(self))]
        items.sort(*args, **kwargs)
        self.extend(items)