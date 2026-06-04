from official_ip_fetcher_xethhung12 import model_module
from dataclasses import asdict
import os
import json
import hashlib
import boto3
from botocore.exceptions import ClientError

class Repo:
    def check_if_cf_ipv4_expired(self, signature: str)-> bool:
        pass
    
    def get_cf_ipv4(self)-> list[model_module.OfficialIPModel]:
        pass

    def save_cf_ipv4(self, ips: list[model_module.OfficialIPModel]):
        pass

    def check_if_cf_ipv6_expired(self, signature: str)-> bool:
        pass

    def get_cf_ipv6()-> list[model_module.OfficialIPModel]:
        pass

    def save_cf_ipv6(self, ips: list[model_module.OfficialIPModel]):
        pass

    def _check_if_expired(self, file_name, signature: str)-> bool:
        pass
    
    def _save_signature(self, file_name, signature: str):
        pass

    def check_if_google_common_bot_expired(self, signature: str)-> bool:
        pass
    
    def check_if_google_special_bot_expired(self, signature: str)-> bool:
        pass

    def check_if_google_user_trigger_fetcher_expired(self, signature: str)-> bool:
        pass

    def check_if_google_user_trigger_google_fetcher_expired(self, signature: str)-> bool:
        pass

    def check_if_google_user_trigger_agent_expired(self, signature: str)-> bool:
        pass

    def get_google_common_bot(self)-> list[model_module.OfficialIPModel]:
        pass

    def get_google_special_bot(self)-> list[model_module.OfficialIPModel]:
        pass

    def get_google_user_trigger_fetcher(self)-> list[model_module.OfficialIPModel]:
        pass

    def get_google_user_trigger_google_fetcher(self)-> list[model_module.OfficialIPModel]:
        pass

    def get_google_user_trigger_agent(self)-> list[model_module.OfficialIPModel]:
        pass

    def save_google_common_bot(self, ips: list[model_module.OfficialIPModel]):
        pass

    def save_google_special_bot(self, ips: list[model_module.OfficialIPModel]):
        pass

    def save_google_user_trigger_fetcher(self, ips: list[model_module.OfficialIPModel]):
        pass

    def save_google_user_trigger_google_fetcher(self, ips: list[model_module.OfficialIPModel]):
        pass

    def save_google_user_trigger_agent(self, ips: list[model_module.OfficialIPModel]):
        pass

class FileRepo(Repo):
    def check_if_cf_ipv4_expired(self, signature: str)-> bool:
        file__name = "cf_ipv4.sig"
        return self._check_if_expired(file__name, signature)
    
    def check_if_cf_ipv6_expired(self, signature: str)-> bool:
        file__name = "cf_ipv6.sig"
        return self._check_if_expired(file__name, signature)

    
    def _get_ip(self, file_name)-> list[model_module.OfficialIPModel]:
        if not os.path.exists(file_name):
            return []
        with open(file_name, "r") as f:
            data = json.load(f)
            return [model_module.OfficialIpModel(i['ip'], i['mask'], model_module.IpVersion(i['version'])) for i in data]

    def get_cf_ipv4(self)-> list[model_module.OfficialIPModel]:
        return self._get_ip("cf_ipv4.json")

    def save_cf_ipv4(self, ips: list[model_module.OfficialIPModel]):
        self._save_content("cf_ipv4.json", "cf_ipv4.sig", ips)

    def get_cf_ipv6(self)-> list[model_module.OfficialIPModel]:
        return self._get_ip("cf_ipv6.json")

    def save_cf_ipv6(self, ips: list[model_module.OfficialIPModel]):
        self._save_content("cf_ipv6.json", "cf_ipv6.sig", ips)
    
    def _save_content(self, file_name, sign_name, ips: list[model_module.OfficialIPModel]):
        data = json.dumps([ asdict(i) for i in ips ], indent=2, ensure_ascii=False)
        hash_str = hashlib.sha256(data.encode()).hexdigest()
        self._save_signature(sign_name, hash_str)
        with open(file_name, "w") as f:
            f.write(data)

    def _check_if_expired(self, file_name, signature: str)-> bool:
        if not os.path.exists(file_name):
            return True
        sign = open(file_name, "r").read()
        return signature != sign
    
    @staticmethod
    def _save_signature(file_name, signature: str):
        with open(file_name, "w") as f:
            f.write(signature)
    
    def check_if_google_common_bot_expired(self, signature: str)-> bool:
        return self._check_if_expired("google_common_bot.sig", signature)
    
    def get_google_common_bot(self)-> list[model_module.OfficialIPModel]:
        return self._get_ip("google_common_bot.json")

    def check_if_google_special_bot_expired(self, signature: str)-> bool:
        return self._check_if_expired("google_special_bot.sig", signature)
    
    def get_google_special_bot(self)-> list[model_module.OfficialIPModel]:
        return self._get_ip("google_special_bot.json")
    
    def check_if_google_user_trigger_fetcher_expired(self, signature: str)-> bool:
        return self._check_if_expired("google_user_trigger_fetcher.sig", signature)
    
    def get_google_user_trigger_fetcher(self)-> list[model_module.OfficialIPModel]:
        return self._get_ip("google_user_trigger_fetcher.json")
    
    def check_if_google_user_trigger_google_fetcher_expired(self, signature: str)-> bool:
        return self._check_if_expired("google_user_trigger_google_fetcher.sig", signature)
    
    def get_google_user_trigger_google_fetcher(self)-> list[model_module.OfficialIPModel]:
        return self._get_ip("google_user_trigger_google_fetcher.json")
    
    def check_if_google_user_trigger_agent_expired(self, signature: str)-> bool:
        return self._check_if_expired("google_user_trigger_agent.sig", signature)
    
    def get_google_user_trigger_agent(self)-> list[model_module.OfficialIPModel]:
        return self._get_ip("google_user_trigger_agent.json")

    def save_google_common_bot(self, ips: list[model_module.OfficialIPModel]):
        self._save_content("google_common_bot.json", "google_common_bot.sig", ips)

    def save_google_special_bot(self, ips: list[model_module.OfficialIPModel]):
        self._save_content("google_special_bot.json", "google_special_bot.sig", ips)

    def save_google_user_trigger_fetcher(self, ips: list[model_module.OfficialIPModel]):
        self._save_content("google_user_trigger_fetcher.json", "google_user_trigger_fetcher.sig", ips)

    def save_google_user_trigger_google_fetcher(self, ips: list[model_module.OfficialIPModel]):
        self._save_content("google_user_trigger_google_fetcher.json", "google_user_trigger_google_fetcher.sig", ips)

    def save_google_user_trigger_agent(self, ips: list[model_module.OfficialIPModel]):
        self._save_content("google_user_trigger_agent.json", "google_user_trigger_agent.sig", ips)


class S3Repo(FileRepo):
    def __init__(self, bucket: str, prefix: str = "", endpoint_url: str = None,
                 aws_access_key_id: str = None, aws_secret_access_key: str = None,
                 region_name: str = None):
        self._bucket = bucket
        self._prefix = prefix.rstrip("/") + "/" if prefix else ""
        self._s3 = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )

    def _key(self, file_name: str) -> str:
        return f"{self._prefix}{file_name}"

    def _read_object(self, file_name: str) -> str | None:
        try:
            response = self._s3.get_object(Bucket=self._bucket, Key=self._key(file_name))
            return response["Body"].read().decode("utf-8")
        except ClientError as e:
            if e.response["Error"]["Code"] in ("NoSuchKey", "404"):
                return None
            raise

    def _write_object(self, file_name: str, content: str):
        self._s3.put_object(
            Bucket=self._bucket,
            Key=self._key(file_name),
            Body=content.encode("utf-8"),
        )

    def _get_ip(self, file_name: str) -> list[model_module.OfficialIPModel]:
        content = self._read_object(file_name)
        if content is None:
            return []
        data = json.loads(content)
        return [model_module.OfficialIpModel(i["ip"], i["mask"], model_module.IpVersion(i["version"])) for i in data]

    def _save_content(self, file_name: str, sign_name: str, ips: list[model_module.OfficialIPModel]):
        data = json.dumps([asdict(i) for i in ips], indent=2, ensure_ascii=False)
        hash_str = hashlib.sha256(data.encode()).hexdigest()
        self._save_signature(sign_name, hash_str)
        self._write_object(file_name, data)

    def _check_if_expired(self, file_name: str, signature: str) -> bool:
        content = self._read_object(file_name)
        if content is None:
            return True
        return signature != content.strip()

    def _save_signature(self, file_name: str, signature: str):
        self._write_object(file_name, signature)
