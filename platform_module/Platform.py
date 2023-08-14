import platform

print(f"OS : {platform.system()}")
print(f"Version/Release : {platform.release()}")
print(f"Architecture : {platform.architecture()[0]}")
print(f"Installed Python Version : {platform.python_version()}")