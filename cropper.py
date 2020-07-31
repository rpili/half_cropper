import ffmpy

ff = ffmpy.FFmpeg(
        inputs={'2020-07-28 11-18-38.mp4': None},
        outputs={'output_a.mp4': ['-filter:v', 'crop=100:100:500:500'],
                 'output_b.mp4': ['-filter:v', 'crop=100:100:300:300']}
        )

print(ff.cmd)

halfcrop = ffmpy.FFmpeg(
        inputs={'2020-07-28 11-18-38.mp4': None},
        outputs={'half_left.mp4': ['-filter:v', 'crop=in_w/2:in_h:0:0'],
                 'half_right.mp4': ['-filter:v', 'crop=in_w/2:in_h:in_w/2:in_h']}
        )

print(halfcrop.cmd)
halfcrop.run()

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
