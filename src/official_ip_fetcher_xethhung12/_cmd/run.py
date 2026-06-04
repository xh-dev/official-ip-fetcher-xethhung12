from official_ip_fetcher_xethhung12 import cf_module, model_module, repo_module, run_module
from j_vault_http_client_xethhung12 import client
def main():
    client.load_to_env()
    run_module.main()
