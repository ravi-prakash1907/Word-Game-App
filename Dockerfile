FROM python:3
COPY src .
CMD [ "python", "./main.py" ]
