from dataclasses import asdict

def main():
    from official_ip_fetcher_xethhung12 import cf_local_module, google_local_module,repo_module
    # repo = repo_module.FileRepo()
    repo = repo_module.S3Repo(
        bucket="hkplive-ot7-jzcwiezlupaxk",
        prefix = "/official-ip-fetcher/", 
        endpoint_url = "https://t3.storageapi.dev",
        aws_access_key_id = "tid_momEWsKMbmxjIhBiETGuFEOTPiPhOclTlxgCrlESpnwuAHbcbl", 
        aws_secret_access_key = "tsec_o8Ug6uXH3PFmFW_c9fjGmIcRYe72tf2LuGw5IvcnXGpiO449OgCzNfEJzEcLvv-1zW4gsG",
        region_name = "auto"
    )
    print(cf_local_module.get_cf_ipv4_no_cache(repo))
    print(cf_local_module.get_cf_ipv6_no_cache(repo))
    print(google_local_module.get_google_common_bot_no_cache(repo))
    print(google_local_module.get_google_special_bot_no_cache(repo))
    print(google_local_module.get_google_user_trigger_fetcher_no_cache(repo))
    print(google_local_module.get_google_user_trigger_google_fetcher_no_cache(repo))
    print(google_local_module.get_google_user_trigger_agent_no_cache(repo))
