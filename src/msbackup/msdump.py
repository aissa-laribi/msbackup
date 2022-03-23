import sys
import subprocess
import shlex

def dump(user, host, dbname):
    try:
        return subprocess.run(['mysqldump', '--user', user, '-h', host, '-p', dbname], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)