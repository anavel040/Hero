import os
import subprocess
import sys
import requests

def ssh_installed():
    try:
        result = subprocess.run(["which", "ssh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0 and bool(result.stdout)
    except Exception as e:
        return False
( Ini hanya sebagian yang ditampilkan, tidak di izinkan public untuk mengkonsumsi nya )
