FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Create non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

CMD ["python", "app.py"]