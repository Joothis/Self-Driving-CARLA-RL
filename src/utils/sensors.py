import carla
import cv2
import numpy as np

class CameraSensor:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.world = vehicle.get_world()
        self.frame = None
        
        # Setup RGB camera
        camera_bp = self.world.get_blueprint_library().find('sensor.camera.rgb')
        camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
        self.sensor = self.world.spawn_actor(
            camera_bp, 
            camera_transform, 
            attach_to=self.vehicle
        )
        self.sensor.listen(self._process_image)
    
    def _process_image(self, image):
        # Convert raw CARLA image to RGB array
        array = np.frombuffer(image.raw_data, dtype=np.uint8)
        array = np.reshape(array, (image.height, image.width, 4))
        array = array[:, :, :3]  # Remove alpha channel
        array = cv2.resize(array, (84, 84))  # Resize for RL input
        self.frame = array

    def get_frame(self):
        return self.frame

    def destroy(self):
        self.sensor.destroy()