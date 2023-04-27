import os
from pathlib import Path

dir = Path(__file__).resolve().parent
json_path = os.path.join(dir, 'requirements.txt')
print(json_path)