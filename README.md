## Video Frame Extractor Script 

This Python script extracts frames from a video file at specified intervals and saves them as image files in a desired format. It offers flexibility to customize frame extraction frequency, output image format, and preview the estimated number of output images before extraction.

### Features

* Input Video Path (-i): Allows specifying the path to the input video file.
* Frame Interval (-f): Determines how many frames to skip between saving images (default is every frame, i.e., 1).
* Output Format (-o): Specifies the format of the output image files (jpg or png).
* Dry Run (-d): Displays the estimated number of output images before proceeding and asks for user confirmation.

### Usage

To run the script, use the following command structure:

```bash
python video2image.py -i <video_path> -f <frame_interval> -o <output_format> [-d]
```

### Command-Line Arguments

* `-i`: (Required) Path to the input video file.
* `-f`: (Optional) Number of frames to skip between saved images. Default is 1 (saves every frame).
* `-o`: (Optional) Output image file format. Choices are jpg or png. Default is jpg.
* `-d`: (Optional) Enables a dry run mode, where the script displays the estimated number of output images and waits for the user to press Enter to proceed.

### Example Commands

**Estimate the number of output images without saving:**

```bash
python video2image.py -i path_to_your_video_file.mp4 -f 10 -d
```

This command calculates and displays the estimated number of output images for the given video file, extracting one image every 10 frames. The script waits for the user to press Enter to continue.

**Extract and save frames as PNG images:**

```bash
python video2image.py -i path_to_your_video_file.mp4 -f 10 -o png
```

This command extracts frames from the specified video file every 10 frames and saves them as PNG images.

### Code Explanation

**Argument Parsing:**

The script uses the `argparse` module to handle command-line arguments, making it easy to specify the input video file, frame interval, output format, and dry run mode.

**Video File Handling:**

The script opens the specified video file using `cv2.VideoCapture` and checks if it was successfully opened. If not, it exits with an error message.

**Frame Extraction:**

The total number of frames in the video is obtained using `cv2.CAP_PROP_FRAME_COUNT`.

If the `-d` option is specified, the script calculates and displays the estimated number of output images (`total_frames // args.f`) and waits for user confirmation to proceed.

**Image Saving:**

The script iterates through the frames of the video and saves an image at the specified interval (`args.f`).

The output images are named based on the input video file name and frame number, following the format: `<video_name>_frame_<number>.<format>`.

**User Confirmation:**

If the `-d` option is enabled, the script waits for user input (Enter key) to continue the extraction process, providing a chance to review the estimated output.

### Dependencies

* Python 3.x
* OpenCV (cv2)
* `argparse` module (part of the Python standard library)

### Installation

To use this script, ensure you have Python 3 and OpenCV installed. You can install OpenCV using pip:

```bash
pip install opencv-python
```

### Conclusion

This script provides a flexible and user-friendly way to extract frames from a video file. With customizable options for frame interval, output format, and a dry run mode, users can efficiently manage video-to-image extraction tasks.
