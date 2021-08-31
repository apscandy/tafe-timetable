FROM python:3.9
ADD main.py .
ADD tafe.py .
ADD quote.py .
ADD requirements.txt .
EXPOSE 443
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]