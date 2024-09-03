import cv2
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Extract frames from a video file.')
    parser.add_argument('-i', type=str, required=True, help='Path to the input video file')
    parser.add_argument('-f', type=int, default=1, help='Number of frames to skip between saved images (default: 1)')
    parser.add_argument('-o', type=str, default='jpg', choices=['jpg', 'png'], help='Output image file format (default: jpg)')
    parser.add_argument('-d', action='store_true', help='Display the estimated number of output images without saving them')
    args = parser.parse_args()

    video_path = args.i
    video_name = os.path.splitext(os.path.basename(video_path))[0] 
    output_folder = os.path.join(os.getcwd(), 'output')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file at {video_path}.")
        exit()

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    estimated_images = total_frames // args.f

    if args.d:
        print(f"Estimated number of output images: {estimated_images}")
        input("Proceed? Press ENTER to proceed or Ctrl+C to cancel.")

    frame_count = 0
    save_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % args.f == 0:
            output_file = os.path.join(output_folder, f'{video_name}_frame_{save_count:04d}.{args.o}')
            cv2.imwrite(output_file, frame)
            save_count += 1

        frame_count += 1

    cap.release()

    print(f"Frames extracted and saved to {output_folder}")

if __name__ == '__main__':
    main()
