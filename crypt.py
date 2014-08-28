'''Crypt
This file contains encryption & decryption Functions. 
This will be imported into any encryption related programs.

REQ: for simplicity I have refined this algorithm to members of the alphabet
ie. special characters and numbers will not be decrypted accurately

'''
import random

global __start__
__start__ = ord('a')

global __end__
__end__ = ord('z')
   
def encrypt(string):
   '''(str)->(dict)
   The encrypt function takes a string a returns the randomly generated key
   with the encrypted text in an associative array.
   >>> encrypt('a')   
   {21: 'v'}
   
   >>> encrypt('whatever')
   {17: 'oyrlvnvj'}
   
   >>> encrypt('What is life')
   {23: 'ufxr gq jgdc'}
   
   '''
   _key = 0
   afterstr = ''
   __afterdict__= {}
   b4str = str(string).lower()  
   
   # first things first gotta get a key
   
   # note 26 letters in the alphabet & 10 ints + special chars
   
   # note to self:  remember ord() and char()
   _key = random.randint(1, 25)
   '''the key will serve as a method to varify the correct reciever and to 
         encrypt the cyphertext'''      
   
   # make a list of the elements in the cyphertext
   b4lst = list(b4str)
   
   #make list of ascii numbers in string
   b4lst2 = []
   for i in b4lst:
      if(i == ' '):
         b4lst2.append(' ')
      else:
         b4lst2.append(ord(i))
   
   # make the list of new ascii values
   i = 0
   afterlst = []
   while(i  < len(b4lst2)):
      if(b4lst2[i] != ' '):
         if((b4lst2[i] + _key) >= __end__):
            #if it exceeds the letter range
            diff = (b4lst2[i] + _key) - __end__
            afterlst.append(diff + __start__)
            i+=1
            
         elif((b4lst2[i] + _key) <= __end__):
            #if it is within the letter range
            afterlst.append((b4lst2[i] + _key))
            i+=1
      else:
         afterlst.append(' ')
         i+=1
         
   # now we have to change the new ascii values back into characters
   afterlst2 = []
   for i in afterlst:
      if(i == ' '):
         afterlst2.append(' ')
      else:
         afterlst2.append(chr(i))
      
   # gotta stringyfy afterlst2
   afterstr = stringyfy(afterlst2)
   
   # gotta remember the key and the encrypted text so we can decrypt
   __afterdict__ = {_key: afterstr}
   return __afterdict__
 
def decrypt(dic):
   '''(dict)-> (str)
   this function will take __afterdict__ and reverse the encrytion function to 
   produce the origianl cypher text with the help of the key of course!
   
   >>> decrypt({25: 'z'})
   'a'
   
   >>> decrypt({17: 'oyrlvnvj'})
   'whatever'
   
   >>> decrypt(encrypt('What is life'))
   'What is life'
   '''
   # remember dict.keys() & dict.vaules()
   # get the key & the encrypted txt
   keys = list(dic.keys())
   key = int(keys[0])
   cryptxt = dic.get(key)
   
   # apply decryption algorithm
   #make a list of decrypted ascii values for cyphertxt
   numtxt = []
   for i in list(cryptxt):
      if(i == ' '):
         numtxt.append(' ')
      # special case
      elif((ord(str(i)) - key) < __start__):
         diff1 = ord(str(i)) - __start__
         diff2 = key - diff1
         final = __end__ - diff2
         numtxt.append(final)
      else:
         numtxt.append(ord(str(i)) - key)
   
   #make decrpyt list
   dcryptlst = []
   for i in numtxt:
      if(i == ' '):
         dcryptlst.append(' ')
      else:
         dcryptlst.append(chr(i))
         
   #make it a astring
   final_string = stringyfy(dcryptlst)
   
   return final_string
      
#-----------------------------------------------------------------------------#      
def stringyfy(lst):
   '''(list) -> string
   when a list is imuted it takes all the elements and concatenates 
   them to make a string.
   
   >>> stringyfy([1,2,3,4])
   '1234'
   
   >>> stringyfy(['me',' ','is',' ','so',' ','fine'])
   'me is so fine'
   
   REQ: integers, floats, strings and characters ONLY!
   
   '''
   #in retrospect not the longest of codes :)
   nstring = ''
   for i in lst:
      nstring = nstring + str(i)
   return nstring
