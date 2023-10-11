cricket.py#Define the base class player
class player:
  def--init--(self):
  def play(self):
    print("The player is playing cricket.")
    # Define the derived class batsman
    class batsman(player):
      def play(self):
        print("The batsman is batting ")
# Define the derived class bowler
class bowler(player):
  def play(self):
print("The bowler is bowling")
#create objects of batsman and bowler classes
b1=batsman()
b2=bowler()
# call the play() method for each object
b1.play()
b2.play()
