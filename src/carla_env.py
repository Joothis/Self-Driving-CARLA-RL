import gym
import carla
import numpy as np
from gym import spaces
from utils.sensors import CameraSensor
from utils.rewards import RewardCalculator
from config import ENV_PARAMS  # Import hyperparameters

class CarlaEnv(gym.Env):
    def __init__(self):
        super(CarlaEnv, self).__init__()
        
        # Connect to CARLA server
        self.client = carla.Client('localhost', 2000)
        self.client.set_timeout(10.0)
        self.world = self.client.get_world()
        
        # Define action/observation spaces
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2,))  # Throttle, Steering
        self.observation_space = spaces.Box(low=0, high=255, shape=(84, 84, 3), dtype=np.uint8)
        
        # Initialize vehicle, sensors, and reward calculator
        self.vehicle = None
        self.camera_sensor = None
        self.reward_calculator = None
        self._spawn_vehicle()

    def _spawn_vehicle(self):
        # Cleanup existing actors
        if self.vehicle:
            self.vehicle.destroy()
        if self.camera_sensor:
            self.camera_sensor.destroy()
        
        # Spawn new vehicle
        blueprint = self.world.get_blueprint_library().filter('model3')[0]
        spawn_point = self.world.get_map().get_spawn_points()[0]
        self.vehicle = self.world.spawn_actor(blueprint, spawn_point)
        self.vehicle.set_autopilot(False)
        
        # Initialize sensors and reward calculator
        self.camera_sensor = CameraSensor(self.vehicle)
        self.reward_calculator = RewardCalculator(self.vehicle, self.world, ENV_PARAMS)

    def reset(self):
        self._spawn_vehicle()
        obs = self.camera_sensor.get_frame()
        return obs

    def step(self, action):
        throttle = np.clip(action[0], -1.0, 1.0)
        steer = np.clip(action[1], -1.0, 1.0)
        
        # Apply control
        control = carla.VehicleControl(throttle=throttle, steer=steer)
        self.vehicle.apply_control(control)
        
        # Get observation and calculate reward
        obs = self.camera_sensor.get_frame()
        reward = self.reward_calculator.calculate_reward()
        done = self._check_termination()
        
        return obs, reward, done, {}

    def _check_termination(self):
        # Terminate episode on collision or timeout
        collision_history = self.vehicle.get_collision_history()
        return len(collision_history) > 0

    def close(self):
        if self.vehicle:
            self.vehicle.destroy()
        if self.camera_sensor:
            self.camera_sensor.destroy()