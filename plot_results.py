import matplotlib.pyplot as plt
import numpy as np


def plot_ms_ssim():
    ms_ssim_h264 = np.array([0.996386, 0.997293, 0.997970, 0.998560, 0.999009])
    ms_ssim_h265 = np.array([0.996964, 0.997650, 0.998183, 0.998622, 0.998947])
    ms_ssim_vp9 = np.array([0.996800, 0.997453, 0.998122, 0.998664, 0.999095])

    plt.xticks(np.arange(0, 5), [0.1, 0.2, 0.3, 0.4, 0.5])
    plt.plot(ms_ssim_h264, label="H.264")
    plt.plot(ms_ssim_h265, label="H.265")
    plt.plot(ms_ssim_vp9, label="VP9")
    plt.legend(loc='best')
    plt.xlabel("BPP")
    plt.ylabel('MS-SSIM')


def plot_psnr():
    psnr_h264 = np.array([47.064842, 48.239937, 49.310875, 50.506340, 51.683334])
    psnr_h265 = np.array([48.682232, 49.703697, 50.816949, 51.806969, 52.708218])
    psnr_vp9 = np.array([48.853405, 49.932610, 51.318150, 52.884586, 54.651627])

    plt.xticks(np.arange(0, 5), [0.1, 0.2, 0.3, 0.4, 0.5])
    plt.plot(psnr_h264, label="H.264")
    plt.plot(psnr_h265, label="H.265")
    plt.plot(psnr_vp9, label="VP9")
    plt.legend(loc='best')
    plt.xlabel("BPP")
    plt.ylabel('PSNR')


def plot_vmaf():
    vmaf_h264 = np.array([94.939400, 95.705688, 96.085732, 96.478592, 96.709030])
    vmaf_h265 = np.array([95.440704, 95.965714, 96.432251, 96.733727, 96.994194])
    vmaf_vp9 = np.array([95.377472, 96.059372, 96.522629, 96.861298, 97.084274])
    plt.style.use(['dark_background'])
    plt.xticks(np.arange(0, 5), [0.1, 0.2, 0.3, 0.4, 0.5])
    plt.plot(vmaf_h264, label="H.264")
    plt.plot(vmaf_h265, label="H.265")
    plt.plot(vmaf_vp9, label="VP9")
    plt.legend(loc='best')
    plt.xlabel("BPP")
    plt.ylabel('VMAF')
