import numpy as np
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
table=pd.DataFrame({"colum 1":[1,2,3,4,5,6,7],"column 2":[11,12,13,14,15,16,17]})
from matplotlib import pyplot as plt
x=np.linspace(0,10,100)


st.title("hii im streamlot")
st.subheader("hi this is shantanu")
st.header("I am header")
st.text("holaa this is shantanu, this is my new program on streamlit")
st.markdown(" *italicized text*")
st.markdown("---")
st.caption("hi im caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print("helo world")
def fucnt():
dvsdvr
kartik chumtiya
return 0;"""
st.code(code,language="python")
st.table(table)
st.dataframe(table)
st.image("image.jpg", caption="this is my car", width=700)
st.audio("audio.mp3")
st.video("video.mp4")
st.button('Click me')
checkbox_state = st.checkbox("Toggle me")

if checkbox_state:
    st.write("Checkbox is ON")
else:
    st.write("Checkbox is OFF")
    
radio_btn=st.radio("in which country do u live", options=("us","india","brazil"))
print(radio_btn)

st.selectbox('Pick one', ['cats', 'dos'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('tell something about u')
st.date_input("today date")
st.time_input('Meeting time')
st.file_uploader('Upload a file', type=["png"])

st.markdown("---")
st.markdown("# Registration")
with st.form("form2"):
    col1, col2 = st.columns(2)
    f_name=col1.text_input("First name")
    l_name=col2.text_input("Last name")
    form_email = st.text_input("Email")
    form_password = st.text_input("Password", type="password")
    form_number = st.text_input("Number")
    day,month,year=st.columns(3)
    day.text_input("day")
    month.text_input("month")
    year.text_input("year")
    s_state=form_submit_button = st.form_submit_button("Submit")
    if s_state:
        if f_name =="" and l_name=="":
            st.warning("plss barra re form")
        else:
            st.success("array waah")
    st.title("Embed YouTube Video")



youtube_url = "https://www.youtube.com/watch?v=AGxza2_oEcA&ab_channel=StewieTV"
st.video(youtube_url)
            
st.markdown("---")

opt=st.sidebar.radio("select any graph", options=["line", "bar"])
if opt=="line":
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x),'--')
    st.write(fig)
    