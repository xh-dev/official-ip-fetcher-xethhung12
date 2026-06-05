from official_ip_fetcher_xethhung12 import cf_module, repo_module, model_module
import hashlib
from dataclasses import asdict
import json
import logging

logger = logging.getLogger(__name__)

def get_cf_ipv4_no_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    logger.debug("Fetching CF IPv4 (no cache)")
    dicts = [ asdict(i) for i in cf_module.get_cf_ipv4()]
    hash= hashlib.sha256(json.dumps(dicts).encode()).hexdigest()
    isExpired = repo.check_if_cf_ipv4_expired(hash)
    if isExpired:
        logger.info("CF IPv4 cache expired, saving new data")
        repo.save_cf_ipv4(cf_module.get_cf_ipv4())
    else:
        logger.debug("CF IPv4 cache is up to date")
    return get_cf_ipv4_cached(repo)

def get_cf_ipv6_no_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    logger.debug("Fetching CF IPv6 (no cache)")
    dicts = [ asdict(i) for i in cf_module.get_cf_ipv6()]
    hash= hashlib.sha256(json.dumps(dicts).encode()).hexdigest()
    isExpired = repo.check_if_cf_ipv6_expired(hash)
    if isExpired:
        logger.info("CF IPv6 cache expired, saving new data")
        repo.save_cf_ipv6(cf_module.get_cf_ipv6())
    else:
        logger.debug("CF IPv6 cache is up to date")
    return get_cf_ipv6_cached(repo)

def get_cf_ipv6_cached(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    return repo.get_cf_ipv6()

def get_cf_ipv4_cached(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    return repo.get_cf_ipv4()