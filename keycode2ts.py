import datetime
import time

from pynput.keyboard import Key, Listener

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", default=None,
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print any messages to stdout")
parser.add_option("-t", "--title", dest="title", default="",
                  help="add experiment title to the filename", metavar="TITLE")
parser.add_option("-n", "--nowtime",
                  action="store_true", dest="nowtime", default=False,
                  help="add timestamp to filename")

(options, args) = parser.parse_args()

def on_press(key):
    msg = '{},{} pressed'.format(time.time(), key)
    if file:
        print(msg, file=file)
    if options.verbose:
        print(msg)

def on_release(key):
    msg = '{},{} release'.format(time.time(), key)
    if file:
        print(msg, file=file)

    if options.verbose:
        print(msg)
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
now  = time.strftime("%Y-%m-%d %H-%M-%S")
file = None

if options.filename:
    fname = options.filename
    if options.title != "":
        fname = "{}_{}".format(options.filename, options.title)
    if options.nowtime:
        fname = "{}_{}_{}".format(options.filename, options.title, now)
    file = open(fname, "w")


with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
