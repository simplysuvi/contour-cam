# import cv2
# import streamlit as st
# from streamlit_webrtc import VideoTransformerBase, webrtc_streamer, WebRtcMode


# class VideoTransformer(VideoTransformerBase):
#     def __init__(self):
#         self.threshold1 = 100
#         self.threshold2 = 100

#     def transform(self, frame):
#         img = frame.to_ndarray(format="bgr24")
#         edged = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)
#         return edged


# st.title("Contour Detection App")
# st.subheader("Contour detection to highlight edges in a live video feed.")
# webrtc_ctx = webrtc_streamer(
#     key="stream",
#     mode=WebRtcMode.SENDRECV,
#     video_processor_factory=VideoTransformer,
#     media_stream_constraints={"video": True, "audio": False},
#     async_processing=True,
# )
# # ctx = webrtc_streamer(key="stream", video_transformer_factory=VideoTransformer)

# if webrtc_ctx.video_transformer:
#     if webrtc_ctx.video_transformer:
#         webrtc_ctx.video_transformer.threshold1 = st.slider("Threshold 1", 0, 1000, 100)
#         webrtc_ctx.video_transformer.threshold2 = st.slider("Threshold 2", 0, 1000, 200)

import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer


class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

        return img


webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
