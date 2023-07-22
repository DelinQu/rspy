# use opencv read video and center crop
import argparse

import cv2 as cv

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, default="video.mp4", help="video path")
parser.add_argument("--ratio", type=float, default=0.01, help="crop ratio")
parser.add_argument("--output", type=str, default="video.mp4", help="output path")

args = parser.parse_args()

if __name__ == "__main__":
    video = cv.VideoCapture(args.input)
    FPS = video.get(cv.CAP_PROP_FPS)
    frames = []
    while True:
        ret, frame = video.read()
        if ret:
            h, w = frame.shape[:2]
            h_crop = int(h * args.ratio)
            w_crop = int(w * args.ratio)
            frame = frame[:, w_crop : w - w_crop * 2]
            frame = cv.resize(frame, (640, 480))
            frames.append(frame)
        else:
            break
    video.release()

    writer = cv.VideoWriter(args.output, cv.VideoWriter_fourcc(*"mp4v"), FPS, (frames[0].shape[1], frames[0].shape[0]))
    for frame in frames:
        writer.write(frame)
    writer.release()
