import simpleModule
import platform
from moduleWithMultipleExports import person

simpleModule.greeting("Cleomir")
print(platform.system())
print(dir(platform))
print(person)