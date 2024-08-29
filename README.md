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
$ docker run -d -p 5000:5000 --name backend-service quay.io/riadh_hamdi/webhook_backend:latest
#or
$ podman run -d -p 5000:5000 --name backend-service quay.io/riadh_hamdi/webhook_backend:latest
  
```

* Run the webhook_ui application and provide the backend URI through an environment variable 

```bash
$ docker run -d -p 5001:5001 --name frontend-service -e BACKEND_URL="http://backend-service:5000/webhooks" quay.io/riadh_hamdi/webhook_frontend:latest

#or

$ podman run -d -p 5001:5001 --name frontend-service -e BACKEND_URL="http://backend-service:5000/webhooks" quay.io/riadh_hamdi/webhook_frontend:latest
```

## On openshift 

* deploy the backend 

```bash
$ oc new-app --name webhook-backend --context-dir webhook_backend https://github.com/riadhhamdi/webhook-app-microservices.git  
$ oc delete svc/webhook-backend
$ oc expose deploy/webhook-backend --port 5000
$ oc expose svc/webhook-backend
```
* deploy the frontend 

```bash
$ oc new-app --name webhook-frontend --context-dir webhook_ui https://github.com/riadhhamdi/webhook-app-microservices.git -e BACKEND_URL=http://webhook-backend.<namespace>.svc.cluster.local:5000/webhooks

## For example for my config in the namespace "hooks" the command is the following
## $ oc new-app --name webhook-frontend --context-dir webhook_ui https://github.com/riadhhamdi/webhook-app-microservices.git -e BACKEND_URL=http://webhook-backend.hooks.svc.cluster.local:5000/webhooks
 
$ oc delete svc/webhook-frontend
$ oc expose deploy/webhook-frontend --port 5001
$ oc expose svc/webhook-frontend
```

# Usage of the application 

* First check that the backend application is working corretly
 
```bash 
$ curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://<BAKCNED_ADDRESS>/webhook
## Example on openshift 
$ curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://webhook-backend-webhooks-microk8s.apps.cluster-lhpl8.lhpl8.sandbox697.opentlc.com/webhook

## Example on docker 
$ curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://localhost:5000/webhook

## The result should be the following ##$
## {"message":"Webhook received","status":"success"} 
```
