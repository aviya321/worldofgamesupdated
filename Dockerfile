FROM python:3.9
RUN pip install flask
# Copy the current directory contents into the container as /app
COPY Mainscores.py /app/
COPY scores.txt /app/
# Set the working directory to /app
WORKDIR /app/
ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0
# Make port 5000 available to the world outside this container
EXPOSE 5000
CMD ["python", "MainScores.py"]

