FROM python:3.12-slim

WORKDIR /app

COPY canbeshipped.py .
COPY digital_product.py .
COPY physical_product.py .
COPY product.py .
COPY file.py .
COPY inventory.json .
COPY main.py .
COPY order.py .
COPY orderline.py .
COPY inventory.py .
COPY supplier.py .

CMD ["python", "main.py"]