import tkinter as tk
from tkinter import ttk
from pytube import YouTube, helpers
import threading


class LinkDownload(tk.Tk):
    def __init__(self, title=None):
        super().__init__()
        self.title(title)
        self.geometry('640x480')  # 修改窗口大小以适应新的控件
        self.create_widgets()

    def create_widgets(self):
        self.prompt_var = tk.StringVar()
        self.prompt_var.set("请输入链接")
        self.prompt_label = tk.Label(self, textvariable=self.prompt_var)
        self.prompt_label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.progress_var = tk.StringVar()
        self.progress_label = tk.Label(self, textvariable=self.progress_var)
        self.progress_label.pack()
        self.button = tk.Button(
            self, text='链接下载', command=self.start_download_thread)
        self.button.pack()

        # 创建一个表格来显示下载历史
        self.tree = ttk.Treeview(self, columns=(
            '视频标题', '链接', '状态'), show='headings')
        self.tree.column('视频标题', width=200, anchor='center')
        self.tree.column('链接', width=200, anchor='center')
        self.tree.column('状态', width=100, anchor='center')
        self.tree.heading('视频标题', text='视频标题')
        self.tree.heading('链接', text='链接')
        self.tree.heading('状态', text='状态')
        self.tree.pack()

    def progress_function(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        liveprogress = (bytes_downloaded / total_size) * 100
        self.progress_var.set("下载进度：{:.1f}%".format(liveprogress))

    def download(self):
        link = self.entry.get()
        yt = YouTube(link, on_progress_callback=self.progress_function)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        stream = streams.get_highest_resolution()
        print("开始下载: ", yt.title)
        stream.download(output_path='C:\\Users\\GeekerHWH\\Downloads')
        print("下载完成")
        self.entry.delete(0, 'end')
        self.progress_var.set("")
        self.prompt_var.set("下载完成，请输入下一个需要下载的链接")
        self.button['text'] = '链接下载'
        self.button['state'] = 'normal'

        # 在表格中添加下载历史
        self.tree.insert('', 'end', values=(yt.title, link, '完成'))

    def start_download_thread(self):
        self.button['text'] = '解析大概需要10秒，请耐心等待'
        self.button['state'] = 'disabled'
        download_thread = threading.Thread(target=self.download)
        download_thread.start()


if __name__ == '__main__':
    app = LinkDownload('YouTube Downloader')
    app.mainloop()
