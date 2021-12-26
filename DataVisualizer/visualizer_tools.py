from matplotlib import pyplot as plt

class Visualizer:
  def __init__(self):
    self.name = ""
    self.data = None

  def plot(self):
    pass

class CloseVisualizer(Visualizer):
  def __init__(self):
    self.file_name = 'close.png'
  
  def plot(self, name, data):
    self.name = name
    self.data = data
    plt.figure()
    plt.plot(self.data['Date'], self.data['Close'])
    plt.savefig('reports/{0}/{1}'.format(self.name, self.file_name))

class OpenVisualizer(Visualizer):
  def __init__(self):
    self.file_name = 'open.png'
  
  def plot(self, name, data):
    self.name = name
    self.data = data
    plt.figure()
    plt.plot(self.data['Date'], self.data['Open'])
    plt.savefig('reports/{0}/{1}'.format(self.name, self.file_name))