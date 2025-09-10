import  arabic_reshaper 
from bidi.algorithm  import get_display
import os
import random 
from tkinter import * 
import time 

base = {}
user_globals = {}
user_locals = {}

log = print 

width = os.get_terminal_size().columns
a = get_display(arabic_reshaper.reshape("بسم الله رحمان رحیم"))
aa = get_display(arabic_reshaper.reshape("اعوذ بالله من الشیطان الرجیم"))
b = get_display(arabic_reshaper.reshape(": کد خود را وارد کنید"))
c = get_display(arabic_reshaper.reshape("صدق الله العلی العظیم"))
d = get_display(arabic_reshaper.reshape("ارور: استغفرالله ربی و اتوبو علیه"))
e = get_display(arabic_reshaper.reshape("اللهم صلی الله محمد و آل محمد و عجل فرجهم"))
f = get_display(arabic_reshaper.reshape("چند حیوان در کشتی نوح میخواهید؟"))
g = get_display(arabic_reshaper.reshape("برود تا قیامت:"))
h = get_display(arabic_reshaper.reshape("تا توبه کند:"))
j = get_display(arabic_reshaper.reshape(": مرجع تقلید"))
k = get_display(arabic_reshaper.reshape(": رساله"))
l = get_display(arabic_reshaper.reshape("اهلا و سهلا بالبایتون الاسلامیه: صنع بالاخوین الجهادی السیده الایلیا و البارسا"))
m = get_display(arabic_reshaper.reshape(": به امید خدا کد خود را وارد کنید"))
n = get_display(arabic_reshaper.reshape(": به جهاد ادامه دهید و کد بنویسید"))
o = get_display(arabic_reshaper.reshape(": هر خط کد مارا به نابودی دشمنان اسلام نزدیک میکند"))
p = get_display(arabic_reshaper.reshape(": الجهاد فی سبیل الله"))
ayat = get_display(arabic_reshaper.reshape(""""کمی آئت الکرسی بخوان : اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ  لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ  لَهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ  مَنْ ذَا الَّذ...َ الْعَلِيُّ الْعَظِيمُ
"""))
q = get_display(arabic_reshaper.reshape("خدا یاورتان باشد"))
rr = get_display(arabic_reshaper.reshape("مرگ بر آمریکا"))
rrr = get_display(arabic_reshaper.reshape("مرگ بر ضد ولایت فقیه"))
rrrr = get_display(arabic_reshaper.reshape("نه به جمهوری اسلامی"))
rrrrr = get_display(arabic_reshaper.reshape("وارد کردن یاد خدا به کد"))
def client():
   
    while True:
         greet = input(">>> ")
         if "allah" in greet:
            break
    print(f"<<<<<<<<<<<<<<<<{a}>>>>>>>>>>>>>>>>>".center(width), l.center(width))
    print(f"  ________________________ \n |{rrrrr}| \n |_______________________|")
    length = 81
    for i in range(length + 1):
        bar = "_" * i + "."* (length - 1)
        print(f"\r{bar}"[:80].center(width), end='', flush=True)
        time.sleep(0.05)
    print()
        
    abdollah()
            



def abdollah():   
    while True:
        try:
            code = input(f" \n {random.choice([m, n, o, p])}")
            with open("user.txt", "a", encoding="UTF-8") as f:
                f.write(code + "\n")

            if code.strip().lower() in {"exit", "quit"}:
              print(f"<<<<<<<<<<<<<<<{c}>>>>>>>>>>>>>>>".center(width))
              break
            elif code.strip().lower() in {r"\help", "/help"}:

                def check():
                    if var.get() == True and var0.get() == True and var1.get() == True:
                        window.destroy()
                    elif var.get() == False and var0.get() == False and var1.get() == False:
                        window.destroy()
                        print(get_display(arabic_reshaper.reshape("تو برادر جهادی نیستی:(((")))


                    else: 
                        pass 

 


                window = Tk()
                window.title("may allah be with you...")
                window.config(background= "gold" )
                label = Label(window, text=f"{ayat}", font=("arial", 20, "italic"),
                              bg="gold", fg="white", relief=RAISED,
                               bd= 20, padx=20, pady=40, )
                label.pack()

                var = BooleanVar()
                var0 = BooleanVar()
                var1 = BooleanVar()

                chexkbox1= Checkbutton(text=f"{rr}", onvalue=True, offvalue=False, variable= var)
                chexbox2= Checkbutton(text=f"{rrr}", onvalue=True, offvalue=False, variable= var0)
                chexboox0= Checkbutton(text=f"{rrrr}", onvalue=False, offvalue=True, variable=var1)

                chexkbox1.pack()
                chexbox2.pack()
                chexboox0.pack()

                button = Button(background="black", text=f"{q}", foreground="gold", command= check )
                button.pack()
                

                window.mainloop()
            elif "show" in code:
                with open("user.txt", "r", encoding="UTF-8"):
                    content = f.read()
                    print(content)
            try:
                    result = eval(code, user_globals, user_locals)
                    print(result)
            except SyntaxError:
                exec(code, user_globals, user_locals)
        except Exception as e:

            if e == NameError:
                error = get_display(arabic_reshaper.reshape("ارزش های اسلامی خود را باز نگری کنید..."))
                print(f"<_________________________________________{error}_________________________________________>")
            elif e == SyntaxError:
                error = q 
                print(f"<_________________________________________{error}_________________________________________>")
            else:
                error = get_display(arabic_reshaper.reshape("ارزش های اسلامی خود را باز نگری کنید..."))
                print(f"<_________________________________________{error}_________________________________________>")

client()