import pandas as pd
import streamlit as st
import time


def section_divider():
    st.write("---")

def loading_animation():
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        bar.progress(i + 1)
        time.sleep(0.01)

