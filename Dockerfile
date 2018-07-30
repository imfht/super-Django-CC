FROM python:3.6
WORKDIR /app
COPY djangodocker djangodocker
COPY ./* /app/
RUN pip install -r requirements.txt && \
        python manage.py runserver
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
