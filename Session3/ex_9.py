import re


def upper_case_callback(matchobj):
    return matchobj.group(0).upper()


rex = 'snow|frozen|icy'
pattern = re.compile(rex)

fw = open('./frozen_bis.srt', mode='w')
fw.write(pattern.sub(upper_case_callback, open('./frozen.srt').read()))
