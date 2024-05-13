# 1. Python 3.9 imajını temel al
FROM python:3.9

# 2. Çalışma dizinini /app olarak ayarla
WORKDIR /app

# 3. Uygulama dosyalarını Docker içine kopyala (/app dizinine)
COPY ./app /app

# 4. Gerekli Python paketlerini yükle (requirements.txt dosyasındaki bağımlılıkları yükle)
RUN pip install -r requirements.txt
