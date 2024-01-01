import time as t
import colorama  # Import the colorama library
from colorama import Fore, Back, Style  # Import color functions

colorama.init()  # Initialize colorama

#ban quyen le manh kien

x = "Nguyễn Văn Thái"

b = len(x)

def cake():
    print(Fore.LIGHTBLUE_EX + " " * 23 + "i  i  i  i")  # Blue candles
    t.sleep(1)
    print(Fore.LIGHTBLUE_EX + " " * 23 + "i  i  i  i")
    t.sleep(1)
    print(Fore.LIGHTBLUE_EX + " " * 21 + "__i__i__i__i__")
    t.sleep(1)
    print(Fore.YELLOW + " " * 20 + "|" + " " * 12 + "|")  # Yellow cake base
    t.sleep(1)
    print(Fore.YELLOW + " " * 20 + "|" + " " * 12 + "|")
    t.sleep(1)
    print(Fore.YELLOW + " " * 20 + "|" + " " * 12 + "|")
    t.sleep(1)
    print(Fore.YELLOW + " " * 16 + "-" * 24)
    t.sleep(1)
    print(Fore.YELLOW + " " * 16 + "|" + " " * 20 + "|")
    t.sleep(1)
    print(Fore.YELLOW + " " * 16 + "|" + " " * int((20 - b) / 2) + x + " " * int((20 - b) / 2 - 2) + "|")
    t.sleep(1)
    print(Fore.YELLOW + " " * 16 + "|" + " " * 20 + "|")
    t.sleep(1)
    print(Fore.YELLOW + " " * 16 + "-" * 24)


def menu():
    print()
    for i in range(4):
        if i == 3:
            print(Fore.MAGENTA + " " * 13 + "HAPPY BIRTHDAY")  
        elif i == 0 or i == 1:
            print(Fore.GREEN + " " * 15 + "HAPPY BIRTHDAY TO Văn Thái")  
        elif i == 2:
            print(Fore.CYAN + " " * 15 + "HAPPY BIRTHDAY", "*", x.upper(), "*", "\n")  
        t.sleep(1.8)
        print()

def heart():
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print(Fore.RED + "", end=" ")  # Red heart
            else:
                print(end="  ")
        print()

# Thêm đoạn code để đếm ngược thời gian
def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60) # Tách phút và giây từ biến seconds
        timeformat = '{:02d}:{:02d}'.format(mins, secs) # Định dạng thời gian hiển thị đếm ngược
        print(timeformat, end='\r') # Hiển thị thời gian đếm ngược
        t.sleep(1) # Chờ 1s và cập nhật thời gian
        seconds -= 1 # Đếm ngược từng giây cho đến 0
    print("Chúc mừng sinh nhật Tôi !") # In câu chúc mừng khi kết thúc đếm ngược

print(Fore.LIGHTBLUE_EX + "#" * 9 + " HAPPY BIRTHDAY " + "*" + x.upper() + "*" + "#" * 9)
t.sleep(1.5)
menu()
cake()

print(Fore.LIGHTGREEN_EX + " " * 2, "Tuổi mới chúc bản thân hoàn thành mục tiêu của mình và thành công trên con đường học tập\n \n\n".upper())
t.sleep(2)
x = "Văn Thái"
a = x.split()
for i in a:
    print(Fore.LIGHTCYAN_EX + "\t\t", i.title())
    t.sleep(1)

print(Style.RESET_ALL)
# Gọi hàm đếm ngược với số giây mong muốn
countdown(5)
