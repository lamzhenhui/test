from moviepy.editor import VideoFileClip, clips_array

# 读取两个输入的MP4文件
clip1 = VideoFileClip("/Users/meta/lam/test/python_test/demo/11.mp4")
clip2 = VideoFileClip("/Users/meta/lam/test/python_test/demo/22.mp4")

# 使用clips_array合并两个视频，可以设置布局参数
final_clip = clips_array([[clip1, clip2]])

# 生成输出的MP4文件
final_clip.write_videofile("output.mp4")
