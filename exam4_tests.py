#exam 4 test script CSENA
#!/usr/bin/env python3

def kmers_and_subskmers_shortseq():
  expected1 = [[AG,GT],[GT,TT],[TT,TA],[TA,AG],[AG]]
  assert kmers_and_subskmers('AGTTAG') == expected1
