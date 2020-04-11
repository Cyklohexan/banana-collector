import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"

        self.layer_1 = nn.Linear(state_size, 32)
        self.layer_2 = nn.Linear(32, 64)
        self.layer_3 = nn.Linear(64, 128)
        self.activ_1 = nn.ReLU()
        self.layer_out = nn.Linear(128, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = self.layer_1(state)
        x = self.activ_1(x)
        x = self.layer_2(x)
        x = self.activ_1(x)
        x = self.layer_3(x)
        x = self.activ_1(x)
        out = self.layer_out(x)

        return out
