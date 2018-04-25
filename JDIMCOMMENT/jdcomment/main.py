# Author:song
from scrapy import cmdline
name = 'jdcm'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())