from tabulate import tabulate
import random
tables = ["plain", "simple", "github", "grid", "simple_grid", "rounded_grid", "heavy_grid", "mixed_grid", "double_grid", "fancy_grid", "outline", "simple_outline", "rounded_outline", "heavy_outline", "mixed_outline", "double_outline", "fancy_outline", "pipe", "orgtbl", "asciidoc", "jira", "presto", "pretty", "psql", "rst", "mediawiki", "moinmoin", "youtrack", "html", "unsafehtml", "latex", "latex_raw", "latex_booktabs", "latex_longtable", "textile", "tsv"]
for x in range(35):
  fmt = tables[random.randint(1,30)]
  print(tabulate([["F",24],["M",19]], headers=["Letter", "Number"], tablefmt=fmt))
  print(fmt)
