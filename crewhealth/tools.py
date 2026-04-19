import paramiko
from crewai.tools import BaseTool

# class DiskTool(BaseTool):
#     name: str = "Check tmp usage"
#     description: str = "Checks /tmp disk usage and warn if above 60%"

#     def _run(self) -> str:
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(hostname= "192.168.136.128", username="admin")
#         stdin, stdout, stderr = ssh.exec_command("df -P /tmp")
#         output = stdout.read().decode().split()
#         usage = int(output[4].replace("%", ""))
#         ssh.close()
#         return f"WARNING: {usage}%" if usage > 60 else f"OK: {usage}%"

class DiskTool(BaseTool):
    name: str = "Check tmp usage"
    description: str = "Checks /tmp disk usage and warn if above 60%"

    def _run(self) -> str:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="192.168.136.128", username="admin")
        stdin, stdout, stderr = ssh.exec_command("df -P /tmp")
        lines = stdout.read().decode().strip().split('\n')
        columns = lines[1].split()
        usage = int(columns[4].replace("%", ""))
        ssh.close()
        return f"WARNING: {usage}%" if usage > 60 else f"OK: {usage}%"