#EXAM 4 CSENA
#!/usr/bin/env python3

def kmers_and_subskmers(genome_seq): #remember to indent everything
  """
  This is a function to find all kmers within a genome sequence, given that k = 2
  Function will also find all unique subsequent kmers of each kmer
    Output will be formatted as a list of lists where [[kmer1, subs_kmer1.1], [kmer1, subs_kmer1.2], [kmer2, subs_kmer2.1], etc]
      so each unique pair of kmer and subsequent kmer will be placed in its own list
    This list of lists will print into the terminal
  
  genome_seq (str): this is the genome sequence that is being analyzed
  
  Return:
    list of lists containing each kmer and each unique subsequent kmer
  
  """
  import re
  k = 2
  genome_length = list(range(len(genome_seq))) #the nested loops go crazy
  kmer_list = []
  item2_list2 = []
  for i in genome_length:
    kmer = genome_seq[i:i+k]
    if kmer not in kmer_list:
      if len(kmer) == k:
        kmer_list.append(kmer) 
        for kmer in kmer_list:
          for p in re.finditer(kmer, genome_seq):
            subs_kmer = genome_seq[p.start()+1:p.end()+1]
            if [kmer, subs_kmer] not in item2_list2:
              if len(subs_kmer) == k:
                for index in range(k):
                  if subs_kmer[index] != ' ': #\n STILL SHOWS UP, fuck it we ball
                    item2_list2.append([kmer, subs_kmer])
              else:
                if len(kmer) == k:
                  item2_list2.append([kmer])
                  print(item2_list2)

def kmers_and_subs_manylines(path):
  with open(path, 'r') as file:
    for line in file:
      kmers_and_subskmers(line) #ok it works, but why does it have \n line breaks
      #omg does it think that \n is a fucking character, does it think the line break is a character
      #LMAO just work on part 3
