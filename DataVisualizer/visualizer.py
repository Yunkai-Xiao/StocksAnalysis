from scraper import Scraper
from matplotlib import pyplot as plt
import os
from os.path import isdir
from visualizer_tools import CloseVisualizer, OpenVisualizer
# Create folders
if isdir('reports') == False:
  os.mkdir('reports')
  print('Reports folder created.')

# Load Data
sc = Scraper()
datas = sc.get_data()

# Visualizing
visualizers = [CloseVisualizer(), OpenVisualizer()]

for key in datas:
  if isdir('reports/%s' % key) == False:
    os.mkdir('reports/%s' % key)
  for vis in visualizers:
    vis.plot(key, datas[key])
  
print("%d Data is visualized completely." % len(datas))


