resource "digitalocean_loadbalancer" "public" {
    name   = "kubernetes-load-balancer"
    region = "lon1"

    forwarding_rule {
        entry_port     = 80
        entry_protocol = "tcp"
        target_port     = 80
        target_protocol = "tcp"
    }

    forwarding_rule {
        entry_port     = 443
        entry_protocol = "tcp"
        target_port     = 443
        target_protocol = "tcp"
    }

    healthcheck {
        port     = 22
        protocol = "tcp"
    }

    droplet_ids = [for node in digitalocean_kubernetes_cluster.my_cluster.node_pool[0].nodes: node.droplet_id]
}

output "load_balancer_ip" {
    value = digitalocean_loadbalancer.public.ip
}
