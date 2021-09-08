FROM python:3.9 AS builder
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /bot
COPY main.py /bot
COPY tafe.py /bot
COPY quote.py /bot

FROM python:3.9-slim
WORKDIR /bot
COPY --from=builder /bot /bot 

EXPOSE 443

CMD ["python3", "main.py"]
