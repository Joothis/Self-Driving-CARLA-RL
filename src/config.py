# Reinforcement Learning Hyperparameters
MODEL_PARAMS = {
    "learning_rate": 3e-4,
    "gamma": 0.99,            # Discount factor
    "gae_lambda": 0.95,       # For Generalized Advantage Estimation
    "ent_coef": 0.01,         # Entropy coefficient (encourage exploration)
    "vf_coef": 0.5,           # Value function loss coefficient
    "batch_size": 64,
    "n_steps": 2048,          # Steps per environment update
}

# Environment Settings
ENV_PARAMS = {
    "max_speed": 30.0,        # Maximum allowed speed (m/s)
    "target_speed": 20.0,     # Ideal speed for reward calculation
    "collision_penalty": -50, # Penalty for collisions
    "lane_deviation_penalty": -0.1,  # Penalty per meter from lane center
}

# Paths
PATHS = {
    "model_save": "models/",
    "tensorboard_log": "logs/",
}