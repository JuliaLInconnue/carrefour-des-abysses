init python:
  class Event(object):
    def __init__(self, Day, Month, IsActive):
      #self.Hour = Hour
      self.Day = Day
      self.Month = Month
      #self.Block = Block
      self.IsActive=IsActive
    def DateCheck(self,c):
      if self.Day == c.Days and self.Month == c.Month and self.IsActive:
        return True
      else:
        return False
    def SetInactive(self):
      set.IsActive = False