import streamlit as st
import os
import time
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

import pandas as pd
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.visualization import VisualizationTools

# Create a Streamlit app: Title and Instructions

# Add a place to enter the API key
with st.sidebar:
    st.write("Add your Gemini API key")
    api_key = st.text_input("GOOGLE_API_KEY", type="password")

st.title("Welcome to the Data Analyst App")
st.caption("Once you upload a file, the app will generate a report with graphics and insights based on the data in the file.")
st.divider()

# File Uploader
st.subheader("Upload a file to get started:")
uploaded_file = st.file_uploader("Choose a file", type="csv")


if st.button("Generate Report"):
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    # Load data Function
    def load_data(file_path):
        """
        Load data from a given CSV file path and convert it to a JSON string of records.

        Parameters
        ----------
        file_path : str = The path to the CSV file to load.

        Returns:  A JSON string of records representing the data in the CSV file.
        """
        return pd.read_csv(file_path).to_json(orient="records")

    # Progress bar update
    my_bar.progress(25, text=progress_text)

    # Create an agent with visualization capabilities
    viz_agent = Agent(
        model=Gemini(id="gemini-2.0-flash", api_key=api_key),
        tools=[VisualizationTools(output_dir="charts")],
        instructions=[
            "You are a data visualization expert and business analyst.",
            "Read the data from using the load_data tool.",
            "Create a brief report for the data in context {dataset}. Be concise.",
            "Suggest the most appropriate charts and graphs based on the provided data"
            "Create up to 5 charts for each data set.",
            "To create charts, use the 'VisualizationTools' available.",
            "Always provide meaningful titles, axis labels, and context.",
            "For each chart, suggest insights based on the data visualized.",
            "Format data appropriately for each chart type.",
        ],
        context={"dataset": load_data(uploaded_file)},
        add_context=True,
        show_tool_calls=True,
        markdown=True,
    )

    # Progress bar update
    my_bar.progress(50, text=progress_text)

    # Run the agent
    response = viz_agent.run("Create a report for the data in context.")

    # Progress bar update
    my_bar.progress(100, text=progress_text)

    # Display the generated report
    st.subheader("Generated Report:")
    st.write(response.content)
    

    # Display the generated charts
    st.subheader("Generated Charts:")
    chart_files = os.listdir("charts")
    for chart_file in chart_files:
        chart_path = os.path.join("charts", chart_file)
        chart_image = Image.open(chart_path)
        st.image(chart_image, caption=chart_file)

