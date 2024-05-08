#EXAM 4 CSENA
#!/usr/bin/env python3

def kmers_and_subskmers(genome_seq): #ignore how disgustingly long this function is
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
  import re #allows me to use re.finditer() later
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
                item2_list2.append([kmer, subs_kmer])
              else:
                if len(kmer) == k: #makes sure to include kmers that dont have a full-length subs_kmer
                  item2_list2.append([kmer])
                  with open("output_kmerssubs.txt", "a") as file67: #67 is a random number, i just dont want overlap with other variable names
                    for apple in item2_list2: #im getting creative with variable names
                      file67.write(",".join(map(str, apple)) + "\n") #PERFECT
                      
def kmers_and_subs_manylines(path):
  """
  This function will find all kmers and unique subsequent kmers, given that k=2, within 
  a file containing multiple genome sequences.
  Note: this will take a whie to run depending on size of file being processed, may result in disturbingly large output
  
  path (path): this is the path to the file containing the genome sequences that will be processed
  
  Return:
    Output file "output_kmerssubs.txt" with each kmer and one of its subsequent kmers on each line
    (if you already have a file named "output_kmerssubs.txt" from using kmers_and_subskmers(), it will be overwritten)
  """
  sequence = ""
  part2_list = []
  with open(path, 'r') as file:
    for line in file:
      if line.strip() not in sequence:
        sequence += line.strip() #turning all lines into a single sequence
        print(sequence) #could potentially make a .txt output here to show what sequence actually looks like going into the main function
        kmers_and_subskmers(sequence) #returns repeats for some reason
          
def find_k(path33): #this is how the code for item 3 should theoretically work, but who knows if it actually will
  kmers_and_subs_manylines(path33)
  for coconut in range(len(item2_list2)):
    lime = coconut + 1
    if item2_list2[coconut:coconut+k] = item2_list2[lime:lime+k]:
      k += 1
      kmers_and_subs_manylines(path33)
      if item2_list2[coconut:coconut+k] != item2_list2[lime:lime+k]:
        print(k)
