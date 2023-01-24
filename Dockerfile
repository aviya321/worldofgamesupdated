FROM python:3
RUN pip install flask
COPY Mainscores.py /app/
COPY Scores.txt /app/
WORKDIR /app/
CMD python Mainscores.py
