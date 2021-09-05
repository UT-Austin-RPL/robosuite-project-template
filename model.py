import numpy as np

class NaiveModel(object):
    def __init__(self, dof):
        self.dof = dof

    def __call__(self, obs=None):
        return np.random.randn(self.dof)