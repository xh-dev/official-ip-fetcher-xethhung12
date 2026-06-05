
from dataclasses import asdict
from official_ip_fetcher_xethhung12 import model_module
from typing import Tuple
def get_google_common_bot()-> Tuple[str, list[model_module.OfficialIpModel]]:
    url = "https://developers.google.com/static/crawling/ipranges/common-crawlers.json"
    return _common_fetch(url)

def get_google_special_bot()-> Tuple[str, list[model_module.OfficialIpModel]]:
    url = "https://developers.google.com/static/crawling/ipranges/special-crawlers.json"
    return _common_fetch(url)

def get_google_user_trigger_fetcher()-> Tuple[str, list[model_module.OfficialIpModel]]:
    url = "https://developers.google.com/static/crawling/ipranges/user-triggered-fetchers.json"
    return _common_fetch(url)

def get_google_user_trigger_google_fetcher()-> Tuple[str, list[model_module.OfficialIpModel]]:
    url = "https://developers.google.com/static/crawling/ipranges/user-triggered-fetchers-google.json"
    return _common_fetch(url)

def get_google_user_trigger_agent()-> Tuple[str, list[model_module.OfficialIpModel]]:
    url = "https://developers.google.com/static/crawling/ipranges/user-triggered-agents.json"
    return _common_fetch(url)

def _common_fetch(url)->Tuple[str, list[model_module.OfficialIpModel]]:
    import requests

    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        time_str = response_json['creationTime']
        prefixes = response_json['prefixes']
        ips = []
        for prefix in prefixes:
            version = model_module.IpVersion.V4 if 'ipv4Prefix' in prefix else model_module.IpVersion.V6
            ip, mask = (prefix['ipv4Prefix'] if version == model_module.IpVersion.V4 else prefix['ipv6Prefix']).split("/")
            ips.append(model_module.OfficialIpModel(ip=ip, mask=int(mask), version=model_module.IpVersion.V4))
        return time_str, ips
    else:
        raise Exception(f"Failed to fetch Cloudflare IPv4 addresses: {response.status_code}")