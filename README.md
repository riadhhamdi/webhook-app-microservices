# Web Hook application 

This repository contains two applications that make you test webhooks quickely and easily 

The applications are: 

webhook_backend: this deploy a flask application that acts as a webhook listener you can use it as a webhook URL for third party applications

webhook_ui: this is the UI that shows the data that has been collected when third party applications trigger the webhook_backend application 


#Installation

## Using docker/podman

These applications are build into two images and pushed to quay.io you can use them directly 

* Run the webhook_backend application using the following command 

```bash
$ docker run -d -p 5000:5000 --name backend-service webhook_backend
#or
$ podman run -d -p 5000:5000 --name backend-service webhook_backend
  
```

* Run the webhook_ui application and provide the backend URI through an environment variable 

```bash
$ docker run -d -p 5001:5001 --name frontend-service --link backend-service:webhook_backend -e BACKEND_URL="http://backend-service:5000/webhooks" webhook_frontend

#or
$ docker run -d -p 5001:5001 --name frontend-service --link backend-service:webhook_backend -e BACKEND_URL="http://backend-service:5000/webhooks" webhook_frontend
  
```
