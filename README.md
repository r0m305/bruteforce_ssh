Written by Romeos CyberGypsy
[-] For educational purposes only.
I will not be held accountable for any misuse of the sript
Usage: bruteforce_ssh.py [options]

Options:
  -h, --help            show this help message and exit
  -H HOST, --hostname=HOST
                        IP Address or url running ssh server
  -u USER, --username=USER
                        Username to bruteforce. Defaults to root
  -w WORDLIST, --wordlist=WORDLIST
                        List containing passwords, one per line
  -t THREADS, --threads=THREADS
                        Number of concurrent threads to run at a time.Range
                        between 1-15.Defaults to 5
  -T TIMEOUT, --timeout=TIMEOUT
                        Timeout in seconds. Defaults to 2 seconds

Example usage:
  python bruteforce_ssh.py -H 192.168.43.217 -u romeos -w wordlist2.txt -t 5 -T 5

  where:
        -H indicates the ip address or url hosting the ssh server
        -u indicates the username to bruteforce
        -w indicates the wordlist to use
        -t indicates the number of concurrent threads to use at a time
        -T indicates the timeout in seconds

NOTE: For higher chances of success, please use proxychains alongside this script

As always, happy hacking
