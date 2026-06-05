from official_ip_fetcher_xethhung12 import google_module, repo_module, model_module

def get_google_common_bot_no_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    google_common_bot_time_str, google_common_bot_ips = google_module.get_google_common_bot()
    if repo.check_if_google_common_bot_expired(google_common_bot_time_str):
        repo.save_google_common_bot(google_common_bot_ips)
    return repo.get_google_common_bot()
    
def get_google_common_bot_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    return repo.get_google_common_bot()

def get_google_special_bot_no_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    google_special_bot_time_str, google_special_bot_ips = google_module.get_google_special_bot()
    if repo.check_if_google_special_bot_expired(google_special_bot_time_str):
        repo.save_google_special_bot(google_special_bot_ips)
    return repo.get_google_special_bot()

def get_google_special_bot_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    return repo.get_google_special_bot()

def get_google_user_trigger_fetcher_no_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    google_user_trigger_fetcher_time_str, google_user_trigger_fetcher_ips = google_module.get_google_user_trigger_fetcher()
    if repo.check_if_google_user_trigger_fetcher_expired(google_user_trigger_fetcher_time_str):
        repo.save_google_user_trigger_fetcher(google_user_trigger_fetcher_ips)
    return repo.get_google_user_trigger_fetcher()

def get_google_user_trigger_fetcher_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    return repo.get_google_user_trigger_fetcher()

def get_google_user_trigger_google_fetcher_no_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    google_user_trigger_google_fetcher_time_str, google_user_trigger_google_fetcher_ips = google_module.get_google_user_trigger_google_fetcher()
    if repo.check_if_google_user_trigger_google_fetcher_expired(google_user_trigger_google_fetcher_time_str):
        repo.save_google_user_trigger_google_fetcher(google_user_trigger_google_fetcher_ips)
    return repo.get_google_user_trigger_google_fetcher()

def get_google_user_trigger_google_fetcher_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    return repo.get_google_user_trigger_google_fetcher()

def get_google_user_trigger_agent_no_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    google_user_trigger_agent_time_str, google_user_trigger_agent_ips = google_module.get_google_user_trigger_agent()
    if repo.check_if_google_user_trigger_agent_expired(google_user_trigger_agent_time_str):
        repo.save_google_user_trigger_agent(google_user_trigger_agent_ips)
    return repo.get_google_user_trigger_agent()

def get_google_user_trigger_agent_cache(repo: repo_module.Repo)-> list[model_module.OfficialIpModel]:
    return repo.get_google_user_trigger_agent()

