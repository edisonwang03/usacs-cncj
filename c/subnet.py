def to_binary(ip: str) -> str:
    """Convert an IP address to binary.

    Args:
        ip (str): The IP address to convert.

    Returns:
        str: The binary representation of the IP address.
    """
    binary = ""
    for octet in ip.split("."):
        binary += format(int(octet), "08b")
    return binary


def is_in_subnet(ip: str, subnet: str) -> bool:
    """
    Check if an IP address is in a subnet.

    Args:
        ip (str): The IP address to check. In the format of 'x.x.x.x'.
        subnet (str): The subnet to check against. In the format of 'x.x.x.x/y'.

    Returns:
        bool: True if the IP address is in the subnet, False otherwise.
    """
    # IMPLEMENT FUNCTION HERE

    # STEP 1: Obtain the prefix bit length from the subnet

    # STEP 2: Convert the IP address and subnet IP address to binary

    # STEP 3: Compare the first prefix_length bits of the IP address and subnet
    
    return False


if __name__ == "__main__":
    test_cases = [
        ("192.168.1.1", "192.168.1.0/24", True),
        ("192.168.1.1", "192.168.2.0/24", False),
        ("10.0.0.1", "10.0.0.0/8", True),
        ("172.16.0.1", "172.16.0.0/12", True),
        ("192.168.1.1", "192.168.1.1/32", True),
        ("192.168.1.1", "192.168.1.2/32", False),
    ]

    for ip, subnet, expected in test_cases:
        result = is_in_subnet(ip, subnet)
        print(f"is_in_subnet({ip}, {subnet}) = {result} (expected: {expected})")
