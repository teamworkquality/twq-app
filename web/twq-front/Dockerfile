FROM mhart/alpine-node:8
WORKDIR /app
COPY . /app
RUN npm install -g --silent 
EXPOSE 8000
CMD ["sh","run.sh"]