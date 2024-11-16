def binary_sum(data1, data2):
    #integer
    int1 = int(data1, 2)
    int2 = int(data2, 2)
    #addition in integer
    int_sum = int1 + int2
    #overflow handler
    while int_sum > 0xFFFF:
        carry = int_sum >> 16
        int_sum = (int_sum & 0xFFFF) + carry 
    #to binary
    bin_sum = bin(int_sum)[2:]
    #fill in 0
    bin_sum = bin_sum.zfill(16)
    return bin_sum
def checksum(data1, data2):
    # Calc bin sum
    bin_sum = binary_sum(data1, data2)
    int_sum = int(bin_sum, 2)
    # Calc checksum
    int_checksum = ~int_sum & 0xFFFF
    bin_checksum = bin(int_checksum)[2:].zfill(16)
    return bin_checksum

def main():
    while True:
        try:
            data1 = input("Enter the first 16-digit binary number: ")
            data2 = input("Enter the second 16-digit binary number: ")
            
            if not all(digit in '01' for digit in data1) or not all(digit in '01' for digit in data2):
                raise ValueError("Invalid digit found in the number!")
            
            if len(data1) != 16 or len(data2) != 16:
                raise ValueError("Both numbers must be 16 digits long.")
            checksum_value = checksum(data1, data2)
            print(f"Checksum: {checksum_value}")
            break
        except ValueError as e:
            print(e)
            print("Please enter valid 16-digit binary numbers.")
main()
