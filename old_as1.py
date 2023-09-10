def printAddress(address):
    octets = [address[i:i+8] for i in range(0, len(address), 8)]
    decimal_octets = [str(int(octet, 2)) for octet in octets]
    decimal_representation = ".".join(decimal_octets)
    return (decimal_representation)

def addressToBinary(decimal_address):
    octets = decimal_address.split('.')
    binary_octets = [format(int(octet), '08b') for octet in octets]
    
    binary_string = ''.join(binary_octets)
    
    return (binary_string)

def main():
    # Step 1: Select the class for IPv4 subnet mask
    subnet_class = input("Select the class for IPv4 subnet mask (A, B, C): ").upper()
    
    if subnet_class not in ["A", "B", "C"]:
        print("Invalid subnet class. Please choose A, B, or C.")
        return

    # Step 2: Enter a valid subnet mask
    valid_subnet_masks = {
        "A": list(range(8, 16)),  # Class A subnet mask range: /8 to /15
        "B": list(range(16, 24)),  # Class B subnet mask range: /16 to /23
        "C": list(range(24, 31))
    }

    while True:
        try:
            subnet_mask_length = int(input(f"Enter the subnet mask length for class {subnet_class} (/{min(valid_subnet_masks[subnet_class])} to /{max(valid_subnet_masks[subnet_class])}): /"))
            if subnet_mask_length not in valid_subnet_masks[subnet_class]:
                print(f"Invalid subnet mask length for class {subnet_class}.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid subnet mask length.")
    
    subnet_mask = ""
    for i in range(0, subnet_mask_length):
        #subnet_mask.append("1")
        subnet_mask = subnet_mask + "1"
    for i in range(subnet_mask_length, 32):
        #subnet_mask.append("0")
        subnet_mask = subnet_mask + "0"


    # Step 3: Calculate the number of subnets
    num_subnets = 2 ** (32 - subnet_mask_length)

    # Step 4: Calculate number of host addresses per subnet
    num_host_addresses = num_subnets - 2  # Subtract 2 for network ID and broadcast

    # Step 5: Enter the IP address to calculate network ID and broadcast address
    ip_address_decimal = input("Enter an IP address in the subnet: ")
    ip_address = addressToBinary(ip_address_decimal)

    # Calculate network ID and broadcast address
    network_id, broadcast_address = calculate_network_id_broadcast(ip_address, subnet_mask)

    # Display results
    print("\n\n")
    print(f"Subnet Mask: {printAddress(subnet_mask)}")
    print(f"Number of Subnets: {num_subnets}")
    print(f"Number of Host Addresses per Subnet: {num_host_addresses}")
    print(f"Network ID: {printAddress(network_id)}")
    print(f"Broadcast Address: {printAddress(broadcast_address)}")

def calculate_network_id_broadcast(ip_address, subnet_mask):
    network_id_binary = ''
    for bit1, bit2 in zip(ip_address, subnet_mask):
        # Perform the AND operation on each pair of bits and append the result
        network_id_binary += '1' if bit1 == '1' and bit2 == '1' else '0'

    negated_subnet_mask = ''.join(['1' if bit == '0' else '0' for bit in subnet_mask])

    broadcast_address = ''
    for bit1, bit2 in zip(ip_address, negated_subnet_mask):
        # Perform the OR operation on each pair of bits and append the result
        broadcast_address += '1' if bit1 == '1' or bit2 == '1' else '0'
    return network_id_binary, broadcast_address

if __name__ == "__main__":
    main()

