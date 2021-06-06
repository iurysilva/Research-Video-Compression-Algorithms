import subprocess
import os
from video import Video
from sewar.full_ref import psnr
import numpy
import tensorflow as tf


def do_compression(algorithm, video_number, path, out_path, bit_rate):
    name = os.listdir(path)[video_number]
    video_path = "%s/%s" % (path, name)
    out = "%s/%s_compressed.mkv" % (out_path, video_number)
    try:
        os.mkdir(out_path)
    except OSError:
        print("Creation of the directory %s failed" % out_path)
    else:
        print("Successfully created the directory %s " % out_path)

    if '%s_compressed.mkv' % video_number in os.listdir(out_path):
        print('removing video from folder')
        os.remove(out)

    if algorithm == "265":
        command = "ffmpeg -i %s -c:v libx265 -preset slower -b:v %sk -c:a aac -b:a 128k %s" % (video_path, bit_rate, out)
    elif algorithm == "av1":
        command = "ffmpeg -i %s -c:v libaom-av1 -b:v %sk %s" % (video_path, bit_rate, out)
    elif algorithm == "264":
        command = "ffmpeg -i %s -c:v libx264 -preset slower -b:v %sk -c:a copy %s" % (video_path, bit_rate, out)
    else:
        return video_path, out

    command = command.split()
    p = subprocess.Popen(command, cwd="E:\Documentos\GitHub\Video-Compression-Algorithms")
    p.wait()
    return video_path, out


def print_vp9(video_number, path, out_path, bit_rate):
    name = "%s/%s" % (path, os.listdir(path)[video_number])
    out = "%s/%s_compressed.mkv" % (out_path, video_number)
    print("ffmpeg -i %s -c:v libvpx-vp9 -b:v %sk -pass 1 -an -f null NUL && ^\n" % (name, bit_rate))
    print("ffmpeg -i %s -c:v libvpx-vp9 -b:v %sk -pass 2 -c:a libopus %s" % (name, bit_rate, out))


def calculate_metrics(video_path, reference_path):
    metric_command = 'ffmpeg_quality_metrics %s %s -m ssim psnr vmaf' % (video_path, reference_path)
    # metric_command = 'ffmpeg_quality_metrics %s %s -m ssim' % (video_path, reference_path)
    metric_command = metric_command.split()
    compare = subprocess.Popen(metric_command, cwd="E:\Documentos\GitHub\Video-Compression-Algorithms")


def calculate_psnr(video_path, reference_path):
    video = Video(video_path)
    reference_video = Video(reference_path)
    results = tf.image.psnr(video.frames, reference_video.frames, 255)
    print('PSNR mean: ', numpy.mean(results))
    return video, reference_video


def calculate_compression_rate(num1, num2):
    return 100 - ((num1 * 100)/num2)