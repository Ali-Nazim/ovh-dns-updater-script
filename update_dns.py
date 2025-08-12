import requests
import ovh
from dotenv import load_dotenv
import os

def get_public_ip():
    resp = requests.get("https://api.ipify.org/?format=json")
    resp.raise_for_status()
    return resp.json()["ip"]

def main():
    load_dotenv()
    DOMAIN_NAME = "canalab.ovh"
    client = ovh.Client(
        endpoint=os.getenv('OVH_ENDPOINT', 'ovh-ca'),
        application_key=os.getenv('OVH_APPLICATION_KEY'),
        application_secret=os.getenv('OVH_APPLICATION_SECRET'),
        consumer_key=os.getenv('OVH_CONSUMER_KEY')
    )
    ip = get_public_ip()
    record_ids = client.get(f'/domain/zone/{DOMAIN_NAME}/record', fieldType='A')
    if not record_ids:
        print(f"No A records found for {DOMAIN_NAME}.")
        return
    updated = False
    for rid in list(record_ids):
        record = client.get(f'/domain/zone/{DOMAIN_NAME}/record/{rid}')
        current_target = record.get("target")
        if current_target != ip:
            client.put(f'/domain/zone/{DOMAIN_NAME}/record/{rid}', target=ip)
            print(f"Updated record {rid} from {current_target} to {ip}")
            updated = True
        else:
            print(f"Record {rid} already up to date ({ip})")

    if updated:
        # Refresh zone only if any record was updated
        client.post(f'/domain/zone/{DOMAIN_NAME}/refresh')
        print(f"Refreshed zone {DOMAIN_NAME}")
    else:
        print("No records needed updating.")

if __name__ == "__main__":
    main()