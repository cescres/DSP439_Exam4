#exam 4 test script CSENA
#!/usr/bin/env python3

#its pretty difficult to pytest a function that produces an output file so the main function will be tested only
    #if theres a way, i cant figure it out
    #my theory is if the main function works, so should the others that are based on the main function
      #best i can do
      
def kmers_and_subskmers_shortseq(): #test a short sequence
  expected1 = [[AG,GT],[GT,TT],[TT,TA],[TA,AG],[AG]]
  assert kmers_and_subskmers('AGTTAG') == expected1

def kmers_and_subskmers_noval(): #test that there will be no output for no sequence
  exected2 = []
  assert kmers_and_subskmers('') == expected2

def kmers_and_subskmers_tooshort():#makes sure function will return nothing if the sequence is too short
  expected3 = []
  assert kmers_and_subskmers('A') == []
  
def kmers_and_subskmers_oddnum(): #make sure function also works with odd-number of bases
  expected4 = [[AG,GT],[GT,TC],[TC,CG],[CG]]
  assert kmers_and_subskmers('AGTCG')
