from scraper import Scraper
from matplotlib import pyplot as plt

# Load Data
sc = Scraper()
datas = sc.get_data()
for key in datas:
  print(datas[key]['Date'][0])
print("%d Data is scraped completely." % len(datas))

# Begin to visualize data
# for tics in datas:
#   cur_data = datas[tics]
#   print(cur_data.head())