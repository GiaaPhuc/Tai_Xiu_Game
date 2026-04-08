import pygame
import sys
import random
from src.config import *
from src.dice_logic import roll_three_dice, check_win
from src.gui_manager import GUIManager

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tài Xỉu Casino - Chọn Mức Cược")
    clock = pygame.time.Clock()
    gui = GUIManager(screen)

    # --- Load Assets ---
    try:
        bg = pygame.image.load(ASSETS_PATH + "background.png").convert()
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        btn_tai = pygame.image.load(ASSETS_PATH + "button_tai.png").convert_alpha()
        btn_xiu = pygame.image.load(ASSETS_PATH + "button_xiu.png").convert_alpha()
        rect_tai = btn_tai.get_rect(center=(WIDTH * 0.75, HEIGHT * 0.82))
        rect_xiu = btn_xiu.get_rect(center=(WIDTH * 0.25, HEIGHT * 0.82))
        shaker_img = pygame.image.load(ASSETS_PATH + "shaker.png").convert_alpha()
        shaker_img = pygame.transform.scale(shaker_img, (380, 320))
        dice_imgs = [pygame.transform.scale(pygame.image.load(f"{DICE_PATH}dice_{i}.png").convert_alpha(), (120, 120)) for i in range(1, 7)]
        snd_roll = pygame.mixer.Sound(SOUND_PATH + "dice_roll.mp3")
        snd_win = pygame.mixer.Sound(SOUND_PATH + "win.mp3")
        snd_lose = pygame.mixer.Sound(SOUND_PATH + "lose.mp3")
    except Exception as e:
        print(f"Lỗi: {e}"); return

    # --- Biến khởi tạo ---
    balance = INITIAL_BALANCE
    current_bet = BET_OPTIONS[0] # Mặc định cược mức đầu tiên (10k)
    dices = [1, 2, 3]
    message = "CHỌN MỨC CƯỢC RỒI ĐẶT TÀI/XỈU"
    state = "IDLE"
    roll_time, player_choice = 0, ""

    # Tạo các vùng chọn mức cược (4 hình chữ nhật dưới cùng màn hình)
    bet_rects = []
    for i in range(len(BET_OPTIONS)):
        rect = pygame.Rect(WIDTH//2 - 220 + i*110, HEIGHT - 60, 100, 40)
        bet_rects.append(rect)

    while True:
        screen.blit(bg, (0, 0))
        now = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                # 1. Kiểm tra chọn mức cược
                for i, rect in enumerate(bet_rects):
                    if rect.collidepoint(mouse_pos):
                        current_bet = BET_OPTIONS[i]

                # 2. Kiểm tra đặt cược Tài/Xỉu
                if state != "ROLLING":
                    if rect_tai.collidepoint(mouse_pos): player_choice = 'tai'
                    elif rect_xiu.collidepoint(mouse_pos): player_choice = 'xiu'
                    else: player_choice = None

                    if player_choice:
                        if balance >= current_bet:
                            state, roll_time = "ROLLING", now
                            snd_roll.play()
                            message = f"ĐANG CƯỢC {current_bet:,} VNĐ..."
                        else:
                            message = "KHÔNG ĐỦ TIỀN CƯỢC!"

        # --- Logic Trạng thái ---
        if state == "ROLLING":
            dices = [random.randint(1, 6) for _ in range(3)]
            screen.blit(shaker_img, (WIDTH//2-190 + random.randint(-3,3), HEIGHT//2-160 + random.randint(-3,3)))
            if now - roll_time > ROLL_DURATION:
                state, dices = "RESULT", roll_three_dice()
                if check_win(dices, player_choice):
                    balance += current_bet
                    message = f"THẮNG {current_bet:,}! TỔNG: {sum(dices)}"
                    snd_win.play()
                else:
                    balance -= current_bet
                    message = f"THUA {current_bet:,}! TỔNG: {sum(dices)}"
                    snd_lose.play()
        else:
            # Vẽ xúc xắc thật
            for i, v in enumerate(dices):
                screen.blit(dice_imgs[v-1], (WIDTH//2-180 + i*130, HEIGHT//2-60))

        # --- Vẽ Giao diện ---
        screen.blit(btn_tai, rect_tai)
        screen.blit(btn_xiu, rect_xiu)
        gui.draw_balance(balance)
        gui.draw_text(message, WIDTH//2, 80, YELLOW, center=True)
        
        # Vẽ các nút chọn mức cược
        for i, rect in enumerate(bet_rects):
            color = ORANGE if current_bet == BET_OPTIONS[i] else GRAY
            pygame.draw.rect(screen, color, rect, border_radius=5)
            # Vẽ số tiền lên nút
            bet_txt = pygame.font.SysFont("Arial", 18, bold=True).render(f"{BET_OPTIONS[i]//1000}K", True, WHITE)
            screen.blit(bet_txt, bet_txt.get_rect(center=rect.center))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__": main()