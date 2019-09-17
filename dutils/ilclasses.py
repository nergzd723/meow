# I love classes or how to Hello World in 20 lines
class TransmitVeryImportantmsg:
  def enc(self):
    m = 'Hello World'
    result = m
    return result
class Main:
  def printl(self, arg):
    print(arg)
class Hello:
  def __init__(self):
    m = Main()
    t = TransmitVeryImportantmsg()
    n = t.enc()
    m.printl(n)
if __name__ == "__main__":
  try:
    h = Hello()
  except:
    class Error:
      def __init__(self):
        print('Lol you just screwed up your Hello World Program\n Who might even thought')
    e = Error()
