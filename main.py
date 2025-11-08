import subprocess

command = ["git", "status"]
result=subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
