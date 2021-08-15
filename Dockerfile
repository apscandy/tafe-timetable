FROM python:3.9
ADD main.py .
ADD tafe.py .
ADD quote.py .
ADD .env .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]