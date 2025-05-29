import subprocess
import sys
import os

def get_resource_path(relative_path):
    """Get path for bundled file inside the .exe."""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

video_path = get_resource_path("gaster.mp4")

def play_video():
    command = ["ffplay", "-fs", "-autoexit", video_path]
    subprocess.run(command)

play_video()
