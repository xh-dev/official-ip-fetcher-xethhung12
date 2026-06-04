from dataclasses import asdict
from official_ip_fetcher_xethhung12 import model_module
def get_cf_ipv4()-> list[model_module.OfficialIPModel]:
    import requests

    url = "https://www.cloudflare.com/ips-v4"
    response = requests.get(url)
    if response.status_code == 200:
        ips = []
        for line in response.text.splitlines():
            ip, mask = line.split("/")
            ips.append(model_module.OfficialIpModel(ip=ip, mask=int(mask), version=model_module.IpVersion.V4))
        return ips
    else:
        raise Exception(f"Failed to fetch Cloudflare IPv4 addresses: {response.status_code}")
    
def get_cf_ipv6()-> list[model_module.OfficialIPModel]:
    import requests

    url = "https://www.cloudflare.com/ips-v6"
    response = requests.get(url)
    if response.status_code == 200:
        ips = []
        for line in response.text.splitlines():
            ip, mask = line.split("/")
            ips.append(model_module.OfficialIpModel(ip=ip, mask=int(mask), version=model_module.IpVersion.V6))
        return ips
    else:
        raise Exception(f"Failed to fetch Cloudflare IPv6 addresses: {response.status_code}")