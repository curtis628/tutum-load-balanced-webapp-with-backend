# tutum-load-balanced-webapp-with-backend
A tutum application (stackfile) that includes and uses two custom (but simple) python Docker images. Useful as an example stackfile that display's Tutum's load balancing for both frontends and backends.

This was project was heavily influenced by [Tutum's python-quickstart](https://github.com/tutumcloud/quickstart-python) project and from reading Tutum's docs on [Load balancing a Web Service](https://support.tutum.co/support/solutions/articles/5000050235-load-balancing-a-web-service)

## How I Built It
I built the Docker image locally, and then tagged/pushed to my private repository hosted on tutum.co.

```
$> cd greeting-rest
$> docker build -t curtis628/greeting-rest .
$> cd ..
$> docker build -t curtis628/greeting-web .
$> docker tag -f curtis628/greeting-rest tutum.co/curtis628/repo:greeting-rest-1.0
$> docker push tutum.co/curtis628/repo:greeting-rest-1.0
$> docker tag -f curtis628/greeting-web tutum.co/curtis628/repo:greeting-web-1.0
$> docker push tutum.co/curtis628/repo:greeting-web-1.0 
```

Once my Docker images were tagged and pushed to my private Tutum repository, I could use them in my Tutum stackfile.

## How You Can Use It
You can use my stackfile by viewing it on stackfiles.io and clicking "Deploy to Tutum"
