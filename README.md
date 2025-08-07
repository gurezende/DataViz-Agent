# 📊 Data Analyst App powered by Gemini AI

Welcome to the **Data Analyst App** – a Streamlit-powered web application that allows you to upload CSV datasets and automatically generates insightful visual reports using Google Gemini and Agno AI agents.

---

## 📌 Project Description

This app leverages the **Gemini LLM** through the **Agno agentic framework**, alongside visualization tools, to automate the process of data analysis and reporting. Once you upload a dataset, the app:
- Loads and processes your data
- Infers useful visualizations (up to 5 charts)
- Summarizes key insights
- Displays interactive charts and findings

Perfect for analysts, business users, and anyone who wants **automated exploratory data analysis** in seconds.

---

## 🛠 Requirements

- Python 3.8+
- Google Gemini API key  
- Virtual environment (recommended)

**Python Libraries:**
- `streamlit`
- `pandas`
- `Pillow`
- `python-dotenv`
- `agno` (Agno agent framework)

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/data-analyst-app.git
cd data-analyst-app
```

2. Set up your environment variables:
Create a `.env` file in the root directory and add your Gemini API key:

3. Run the Streamlit app:

```bash
streamlit run scritps/app.py
```

If you are running directly from the deployed app:
1. Use the sidebar to enter your API key

2. upload your CSV file

3. Click “Generate Report”.

## 🧠 Code Brief Explanation

* `app.py`: Main Streamlit script handling UI, file upload, progress bar, and chart display.
* `load_data()`: Reads the uploaded CSV and converts it into JSON records.
* `Agent`: Created using agno.agent.Agent, connected to the Gemini model and equipped with visualization tools.
* `VisualizationTools`: Handles automatic chart generation based on dataset insights.
* `charts/`: Stores the PNG image files generated from the data.

## 📽 Demonstration

Here’s how the app works in action:

![](img/output.gif)

Upload a CSV file.

App uses Gemini + Agno to interpret and visualize.

Report + charts are shown instantly.

## 👨‍💻 Abo0ut

This project was built to demonstrate how AI agents can:

* Automate exploratory data analysis
* Interpret raw data
* Generate meaningful charts and business insights

Built with ❤️ using:

* Agno
* Gemini API
* Streamlit

### Developed by [Gustavo R. Santos](https://gustavorsantos.me)

## 📄 License
This project is licensed under the MIT License.