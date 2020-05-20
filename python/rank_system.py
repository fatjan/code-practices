# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
  
    def inc_progress(self, num):
        if self.rank == 8 or num == 8:
            prog_value = 0
        elif self.rank > num:
            diff = self.rank - num
            if diff == 1:
                prog_value = 1
            else:
                prog_value = 0
        else:
            if self.rank < 0:
                if num < 0:
                    diff = num - self.rank
                else:
                    diff = num - self.rank - 1
            else:
                if num > 0:
                    diff = num - self.rank
            prog_value = 10 * diff ** 2
       
        self.progress += prog_value
        print('prog_value', prog_value)
        rank_up = self.progress // 100
        if self.progress >= 100:
            if self.rank + rank_up > 8:
                self.rank = 8
            elif self.rank + rank_up > -1 and self.rank != 8:
                self.rank += rank_up + 1
            elif self.rank != 8:
                self.rank += rank_up
            if self.rank == 8:
                self.progress += 0
            else:
                self.progress %= 100
      
# user = User()
# print(user.rank) # => -8
# print(user.progress) # => 0
# user.inc_progress(-7)
# print(user.progress) # => 10
# user.inc_progress(-5) # will add 90 progress
# print(user.progress) # => 0 # progress is now zero
# print(user.rank) # => -7 # rank was upgraded to -7

# -3 6 7 -6 -7 -7 -1 -8 -4 7
# user = User()
# print(user.rank) # => -8
# print(user.progress) # => 0
# user.inc_progress(-3)
# print(user.rank) # => -6
# print(user.progress) # => 50
# user.inc_progress(6)
# print(user.rank) # => 7
# print(user.progress) # => 60
# user.inc_progress(7)
# print(user.rank) # => 7
# print(user.progress) # => 63

# -6 6 -2 1 1 3 8 -7 -1 5
# user = User()
# print(user.rank) # => -8
# print(user.progress) # => 0
# user.inc_progress(-6)
# print(user.rank) # => 
# print(user.progress) # => 
# user.inc_progress(6)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(-2)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(1)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(1)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(3)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(8)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(-7)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(1)
# print(user.rank) # => 
# print(user.progress) # => 0
# user.inc_progress(5)
# print(user.rank) # => 
# print(user.progress) # => 0

# -5 -8 7 -7 7 -5 -7 8 2 -2
user = User()
print(user.rank) # => -8
print(user.progress) # => 0
user.inc_progress(-5)
print(user.rank) # => 
print(user.progress) # => 
user.inc_progress(-8)
print(user.rank) # => 
print(user.progress) # => 93
user.inc_progress(7)
print(user.rank) # => 
print(user.progress) # => 0
user.inc_progress(-7)
print(user.rank) # => 
print(user.progress) # => 0
user.inc_progress(7)
print(user.rank) # => 
print(user.progress) # => 0
user.inc_progress(-5)
print(user.rank) # => 
print(user.progress) # => 0
user.inc_progress(-7)
print(user.rank) # => 
print(user.progress) # => 0
user.inc_progress(8)
print(user.rank) # => 
print(user.progress) # => 0
user.inc_progress(2)
print(user.rank) # => 
print(user.progress) # => 0
user.inc_progress(-2)
print(user.rank) # => 
print(user.progress) # => 0