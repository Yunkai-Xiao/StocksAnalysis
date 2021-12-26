class Pattern:
  def __init__(self, data, percent_diff_allowed = 0.05):
    self._length = 0
    self._percent_diff_allowed = percent_diff_allowed
    self._pattern = []

  def load_pattern(self, patterns):
    self._pattern = patterns
    