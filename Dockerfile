FROM python:3.8

WORKDIR /User/local/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","C:\Users\Beytullah\Documents\GitHub\Breast-Cancer-Classification\src\app.py"]