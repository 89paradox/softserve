# minecraft manager for softserve
import os
if os.path.exists("paper-1.18.2-359.jar"):
  os.system("java -jar paper-1.18.2-359.jar")
  exit()
else:
  print("Downloading MC..")
  os.system("wget https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/359/downloads/paper-1.18.2-359.jar")
  print("Running..")
  os.system("java -jar paper-1.18.2-359.jar")
  exit()
exit()
