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
    INDEX_OF_FRAMEGENERATOR = 0
    INDEX_OF_LABELGENERATOR = 1

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

    class LabelGenerator:
        def __init__(self, target_frame, text):
            self.target_frame = target_frame
            self.text = text

        def create_a_label(self):
            self.label = tk.Label(self.target_frame, text=self.text)
            self.label.pack()

    def __init__(self, window):
        self.window = window
        self.tabs = {}

        self.notebook = tkinter.ttk.Notebook(self.window, width=300, height=300)
        self.notebook.pack()

        self.create_a_tab("탭1")
        self.create_a_tab("탭2")
        self.create_a_tab("탭3")

    def create_a_tab(self, tab_name="새 탭"):
        self.tabs[tab_name] = list()
        self.tabs[tab_name].append(TabManager.FrameGenerator(self.window))
        self.tabs[tab_name][TabManager.INDEX_OF_FRAMEGENERATOR].create_a_frame()

        self.tabs[tab_name].append(
            TabManager.LabelGenerator(
                self.tabs[tab_name][TabManager.INDEX_OF_FRAMEGENERATOR].frame,
                text=f"{tab_name}의 내용",
            )
        )

        self.notebook.add(
            self.tabs[tab_name][TabManager.INDEX_OF_FRAMEGENERATOR].frame, text=tab_name
        )

        self.tabs[tab_name][TabManager.INDEX_OF_LABELGENERATOR].create_a_label()


if __name__ == "__main__":
    notepad = Notepad()
