import subprocess

# Check current usage
print("Current disk usage:")
result = subprocess.run('ssh admin@192.168.136.128 "df -h /"', shell=True, capture_output=True, text=True)
print(result.stdout)

# Check what's in /tmp
print("\nFiles in /tmp:")
result = subprocess.run('ssh admin@192.168.136.128 "ls -la /tmp/ | head -20"', shell=True, capture_output=True, text=True)
print(result.stdout)

# Clean /tmp
print("\nCleaning /tmp...")
result = subprocess.run('ssh admin@192.168.136.128 "sudo rm -rf /tmp/*"', shell=True, capture_output=True, text=True)
print(f"Cleanup result: {result.returncode}")

# Check new usage
print("\nNew disk usage:")
result = subprocess.run('ssh admin@192.168.136.128 "df -h /"', shell=True, capture_output=True, text=True)
print(result.stdout)