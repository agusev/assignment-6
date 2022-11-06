FROM ubuntu
RUN apt update
RUN apt install python3-pip -y
WORKDIR /server2
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app .
COPY . .
EXPOSE 5007
ENV app=app.py
ENTRYPOINT [ "flask"]

CMD ["run", "-h", "0.0.0.0", "-p", "5007"]