import multiprocessing

bind = "0.0.0.0:5105"
workers = multiprocessing.cpu_count() * 2 + 1
reload = True
worker_class ='flask_sockets.worker'

# secrets_file = os.getenv("GATEWAY_SECRETS_PATH")

# with open(secrets_file, 'r') as h:
#     secrets = h.read().strip().split("\n")
# raw_env = secrets
# #tests

