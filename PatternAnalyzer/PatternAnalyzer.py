from Pattern import Pattern

class PatternAnalyzer:
  def __init__(self):
    self.patterns = [] # Include all patterns that needs to be analyze
    self.datas = None

  def load_data(self, data):
    self.datas = data # TODO: check what format of data is

  def evaluate_pattern(self):
