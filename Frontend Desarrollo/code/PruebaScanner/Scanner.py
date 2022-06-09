#! /usr/bin/python
# -*- coding:utf-8 -*-

import sys, os, time
import sane

output = sys.argv[1] if len(sys.argv) > 1 else 'output.pdf'
dirname = '/tmp/%s-%s' % (time.time(), os.getpid())
os.mkdir(dirname)

sane.init()
print 'Available devices:', sane.get_devices()

s = sane.open(sane.get_devices()[0][0])
s.mode = 'color'
s.resolution = 150

print 'Device parameters:', s.get_parameters()

files = []
for i, img in enumerate(s.multi_scan()):
    fname = os.path.join(dirname, 'img%s.pdf' % i)
    files.append(fname)

    print "Saving on '%s'" % fname
    img.save(fname)

    if raw_input('Another page? (Y/n): ').lower().startswith('n'):
        break

s.close()

print "scanned pages: %s" % (i+1)

if len(files)  == 1:
    os.system("mv '%s' '%s'" % (fname, output))
else:
    os.system("pdfjoin --fitpaper true --outfile %s %s" % (output, str.join(' ', files)))