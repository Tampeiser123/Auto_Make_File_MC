import subprocess
from subprocess import PIPE
import signal
import time
import os


def run_mc():
    p = subprocess.Popen(['gnome-terminal'], start_new_session=True)

    time.sleep(1)

    p.communicate(subprocess.run(['xdotool', 'type', 'mc']))
    p.communicate(subprocess.run(['xdotool', 'key', 'Return']))
    p.communicate(subprocess.run(['xdotool', 'type', 'echo 123 >> m.txt']))
    p.communicate(subprocess.run(['xdotool', 'key', 'Return']))

run_mc()