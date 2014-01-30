import csv
import hashlib
import binascii
import string
FILENAME = "../data/w001day2-raw.csv"

def hex2bin(str):
   bin = ['0000','0001','0010','0011',
         '0100','0101','0110','0111',
         '1000','1001','1010','1011',
         '1100','1101','1110','1111']
   aa = ''
   for i in range(len(str)):
      aa += bin[string.atoi(str[i],base=16)]
   return aa




# kind: 1 for accel_x 
#       2 for accel_y.....
# Input : *.csv
# Output: *.bin at the same directory 
# Step: jump every x data 
# Like Step= 1, then data with index 0, 2, 4,...  will be processed
def process_data(FILENAME, kind, step):
    with open(FILENAME, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar= '|')
        newFILENAME = FILENAME.split(".csv")[0]+".bin"
        f = open(newFILENAME,'w')
        i = 0
        for row in spamreader:
            for cell in row:
                #print cell.split("\t")[1]  # accel_x
                rawdata = cell.split("\t")[kind]  # accel_y
                #print accel_y

                # if 0 then drop
                if rawdata[-6:] != '-0.0':
                    print rawdata[-6:]
                    hash_res = hashlib.sha1(rawdata[-7:]).hexdigest()
                    bindata = binascii.unhexlify(hash_res)
                #hex2bin(hash_res)
                    if i == 0:
                        f.write(bindata)
                        i = i + 1
                    if i == step:
                        i = 0
        f.close()
            
            
process_data(FILENAME, 2, 1)
