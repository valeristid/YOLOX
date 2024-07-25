import av
import argparse
import os

def count_frames(video_path):
    container = av.open(video_path)
    stream = container.streams.video[0]

    frame_count = 0
    for frame in container.decode(video=0):
        frame_count += 1

    print(f"Total number of frames: {frame_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count frames in video")
    parser.add_argument('-i', '--input', required=True, help="Path to the input video file")
    args = parser.parse_args()

    video_path = args.input

    if not os.path.isfile(video_path):
        print(f"Error: The file {video_path} does not exist.")
    else:
        count_frames(video_path)
