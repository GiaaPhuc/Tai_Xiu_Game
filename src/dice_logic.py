import random

def roll_three_dice():
    """Tạo ra 3 số ngẫu nhiên từ 1 đến 6"""
    return [random.randint(1, 6) for _ in range(3)]

def check_win(dices, bet_choice):
    """
    Kiểm tra kết quả:
    - Tài (tai): Tổng từ 11 đến 17
    - Xỉu (xiu): Tổng từ 4 đến 10
    - Lưu ý: Bộ ba giống nhau thường nhà cái ăn, nhưng ở đây làm đơn giản cho bạn dễ chơi.
    """
    total = sum(dices)
    
    if bet_choice == 'tai':
        return total >= 11
    elif bet_choice == 'xiu':
        return total <= 10
    
    return False