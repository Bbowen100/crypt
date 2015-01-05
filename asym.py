'''Asym
This file is a text based prompt for a user to perform an A-symmetrical
encryption
'''
import crypt

def main():
    print()
    print('to end this program please enter "done"')
    print('encryption - 0 , decryption - 1')
    action = input('Please enter the integer of the action || "done": ')
    
    if(action == '0'):
        str0 = input('word/phrase: ')
        print('data:',crypt.encrypt(str0))
        main()
        
    elif(action == '1'):
        str1 = int(input('key: '))
        str12 = input('text: ')
        ans = {str1: str12}
        print('decrypted text:',crypt.decrypt(ans))
        main()
        
    elif(action == 'done'):
        print('Alright Bye Bye.')
        
if(__name__ == "__main__"):
    main()  
