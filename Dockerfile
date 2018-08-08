FROM python:3.6
WORKDIR /app
ADD ./ /app/
RUN pip install -r requirements.txt 
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
