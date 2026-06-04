from dataclasses import dataclass
from enum import IntEnum

class IpVersion(IntEnum):
    V4 = 4
    V6 = 6


@dataclass
class OfficialIpModel:
    ip: str
    mask: int
    version: IpVersion

    def isNetwork(self)-> bool:
        if self.version == IpVersion.V4:
            return self.mask != 32
        elif self.version == IpVersion.V6:
            return self.mask != 128
        else:
            raise ValueError(f"invalid ip version: {self.version}")
