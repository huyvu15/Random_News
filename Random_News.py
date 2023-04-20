import tkinter as tk
import requests
from bs4 import BeautifulSoup
import webbrowser
from PIL import Image, ImageTk
from tkinter.font import Font


class Random_News:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random News")
        self.root.geometry("800x600")
        
        # set icon
        icon_image = tk.PhotoImage(file="D:\Py\Tkinter\Project\Random_news\icon.ico")
        self.root.iconphoto(False, icon_image)

        self.root.attributes('-topmost', False)# để là True thì khi mở tab khác thì tab này vẫn hiện
        
        #set backgrouond
        img = Image.open("D:\Py\Tkinter\Project\Random_news\had.png")
        background_image = ImageTk.PhotoImage(img)
        background_label = tk.Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        self.label1 = tk.Label(self.root, text="Bảng tin hôm nay", fg="blue", font=("cambria", 16))
        self.label1.place(x=350, y=150)

        # my_font = Font(size=12)
        self.listbox = tk.Listbox(self.root, width=70) #font=my_font)
        self.listbox.place(x=210, y=180)

        self.button_yes = tk.Button(self.root, text='Xem!', font=("Arial", 14), command=self.show_article, bg= 'cyan')
        self.button_yes.place(x=320, y=360)

        self.button_no = tk.Button(self.root, text='Next!', font=("Arial", 14), command=self.get_new_article, bg = 'red')
        self.button_no.place(x=480, y=360)

        self.button_exit = tk.Button(self.root, text='Exit!', font=("Arial", 14), command=self.root.quit, bg='yellow')
        self.button_exit.place(x=750, y=542)

        self.count = 0
        self.load_article()

        self.root.mainloop()

    def load_article(self):
        url = requests.get("https://dantri.com.vn") # lấy đường dẫn 
        soup = BeautifulSoup(url.content, "html.parser")# lấy nội dung
        titles = soup.find_all(class_="article-title")# tìm tiêu đề và lưu và titles
        self.new_title = titles[self.count].text.strip()# loại bỏ ký tự space ở phần cuối trong tiêu đề bài báo
        children = titles[self.count].findChildren("a", recursive=False)
        self.find_a = children[0]['href']# tìm thẻ chứa nội dung tiêu đề bài báo
        self.listbox.delete(0, tk.END)
        c = "\n Bài báo:" + " \"" + self.new_title + "\""
        self.listbox.insert(tk.END, c)
        self.listbox.insert(tk.END, " ")
        self.listbox.insert(tk.END, " Bạn có muốn đọc ko??")
        self.listbox.insert(tk.END, " --------------------------------------o0o------------------------------------------ ")
        self.listbox.insert(tk.END, " --------------------------------------o0o------------------------------------------ ")
        self.listbox.insert(tk.END, " --------------------------------------o0o------------------------------------------ ")
        self.listbox.insert(tk.END, " --------------------------------------o0o------------------------------------------ ")
        self.listbox.insert(tk.END, " --------------------------------------o0o------------------------------------------ ")
        self.listbox.insert(tk.END, " --------------------------------------o0o------------------------------------------ ")
        self.listbox.insert(tk.END, " --------------------------------------o0o------------------------------------------ ")
        
        self.listbox.config(fg="blue")

    def get_new_article(self):
        self.count += 1
        self.load_article()
        
        self.listbox.insert(tk.END, "Try again!")
        
        self.listbox.config(fg="blue")
        
    def show_article(self):
        webbrowser.open_new(self.find_a)

if __name__ == '__main__':
    Random_News()
