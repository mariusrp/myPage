# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not $
# For more information, please refer to https://aka.ms/vscode-docker-python-user-rights`
EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

#CMD ["/bin/bash"]
#ENTRYPOINT gunicorn -w 4 run:app -b 0.0.0.0:80
#CMD ["python","./run.py"]