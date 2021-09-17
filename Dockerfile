# Multi stage build to reduce the size of image from around 900MB to 120MB a diffence of 152.94%
# Setting up python and installing pip packages required
FROM python:3.9 AS builder
COPY requirements.txt .
RUN pip install -r requirements.txt

# Creating a working directory and copying files needed
WORKDIR /bot
COPY main.py /bot
COPY tafe.py /bot
COPY quote.py /bot

# Second stage of build setting up working directory and copying files from first build
FROM python:3.9-slim
WORKDIR /bot
COPY --from=builder /bot /bot 

# Exposing port 443 for discord ssl traffic
EXPOSE 443
CMD ["python3", "main.py"]
