from stable_baselines3 import PPO
from carla_env import CarlaEnv
from config import MODEL_PARAMS  # Hyperparameters

def train():
    env = CarlaEnv()
    model = PPO(
        "CnnPolicy", 
        env, 
        verbose=1, 
        tensorboard_log="./logs/",
        **MODEL_PARAMS
    )
    model.learn(total_timesteps=100000)
    model.save("models/carla_ppo_final")
    env.close()

if __name__ == "__main__":
    train()