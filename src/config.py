import pygame

# Cấu hình màn hình
WIDTH = 1280
HEIGHT = 720

# Màu sắc (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Đường dẫn tài nguyên (Path)
ASSETS_PATH = "assets/images/"
DICE_PATH = "assets/images/dice/"
FONT_PATH = "assets/fonts/font.ttf"

# Cài đặt Game
INITIAL_BALANCE = 1000000  # Vốn 1 triệu
DEFAULT_BET = 50000        # Cược mỗi ván 50k
FPS = 60                   # Tốc độ khung hình

# Thêm vào src/config.py
SOUND_PATH = "assets/sounds/"
SHAKER_IMAGE = "assets/images/shaker.png"

# Thời gian lắc (giây)
ROLL_DURATION = 2000 # 2000 miligiây = 2 giây

# Thêm vào src/config.py
BET_OPTIONS = [10000, 50000, 100000, 500000]
# Màu sắc cho nút chọn tiền
GRAY = (100, 100, 100)
ORANGE = (255, 165, 0)