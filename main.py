import pygame
import sys
import random
from src.config import *
from src.dice_logic import roll_three_dice, check_win
from src.gui_manager import GUIManager, Firework

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tài Xỉu Casino - Ultimate Edition")
    clock = pygame.time.Clock()
    gui = GUIManager(screen)

    # Màu vàng Gold
    COLOR_SLOGAN = (255, 215, 0) 

    # --- Load Assets ---
    try:
        bg = pygame.image.load(ASSETS_PATH + "background.png").convert()
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        
        SCALE_FACTOR = 0.7 
        btn_tai_raw = pygame.image.load(ASSETS_PATH + "button_tai.png").convert_alpha()
        btn_xiu_raw = pygame.image.load(ASSETS_PATH + "button_xiu.png").convert_alpha()
        
        new_btn_size = (int(btn_tai_raw.get_width() * SCALE_FACTOR), int(btn_tai_raw.get_height() * SCALE_FACTOR))
        btn_tai = pygame.transform.scale(btn_tai_raw, new_btn_size)
        btn_xiu = pygame.transform.scale(btn_xiu_raw, new_btn_size)
        
        rect_tai = btn_tai.get_rect(center=(WIDTH * 0.75, HEIGHT * 0.75))
        rect_xiu = btn_xiu.get_rect(center=(WIDTH * 0.25, HEIGHT * 0.75))
        
        shaker_img = pygame.image.load(ASSETS_PATH + "shaker.png").convert_alpha()
        shaker_img = pygame.transform.scale(shaker_img, (380, 320))
        shaker_rect = shaker_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        
        dice_imgs = [pygame.transform.scale(pygame.image.load(f"{DICE_PATH}dice_{i}.png").convert_alpha(), (120, 120)) for i in range(1, 7)]
        
        snd_roll = pygame.mixer.Sound(SOUND_PATH + "dice_roll.mp3")
        snd_win = pygame.mixer.Sound(SOUND_PATH + "win.mp3")
        snd_lose = pygame.mixer.Sound(SOUND_PATH + "lose.mp3")
        
        # --- KHẮC PHỤC LỖI DẤU TIẾNG VIỆT ---
        # Đổi Arial sang "Segoe UI" hoặc "Tahoma" để hỗ trợ dấu "ố", "ớ" tốt hơn
        # Nếu máy bạn không có Segoe UI, nó sẽ tự chọn font mặc định hỗ trợ Unicode
        slogan_font = pygame.font.SysFont("Segoe UI, Tahoma, Arial", 26, bold=True, italic=True)
        
    except Exception as e:
        print(f"Lỗi load tài nguyên: {e}"); return

    balance = INITIAL_BALANCE
    current_bet = BET_OPTIONS[0]
    dices, message, state = [1, 2, 3], "CHỌN MỨC CƯỢC RỒI ĐẶT TÀI/XỈU", "IDLE"
    roll_time, player_choice = 0, ""
    fireworks = []
    shake_intensity = 0 

    bet_rects = []
    num_options = len(BET_OPTIONS)
    button_w, button_h, spacing = 90, 40, 15
    total_row_w = (num_options * button_w) + ((num_options - 1) * spacing)
    start_x = (WIDTH - total_row_w) // 2

    for i in range(num_options):
        rect = pygame.Rect(start_x + i * (button_w + spacing), HEIGHT - 45, button_w, button_h)
        bet_rects.append(rect)

    while True:
        now = pygame.time.get_ticks()
        off_x = random.randint(-shake_intensity, shake_intensity) if shake_intensity > 0 else 0
        off_y = random.randint(-shake_intensity, shake_intensity) if shake_intensity > 0 else 0
        if shake_intensity > 0: shake_intensity -= 1

        screen.blit(bg, (off_x, off_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(bet_rects):
                    if rect.collidepoint(event.pos):
                        current_bet = BET_OPTIONS[i]
                        state = "IDLE"
                        message = f"MỨC CƯỢC: {current_bet:,} VNĐ"

                if state != "ROLLING":
                    if rect_tai.collidepoint(event.pos): player_choice = 'tai'
                    elif rect_xiu.collidepoint(event.pos): player_choice = 'xiu'
                    else: player_choice = None

                    if player_choice:
                        if balance >= current_bet:
                            state, roll_time = "ROLLING", now
                            snd_roll.play()
                            #message = f"BẠN CƯỢC {current_bet:,} VNĐ"
                            message = f"ĐANG LẮC..."
                        else:
                            message = "KHÔNG ĐỦ TIỀN CƯỢC!"

        for fw in fireworks:
            fw.update(); fw.draw(screen)
        fireworks = [fw for fw in fireworks if len(fw.particles) > 0]

        if state == "ROLLING":
            dices = [random.randint(1, 6) for _ in range(3)]
            screen.blit(shaker_img, (shaker_rect.x + random.randint(-4,4) + off_x, shaker_rect.y + random.randint(-4,4) + off_y))
            if now - roll_time > ROLL_DURATION:
                state, dices = "RESULT", roll_three_dice()
                if check_win(dices, player_choice):
                    balance += current_bet
                    message = f"THẮNG {current_bet:,}! TỔNG: {sum(dices)}"
                    snd_win.play()
                    for _ in range(6):
                        fireworks.append(Firework(random.randint(100, WIDTH-100), random.randint(100, HEIGHT-300)))
                else:
                    balance -= current_bet
                    message = f"THUA {current_bet:,}! TỔNG: {sum(dices)}"
                    snd_lose.play()
                    shake_intensity = 15 
        else:
            for i, v in enumerate(dices):
                screen.blit(dice_imgs[v-1], (WIDTH//2-180 + i*130 + off_x, HEIGHT//2-150 + off_y))

        if state == "RESULT" and not check_win(dices, player_choice):
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((100, 0, 0, 100)) 
            screen.blit(overlay, (0, 0))

        screen.blit(btn_tai, (rect_tai.x + off_x, rect_tai.y + off_y))
        screen.blit(btn_xiu, (rect_xiu.x + off_x, rect_xiu.y + off_y))
        gui.draw_balance(balance)
        gui.draw_text(message, WIDTH//2 + off_x, 80 + off_y, YELLOW, center=True)
        
        # Vẽ Slogan với Font Segoe UI (Hỗ trợ dấu tiếng Việt cực tốt)
        slogan_text = slogan_font.render("Dám nghĩ dám làm,", True, COLOR_SLOGAN)
        screen.blit(slogan_text, slogan_text.get_rect(center=(WIDTH//2 + off_x, HEIGHT - 95 + off_y)))
        slogan_text = slogan_font.render("đổi đời đổi vận...", True, COLOR_SLOGAN)
        screen.blit(slogan_text, slogan_text.get_rect(center=(WIDTH//2 + off_x, HEIGHT - 70 + off_y)))
        
        for i, rect in enumerate(bet_rects):
            color = (255, 140, 0) if current_bet == BET_OPTIONS[i] else (70, 70, 70)
            pygame.draw.rect(screen, color, rect.move(off_x, off_y), border_radius=8)
            pygame.draw.rect(screen, WHITE, rect.move(off_x, off_y), 2, border_radius=8)
            val = BET_OPTIONS[i]
            txt = f"{val//1000000}M" if val >= 1000000 else f"{val//1000}K"
            btn_txt = pygame.font.SysFont("Arial", 18, bold=True).render(txt, True, WHITE)
            screen.blit(btn_txt, btn_txt.get_rect(center=rect.move(off_x, off_y).center))

        pygame.display.flip(); clock.tick(FPS)

if __name__ == "__main__":
    main()