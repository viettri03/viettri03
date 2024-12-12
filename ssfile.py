import tkinter as tk
import random

# Tạo cửa sổ chính
root = tk.Tk()
root.title("EM BIẾT ANH MUỐN NÓI ĐIỀU GÌ KHÔNG HẢ?")
root.geometry("400x200")  
root.configure(bg="pink") 

# Thêm nhãn (Label)
label = tk.Label(root, text="ANH CÓ ĐIỀU MUỐN NÓI VỚI EM!", font=("Arial", 18, "bold"), bg="pink")
label.pack(pady=20)  

# Hàm tạo cửa sổ mới
def open_new_window():

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = random.randint(0, screen_width - 300)  
    y = random.randint(0, screen_height - 100)
    
    # Tạo cửa sổ mới
    new_window = tk.Toplevel(root)  
    new_window.title("LỜI NHẮN")
    new_window.geometry(f"300x100+{x}+{y}")
    new_window.configure(bg="pink") 
    
    # Thêm nhãn vào cửa sổ mới
    new_label = tk.Label(new_window, text="ANH ĐANG RẤT NHỚ EM!", font=("Arial", 14, "bold"), bg="pink")
    new_label.pack(pady=20)
    
    # Sau 1 giây tạo thêm cửa sổ mới
    root.after(600, open_new_window)

# Tạo nút bo tròn và hiệu ứng khi ấn
def on_enter(e):
    button.config(bg="#ff9999", fg="white")  # Đổi màu khi di chuột vào

def on_leave(e):
    button.config(bg="white", fg="black")  # Trở về màu gốc khi rời chuột

# Nút với góc bo tròn và hiệu ứng
button = tk.Button(
    root, 
    text="ẤN VÀO ĐÂY ĐI", 
    command=open_new_window, 
    font=("Arial", 14, "bold"),  # Phông chữ lớn hơn và in đậm
    bg="white", 
    fg="black", 
    activebackground="#ff6666", 
    activeforeground="white", 
    relief="flat",
    bd=0,
    highlightthickness=0,
    padx=20, 
    pady=10
)
button.pack(pady=10)

# Gắn sự kiện hover
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Chạy vòng lặp chính
root.mainloop()