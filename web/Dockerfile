FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: improves reload speed
RUN pip install watchdog

CMD ["streamlit", "run", "main.py", "--server.port=8502", "--server.address=0.0.0.0", "--server.runOnSave=true"]
