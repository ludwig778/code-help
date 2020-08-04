provider "digitalocean" {
}

resource "digitalocean_kubernetes_cluster" "my_cluster" {
  name    = "my_cluster"
  region  = "fra1"
  version = "1.18.6-do.0"
  tags    = []

  node_pool {
    name       = "worker-pool"
    size       = "s-2vcpu-2gb"
    node_count = 1
  }
}

provider "kubernetes" {
  load_config_file = false
  host  = digitalocean_kubernetes_cluster.my_cluster.endpoint
  token = digitalocean_kubernetes_cluster.my_cluster.kube_config[0].token
  cluster_ca_certificate = base64decode(
    digitalocean_kubernetes_cluster.my_cluster.kube_config[0].cluster_ca_certificate
  )
}

resource "local_file" "kube_config" {
  content = digitalocean_kubernetes_cluster.my_cluster.kube_config[0].raw_config
  filename = "${path.module}/kube_config.yml"
}

