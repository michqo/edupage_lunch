from dataclasses import dataclass


@dataclass
class EdupageUser:
    username: str
    password: str
    subdomain: str
