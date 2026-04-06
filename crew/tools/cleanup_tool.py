from crewai.tools import BaseTool
import subprocess

class CheckDiskTool(BaseTool):
    name: str = "check_disk"
    description: str = "Check disk usage percentage on Linux server"
    
    def _run(self, host: str = "192.168.136.128") -> str:
        cmd = 'ssh admin@192.168.136.128 "df / | awk \'NR==2 {print $5}\' | sed \'s/%//\'"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            return f"ERROR: {result.stderr}"
        
        usage = result.stdout.strip()
        return usage if usage else "ERROR"

class CleanupTool(BaseTool):
    name: str = "cleanup"
    description: str = "Delete all files in /tmp directory"
    
    def _run(self, host: str = "192.168.136.128") -> str:
        # Delete all files in /tmp
        cmd = 'ssh admin@192.168.136.128 "sudo rm -rf /tmp/* 2>/dev/null"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            return f"ERROR: {result.stderr}"
        
        # Check new usage
        check_cmd = 'ssh admin@192.168.136.128 "df / | awk \'NR==2 {print $5}\' | sed \'s/%//\'"'
        check_result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)
        new_usage = check_result.stdout.strip()
        
        return f"SUCCESS: Deleted files in /tmp. New disk usage: {new_usage}%"

# Create instances
check_disk = CheckDiskTool()
cleanup = CleanupTool()