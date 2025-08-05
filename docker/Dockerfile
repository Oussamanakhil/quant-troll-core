# === 🧠 Stored Execution Rules ===
# - Creates reproducible environment
# - Installs dependencies from requirements.txt
# - Supports Streamlit + MLflow if needed

FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "dashboard/streamlit_dashboard.py"]
