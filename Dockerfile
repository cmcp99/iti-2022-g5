# 
FROM python:3.9

# 
WORKDIR /iti-2022-g5

# 
COPY ./requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# 
COPY ./server.py .

# 
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
