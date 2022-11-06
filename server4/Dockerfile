FROM ubuntu
RUN apt update
RUN apt install python3-pip -y
WORKDIR /server1
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app .
COPY . .
EXPOSE 5009
ENV app=app.py
ENTRYPOINT [ "flask"]

CMD ["run", "-h", "0.0.0.0", "-p", "5009"]