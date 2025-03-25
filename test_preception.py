from roboexp import (
    # RobotExplorationReal,
    # RoboMemory,
    RoboPercept,
    # RoboActReal,
    # RoboDecision,
    RS_D455,
)
from datetime import datetime
import os
import time

camera = RS_D455("234222303793", frame_rate=15)

object_level_labels = [
    "table",
    "refrigerator",
    "cabinet",
    "can",
    "doll",
    "plate",
    "spoon",
    "fork",
    "hamburger",
    "condiment",
    "box", 
]
part_level_labels = ["handle"]

grounding_dict = (
    " . ".join(object_level_labels) + " . " + " . ".join(part_level_labels)
)
# Initialize the perception module
robo_percept = RoboPercept(grounding_dict=grounding_dict, lazy_loading=False)

import matplotlib.pyplot as plt

while True:
    start = time.time()
    points, colors, depths, mask = camera.get_observations()
    observations = {
        "wrist": {
            "position": points,
            "rgb": colors,
            "depths": depths,
            "mask": mask,
        }
    }
    obs = robo_percept.get_attributes_from_observations(observations, visualize=True)
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")