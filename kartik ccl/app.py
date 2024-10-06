import streamlit as st
def main():
    st.markdown("<h1 style='text-align: center;'>Video Streaming</h1>", unsafe_allow_html=True)
    
    vid1,vid2,vid3,vid4,vid5 = st.columns(5)

    if vid1.button("20770858-hd_1080_1920_30fps.mp4"):
        video1()
    if vid2.button("20600550-hd_1920_1080_30fps.mp4"):
        video2()
    if vid3.button("20576968-hd_1920_1080_25fps.mp4"):
        video3()
    if vid4.button("15921892-hd_1920_1080_50fps.mp4"):
        video4()
    if vid5.button("6060027-hd_1080_1920_25fps.mp4"):
        video5()





def video1():
    VIDEO_FILENAME = "6060027-hd_1080_1920_25fps.mp4"  # Replace with your video filename
    st.markdown("<h1 style='font-family: Arial, sans-serif;font-style: italic;text-align: left;font-size: 18px;'>How to eat sushi with chop stick.</h1>", unsafe_allow_html=True)
    video_file = open(VIDEO_FILENAME, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

def video2():
    VIDEO_FILENAME = "15921892-hd_1920_1080_50fps.mp4"  # Replace with your video filename
    st.markdown("<h1 style='font-family: Arial, sans-serif;font-style: italic;text-align: left;font-size: 18px;'>Cow Wandering in Field</h1>", unsafe_allow_html=True)
    video_file = open(VIDEO_FILENAME, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

def video3():
    VIDEO_FILENAME = "20576968-hd_1920_1080_25fps.mp4"  # Replace with your video filename
    st.markdown("<h1 style='font-family: Arial, sans-serif;font-style: italic;text-align: left;font-size: 18px;'>Sunset Spot</h1>", unsafe_allow_html=True)
    video_file = open(VIDEO_FILENAME, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

def video4():
    VIDEO_FILENAME = "20600550-hd_1920_1080_30fps.mp4"  # Replace with your video filename
    st.markdown("<h1 style='font-family: Arial, sans-serif;font-style: italic;text-align: left;font-size: 18px;'>Manali </h1>", unsafe_allow_html=True)
    video_file = open(VIDEO_FILENAME, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

def video5():
    VIDEO_FILENAME = "20770858-hd_1080_1920_30fps.mp4"  # Replace with your video filename
    st.markdown("<h1 style='font-family: Arial, sans-serif;font-style: italic;text-align: left;font-size: 18px;'>Rajastan </h1>", unsafe_allow_html=True)
    video_file = open(VIDEO_FILENAME, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)


if __name__ == "__main__":
    main()
