__author__ = "Sean Davis"
__email__ = "seandavi@gmail.com"
__license__ = "MIT"

import os
from snakemake.shell import shell

indexname = os.path.dirname(snakemake.input.indexname)

#extra = snakemake.params.get("extra", "")
#log = snakemake.log_fmt_shell(stdout=True, stderr=True)

shell("salmon quant -p {snakemake.threads} -l A "
      "-i {indexname} " 
      "-1 <( gunzip -c {snakemake.input.read1} ) "
      "-2 <( gunzip -c {snakemake.input.read2} ) "
      "-o quantification/{snakemake.wildcards.source} "
      "--seqBias --gcBias -g {snakemake.input.transcript2gene} "
      "--numGibbsSamples 200 ")
