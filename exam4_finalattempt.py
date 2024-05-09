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
  kmer_list = [] #this is the list of kmers from the sequence being analyzed
  item2_list2 = [] #this a list of the kmer+subs_kmer pairs that will be going into the output file
  for i in genome_length:
    kmer = genome_seq[i:i+k] #find all kmers based on indeces
    if kmer not in kmer_list: #make sure kmer is unique
      if len(kmer) == k: #make sure length is appropriate (=k)
        kmer_list.append(kmer) #add to list of kmers
        for kmer in kmer_list:
          for p in re.finditer(kmer, genome_seq): #for each kmer, find the location within the sequence
            subs_kmer = genome_seq[p.start()+1:p.end()+1] #and then find the subsequent kmer
            if [kmer, subs_kmer] not in item2_list2: #make sure pair of kmer+subs_kmer is unique
              if len(subs_kmer) == k: #make sure length is appropriate for subs_kmer as well
                item2_list2.append([kmer, subs_kmer])
              else:
                if len(kmer) == k: #makes sure to include kmers that dont have a full-length subs_kmer
                  item2_list2.append([kmer])
                  with open("output_kmerssubs.txt", "a") as file67: #67 is a random number, i just dont want overlap with other variable names
                    for apple in item2_list2: #im getting creative with variable names
                      file67.write(",".join(map(str, apple)) + "\n") #make the output file with line breaks between each pair
                      
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
  sequence = "" #we are going to be putting every line into one single string
  part2_list = [] # this actually does nothing
  with open(path, 'r') as file:
    for line in file:
      if line.strip() not in sequence: #take each line and put them together to form one single string
        sequence += line.strip() #turning all lines into a single sequence
        print(sequence) #could potentially make a .txt output here to show what sequence actually looks like going into the main function
        kmers_and_subskmers(sequence) #run thru main function to produce an output file with pairs of kmers+subs_kmers
          
def find_k(path33): #this is code for item 3
  """
  This function will find the smallest value of k such that there is only one unique subsequent kmer for each kmer.
  This value will print in the terminal.
  
  path33 (path): this is the path to the file containing the sequences that will be processed
  
  Return:
    a k-value such that each kmer in the sequence only has one unique subsequent kmer
  
  """
  kmers_and_subs_manylines(path33) #once again, this is just a random number for the var name
  for coconut in range(len(item2_list2)): #coconut is meaningless, and so is lime
    lime = coconut + 1
    if item2_list2[coconut:coconut+k] = item2_list2[lime:lime+k]: #compare pairs of kmers+subs_kmers to each other to make sure they are unique
      k += 1 #if there are repeats, add 1 to k
      kmers_and_subs_manylines(path33) #and run the main function with this new k value
      if item2_list2[coconut:coconut+k] != item2_list2[lime:lime+k]: #make sure there are no repeats
        print(k) #and if no repeats, print the k value
