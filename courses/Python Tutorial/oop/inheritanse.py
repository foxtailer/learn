class Verification:
  def __init__(self, login, password):
    self.login = login
    self.password = password
    self.__lenPassword()

  def __lenPassword(self):
    if len(self.password) < 8:
      raise ValueError ("Week password!")
    
  def save(self):
    with open("users", "a") as r:
      r.write(f"{self.login, self.password}\n")


class V2(Verification):

  def __init__(self, login, password, age):
    # super().__init__(self, login, password)
    Verification.__init__(self, login, password)
    self.save()
    self.age = age
    
  def save(self):
    with open("users", "r") as r:
      for i in r:
        if i == f"{self.login, self.password}\n":
          raise ValueError("Alredy exist")
    
    Verification.save(self)



x = V2("x", "123456789")
x.save()