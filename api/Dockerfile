FROM frolvlad/alpine-python3

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt 
EXPOSE 8000
CMD ["sh", "run.sh"]