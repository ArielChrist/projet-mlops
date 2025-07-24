FROM python:3.11-slim

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src/
COPY configs/ configs/
COPY run_api.py .


EXPOSE 8000

CMD ["python", "run_api.py"]