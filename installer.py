#!/usr/bin/python
import os, sys
from time import sleep

if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

header = """

  ______________________
< dedsploit installer!!! >
  ----------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||

"""

print header
print "\033[1;36mOperating Systems Available:\033[1;36m "
print "===================================="
print "(1) Kali Linux / Ubuntu "
print "(2) Darwin / macOS"
print "===================================="

option = input("\033[36m[>] Select Operating System: \033[0m")

if option == 1:
    print "\033[1;33m[*] Installing... [*]\033[0m"
    sleep(2)
    install = os.system("apt-get update && apt-get install -y build-essential slowhttptest python-pip git")
    install1 = os.system("pip2.7 install python-nmap paramiko scapy terminaltables")
    install2 = os.system("cp -R dedsploit/ /opt/ && cp dedsploit.py /opt/dedsploit && cp run.sh /opt/dedsploit && cp run.sh /usr/bin/dedsploit && chmod +x /usr/bin/dedsploit")

    print "\033[1;32m[!] Finished Installing! Run 'dedsploit' to run program [!]\033[0m"
    sys.exit()
elif option == 2:
    print "\033[1;33m[*] Installing... [*]\033[0m"
    sleep(2)
    brew = os.popen('if ! type "brew" > /dev/null; then echo "OS has brew"; else echo "No homebrew. Preparing to install..."; fi').read()
    if brew == "No homebrew. Preparing to install...":
        install = os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    git = os.popen('if ! type "git" > /dev/null; then echo "OS has git"; else echo "No git. Preparing to install..."; fi').read()
    userAccount = os.popen("who am i | awk '{print $1}'").read()[:-1]
    if git == "No git. Preparing to install...":
            install1 = os.system("sudo -H -u "+userAccount+" bash -c 'brew update && brew install git'")
    install1half = os.system("sudo -H -u "+userAccount+" bash -c 'brew install slowhttptest'")
    pypip = os.popen('if ! type "git" > /dev/null; then echo "OS has pip"; else echo "No pip. Preparing to install..."; fi').read()
    if pypip == "No pip. Preparing to install...":
        os.system("easy_install pip")
    install2 = os.system("pip2.7 install python-nmap paramiko scapy terminaltables")
    install3 = os.system("git clone https://github.com/dugsong/libdnet.git && cd libdnet && ./configure && make && cd python && python2.7 setup.py install && cd .. && cd .. && rm -rf libdnet")
    install4 = os.system("cp -R dedsploit/ /opt/ && cp dedsploit.py /opt/dedsploit && cp run.sh /opt/dedsploit && cp run.sh /usr/local/bin/dedsploit && chmod +x /usr/local/bin/dedsploit &&  clear && echo 'Finished installing! Run sudo python dedsploit.py to start.'")

else:
    print "Whoops! Something went wrong!"
