print("Welcome to xmas")
import time ; time.sleep(3)
print("")
print("FOLLOW ME")
print("""SNAPCHAT:gxreguy
instagram:xmlven""")
import time ; time.sleep(3)
usr=input('Enter Email Id:')  

pwd=input('Enter Password:')  

import time ; time.sleep(3)
print("Hello, " + usr)
import time ; time.sleep(3)

print("did you just get trolled?")
import time ; time.sleep(3)
print(">              <")
print(" >            <")
print("  >          <")
print("   >        <")
print("    >      <")
print("     >    <")
print("      >  <")
print("       ><")
print("      >  <")
print("     >     <")
print("    >       <")
print("   >         <")
print("  >           <")
print(" >             <")
print(">               <")

print("M. A. S.  YESSSSSSSS")
import time ; time.sleep(3)
name=input('write your name:')
import time ; time.sleep(2)
print("")
print("Give us a sec while we type your name into a sentence...")
print("")
import time ; time.sleep(2)
print("did you know this dudes a bitch. who you ask? " + name)
import time ; time.sleep(2)
print("")
i = 1
while i <=10:
  print(i)
  i = i + 1
print("")
from datetime import date

today = date.today()
print("Today's date:", today)
print ("———————————")
print ("Todays Time Is Below")
print("———————————")
import time
print (time.strftime("%H:%M:%S"))
import time ; time.sleep(2)
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='target', dest='target')
parser.add_argument('-c', help='choice', dest='choice')
parser.add_argument('--domains', help='stdin type: domain', dest='domains', action='store_true')
parser.add_argument('--ips', help='stdin type: ip', dest='ips', action='store_true')
args = parser.parse_args()

ips = args.ips
target = args.target
choice = args.choice
domains = args.domains
data = False
if ips or domains:
    data = sys.stdin.readlines()

arged = False
if target and choice:
    arged = True

if sys.version_info < (3, 0):
    input = raw_input
def menu():
    print('''
%s1.%s trace ''')
def dog(choice, target):
    if not args.target:
        banner()
    if arged:
        hq(choice, target)
    else:
        while True:
            menu()
            result = False
            choice = input('\033[1;91m>>\033[0m ')
            hq(choice)
if data:
    kind = 'domain'
    if ips:
        kind = 'ip'
    targets = extractor(data, kind)
    if choice:
        for target in targets:
            print ('%s %s' % (run, target))
            hq(choice, target)
            print (red + ('-' * 60) + end)
    else:
        for target in targets:
            sys.stdout.write(target + '\n')
