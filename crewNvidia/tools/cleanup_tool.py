# tools/cleanup_tool.py
from crewai.tools import BaseTool
import subprocess

class CleanupTmpTool(BaseTool):
    name: str = "cleanup_tmp_directory"
    description: str = "Clean /tmp directory on remote Linux VM if disk usage reaches 80%"

    def _run(self) -> str:
        host = "192.168.136.128"
        username = "admin"
        
        remote_command = """
        usage=$(df /tmp | awk 'NR==2 {print $5}' | sed 's/%//');
        if [ "$usage" -ge 80 ]; then
            find /tmp -type f -delete
            echo "SUCCESS: Cleanup executed. /tmp usage was ${usage}%"
        else
            echo "INFO: No cleanup needed. /tmp usage is ${usage}%"
        fi
        """
        
        ssh_command = ["ssh", f"{username}@{host}", remote_command]
        
        try:
            result = subprocess.run(
                ssh_command,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"ERROR: Cleanup failed: {result.stderr}"
        except Exception as e:
            return f"ERROR: {str(e)}"

# Create an instance to export
cleanup_tmp_directory = CleanupTmpTool()