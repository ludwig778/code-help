data "template_file" "shell_script" {
  template = file("cloud_init_basic.sh")
}

data "template_cloudinit_config" "cloudinit_config" {
  gzip          = false
  base64_encode = false

  part {
    content_type = "text/x-shellscript"
    content      = data.template_file.shell_script.rendered
  }
}
