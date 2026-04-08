import pygame
from src.config import WHITE, FONT_PATH

class GUIManager:
    def __init__(self, screen):
        self.screen = screen
        # Load font từ thư mục assets/fonts bạn đã tạo
        try:
            self.font_main = pygame.font.Font(FONT_PATH, 45)
            self.font_small = pygame.font.Font(FONT_PATH, 25)
        except:
            # Nếu file font.ttf bị lỗi, sẽ dùng font mặc định của hệ thống
            print("Cảnh báo: Không tìm thấy file font.ttf, dùng font mặc định.")
            self.font_main = pygame.font.SysFont("Arial", 45, bold=True)
            self.font_small = pygame.font.SysFont("Arial", 25)

    def draw_text(self, text, x, y, color=WHITE, center=False):
        """Hàm vẽ chữ lên màn hình"""
        text_surface = self.font_main.render(text, True, color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_balance(self, balance):
        """Hiển thị số dư tiền ở góc màn hình"""
        text = f"Số dư: {balance:,} VNĐ"
        # Vẽ chữ màu xanh lá cho tiền
        text_surface = self.font_small.render(text, True, (0, 255, 0))
        self.screen.blit(text_surface, (30, 30))