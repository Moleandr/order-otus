### Build and push image
```shell
docker build -f .docker/Dockerfile -t order-otus ./
```
```shell
docker image tag order-otus:latest moleandr/order-otus:latest
```
```shell
docker image push moleandr/order-otus:latest
```

### Install
```shell
helm dependency update .helm/order-otus
```

```shell
helm upgrade --install  order-otus .helm/order-otus --namespace order-otus --create-namespace
```

### Uninstall
```shell
helm uninstall --namespace order-otus order-otus
```

### IngressController
```shell
helm repo add traefik https://traefik.github.io/charts
```
```shell
helm repo update
```
```shell
helm install traefik traefik/traefik
```