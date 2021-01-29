import subprocess
import os
from datetime import datetime

def validate_barcode(barcode):
    """
    validate the barcode string using the first 8 characters and converting it to a datetime
    """
    str_format = "%Y%m%d"
    try:
        datetime.strptime(barcode[:8], str_format)
        return True
    except ValueError:
        return False


def run_Rscript(script_name, **kwargs):
    """
    use subprocess library to run Rscript command
    """
    # host = os.getenv("HOSTNAME")
    # just to see which pyapi server is being used
    # print(f'hostname: {host}')

    username = os.getenv("UNAME", "bdb")
    version = os.getenv("VERSION", "1_2_1b")
    omiq_path = os.path.join("/home", username, "R")
    if script_name == "main_driver":
        rscript_path = os.path.join(omiq_path, f"omiq_v{version}",
                                    "OmiqPipeline",f"{script_name}.R")
    else:
        rscript_path = os.path.join(omiq_path, f"{script_name}.R")

    # for testing
    # rscript_path = '/Users/spencertrinh/GitRepos/romiq-docker-nossh/services/romiq/test.R'

    # run rscript
    cmd = ["Rscript"]
    cmd.append(rscript_path)
    barcode = kwargs.get('barcode', '')
    re_run = kwargs.get('re_run', '')
    if barcode:
        cmd.append(barcode)
    else:
        raise("need to supply barcode argument")
    if re_run not in ['', None]:
        cmd.append(re_run)

    print('='*40)
    print(f'running command: \"{cmd}\"')
    print('='*40)

    try:
        process = subprocess.check_output(cmd, universal_newlines=True)
    except subprocess.SubprocessError as e:
        err = f'Status: FAIL {e.returncode} {e.output}'
        print(err)
        process = err
    print(process)
    return process

