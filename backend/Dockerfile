FROM python:3.11.4-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
# optionally install dev tools
RUN apt update -y && apt install -y libpq-dev iputils-ping
# we don't need nmap as of now but it is good for debugging
# RUN apt install nmap
RUN pip install -r requirements.txt
# this is for debugging
# ENTRYPOINT ["tail", "-f", "/dev/null"]
# ENTRYPOINT [ "/bin/bash" ]
EXPOSE 5000
CMD ["python", "server.py"]
