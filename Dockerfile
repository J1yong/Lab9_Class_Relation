FROM python:3.12-slim

WORKDIR /app

COPY canbeshipped.py .
COPY digital_product.py .
COPY physical_product.py .
COPY product.py .
COPY file_manager.py .
COPY inventory_manager.py .
COPY inventory.json .
COPY main.py .

CMD ["python", "main.py"]