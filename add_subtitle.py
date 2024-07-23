from moviepy.editor import *
import pandas as pd 

def addSubtitle(text, video):
    """ 
        Given a video and transcript for each time step, it generate the video with the trancript

        Parameters:
        transcript -> must be a location of tsv/csv file with there three column: start, end, text(usually taken from generated from whisper model)
        video -> must be location of a video file
    """
    captions = pd.read_csv(transcript, sep='\t').to_dict('records')
    clip = VideoFileClip(video)

    arr = []
    for caption in captions:
        txt_clip = TextClip(caption["text"], fontsize = 10, color = 'yellow')
        txt_clip = txt_clip.set_pos(("center","bottom")).set_start(caption["start"]/1000).set_end(caption["end"]/1000)
        arr.append(txt_clip)
                                                                
    arr.insert(0, clip)  

    return CompositeVideoClip(arr) 


if __name__ == "__main__":
    video = addSubtitle('audio.tsv','samplevideo.mp4')
    video.write_videofile("samplevideo_composition.mp4")
