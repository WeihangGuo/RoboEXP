# If cuda 12.1
pip install torch==2.5.1+cu121 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install open_clip_torch
pip install --upgrade openai
pip install opencv-python
pip install transforms3d
pip install open3d
# Install SegmentAnything and GroundingDINO
pip install git+https://github.com/IDEA-Research/Grounded-Segment-Anything.git#subdirectory=segment_anything 
pip install git+https://github.com/IDEA-Research/GroundingDINO.git
pip install graphviz

# Install the xarm python sdk
pip install git+https://github.com/xArm-Developer/xArm-Python-SDK.git

# Install the realsense2
pip install pyrealsense2
