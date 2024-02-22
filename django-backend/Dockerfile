FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y telnet && apt-get install -y zip

COPY . .
# Copying the entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Copying requirements and installing them
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY media.zip ./

RUN mkdir /temp_media && unzip -o media.zip -d /temp_media

# Setting the default command to be executed by the entrypoint script
CMD ["sh", "-c", "/usr/local/bin/docker-entrypoint.sh"]


