import netmiko
from netmiko import ConnectHandler

from collector import collect_full_info

ssh_Cli = ConnectHandler(
    device_type = "linux",
    host = "5.44.***.***",
    port = 22,
    username = "ubuntu",
    password = "***",
)

#output = ssh_Cli.send_command("netstat -tulpn")
#print(output)

info = collect_full_info(ssh_Cli)

print("\n=== FULL INFO ===")
for key, value in info.items():
    print(f"\n--- {key.upper()} ---")
    print(value)

ssh_Cli.disconnect()
