import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from bugme import controller

if __name__ == "__main__":
    c = controller.Controller()
    c.run()