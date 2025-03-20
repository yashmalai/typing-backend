FROM python:3.11-slim

WORKDIR /home/typing

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x /home/typing/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["sh", "/home/typing/entrypoint.sh"]