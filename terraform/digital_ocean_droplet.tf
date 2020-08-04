provider "digitalocean" {
}

resource "digitalocean_droplet" "my_app" {
  name = "my_app"
  image = "ubuntu-18-04-x64"
  region = "lon1"
  size = "s-1vcpu-1gb"
  ssh_keys = [
    "5a:48:9f:ca:68:37:c1:9c:c5:13:d0:a8:30:7e:44:d7"
  ]
  user_data = cloud_init = data.template_cloudinit_config.cloudinit_config.rendered 
}
