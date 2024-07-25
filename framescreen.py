import av
from PIL import Image
import argparse
import os

def save_frames(video_path, frame_numbers):
    container = av.open(video_path)
    stream = container.streams.video[0]

    print("Processing video...")

    frame_index = 0
    frame_numbers_set = set(frame_numbers)

    try:
        for frame in container.decode(video=0):
            if frame_index in frame_numbers_set:
                img = frame.to_image()

                if isinstance(img, Image.Image):
                    output_filename = f'frame_{frame_index}.jpg'
                    img.save(output_filename)
                    print(f"Saved frame {frame_index} as {output_filename}")
            frame_index += 1

            if frame_index > max(frame_numbers):
                break
    except Exception as e:
        print(f"Error decoding video: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from video")
    parser.add_argument('-i', '--input', required=True, help="Path video file")
    parser.add_argument('-f', '--frames', required=True, help="Comma-separated list of frame numbers")
    args = parser.parse_args()

    video_path = args.input
    frame_numbers = list(map(int, args.frames.split(',')))

    if not os.path.isfile(video_path):
        print(f"Error: The file {video_path} does not exist.")
    else:
        save_frames(video_path, frame_numbers)
