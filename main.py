import streamlit as st
from streamlit_lottie import st_lottie
import time
from modules import load_anime,img_to_base64,raw_values,load_model,predict_price,load_data
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(
    page_title="Predictly",
    page_icon="avatar_streamly.png",
    layout="wide",
    initial_sidebar_state="expanded",
    )
# -----------------------------------------------------------------top--------------------------------------------------------------------------------- #

col1, col2= st.columns(2)
with col1:
    colh1,colh2,colh3 = st.columns([0.4,0.3,0.2])
    with colh1:
        gradient_text_html = """
            <style>
            .gradient-text {
                font-weight: bold;
                background: -webkit-linear-gradient(left, red, orange);
                background: linear-gradient(to right, red, orange);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                display: inline;
                font-size: 3em;
            }
            </style>
            <div class="gradient-text">Predictly</div>
            """
        st.markdown(gradient_text_html, unsafe_allow_html=True)
    with colh2:
        
        with open('lottie/Anime.json', 'r') as f:
            st_lottie(load_anime(f), height=100)

with col2:
    col2,col3,col4 = st.columns(3)
    col2.metric("Leading smartphone brand ", "Samsung", "-")
    col3.metric("Smartphone users in Kenya", "33 M", "+")
    col4.metric("5G subscriptions", "500k", "+")

st.divider() 

# --------------------------------------------------------------------sidebar image------------------------------------------------------------------------------ #

st.markdown(
    """
    <style>
    .cover-glow {
        width: 100%;
        height: auto;
        padding: 3px;
        box-shadow:
            0 0 10px #301300, /* Dark brown */
            0 0 5px #602600, /* Deep orange */
            0 0 0px #903900, /* Reddish-orange */
            0 0 2px #301300, /* Bright orange */
            0 0 0px #301300, /* Vivid orange */
            0 0 0px #301300, /* Light orange */
            0 0 0px #602600; /* Pale orange */       
        position: relative;
        z-index: -1;
        border-radius: 30px;  /* Rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

img_base64 = img_to_base64("img/panther2.jpeg")
st.sidebar.markdown(
    f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

# --------------------------------------------------------------------sidebar info ------------------------------------------------------------------------------ #

with st.sidebar:
    col21,col22,co23 = st.columns([0.3,0.8,0.3])
    with col22:
        st.markdown("""
        <div style="text-align: center; background-color: #f0f0f0; padding: 0px 0px; border-radius: 10px;">
            <h3 style="color: #602600;"> About Predictly </h3>
        </div>
        """, unsafe_allow_html=True)
    
    st.write('')
    st.write("Predictly is a smart phone price prediction app powered by Streamlit and CatBoost. It helps you estimate phone prices and explore the latest smartphone data.")
    st.write('')

    st.markdown("""
    <div style="text-align: center;">
        <a href="https://github.com/snvice/predictly" target="_blank">GitHub Repository</a>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    colm3,colm1,colm2 = st.columns(3)
    with colm1:
        st.write("〰️〰️〰️")

    cols1,cols2 =st.columns([0.3,0.9])
    with cols2:
        gradient_text_html = """
            <style>
            .gradient-text {
                font-weight: bold;
                background: -webkit-linear-gradient(left, red, orange);
                background: linear-gradient(to right, red, orange);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                display: inline;
                font-size: 0.1em;
            }
            </style>
            <div class="gradient-text" style="font-size: 2em;">Predictly</div>
            """
        st.markdown(gradient_text_html, unsafe_allow_html=True)
    
    st.markdown("""
    <div align=center><small>
    <p1> Page views interaction</p1><br>
    <a href="https://www.cutercounter.com/" target="_blank"><img src="https://www.cutercounter.com/hits.php?id=hxpocnn&nd=4&style=44" border="0" alt="hit counter"></a>
    </small></div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------form------------------------------------------------------------------------------- #

if 'predicted' not in st.session_state:
    st.session_state.predicted = False
if 'price' not in st.session_state:
    st.session_state.price = None

css = """
<style>
    .stRadio > div {
        border-radius: 30px;
        border: 0.5px solid #FFFFCC;  
        padding: 10px;
        margin-bottom: 5px;
        box-shadow: 0 7px 4px rgba(0,0,0,0.15);
    }
    .stButton > button {
        font-weight: bold;
        color: white;
        background-color: #602600;
    }
    .city {
        color: white;
        font-size: 35px;  
    }
    .city2 {
        color: orange;
        font-size: 18px;  
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

with st.container():
    with st.form("form", clear_on_submit=False, border=False):

        colf1, colf2, colf3 = st.columns(3)
        brands, rams, internal_storages, batteries, main_cameras, front_cameras, displays, has_5g_options = raw_values()

        with colf2:
            with st.container():
                brand = st.radio('📱 Brand', brands, horizontal=True, index=None)
            with st.container():
                internal_storage = st.radio('📂 Internal Storage', internal_storages, horizontal=True, index=None)  #5
            with st.container():
                main_camera = st.radio('📸 Main Camera', main_cameras, horizontal=True, index=None)
            with st.container():
                display = st.radio('🖥️ Display', displays, horizontal=True, index=None)

        with colf3:
            with st.container():
                ram = st.radio('💾 RAM', rams, horizontal=True, index=None)            
            with st.container():
                battery = st.radio('🔋 Battery', batteries, horizontal=True, index=None)
            with st.container():
                front_camera = st.radio('🤳 Front Camera', front_cameras, horizontal=True, index=None)
            with st.container():
                has_5g = st.radio('5G', has_5g_options, horizontal=True, index=None)

        with colf1:
            with st.container():
                st.write("")
                st.write("")
                st.write("")
                with st.chat_message("assistant", avatar="./img/avatar_streamly.png"):
                    st.markdown("""
                    <div class="info-container">
                        <p class="city"> Welcome to <span class="highlight">Predictly</span>!</p>
                        <p class="city2">Enter phone specs to predict price 👉</p>      
                    </div>
                    """, 
                    unsafe_allow_html=True)
            with st.container():
                st.write("---")
            with st.container():
                cols1, cols2, cols3 = st.columns(3)
                with cols2:
                    submitted = st.form_submit_button("Predict")
            with st.container():   
                    st.write("")
                    if submitted:
                        if not all([brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g]):
                            st.warning("Please select options for all categories.")
                        else:
                            rf = load_model()
                            with st.spinner(text='Predicting price...'):
                                time.sleep(2)
                                price = predict_price(rf, brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g)
                                st.session_state.price = predict_price(rf, brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g)

                                html_temp = """
                                <div style="width:50%; background-color:#FF69B4; padding:2px; border-radius:5px; margin:0 auto;">
                                    <h3 style="color:black; text-align:center; font-size: 18px;">Predicted Price: KSh {:,.0f}</h3>
                                </div>
                                """
                                st.markdown(html_temp.format(price), unsafe_allow_html=True)
                                st.session_state.predicted = True
with st.container():
    colp1,colp2 = st.columns([0.8,0.2])
    with colp1:
        if st.session_state.predicted == False:
            show_data = st.toggle("Show phones in your predicted price bracket", value=False, disabled=True)
            colp1x,colpx2,colpx3 = st.columns(3)
            with colp1x:
                st.info("🚨 Please make a prediction first")
        else:
            show_data = st.toggle("Show phones in that price bracket", value=True)
            if show_data:
                df = load_data("./csv/prices.csv")
                min_price = st.session_state.price - 5000
                max_price = st.session_state.price + 5000
                sliced_df = df[(df['brand'] == brand) & (df['price'].between(min_price, max_price))].sort_values(by="price", ascending=True)
                st.write(sliced_df.head(5), hide_index=True)
    with colp2:
        style_image1 = """
        width: auto;
        max-width: 450px;
        height: auto;
        max-height: 250px;
        display: block;
        justify-content: center;
        border-radius: 10%;
        box-shadow:
            0 0 10px #301300, /* Dark brown */
            0 0 5px #602600, /* Deep orange */
            0 0 0px #903900, /* Reddish-orange */
            0 0 2px #301300, /* Bright orange */
            0 0 0px #301300, /* Vivid orange */
            0 0 0px #301300, /* Light orange */
            0 0 0px #602600; /* Pale orange */    
        """
        st.markdown(
            f'<img src="{"https://github.com/snvice/poa/blob/main/pink3.jpeg?raw=true"}" style="{style_image1}">',
            unsafe_allow_html=True,
)

st.divider()

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

css = """
<style>
    .city3 {
        color: white;
        font-size: 25px;  
    }
</style>
"""
with st.container(border=False):
    colpp1,colpp2 = st.columns([0.4,0.6])
    with colpp1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        with st.chat_message("assistant", avatar="./img/avatar_streamly.png"):
            st.markdown("""
            <div class="info-container">
            <p class="city3">Predictly can also help you find a phone based on your price budget.</p>
            <p class="city3">Select the price to get started.</p>      
            </div>
            """, 
            unsafe_allow_html=True)
    with colpp2:
        number = st.slider("Set your price 🚀", min_value=2000, max_value=120000, step=100, value=48000)
        colppp1, colppp2 = st.columns([0.99, 0.01])
        with colppp1:
            df = load_data("csv/prices.csv")
            min_price = number - 5000
            max_price = number + 5000
            sliced_df = df[df['price'].between(min_price, max_price)].sort_values(by="price", ascending=True)
            st.write(sliced_df.head(5), hide_index=True)
            
st.divider()

# ----------------------------------------------------------------pygwalker---------------------------------------------------------------------------------- #

css = """
<style>
    .city3 {
        color: white;
        font-size: 18px;  
    }
</style>
"""

with st.chat_message("assistant", avatar="./img/stuser.png"):
            st.markdown("""
            <div class="info-container">
            <p class="city3">Explore and visualize phone data interactively with our advanced analytics tool.</p>
            <p class="city3">Use the interface below to start your data exploration journey!</p>
            </div>
            """, 
            unsafe_allow_html=True)

@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = load_data("csv/filtered.csv")
    return StreamlitRenderer(df, spec="./walker_config.json", spec_io_mode="rw", appearance='light')

renderer = get_pyg_renderer()
renderer.explorer()

placeholder = st.empty()
with placeholder.container():
        colb1,colb2,colb3 = st.columns([0.6,0.5,0.3])
        with colb2:
            button = st.button("Hit me")

if 'clicked' not in st.session_state: 
    if button:
        st.snow()
        placeholder.empty()

st.divider()
