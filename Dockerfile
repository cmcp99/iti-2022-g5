# 
FROM python:3.9

# 
WORKDIR /iti-2022-g5

# 
COPY ./requirements.txt /iti-2022-g5/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /iti-2022-g5/requirements.txt

# 
COPY ./server.py /iti-2022-g5/

# 
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
