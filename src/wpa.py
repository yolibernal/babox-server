import subprocess


def scan_for_networks() -> list[str]:
    output = subprocess.check_output(["wpa_cli", "scan"])
    output = subprocess.check_output(["wpa_cli", "scan_results"])
    output = output.decode().split("\n")
    networks = []
    for line in output[2:]:
        if line:
            networks.append(line.split("\t"))

    ssids = [network[-1] for network in networks]

    # deduplicate ssids
    ssids = list(set(ssids))

    return networks


def connect(ssid: str, password: str) -> str:
    output = subprocess.check_output(["wpa_cli", "add_network"])
    network_id = output.decode().split("\n")[-2]
    subprocess.check_output(["wpa_cli", "set_network", network_id, "ssid", f'"{ssid}"'])
    subprocess.check_output(
        ["wpa_cli", "set_network", network_id, "psk", f'"{password}"']
    )
    subprocess.check_output(["wpa_cli", "enable_network", network_id])
    return network_id
