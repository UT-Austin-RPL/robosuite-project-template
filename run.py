import numpy as np

import robosuite
from env import NewLift
from model import NaiveModel

# initialize environment
robots = "Panda"
env = robosuite.make(
    'NewLift',
    robots,
    has_renderer=True,
    has_offscreen_renderer=False,
    use_camera_obs=False,
    control_freq=20,
)

# initailiza model (random model here)
model = NaiveModel(env.robots[0].dof)

# reset the environment
env.reset()
obs = None

for i in range(1000):
    action = model(obs) # sample random action
    obs, reward, done, info = env.step(action)  # take action in the environment
    env.render()  # render on display