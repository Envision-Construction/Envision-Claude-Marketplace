#!/usr/bin/env python3
"""Generate a short-lived GitHub App installation token for git push from GKE pods."""

import argparse
import json
import sys
import time
import urllib.request
import urllib.error

try:
    import jwt
except ImportError:
    print("PyJWT not installed. Install with: pip install PyJWT", file=sys.stderr)
    sys.exit(1)


def generate_jwt(app_id: str, key_file: str) -> str:
    with open(key_file) as f:
        private_key = f.read()

    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + (10 * 60),
        "iss": app_id,
    }
    return jwt.encode(payload, private_key, algorithm="RS256")


def get_installation_id(token: str, org: str) -> str:
    url = "https://api.github.com/app/installations"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    })
    with urllib.request.urlopen(req) as resp:
        installations = json.loads(resp.read())

    for inst in installations:
        if inst.get("account", {}).get("login") == org:
            return str(inst["id"])

    print(f"No installation found for org '{org}'", file=sys.stderr)
    sys.exit(1)


def get_installation_token(jwt_token: str, installation_id: str) -> str:
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    req = urllib.request.Request(url, data=b"{}", method="POST", headers={
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json",
    })
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    return data["token"]


def main():
    parser = argparse.ArgumentParser(description="Generate GitHub App installation token")
    parser.add_argument("--app-id", required=True, help="GitHub App ID")
    parser.add_argument("--key-file", required=True, help="Path to App private key PEM")
    parser.add_argument("--org", default="Envision-Construction", help="GitHub org name")
    args = parser.parse_args()

    jwt_token = generate_jwt(args.app_id, args.key_file)
    installation_id = get_installation_id(jwt_token, args.org)
    token = get_installation_token(jwt_token, installation_id)
    print(token)


if __name__ == "__main__":
    main()
