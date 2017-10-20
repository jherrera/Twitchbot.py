import socket, sys, time
import config

class TwitchBot():
    # Private variables
    sock = None     # Socket object
    tokens = []     # Holds tokens created with the tokenize() method
    config = {}     # Config options
    def __init__(self, options):
        self.config = options
    def connect(self, hostname, port):
        self.sock = socket.socket()
        try:
            self.sock.connect((hostname, port))
            self.sock.setblocking(0)
        except:
            print("Error! An error occurred while trying to establish a connection to the server.")
            exit()
        self.write('PASS '  + self.config['password'], hide=True)
        self.write('NICK '  + self.config['username'])
        self.write('CAP REQ :twitch.tv/membership')
        if(len(self.config['channel']) > 0):
            self.write('JOIN #' + self.config['channel'].lstrip('#').lower())
        #self.write('CAP REQ :twitch.tv/commands')
        #self.write('CAP REQ :twitch.tv/tags')
    def loop(self):
        tok = self.gettok
        while True:
            data = self.read()
            if data == '':
                self.wait()
                continue
            for line in data.split("\r\n"):
                if line.strip() == '':
                    continue
                self.print('-> '+line)
                self.tokenize(line)
                if tok(1) == 'PING':
                    self.write('PONG '+tok('2-'))
                # Commands
                if tok(4) == ':!quit' and self.nick(tok(1)) == self.config['username'].lower():
                    self.quit()
    def print(self, text):
        print(text.encode("cp850", errors="replace").decode(sys.stdout.encoding))
    def wait(self):
        try:
            time.sleep(self.config['rate'])
        except KeyboardInterrupt:
            print('<- ', end="")
            sys.stdout.flush()
            i = input()
            if i.lower() in ['exit', 'quit']:
                self.quit()
            self.write(i, hide=True)
    def quit(self):
        self.write('QUIT :Bye!')
        exit()
    def write(self, text, crlf = True, hide = False):
        self.sock.send(bytes(text+("\r\n" if crlf else ""), 'utf-8'))
        if not hide:
            print('<- '+text)
    def read(self, size = 4096):
        try:
            data = self.sock.recv(size).decode("utf-8")
        except EOFError:
            return None
        except:
            return ''
        return data
    def message(self, to, msg):
        self.write("PRIVMSG " + to + " :" + msg);
    def tokenize(self, line):
        self.tokens = line.split()
    def gettok(self, n):
        if type(n) is int:
            if n == 0:
                return len(self.tokens)
            else:
                try:
                    return self.tokens[n-1]
                except IndexError:
                    return ''
        if type(n) is str:
            tmp = n.split('-')
            if len(tmp) == 1:
                return self.gettok(int(tmp[0]))
            return " ".join(self.tokens[int(tmp[0])-1:((int(tmp[1])) if tmp[1] != '' else None)])
        return ''
    def nick(self, hostmask):
        return hostmask.split('!')[0].lstrip(':')

tb = TwitchBot(config.CFG)
tb.connect('irc.twitch.tv', 6667)
tb.loop()
