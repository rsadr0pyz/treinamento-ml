FROM python:3

RUN useradd -ms /bin/bash vscode

WORKDIR /home/vscode

RUN mkdir /home/vscode/src
RUN apt-get update && apt-get install git

CMD ["sleep", "infinity"]