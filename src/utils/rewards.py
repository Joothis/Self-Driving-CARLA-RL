import carla
import numpy as np

class RewardCalculator:
    def __init__(self, vehicle, world, params):
        self.vehicle = vehicle
        self.world = world
        self.params = params
        self.prev_distance = 0.0
        self.lane_width = 3.5  # Approximate lane width in meters

    def calculate_reward(self):
        """
        Computes the total reward based on:
        - Speed maintenance
        - Lane deviation
        - Collisions
        - Progress toward a goal
        """
        speed_reward = self._speed_reward()
        lane_reward = self._lane_deviation_reward()
        collision_penalty = self._collision_penalty()
        progress_reward = self._progress_reward()

        total_reward = (
            speed_reward +
            lane_reward +
            collision_penalty +
            progress_reward
        )

        return total_reward

    def _speed_reward(self):
        """Reward for maintaining target speed."""
        speed = self._get_speed()
        return -np.abs(speed - self.params["target_speed"]) / 10.0

    def _lane_deviation_reward(self):
        """Penalty for deviating from lane center."""
        waypoint = self.world.get_map().get_waypoint(self.vehicle.get_location())
        vehicle_transform = self.vehicle.get_transform()
        lane_center = waypoint.transform.location
        
        # Calculate lateral deviation
        deviation = vehicle_transform.location.distance(lane_center)
        return self.params["lane_deviation_penalty"] * deviation

    def _collision_penalty(self):
        """Check for collisions."""
        collision_history = self.vehicle.get_collision_history()
        if len(collision_history) > 0:
            return self.params["collision_penalty"]
        return 0.0

    def _progress_reward(self):
        """Reward for moving toward a goal (e.g., distance traveled)."""
        current_location = self.vehicle.get_transform().location
        current_distance = current_location.distance(self.goal_location)
        reward = (self.prev_distance - current_distance) * 0.1  # Reward for moving closer
        self.prev_distance = current_distance
        return reward

    def _get_speed(self):
        """Get speed in m/s."""
        velocity = self.vehicle.get_velocity()
        return np.sqrt(velocity.x**2 + velocity.y**2 + velocity.z**2)