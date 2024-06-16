import streamlit as st
import json
import base64
import pickle
import pandas as pd


@st.cache_data
def load_anime(url):
    anime = json.load(url)
    return anime

# Function to convert image to base64
@st.cache_data
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

@st.cache_data
def raw_values():
    brands = ['Samsung', 'Apple', 'Sony', 'Huawei', 'Xiaomi', 'Infinix', 'Tecno', 'Nokia']
    rams = [1, 2, 3, 4, 6, 8, 10, 12, 15, 16, 18]
    internal_storages = [2, 8, 16, 31, 32, 64, 128, 164, 256, 265, 512]
    batteries = [2000, 3000, 4000, 4500, 5000, 6000]
    main_cameras = [2, 3, 5, 8, 12, 13, 16, 20, 25, 32, 40, 48, 50, 64, 100, 108, 200]
    front_cameras = [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 20, 24, 25, 32, 40, 44, 48, 50, 60]
    displays = [5.5, 6.0, 6.5, 7.0, 7.5]
    has_5g_options = ['No', 'Yes']
    return brands,rams,internal_storages,batteries,main_cameras,front_cameras,displays,has_5g_options

@st.cache_data
def load_model():
    with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model

frequency_encoding = {    
    'Infinix': 90 / 1000,     
    'Xiaomi': 260 / 1000,     
    'Samsung': 218 / 1000,    
    'Tecno': 125 / 1000,      
    'Realme': 43 / 1000,      
    'Huawei': 73 / 1000,      
    'OPPO': 67 / 1000,        
    'Nokia': 56 / 1000,       
    'Apple': 55 / 1000,           
    'Google Pixel': 18 / 1000,
    'Sony': 3 / 1000,      
}

@st.cache_data
def predict_price(_model, brand, ram, internal_storage, battery, main_camera, front_camera, display, has_5g): 
    has_5g = 1 if has_5g.lower() == 'yes' else 0    
    brand_encoded = frequency_encoding.get(brand, 0)  
    input_data = [[brand_encoded, ram, internal_storage, battery, main_camera, front_camera, display, has_5g]]
    predicted_price = _model.predict(input_data)
    return predicted_price[0]

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df