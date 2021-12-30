FROM sellpy/python3-jupyter-sklearn-java

RUN pip3 install --upgrade pip \
    Flask==1.0.2 \ 
    pandas==0.23.4 \
    numpy==1.15.4 \
    scikit_learn==0.20.1 \
    gdown

RUN pip3 install nltk

RUN pip3 install gdown
RUN apt-get install unzip

ARG GDRIVE_DL_LINK

RUN gdown https://drive.google.com/uc?id=${GDRIVE_DL_LINK}
RUN unzip -d . stanford-postagger-full-2016-10-31.zip

RUN [ "python3", "-c", "import nltk; nltk.download('all')" ]

# Add local files and folders
ADD / /app/amazon-kinesis-client-python/

EXPOSE 9651

CMD [ "python3", "./starter.py" ]