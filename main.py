def observed():
  observations = set()
  for i in range(7):
    item = input("Enter an item: ")
    observations.add(item)
  #print(observations)
  #print(type(observations))
#observed()
  return observations


def run():
  print("counting observations ...")
  l = observed()
  count = 0
  for i in l:
    print(i)
    count = count + 1

  #mySet = ()
  #mySet = {("a",1),("b", 4), ("c", 1), ("d", 1)}
run()