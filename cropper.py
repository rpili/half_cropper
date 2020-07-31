import argparse
import ffmpy
import sys 
import re


'''
# original testing code -- cropping random squares to validate
ff = ffmpy.FFmpeg(
        inputs={'2020-07-28 11-18-38.mp4': None},
        outputs={'output_a.mp4': ['-filter:v', 'crop=100:100:500:500'],
                 'output_b.mp4': ['-filter:v', 'crop=100:100:300:300']}
        )

# ff.cmd is a string containing the input to FFmpeg / aka tha FFmpeg command
print(ff.cmd)

# working halfcrop, input filename hard coded in
halfcrop = ffmpy.FFmpeg(
        inputs={'2020-07-28 11-18-38.mp4': None},
        outputs={'half_left.mp4': ['-filter:v', 'crop=in_w/2:in_h:0:0'],
                 'half_right.mp4': ['-filter:v', 'crop=in_w/2:in_h:in_w/2:in_h']}
        )

# printing and running 
print(halfcrop.cmd)
halfcrop.run()
'''

def main():
    # creating a parser object
    crop_parser = argparse.ArgumentParser(description="Crop a video into a left and a right half.")

    # adding arguments to the parser object
    # adding positional argument: video
    crop_parser.add_argument('video',
                             metavar='video',
                             type=str,
                             help='the video you are cropping')
    crop_parser.add_argument('--l',
                             metavar='left',
                             type=str,
                             default='left',
                             help='the output file name for the left crop')
    crop_parser.add_argument('--r',
                             metavar='right',
                             type=str,
                             default='right',
                             help='the output file name for the right crop')

    args = crop_parser.parse_args()
    cropper(args)

def cropper(args):
    findtype  = re.search(r"(\.[a-zA-Z\d]+)", args.video)
    filetype = findtype.group(1)
    left_filename = args.l + filetype
    right_filename = args.r + filetype
    halfcrop = ffmpy.FFmpeg(
            inputs={args.video : None},
            outputs={left_filename : ['-filter:v', 'crop=in_w/2:in_h:0:0'],
                    right_filename : ['-filter:v', 'crop=in_w/2:in_h:in_w/2:in_h']}
            )
    print(halfcrop.cmd)
    halfcrop.run()
    print(f"cropped {args.video} into {args.l} and {args.r}")

if __name__ == '__main__':
    main()

# ffmpeg -i in.mp4 -filter:v "crop=out_w:out_h:x:y" out.mp4
#   out_w is the width of the output rectangle
#   out_h is the height of the output rectangle
#   x and y specify the top left corner of the output rectangle

# to get the bottom right quarter
# ffmpeg -i in.mp4 -filter:v "crop=in_w/2:in_h/2:in_w/2:in_h/2" -c:a copy out.mp4
# input image size can be referred to with: "in_w" and "in_h"
# output image size can be referred to with: "out_w" and "out_h"

# obs recording
#   size = 1280x720
