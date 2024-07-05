import os
import jdk
import asyncio
import threading
import customtkinter

def _asyncio_thread(async_loop, ver: int, add_path: bool):
    async_loop.run_until_complete(java_install(ver, add_path))

def do_tasks(async_loop):
    print("working")
    print(async_loop)
    """ Button-Event-Handler starting the asyncio part. """
    threading.Thread(target=_asyncio_thread, args=(async_loop, answer.get(), True)).start()

async def java_install(ver, add_path=False):
    try:
        print("installing...")
        label2.configure(text="Installing...")
        await asyncio.sleep(1)
        jdk.install(ver)
        path = os.path.expanduser("~") + "\\.jdk"
        java_path = os.path.join(path, os.listdir(path)[0])
        if add_path:
            os.system(f'chcp 65001 & setx JAVA_HOME {java_path} & setx "Path" "%Path%;%JAVA_HOME%\\bin" /m')
        label2.configure(text="Complete.")
        return 0
    except Exception as e:
        return e

def main(async_loop):
    global label, answer, combo, button, label2
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue")
    win = customtkinter.CTk()
    win.title("AJI v0.0.2")
    screenwidth, screenheight = win.winfo_screenwidth(), win.winfo_screenheight()  # 屏幕高度
    width, height = 300, 120
    x, y = int((screenwidth - width) / 2), int((screenheight - height) / 2)

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 大小以及位置

    label = customtkinter.CTkLabel(win, text="Select Java Version:")
    label.pack()

    answer = customtkinter.StringVar()
    answer.set("21") # 新版本官方推荐
    combo = customtkinter.CTkComboBox(win, variable=answer, values=["6", "8", "11", "17", "21"])
    combo.pack()

    button = customtkinter.CTkButton(win, text="Install Java", command=lambda: do_tasks(async_loop))
    button.pack()

    label2 = customtkinter.CTkLabel(win, text="Not Started Yet.")
    label2.pack()

    win.mainloop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    main(loop)
    loop.close()

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.install_java)
#         self.ui.comboBox.addItems(["6", "8", "11", "17", "21"])
    
#     def install_java(self):
#         ver = self.ui.comboBox.currentText()
#         add_path = True
#         error = java_install(ver, add_path)
#         if error == 0:
#             QMessageBox.information(self, "Success", "Installation Complete.", QMessageBox.Yes)
#         else:
#             QMessageBox.critical(self, "Error", "Unable to install.\n{error}", QMessageBox.Yes)
    

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = MainWindow()
#     icon = QIcon("icon.ico")
#     w.setWindowIcon(icon)
#     w.show()
#     app.exec()
