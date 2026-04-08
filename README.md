# 🎲 Tài Xỉu Game - Python Pygame

## Dám nghĩ dám làm, đổi đời đổi vận...

Game **Tài Xỉu** được xây dựng bằng **Python + Pygame** với giao diện đẹp, hiệu ứng âm thanh và kiến trúc code tách module chuyên nghiệp.

---

# 📸 Demo

Game bao gồm:

- 🎲 Hiệu ứng lắc xúc xắc
- 💰 Hệ thống tiền cược
- 🔊 Âm thanh thắng / thua
- 🎨 Giao diện đẹp với assets riêng
- 🧠 Logic game tách riêng

---

# 🛠 Yêu cầu hệ thống

- Python 3.x
- Pygame

---

# 📂 Cấu trúc thư mục

```
TAI_XIU_GAME
│
├── assets
│   │
│   ├── fonts
│   │   └── font.ttf
│   │
│   ├── images
│   │   ├── dice
│   │   │   ├── dice_1.png
│   │   │   ├── dice_2.png
│   │   │   ├── dice_3.png
│   │   │   ├── dice_4.png
│   │   │   ├── dice_5.png
│   │   │   └── dice_6.png
│   │   │
│   │   ├── background.png
│   │   ├── button_tai.png
│   │   ├── button_xiu.png
│   │   └── shaker.png
│   │
│   └── sounds
│       ├── dice_roll.mp3
│       ├── win.mp3
│       └── lose.mp3
│
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── dice_logic.py
│   └── gui_manager.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Cài đặt và Chạy Game

## 1. Clone dự án

```bash
git clone https://github.com/yourusername/tai-xiu-game.git
cd tai-xiu-game
```

---

## 2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## 3. Chạy game

```bash
python main.py
```

---

# ✨ Tính năng & Quy trình Game

Game vận hành theo quy trình chuyên nghiệp, cho phép người chơi quản lý vốn cược:

- **Khởi đầu:** Người chơi bắt đầu với số vốn **100,000,000 VNĐ**.
- **Chọn mức cược:** Trước khi đặt cửa, người chơi chọn số tiền muốn cược **10K, 50K, 100K, 500K, 1M, 5M, 10M** thông qua các nút chọn ở dưới màn hình.
- **Đặt cược:** Click vào nút **TÀI** hoặc **XỈU** để bắt đầu ván đấu với số tiền đã chọn.
- **Hiệu ứng chờ:** Hệ thống thực hiện lắc xúc xắc trong **2 giây** kèm hiệu ứng bát úp (shaker) rung động và âm thanh sống động.
- **Kết quả:** Sau 2 giây, bát mở ra hiển thị kết quả và thông báo Thắng/Thua.
- **Cập nhật:** Tiền cược được tự động cộng hoặc trừ vào số dư ngay lập tức.

---

# 🎯 Luật chơi

| Kết quả | Điều kiện     |
| ------- | ------------- |
| Tài     | Tổng 11 - 17  |
| Xỉu     | Tổng 4 - 10   |
| Bộ ba   | Nhà cái thắng |

---

# 🧠 Kiến trúc Code

### main.py

- Chạy game chính
- Khởi tạo pygame
- Game loop

---

### src/config.py

- Cấu hình game
- Kích thước màn hình
- Màu sắc
- Đường dẫn assets

---

### src/dice_logic.py

- Logic xúc xắc
- Random kết quả
- Tính tài/xỉu

---

### src/gui_manager.py

- Quản lý giao diện
- Button
- Hiển thị tiền
- Hiển thị kết quả

---

# 🔊 Assets

## 🎨 Images

- Background
- Button Tài
- Button Xỉu
- Dice
- Shaker

---

## 🔊 Sounds

- Dice Roll
- Win
- Lose

---

# 📦 requirements.txt

```
pygame
```

---

# ✨ Tính năng

✅ Giao diện đẹp
✅ Kiến trúc code chuyên nghiệp
✅ Hiệu ứng xúc xắc
✅ Âm thanh thắng thua
✅ Button tương tác
✅ Logic tài xỉu chuẩn

---

# 👤 Tác giả

**Võ Gia Phúc**
Sinh viên - VNU-HCM University of Science

---

# 📜 License

Dự án phục vụ mục đích học tập và nghiên cứu.

---

# ❤️ Cảm ơn

Nếu bạn thấy project hữu ích hãy ⭐ GitHub repo nhé!
