import subprocess
import os

def run_Rscript(script_name, **kwargs):
    """
    use subprocess library to run Rscript command
    """
    # host = os.getenv("HOSTNAME")
    # just to see which pyapi server is being used
    # print(f'hostname: {host}')

    username = os.getenv("UNAME")
    version = os.getenv("VERSION")
    omiq_path = os.path.join("/home", username, "R")
    if script_name == "main_driver":
        rscript_path = os.path.join(omiq_path, f"omiq_v{version}",
                                    "OmiqPipeline",f"{script_name}.R")
    else:
        rscript_path = os.path.join(omiq_path, f"{script_name}.R")


    # run rscript
    cmd = f"/usr/bin/Rscript {rscript_path}"
    barcode = kwargs.get('barcode', '')
    re_run = kwargs.get('re_run', '')
    if barcode:
        cmd += f" {barcode}"
    else:
        raise("need to supply barcode argument")
    if re_run not in ['', None]:
        cmd += f" {re_run}"

    print('='*40)
    print(f'running command: \"{cmd}\"')
    print('='*40)

    process = subprocess.Popen(list(cmd), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    stdout_lines = ' '.join(prorcess.stdout)
    print(stdout_lines)
    if stderr:
        stderr_lines = ' '.join(process.stderr)
        print(stderr_lines)
    return stdout_lines

