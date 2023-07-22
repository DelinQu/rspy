# use opencv read video and convert to gif
import argparse

import cv2 as cv
import imageio

parser = argparse.ArgumentParser()
parser.add_argument("--rsv", type=str, default="video.mp4", help="RS video path")
parser.add_argument("--rscv", type=str, default="video.mp4", help="RSC video path")
parser.add_argument("--gif", type=str, default="video.gif", help="gif path")
parser.add_argument("--fps", type=float, default=8, help="gif fps")
parser.add_argument("--start", type=int, default=0, help="start frame")
parser.add_argument("--end", type=int, default=-1, help="end frame")
parser.add_argument("--rs_delay", type=int, default=0, help="RS delay frame")
parser.add_argument("--step", type=int, default=10, help="step frame")
parser.add_argument("--downsample", type=int, default=2, help="downsample")

args = parser.parse_args()

if __name__ == "__main__":
    gif_path = args.gif
    fps = args.fps

    rs_video = cv.VideoCapture(args.rsv)
    rsc_video = cv.VideoCapture(args.rscv)
    frames = []
    resz = lambda x: cv.resize(x, (x.shape[1] // args.downsample, x.shape[0] // args.downsample))

    for i in range(args.rs_delay):
        rs_video.read()

    while True:
        ret_rs, frame_rs = rs_video.read()
        ret_rsc, frame_rsc = rsc_video.read()
        if ret_rs and ret_rsc:
            frame_rs = resz(cv.cvtColor(frame_rs, cv.COLOR_BGR2RGB))
            frame_rsc = resz(cv.cvtColor(frame_rsc, cv.COLOR_BGR2RGB))
            frame = cv.hconcat([frame_rs, frame_rsc])
            frames.append(frame)
        else:
            break

    imageio.mimsave(gif_path, frames[args.start : args.end : args.step], "GIF", duration=1.0 / fps)
