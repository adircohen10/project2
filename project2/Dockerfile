FROM python:3
COPY requirements.txt .
WORKDIR .
COPY . .
RUN pip install -r requirements.txt 
RUN pip install flask
CMD python ./MainScores.py
