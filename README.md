# keycode2ts
Timestamp &amp; keycode dumping. Useful for experimental work

# about

Imagine that you are making the experiment with measuring EEG and press some buttons on keyboard to label consciousness states or other brain processes. keycode2ts tool can simplify part of the work of labeled data creation. Use it.

# help
```
$$$: python keycode2ts.py --help
Usage: keycode2ts.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILE, --file=FILE  write report to FILE
  -q, --quiet           don't print any messages to stdout
  -t TITLE, --title=TITLE
                        add experiment title to the filename
  -n, --nowtime         add timestamp to filename
```
# example

```
$$$: python keycode2ts.py -n -t "experiment breathing" -f first
1533667188.0371642,'d' pressed
1533667188.042151,'s' pressed
...

$$$: git\keycode2ts>more "first_experiment breathing_2018-08-07 20-39-47"
1533667188.0371642,'d' pressed
1533667188.042151,'s' pressed
...
```
