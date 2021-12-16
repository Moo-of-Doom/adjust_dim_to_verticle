import moviepy.editor as mpy
from moviepy.editor import clips_array


LENGTH = '00:00:24.00'

vcodec = "libx264"

videoquality = "24"

RESOLUTION = (720,720)
BANNER_RES = (280,720)
FILE_LOCATION = r"C:\Users\mooof\OneDrive\Desktop"


"slow, ultrafast, veryfast, fast, faster, medium, slower, veryslow --- only one, these are options"
compression = "slow"

title = "test"
banner_title_top = "Banner Top"
banner_title_bot = "Banner Bot"

bannerT = banner_title_top
bannerB = banner_title_bot

loadtitle = FILE_LOCATION + r"\Clips\\" + title + ".mp4"
loadbannerT = FILE_LOCATION + r"\Clips\\" + bannerT + ".mp4"
loadbannerB = FILE_LOCATION + r"\Clips\\" + bannerB + ".mp4"

savetitle = FILE_LOCATION + r"\Reformat Clips\\" + title + ".mp4"  #lets you change the file format



cuts = [('00:00:00.00', LENGTH)]

def edit_video(loadtitle, savetitle, cuts):
    #load file
    video = mpy.VideoFileClip(loadtitle, target_resolution=RESOLUTION)
    videoT = mpy.VideoFileClip(loadbannerT, target_resolution=BANNER_RES)
    videoB = mpy.VideoFileClip(loadbannerB, target_resolution=BANNER_RES)
    # Sample of clip edits
    #
    # video1 = video.subclip('00:00:10.00', '00:00:20.00')
    # video2 = video.subclip('00:00:22.00', '00:00:28.00')
    # video3 = video.subclip('00:00:35.00', '00:00:45.00')
    #
    # clips = [video1,video2,video3]
    # final_clip = mpy.concatenate_videoclips(clips)
    #
    # ex2:
    #
    # video1 = video.cutout("00:00:15.00", "00:00:45.00")
    # this gets a little sketchy so becareful





    #cut file
    clips = []


    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)



    clip_T = videoT.subclip(cut[0], cut[1])
    clip_B = videoB.subclip(cut[0], cut[1])

    clip_T.set_position((0,0))
    clip_B.set_position((0,280))
    final_clip = mpy.concatenate_videoclips(clips)

    final_clip.set_position((0,1000))


    final_clip = clips_array([[clip_T],
                             [final_clip],
                             [clip_B]])
    #adding text
    #
    # txt = mpy.TextClip(r"Subscribe! Find long form videos on youtube.com/Wolfabelle", font='Courier', fontsize=120, color='white', bg_color='gray35')
    # txt = txt.set_position(('center', 0.6),relative=True)
    # txt = txt.set_start((0,21)) #(min, s) will be at the end of the video
    # txt = txt.set_duration(2)  #how many seconds will it stay up?
    # txt = txt.crossfadein(0.5)
    # txt = txt.crossfadeout(0.5)

    final_clip = mpy.CompositeVideoClip([final_clip])


    #save
    final_clip.write_videofile(savetitle, threads=4, fps=24, codec=vcodec, preset=compression, ffmpeg_params=["-crf",videoquality])

    video.close()

if __name__ == '__main__':
    print("boosh")
    edit_video(loadtitle,savetitle,cuts)

















