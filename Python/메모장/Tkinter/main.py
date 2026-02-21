import tkinter as tk
import tkinter.ttk


class Notepad:
    def __init__(self):
        self.window = tk.Tk("600x400")
        self.window.title("메모장")
        self.window.resizable(True, True)

        self.tab_manager = TabManager(self.window)

        self.window.mainloop()


class TabManager:
    class FrameGenerator:
        def __init__(self, target_window):
            self.target_window = target_window

        def create_a_frame(self):
            self._frame = tk.Frame(self.target_window)

        @property
        def frame(self):
            try:
                return self._frame
            except NameError:
                print("create_a_frame()을 사용해야 합니다.")

    def __init__(self, window):
        self.window = window
        self.tabs = {}  # self.tabs = {탭 이름: tk.Frame, ...}

        self.notebook = tkinter.ttk.Notebook(self.window, width=300, height=300)
        self.notebook.pack()

        self.create_a_tab("탭1")
        self.create_a_tab("탭2")
        self.create_a_tab("탭3")

        self.tab_name = "탭1"
        self.label1 = tk.Label(
            self.tabs[self.tab_name].frame, text=f"{self.tab_name}의 내용"
        )
        self.label1.pack()

        self.tab_name = "탭2"
        self.label1 = tk.Label(
            self.tabs[self.tab_name].frame, text=f"{self.tab_name}의 내용"
        )
        self.label1.pack()

        self.tab_name = "탭3"
        self.label1 = tk.Label(
            self.tabs[self.tab_name].frame, text=f"{self.tab_name}의 내용"
        )
        self.label1.pack()

    def create_a_tab(self, tab_name="새 탭"):
        "이름이 tab_name인 새 탭을 생성한다."

        self.tabmanager_frame = TabManager.FrameGenerator(self.window)
        self.tabs[tab_name] = self.tabmanager_frame

        self.tabmanager_frame.create_a_frame()
        self.notebook.add(self.tabmanager_frame.frame, text=tab_name)


if __name__ == "__main__":
    notepad = Notepad()
