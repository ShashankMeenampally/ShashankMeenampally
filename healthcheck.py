import subprocess

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)


def health_check(host):
    output = {}
    
    # 1. Host info
    output["host_info"] = run_command(f"/opt/boksm/bin/suexec /opt/boksm/sbin/hostadm -lT -h {host}")

    # 2. Boks state
    boksstate = run_command(f"/opt/boksm/bin/suexec /opt/boksm/lib/cadm -E SSM_ACTIVE -h {host}")
    
    if boksstate in ["on", "true"]:
        output["boks"] = "OK"
    else:
        output["boks"] = "FAIL"

    # 3. FQ queue
    output["fque"] = run_command(
        f"/opt/boksm/bin/suexec /opt/boksm/lib/boksdiag fque -bridge -name -age | grep -e '^Host' -e '^{host}'"
    )

    # 4. Node key
    output["nodekey"] = run_command(
        f"/opt/boksm/bin/suexec /opt/boksm/lib/cadm -l -f nodekey -h {host} | head -n1"
    )

    # 5. Get IP
    ip = run_command(
        f"/opt/boksm/bin/suexec /opt/boksm/sbin/hostadm -l -p -h {host} | awk '{{print $2}}'"
    )
    output["ip"] = ip

    # 6. Port check
    port_check = run_command(f"nc -zv {ip} 6503")
    
    if "succeeded" in port_check.lower() or "open" in port_check.lower():
        output["port"] = "OK"
    else:
        output["port"] = "FAIL"

    return output
