import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_lottie as st_lottie
import json
import requests

st.set_page_config(page_title="AI Power Meter", page_icon="⚡", layout="wide")

# Load Lottie animation
@st.cache_data
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

lottie_ai = load_lottie_url("https://lottie.host/1201d027-c58a-497b-bc7f-878db0de4139/DH9UDviexx.json")  # Updated to Nature-related animation

# Energy Calculation Functions
def calculate_energy_usage(prompts):
    electricity_per_prompt = 0.002  # Each prompt consumes 0.002 kWh
    co2_per_prompt = 0.0005  # Each prompt emits 0.0005 kg CO2
    total_energy = prompts * electricity_per_prompt
    total_co2 = prompts * co2_per_prompt
    return total_energy, total_co2

def calculate_training_impact(models):
    training_energy = models * 2  # Training one small model uses 2 kWh
    training_co2 = models * 0.5  # Training one model emits 0.5 kg CO2
    return training_energy, training_co2

# App Configuration
st.title("⚡ AI Power Meter: Energy & Impact")
st.subheader("💡 Discover how AI usage consumes energy and affects the environment")

if lottie_ai:
    st_lottie.st_lottie(lottie_ai, height=200)
st.markdown("---")

# User Input for AI Queries
st.header("🔎 AI Prompt Energy Usage")
prompts = st.number_input("Enter the number of AI prompts you generate per day", min_value=1, value=10)
if st.button("Calculate AI Usage Impact"):
    total_energy, total_co2 = calculate_energy_usage(prompts)
    st.metric(label="⚡ Total Energy Used (kWh)", value=f"{total_energy:.3f}")
    st.metric(label="🌍 CO₂ Emissions (kg)", value=f"{total_co2:.4f}")
    data_prompt = pd.DataFrame({
        "Category": ["Electricity Used (kWh)", "CO2 Emissions (kg)"],
        "Value": [total_energy, total_co2]
    })
    fig_prompt = px.bar(data_prompt, x="Category", y="Value", color="Category", title="Energy & Emissions per AI Usage")
    st.plotly_chart(fig_prompt)

st.markdown("---")

# User Input for AI Model Training Impact
st.header("🤖 AI Model Training Impact")
models = st.number_input("Enter the number of small AI models trained", min_value=1, value=1)
if st.button("Calculate Training Impact"):
    training_energy, training_co2 = calculate_training_impact(models)
    st.metric(label="🔋 Total Training Energy Used (kWh)", value=f"{training_energy:,}")
    st.metric(label="☁️ Training CO₂ Emissions (kg)", value=f"{training_co2:,}")
    data_training = pd.DataFrame({
        "Category": ["Training Electricity Used (kWh)", "Training CO2 Emissions (kg)"],
        "Value": [training_energy, training_co2]
    })
    fig_training = px.bar(data_training, x="Category", y="Value", color="Category", title="AI Model Training Energy Impact")
    st.plotly_chart(fig_training)

st.markdown("---")

# How AI Affects the Environment
st.header("⚠️ Environmental Impact of AI")
with st.expander("🔋 Energy Consumption Crisis"):
    st.write("AI data centers require enormous electricity, increasing grid loads and fossil fuel dependency.")
with st.expander("🌡️ Carbon Footprint Increase"):
    st.write("AI-related CO2 emissions contribute to climate change, raising global temperatures.")
with st.expander("📉 E-Waste from AI Hardware"):
    st.write("The demand for AI accelerates GPU and chip production, leading to more e-waste.")

st.markdown("---")

# Solutions for Sustainable AI
st.header("🌱 Towards a Greener AI Future")
st.write("✔ Transition to AI models powered by renewable energy sources.")
st.write("✔ Optimize AI algorithms for lower energy consumption.")
st.write("✔ Encourage sustainable AI policies and carbon-neutral data centers.")

if st.button("I support Green AI! 🌍"):
    st.success("Great! Every step towards sustainability counts! 🌿")

st.markdown("---")
st.write("💡 *Think before you prompt Unnecessarily! AI usage has a real-world environmental cost.*")

# Footer
st.markdown("---")
st.markdown("**Designed & Developed with ♥ by: Vivek Singh | [LinkedIn] (https://www.linkedin.com/in/vivek-singh-858941201/)**"
st.markdown("**Team: ♥ (Vivek Singh, Aditya Rudola and Madhav Arora)**")
st.markdown("© 2025 AI Power Meter. All rights reserved.")
