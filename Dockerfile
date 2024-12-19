FROM python:3.10
EXPOSE 5000

WORKDIR /app

# The copy of requirements.txt here instead of moving the copy . . up front is that
# if the requirements.txt file hasn't changed, then these next two lines will be cached
# and we will save time not running these.
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]

