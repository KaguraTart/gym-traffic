#import os
#os.environ["THEANO_FLAGS"] = "mode=FAST_COMPILE,device=cpu,floatX=float32"


import gym
import gym_traffic
from gym_traffic.agents import DQN
from gym_traffic.runners import SimpleRunner
import gym
from gym.wrappers import Monitor

def test(env, agent, path, runner, nb_episodes = 10, video_callable=None, force=True):
    monitor = Monitor(path, video_callable=video_callable, force=True)(env)
    rewards = runner.run(monitor, agent, nb_episodes=nb_episodes, render=False, train=False)
    monitor.close()

seed = 123
#Create model
train_env = gym.make('Traffic-Simple-cli-v0')
agent = DQN(train_env.observation_space, train_env.action_space)
print "Q"
agent.Q.summary()
print "training_model"
agent.training_model.summary()
runner = SimpleRunner()

nb_epoch = 100
nb_episodes = 1000
for epoch in range(nb_epoch):
    print("Epoch: {}".format(epoch))
    test_env = gym.make('Traffic-Simple-gui-v0')
    path = "output/simple/epoch-{:03d}".format(epoch)
    test(test_env, agent, path, runner)
    runner.run(train_env, agent, nb_episodes=nb_episodes, render=False, train=True)
    agent.save("{}.h5".format(path))
