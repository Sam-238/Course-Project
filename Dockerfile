FROM python:3.14
WORKDIR /student
COPY project.py .
CMD ["python", "project.py"]