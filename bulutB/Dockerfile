FROM python:3.12-slim

WORKDIR /app

# Bağımlılıklar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodu
COPY . .

# Cloud Run varsayılanı
ENV PORT=8080
EXPOSE 8080

# Üretim tipi çalıştırma (önerilen)
CMD ["gunicorn", "-b", ":8080", "main:app"]
