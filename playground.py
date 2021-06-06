from compression import do_compression, print_vp9, calculate_metrics, calculate_psnr
from video import Video
import os


bpp = 0.485
path = "E:/Documentos/GitHub/Video-Compression-Algorithms/datasets/modal_analysis"
out_path = "E:/Documentos/GitHub/Video-Compression-Algorithms/datasets/modal_analysis_compressed"
video_number = 2
algorithm = "vp9"  # 264, 265, vp9

# calculate necessary bit rate value
name = os.listdir(path)[video_number]
video = Video("%s/%s" % (path, name))
bit_rate = (bpp * video.frames_shape[0] * video.frames_shape[1] * video.fps)/1000

video_path, compressed_video_path = do_compression(algorithm, video_number, path, out_path, bit_rate)
if algorithm != "vp9":
    calculate_metrics(video_path, compressed_video_path)
else:
    print_vp9(video_number, path, out_path, bit_rate)


