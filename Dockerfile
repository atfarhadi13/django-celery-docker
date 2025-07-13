# ---------- base ----------
FROM python:3.12-slim

# ---------- runtime opts ----------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ---------- workdir ----------
WORKDIR /app

# ---------- install deps ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- project code ----------
COPY . .

# ---------- expose + default cmd ----------
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
