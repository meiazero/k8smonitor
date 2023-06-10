# monitoring-stack

## Base of the project

-   prometheus repo base:
    https://github.com/techiescamp/kubernetes-prometheus

-   `metrics-server.yaml` is base on:
    https://github.com/kubernetes/kube-state-metrics

# How to use

> in your kubernetes cluster (tested on 1.27) apply the folder if you want to use.

```bash
kubectl apply -f k8s-metrics/
```

```bash
kubectl apply -f prometheus/
```

```bash
kubectl apply -f isolamento/
```

```bash
kubectl apply -f escalabilidade/
```

## Check if everything is working

```bash
kubectl get po,svc,deploy -n monitoring
```

```bash
kubectl get po,svc,deploy,hpa -n escalar
```

```bash
kubectl get po,svc -n isolamento
```

## Access the Prometheus

> go to http://cluster-ip:9090

## Access the Grafana

> check this repo: [getmp](https://github.com/meiazero/getmp)

## License

[MIT License](LICENSE)

## Contributing

> Fork it and send _PR_.

[go to top](#monitoring-stack)
