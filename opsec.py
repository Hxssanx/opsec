import random
import time

opsec = 0


def ultraopsec():
  randomdelete = random.choice([
      "delete",
      "remove",
      "erase",
      "wipe",
      "destroy",
      "obliterate",
      "annihilate",
      "exterminate",
      "eliminate",
      "purge",
  ])

  larp = random.choice([
      "install opsec",
      "install kali",
      "install linux",
      f"{randomdelete} windows",
      f"{randomdelete} macos",
      f"install android",
      f"{randomdelete} ios",
      f"crack femboys", # i really like this one👀
  ])

  current_choice = random.choice(["failed", "success"])
  time.sleep(1)
  print(f"larp@kali> sudo apt {larp}  ")
  time.sleep(0.5)
  if larp == "crack femboys":
    print("ERROR: mmhh~~ you are not allowed to do that daddy~~") # what am i doing with my life🫩
    time.sleep(3)
    current_choice = "failed"
  print(f"Execution result: {current_choice}")
  return current_choice


while opsec < 5:
  choice = ultraopsec()
  if choice == "failed":
    print(f"OPSEC LEVEL: {opsec}")
  else:
    opsec += 1
    print(f"OPSEC LEVEL: {opsec}")

while opsec >= 5:
  print("OPSEC IS TOO HIGH, STOPPING INSTALLATION")
  print("larp@kali> sudo rm -rf / --no-preserve-root") # run ts in your actual linux terminal and see what happens, i dare you
  time.sleep(3)
  while True:
    randomword = random.choice([
        "sudo",
        "apt123123",
        "insta123ll",
        "opse1313c",
        "hellow12313ord",
        "ultraopsec",
        "choice",
        "random",
        "time",
        "print",
        "while",
        "if",
        "else",
        "br123123eak",
        "oh my godd~~ go slower~~", # ouu shii this is a good one too 👀
        "cont12312312inue",
        "fo1211213r",
        "in",
        "ran1313ge",
        "le123123n",
        "str1as",
        "in123t",
        "flo123at",
        "bool",
        "list",
        "dict",
        "set",
        "tuple",
    ])
    randomdelete = random.choice([
        "deleting",
        "removing",
        "erasing",
        "wiping",
        "destroying",
        "obliterating",
        "annihilating",
        "exterminating",
        "eliminating",
        "purging",
    ])
    if randomword == "oh my godd~~ go slower~~":
      print("oh my godd~~ go slower~~")
      for i in range(1,4):
        time.sleep(0.33)
        print("...")
        time.sleep(0.33)
    else:
      print(f"{randomdelete} {randomword}...")
      time.sleep(0.01)