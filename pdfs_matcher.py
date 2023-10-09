import hashlib 

def hash_file(fileName1, fileName2): 
  
    # to store the hash of a file 
    h1 = hashlib.sha1() 
    h2 = hashlib.sha1() 

    with open(fileName1, "rb") as file:  
        # and read the file in small chunks 
        # because we cannot read the large files. 
        morceau = 0
        while morceau != b'': 
            morceau = file.read(1024) 
            h1.update(morceau) 
            

    with open(fileName2, "rb") as file: 

        # Use file.read() to read the size of file a 
        # and read the file in small chunks 
        # because we cannot read the large files. 
        morceau = 0
        while morceau != b'': 
            morceau = file.read(1024) 
            h2.update(morceau) 
    
            #hexdigest() is of 160 bits 
        return h1.hexdigest(), h2.hexdigest() 
  
  
# here you need to specify to the function the 2 documents that you want to verify 
msg1, msg2 = hash_file("rib khaled.pdf","rib khaled.pdf") 
  
if(msg1 != msg2): 
    print("les deux fichiers ne sont pas identiques") 
else: 
    print("les deux fichiers sont identiques") 