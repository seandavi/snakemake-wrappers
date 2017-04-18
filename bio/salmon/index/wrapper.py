__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

indexname = os.path.dirname(snakemake.output[0])

#extra = snakemake.params.get("extra", "")
#log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("salmon index --index={indexname} --transcripts={snakemake.input.transcripts} --gencode")

