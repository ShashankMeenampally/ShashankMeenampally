from crewai.tools import BaseTool
import subprocess

class CleanupTmpTool(BaseTool):
    name: str = "cleanup_tmp_directory"
    description: str = "Clean /tmp directory only if disk usage reaches 80%."

    def _run(self) -> str:
        host = "192.168.136.128"

        # command that runs on remote VM
        remote_command = """
usage=$(df /tmp | awk 'NR==2 {print $5}' | sed 's/%//');
if [ "$usage" -ge 60 ]; then
    find /tmp -type f -delete
    echo "Cleanup executed. /tmp usage was ${usage}%"
else
    echo "No cleanup needed. /tmp usage is ${usage}%"
fi
"""

        command = f"ssh admin@{host} \"{remote_command}\""

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"Cleanup failed: {result.stderr}"

        except Exception as e:
            return f"Error during cleanup: {str(e)}"