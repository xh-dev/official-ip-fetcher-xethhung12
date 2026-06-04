from dataclasses import asdict
import os

def main():
    from official_ip_fetcher_xethhung12 import cf_local_module, google_local_module,repo_module
    # repo = repo_module.FileRepo()
    bucket = os.getenv("S3_BUCKET")
    prefix = os.getenv("S3_PREFIX")
    endpoint_url = os.getenv("S3_ENDPOINT_URL")
    aws_access_key_id = os.getenv("S3_AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("S3_AWS_SECRET_ACCESS_KEY")
    region_name = os.getenv("S3_REGION_NAME")
    repo = repo_module.S3Repo(
        bucket = bucket,
        prefix = prefix, 
        endpoint_url = endpoint_url,
        aws_access_key_id = aws_access_key_id, 
        aws_secret_access_key = aws_secret_access_key,
        region_name = region_name
    )
    print(cf_local_module.get_cf_ipv4_no_cache(repo))
    print(cf_local_module.get_cf_ipv6_no_cache(repo))
    print(google_local_module.get_google_common_bot_no_cache(repo))
    print(google_local_module.get_google_special_bot_no_cache(repo))
    print(google_local_module.get_google_user_trigger_fetcher_no_cache(repo))
    print(google_local_module.get_google_user_trigger_google_fetcher_no_cache(repo))
    print(google_local_module.get_google_user_trigger_agent_no_cache(repo))
