# Autonomous Driving Simulation with CARLA and RL

Train a self-driving car in the CARLA simulator using Proximal Policy Optimization (PPO).

## Project Goal and Tools Used

### **Goal:**
Develop an RL-based autonomous driving agent in the CARLA simulator to navigate urban environments safely and efficiently.

### **Tools Used:**
- **CARLA Simulator (0.9.14)** for realistic driving environments
- **Python** for scripting and machine learning
- **Stable-Baselines3** for reinforcement learning algorithms
- **TensorFlow/PyTorch** for deep learning
- **OpenAI Gym Interface** for CARLA environment
- **OBS Studio / ScreenRec** for recording the demo video

## Setup Instructions

### **1. Install CARLA**
Download [CARLA 0.9.14](https://github.com/carla-simulator/carla/releases) and extract it into the `carla/` folder.

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
# Install CARLA Python API (adjust path/version):
pip install carla/carla-0.9.14-py3.7-linux-x86_64.egg
```

## How to Run the Code

### **1. Start the CARLA Simulator**
```bash
./carla/CarlaUE4.sh -quality-level=Low -windowed -ResX=800 -ResY=600
```

### **2. Train the RL Model**
```bash
python src/train.py
```

### **3. Monitor Training Progress**
```bash
tensorboard --logdir logs/
```

## Project Structure
```
Self-Driving-CARLA-RL/
├── carla/                   # CARLA simulator files (downloaded separately)
├── src/
│   ├── carla_env.py         # Custom Gym environment (CARLA connection logic)
│   ├── train.py             # Training script (PPO/RL)
│   ├── utils/
│   │   ├── sensors.py       # Camera/LiDAR sensor setup
│   │   └── rewards.py       # Reward function calculations
│   └── config.py            # Hyperparameters and paths
├── models/                  # Saved RL models
├── logs/                    # TensorBoard logs
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Where to Use CARLA Connection

- **Primary File**: `src/carla_env.py` manages the connection to the CARLA server via `carla.Client()`.
- **Sensors**: `utils/sensors.py` uses CARLA’s API to spawn and monitor sensors.
- **Training**: `src/train.py` initializes the RL environment, which connects to CARLA.

## Key Challenges and Solutions

### **CARLA Connection Issues:**
- Ensure the simulator is running before executing scripts.
- Use `client.set_timeout(10.0)` to handle delays.

### **Low FPS:**
- Reduce rendering quality (`-quality-level=Low`).
- Disable shadows and post-processing effects in CARLA settings.

### **RL Training Instability:**
- Simplify the reward function.
- Start with a small map (e.g., `Town01`) and short episodes.

## Record a Demo Video
- Use **OBS Studio** or **ScreenRec** to capture the simulation.
- Showcase the car’s behavior before/after training.

## Prepare a Report/Presentation
### **Topics to Cover:**
1. **Problem Statement:** Why autonomous driving simulation?
2. **Methodology:** RL algorithm, reward design, neural network structure.
3. **Results:** Training curves, performance metrics (e.g., collision rate, episode length).
4. **Challenges:** Hardware limitations, CARLA setup quirks, RL stability.

## Advanced Enhancements

### **Future Improvements:**
- **Object Detection:** Integrate **YOLO** to detect pedestrians/vehicles.
- **Multi-Agent Training:** Simulate traffic with multiple autonomous vehicles.
- **Imitation Learning:** Use CARLA’s autopilot data to pretrain the model.
- **Deploy on Raspberry Pi:** Export the trained model to **TensorFlow Lite** for edge inference.

## Key Resources
- **CARLA Documentation:** [https://carla.readthedocs.io](https://carla.readthedocs.io)
- **Stable Baselines3 Tutorial:** [https://stable-baselines3.readthedocs.io](https://stable-baselines3.readthedocs.io)
- **Example Projects:**
  - CARLA + RLlib
  - End-to-End Lane Following

## Common Pitfalls & Fixes

### **1. CARLA Simulator Issues:**
- Ensure the correct version is installed (`0.9.14`).
- Use `./CarlaUE4.sh -opengl` for better Linux compatibility.

### **2. Training Convergence Problems:**
- Check for **reward function anomalies**.
- Train with fewer sensors initially to stabilize learning.

---
This README serves as a complete guide to setting up, running, and improving the autonomous driving project in CARLA using RL.

