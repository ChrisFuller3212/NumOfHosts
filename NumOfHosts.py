"""
NumOfHosts.py

Calculating Hosts from a Network

By: CHRISTIAN FULLER

**The goal of this function is to take input from the user for
the IP Address and the Network Mask. From there, we want to calculate
the number of hosts in the network given by the user and then finally, we 
want to display that number of hosts back to the user. **

"""
#i will be putting my work into a single function called 'main'
def main():
    #using the try and except statement will allow me
    #to use only one error message, therefore saving me
    #typing
    try:

        while True:
            #this line takes ipaddr as input from user
            ipaddr = input("Enter a IP address: ")

            #this line validates the ipaddr from user
            ipOctets= ipaddr.split(".")

            #here, print the ipOctets list using for loop
            ipaddr_list = [int(i) for i in ipOctets]

            #these are parameters made to ensure the integrity
            #of the input so that the input is valid for the ipaddr
            if (len(ipaddr_list) == 4) and \
                (ipaddr_list[0] != 127) and \
                (ipaddr_list[0] != 169) and  \
                (0 <= ipaddr_list[1] <= 255) and \
                (0 <= ipaddr_list[2] <=255) and \
                (0 <= ipaddr_list[3] <= 255):
                break
            
            #if the user doesnt enter a correct value, they try again
            else:
                print("Invalid IP Address, please try again")
                continue

        #this is a pre-made list consisting of possible network/subnet masks
        possibleMasks = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        while True:

            #this line is to take the network mask input from the user
            netmask = input("Enter a Subnet Mask: ")

            #this line validates the entered network mask
            netmaskSubnet = [int(s) for s in netmask.split(".")]

            #here, print the netmaskSubnet using for loop
            #just like before, these are parameters made to ensure the integrity
            #of the input so that the input is valid for the netmask
            if (len(netmaskSubnet) == 4) and \
                (netmaskSubnet[0] == 255) and \
                (netmaskSubnet[1] in possibleMasks) and \
                (netmaskSubnet[2] in possibleMasks) and \
                (netmaskSubnet[3] in possibleMasks) and \
                (netmaskSubnet[0] >= netmaskSubnet[1] >= netmaskSubnet[2] >= netmaskSubnet[3]):
                break

            #like before, if the user doesnt enter a correct value, they try again
            else:
                print("Invalid Network Mask, please try again")
                continue

        #here is a empty list that will be added (appended) with the for loop
        #adding the binary of ipaddr_list
        ipBinary = []

        #this line converts the ip octets from above to binary
        ipoctetsinBinary = [bin(i).split("b")[1] for i in ipaddr_list]

        #make each binary octet of 8 bit length by padding zeros
        #the zfill method adds zeros at the beginning of the string until 
        #the length of a string equals the specified width parameter.
        for i in range(0,len(ipoctetsinBinary)):
            if len(ipoctetsinBinary[i]) < 8:
                paddedBinary = ipoctetsinBinary[i].zfill(8)
                ipBinary.append(paddedBinary)
            else:
                ipBinary.append(ipoctetsinBinary[i])

        #the same concept here as above, this empty list will be filled with
        #the binary of the netmaskSubnet
        netmaskBinary = []

        #Here, i convert each subnet octet to binary by using the split function
        #while also using bin to convert the string to binary
        netmaskOctetsInBinary = [bin(i).split("b")[1] for i in netmaskSubnet]

        #The goal here was to make each binary octet of 8 bit length by adding zeros
        for i in netmaskOctetsInBinary:
            if len(i) < 8:
                paddedMasksBinary = i.zfill(8)
                netmaskBinary.append(paddedMasksBinary)
            else:
                netmaskBinary.append(i)

        #this line is to join netmaskBinary to a list
        #empty variable called subnetmaskBinary. The join 
        #returns a string in which the elements of the sequence 
        #have been joined by the str separator, in this case
        #subnetmaskBinary and netmaskBinary
        subnetmaskBinary = "".join(netmaskBinary)

        #these two lines will calculate number of hosts
        #by using the count from 0 function and by using the
        #abs function which returns the absolute value of a number (number's distance from zero)
        numberofZeros = subnetmaskBinary.count("0")
        numberofHosts = abs(2 ** numberofZeros )

        #lastly, print the result
        print("The entered ip address is: " + ipaddr)
        print("The entered subnet mask is: " + netmask)
        print('The number of hosts in network', ipaddr, 'is', numberofHosts)

    #this is the ValueError message i have in case 
    #the user enters the wrong input 
    except ValueError:
        print("You have entered a incorrect value, bye bye!")

#this last if statement states: 
#if the name = main then this file is the main file
if __name__ == '__main__':
    main()
