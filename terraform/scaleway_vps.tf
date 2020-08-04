provider "scaleway" {}

resource "scaleway_instance_ip" "public_ip" {}

resource "scaleway_instance_security_group" "www" {
  inbound_default_policy  = "drop"
  outbound_default_policy = "accept"

  inbound_rule {
    action = "accept"
    port   = "22"
  }

  inbound_rule {
    action = "accept"
    port   = "80"
  }

  inbound_rule {
    action = "accept"
    port   = "443"
  }
}

resource "scaleway_instance_server" "my_app" {
  name = "my_app"
  type  = "DEV1-S"
  image = "debian-buster"

  tags = []

  root_volume {
    size_in_gb = 20
    delete_on_termination = false
  }
  enable_ipv6 = false

  ip_id = scaleway_instance_ip.public_ip.id

  security_group_id = scaleway_instance_security_group.www.id

  cloud_init = data.template_cloudinit_config.cloudinit_config.rendered
}

output "ips" {
  value = scaleway_instance_ip.public_ip
}
