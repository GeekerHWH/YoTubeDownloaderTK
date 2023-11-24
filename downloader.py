from pytube import YouTube, helpers


def download(url, destination):
    # 输入要下载的YouTube视频链接
    video_url = url

    # 创建YouTube对象
    yt = YouTube(video_url)

    # 获取视频的各种流（不同分辨率和格式）
    streams = yt.streams.filter(progressive=True, file_extension='mp4')

    # 选择要下载的视频流
    stream = streams.get_highest_resolution()

    # 指定下载路径
    download_path = destination

    # print("开始下载: ", yt.title)

    # 下载视频
    stream.download(output_path=download_path)

    # print("下载完成")
