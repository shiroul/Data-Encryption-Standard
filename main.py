class DataEncryptionStandard:
    

    #to generate initial permutation
    initialPermutation = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]
    
    #to generate 56 bit key from 64 bit key
    keyPermutation = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    
    #how much to shift the key for each round
    shiftTable = [
        1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    #to generate 48 bit key from 56 bit key
    #after shifting the key
    compressionPermutation = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]
    
    #to generate 48 bit key from 32 bit right part of initial permutation
    expansionPermutation = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1]
    
    #used in sBox function
    #to generate 32 bit key from 48 bit key
    sBoxTable = [
        # S1
        [
            14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
            0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
            4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
            15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
        ],
        # S2
        [
            15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
            3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
            0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
            13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
        ],
        # S3
        [
            10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
            13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
            13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
            1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
        ],
        # S4
        [
            7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
            13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
            10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
            3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
        ],
        # S5
        [
            2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
            14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
            4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
            11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
        ],
        # S6
        [
            12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
            10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
            9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
            4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
        ],
        # S7
        [
            4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
            13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
            1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
            6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
        ],
        # S8
        [
            13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
            1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
            7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
            2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
        ]
    ]

    pBoxPermutation = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25]

    finalPermutation = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
    
    def __init__(self):
        self.keyStore = []

    def mainFunction(self, s, key, mode):

        # print('PLAINTEKS : ', s, '\n')
        s = self.initialPermutationFunction(self.convertBinary(s)) #initial permutation
        
        L = s[:32]
        R = s[32:]
        if mode == 1:
            index = 15
        else:
            key = self.keyPermutationFunction(self.convertBinary(key)) #key permutation
            C = key[:28]
            D = key[28:]
            self.keyStore = []
        
        for round in range(16):
            print(f"Round : {round+1} =============================================================================================") # print round info
            if mode == 1:
                C , D = self.keyStore[index][:28], self.keyStore[index][28:]
                index-=1
            else:
                C , D = self.shiftKey(C, D, round)
                self.keyStore.append(C + D)

            
            nextL = R
            nextR = self.xorFunction(L, self.sBoxFunction(self.xorFunction(self.expansionPermutationFunction(R), self.compressedPermutationFunction(C + D))))
            L , R = nextL, nextR

            # print('---RESULT EACH ROUND--\n')
            # print(f'L{round+1} : ', L)
            # print(f'Right{round+1} : ', R)
            # print(f'C{round+1} : ', C)
            # print(f'D{round+1} : ', D)
        
        # print('\n---FINAL ROUND---\n')
        # print('L16 : ', L, end='')
        # print(' - R16 : ', R)
        # print('\n\t\t\t\t========SWAP=========\n')
        L, R = R, L
        # print('L16 : ', L, end='')
        # print(' - R16 : ', R)

        temp = self.convertToString(self.finalPermutationFunction(L + R))
        # print(temp)
        return temp
    
    def encrypt(self, plainTeks, key):
        temp = self.mainFunction(plainTeks, key, 0)
        # print('CiperTeks : ', temp)
        return temp
    
    def decrypt(self, ciperTeks):
        # print(ciperTeks)
        return self.mainFunction(ciperTeks, 0, 1)

    # function to convert string to binary
    # string input
    # and return 8 bit binary string
    def convertBinary(self, s):
        # print('---CONVERT BINARY---\n', s , ' => ', end='')
        s = ''.join(format(ord(i), '08b') for i in s)
        # print(s, '\n')
        return s
    
    # function to permutate plaintext that already converted to binary
    # string input in binary
    # and return permutated string
    def initialPermutationFunction(self, s):
        temp = ''
        for x in self.initialPermutation:
            temp+= s[x-1]
        # print('---INITIAL PERMUTATION---\n', s , ' => ', temp, '\n')
        return temp
    
    # function to permutate key that already converted to binary
    # string input in 64 bit binary
    # and return permutated string 56 bit long
    def keyPermutationFunction(self, key):
        temp = ''
        for x in self.keyPermutation:
            temp+= key[x-1]
        # print('---KEY PERMUTATION---\n', key , ' => ', temp, '\n')
        return temp
    
    # function to shift key
    # string input in binary
    # and return shifted key
    def shiftKey(self, left, right, round):
        # print(f'---LEFT SHIFT ROUND---\nShift : {self.shiftTable[round]}x')
        # print('Original')
        # print('Left : ', left, '-- Right : ', right)
        for i in range(self.shiftTable[round]):
            left = left[1:] + left[0]
            right = right[1:] + right[0]
        # print('Shifted')
        # print('Left : ', left, '-- Right : ', right, '\n')
        return left, right
    
    # function to compress key
    # string input in 56 bit binary
    # and return compressed key 48 bit long
    def compressedPermutationFunction(self, key):
        # print('---COMPRESSED PERMUTATION---\n', key , f'{len(key)} bit => ', end='')
        temp = ''
        for x in self.compressionPermutation:
            temp+= key[x-1]
        # print(temp, f'{len(temp)} bit\n')
        return temp
    
    # function to expand right part of initial permutation
    # string input in 32 bit binary right part of initial permutation
    # and return expanded key 48 bit long
    def expansionPermutationFunction(self, s):
        # print('---EXPANSION PERMUTATION---\n', s , f'{len(s)} bit => ', end='')
        temp = ''
        for x in self.expansionPermutation:
            temp+= s[x-1]
        # print(temp, f'{len(temp)} bit\n')
        return temp
    
    # function to xor two binary string
    # input 2 binary string
    # and return xor result
    def xorFunction(self, s1, s2):
        # print('---XOR FUNCTION---\n', s1 , ' ^ ', s2, ' => ', end='')
        temp = ''
        for x in range(len(s1)):
            temp += str(int(s1[x]) ^ int(s2[x]))
        # print(temp, '\n')
        return temp
    
    # function to for sBox Round
    # input 48 bit binary key
    # split 48 bit into 8 parts of 6 bit
    # each part take first and last bit as row
    # and the rest as column
    # use sBoxTable to get the value
    # each part using different sBox
    # and return 32 bit binary key

    def sBoxFunction(self, key):
        print('---S-BOX FUNCTION---\nkey : ', key) # print S-Box input
        temp = ''
        index = 0
        for x in range(0, 48, 6):
            
            row = int(key[x] + key[x+5], 2)
            column = int(key[x+1:x+5], 2)
            temp += format(self.sBoxTable[index][row*16 + column], '04b')
            print(f'S-Box {index+1} : ', key[x:x+6], ' => ', temp[-4:]) # print S-Box output for each box
            index += 1
        print('S-Box Result : ', temp, '\n') # print S-Box result
        return self.pBoxFunction(temp)
    
    # function to permutate sBox output
    # input 32 bit binary key
    # and return permutated key 32 bit long
    def pBoxFunction(self, key):
        # print('---P-BOX FUNCTION---\n', key , f'{len(key)} bit => ', end='')
        temp = ''
        for x in self.pBoxPermutation:
            temp += key[x-1]
        # print(temp, f'{len(temp)} bit\n')
        return temp
    
    # function to permutate final output after 16 rounds
    # input 64 bit binary key
    # and return permutated key 64 bit long
    def finalPermutationFunction(self, s):
        # print('\n---FINAL PERMUTATION---\n', s , f'{len(s)} bit => ', end='')
        temp = ''
        for x in self.finalPermutation:
            temp+= s[x-1]
        # print(temp, f'{len(temp)} bit\n')
        return temp
    
    # function to convert binary string to character
    # input 64 bit binary string
    # convert each 8 bit to character
    # and return string
    def convertToString(self, s):
        print('---CONVERT TO STRING---\n', s , ' => ', end='') # print before converting to string
        temp = ''
        for x in range(0, len(s), 8):
            temp += chr(int(s[x:x+8], 2))
        print(temp) # print after converting to string
        print('\nConverted : ',temp) # print converted string
        return temp