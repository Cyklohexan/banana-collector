# Project Details

## The Environment

For this project, you will train an agent to navigate (and collect bananas!) in a large, square world.

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

## State space

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions.

## Action space

Four discrete actions are available, corresponding to:

* ```0``` - move forward,
* ```1``` - move backward,
* ```2``` - turn left,
* ```3``` - turn right.

# Getting Started

## Setting up Dependencies

In this project we use ```virtualenv``` package in python to set up virtual environment. To create this environment we can use the command:

```
python3 -m virtualenv <env_name> --python=python3
```

Activating this environment to install dependencies and using it can we do by command:

```
source <env_name>/bin/activate
```

Now all we need to do is install required dependencies with:

```
pip install -r requirements.txt
```

## Download the Unity Environment

For this project, you will **not** need to install Unity - this is because we have already built the environment for you, and you can download it from one of the links below. You need only select the environment that matches your operating system:

* Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
* Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
* Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
* Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

Then, place the file in root folder in this repository, and unzip (or decompress) the file.

# Instructions

## Jupyter Notebook



## Command Line

