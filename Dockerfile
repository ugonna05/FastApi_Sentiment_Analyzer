FROM python:3.10-slim
RUN pip install --upgrade pip


 #copy ./app /app


  #set env variables
  ENV PYTHONDONTWRITEBYTECODE 1
  ENV PYTHONUNBUFFERED 1
  ENV PORT 8008
  ENV PATH='$PATH:$HOME/.poetry/bin'

  WORKDIR /app

  COPY . .

  RUN pip install -r requirements.txt

 

  EXPOSE 8008:8000

  # command to run on container start
  CMD ['uvicorn', 'app:app', '--host', '0.0.0.0', '--port', '8008'] 



