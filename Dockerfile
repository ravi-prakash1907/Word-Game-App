FROM python:3
ADD src/main.py /
RUN pip install pystrich
CMD [ "python", "./main.py" ]
