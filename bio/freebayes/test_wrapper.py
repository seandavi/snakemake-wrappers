import subprocess
import os

def setup_module():
    os.chdir(os.path.join(os.path.dirname(__file__), "test"))

def test():
    subprocess.check_call(["snakemake", "calls/a.vcf", "--use-conda", "-F"])
