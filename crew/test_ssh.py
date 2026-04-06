import subprocess
import sys

def test_ssh():
    print("Testing SSH connection...", flush=True)
    cmd = 'ssh admin@192.168.136.128 "echo Connected"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    print(f"Return code: {result.returncode}", flush=True)
    print(f"Stdout: '{result.stdout}'", flush=True)
    print(f"Stderr: '{result.stderr}'", flush=True)
    
    if result.returncode == 0:
        print("SUCCESS: SSH is working!", flush=True)
        
        # Check disk usage
        cmd2 = 'ssh admin@192.168.136.128 "df / | awk \'NR==2 {print $5}\'"'
        result2 = subprocess.run(cmd2, shell=True, capture_output=True, text=True)
        print(f"Disk usage: {result2.stdout.strip()}", flush=True)
        return True
    else:
        print("FAILED: SSH not working", flush=True)
        return False

if __name__ == "__main__":
    test_ssh()