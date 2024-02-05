consul {
  address = "consul:8500"

  retry {
    enabled  = true
    attempts = 12
    backoff  = "250ms"
  }
}
template {
  # template to populate management upstream with the rabbitmq nodes in the nginx 
  source      = "/data/nginx_config/conf.d/rmq_management.conf.ctmpl"
  destination = "/data/nginx_config/conf.d/rmq_management.conf"
  perms       = 0600
  #command     = "service nginx reload"
}
template {
  # template to populate amqp upstream with the rabbitmq nodes in the nginx 
  source      = "/data/nginx_config/stream.d/rmq_amqp.conf.ctmpl"
  destination = "/data/nginx_config/stream.d/rmq_amqp.conf"
  perms       = 0600
  #command     = "service nginx reload"
}