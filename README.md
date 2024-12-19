

Build Docker image:
```
docker build -t rest-apis-flask-python . 
```

Run Docker container with working directory pointing to local volume:
```
docker run -dp 5000:5000 -w //app -v "$(Get-Location)://app" rest-apis-flask-python
```
