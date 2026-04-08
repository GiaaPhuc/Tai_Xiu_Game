import pygame
import sys
import random
from src.config import *
from src.dice_logic import roll_three_dice, check_win
from src.gui_manager import GUIManager

def main():
    # 1. Khởi tạo
    pygame.init()
    pygame.mixer.init() # Bắt buộc phải có để chạy âm thanh
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tài Xỉu Casino - Premium Edition")
    clock = pygame.time.Clock()
    gui = GUIManager(screen)

    # 2. Load Assets với xử lý lỗi
    try:
        bg = pygame.image.load(ASSETS_PATH + "background.png").convert()
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

        btn_tai_img = pygame.image.load(ASSETS_PATH + "button_tai.png").convert_alpha()
        btn_xiu_img = pygame.image.load(ASSETS_PATH + "button_xiu.png").convert_alpha()
        rect_tai = btn_tai_img.get_rect(center=(WIDTH * 0.75, HEIGHT * 0.8))
        rect_xiu = btn_xiu_img.get_rect(center=(WIDTH * 0.25, HEIGHT * 0.8))

        shaker_img = pygame.image.load(ASSETS_PATH + "shaker.png").convert_alpha()
        shaker_img = pygame.transform.scale(shaker_img, (350, 300))

        dice_imgs = [pygame.transform.scale(pygame.image.load(f"{DICE_PATH}dice_{i}.png").convert_alpha(), (120, 120)) for i in range(1, 7)]

        # Load Sounds
        snd_roll = pygame.mixer.Sound(SOUND_PATH + "dice_roll.mp3")
        snd_win = pygame.mixer.Sound(SOUND_PATH + "win.mp3")
        snd_lose = pygame.mixer.Sound(SOUND_PATH + "lose.mp3")
    except Exception as e:
        print(f"Lỗi: Thiếu tài nguyên hoặc sai đường dẫn! Chi tiết: {e}")
        pygame.quit()
        sys.exit()

    # 3. Biến trạng thái
    balance = INITIAL_BALANCE
    dices = [1, 2, 3]
    message = "CHỌN TÀI HOẶC XỈU ĐỂ BẮT ĐẦU"
    state = "IDLE" # IDLE, ROLLING, RESULT
    roll_start_time = 0
    player_choice = ""

    # 4. Vòng lặp chính
    while True:
        screen.blit(bg, (0, 0))
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and state != "ROLLING":
                if balance < DEFAULT_BET:
                    message = "BẠN ĐÃ HẾT TIỀN!"
                    continue
                
                if rect_tai.collidepoint(event.pos):
                    player_choice = 'tai'
                elif rect_xiu.collidepoint(event.pos):
                    player_choice = 'xiu'
                else: continue

                # Bắt đầu lắc
                state = "ROLLING"
                roll_start_time = current_time
                snd_roll.play()
                message = "ĐANG LẮC..."

        # 5. Logic trạng thái
        if state == "ROLLING":
            # Xí ngầu nhảy số giả tạo hiệu ứng
            dices = [random.randint(1, 6) for _ in range(3)]
            start_x = WIDTH // 2 - 180
            for i, val in enumerate(dices):
                screen.blit(dice_imgs[val-1], (start_x + i * 130, HEIGHT // 2 - 60))
            
            # Vẽ cái bát (shaker) rung nhẹ
            offset = random.randint(-4, 4)
            screen.blit(shaker_img, (WIDTH//2 - 175 + offset, HEIGHT//2 - 150 + offset))

            if current_time - roll_start_time > ROLL_DURATION:
                state = "RESULT"
                dices = roll_three_dice()
                if check_win(dices, player_choice):
                    balance += DEFAULT_BET
                    message = f"THẮNG! TỔNG: {sum(dices)}"
                    snd_win.play()
                else:
                    balance -= DEFAULT_BET
                    message = f"THUA! TỔNG: {sum(dices)}"
                    snd_lose.play()

        elif state == "RESULT" or state == "IDLE":
            start_x = WIDTH // 2 - 180
            for i, val in enumerate(dices):
                screen.blit(dice_imgs[val-1], (start_x + i * 130, HEIGHT // 2 - 60))

        # 6. Vẽ UI
        screen.blit(btn_tai_img, rect_tai)
        screen.blit(btn_xiu_img, rect_xiu)
        gui.draw_balance(balance)
        gui.draw_text(message, WIDTH // 2, 80, color=YELLOW, center=True)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()