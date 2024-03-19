# delete services
kubectl delete service quiz-api-service
kubectl delete service quiz-ui-service

# delete deployments
kubectl delete deployment quiz-api-deployment
kubectl delete deployment quiz-ui-deployment

# delete virtual services
kubectl delete virtualservice quiz-api-service
kubectl delete virtualservice quiz-ui-service

# delete gateway
kubectl delete gateway quiz-app-gateway