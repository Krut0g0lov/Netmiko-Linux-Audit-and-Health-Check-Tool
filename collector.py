def run(conn, command):
    try:
        return conn.send_command(command, read_timeout=20)
    except Exception as e:
        return f"error: {e}"


def collect_full_info(conn):
    data = {}

    # standart info
    data["hostname"] = run(conn, "hostname")
    data["os"] = run(conn, "cat /etc/os-release")
    data["kernel"] = run(conn, "uname -a")
    data["uptime"] = run(conn, "uptime")

    # resourses
    data["memory"] = run(conn, "free -m")
    data["disk"] = run(conn, "df -h")

    # network
    data["ip"] = run(conn, "ip -brief a")
    data["routes"] = run(conn, "ip r")
    data["ports"] = run(conn, "ss -tulpn")

    # users
    data["who"] = run(conn, "who")
    data["last_logins"] = run(conn, "last -n 5")

    # security
    data["sudo_users"] = run(conn, "getent group sudo")
    data["ssh_config"] = run(conn, "cat /etc/ssh/sshd_config")

    # services
    data["services"] = run(conn, "systemctl list-units --type=service --state=running")

    # docker
    data["docker"] = run(conn, "docker ps")

    # packages
    data["packages"] = run(conn, "dpkg -l | head -n 20")

    # logs
    data["errors"] = run(conn, "journalctl -p err -n 20")

    return data

