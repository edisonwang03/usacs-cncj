from typing import Dict


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


def forward_packet(dst_ip: str, forwarding_table: Dict[str, str]) -> str:
    """Forward a packet to the next hop IP address. Assumes the dst_ip is in the forwarding table.

    Args:
        dst_ip (str): The destination IP address of the packet.
        forwarding_table (Dict[str, str]): A dictionary mapping destination IP addresses to output ports.

    Returns:
        str: The output port to forward the packet to.
    """

    # STEP 1: Convert the destination IP address to binary

    # STEP 2: Convert the keys of the forwarding table to binary

        # STEP 3: While iterating through the forwarding table, keep track of the mapping with the current longest prefix match

    # STEP 4: Return the output port with the longest prefix match
    return ""


if __name__ == "__main__":
    forwarding_table = {
        "192.168.1.0/24": "A",
        "192.168.2.0/24": "B",
        "10.0.0.0/8": "C",
        "172.16.0.0/12": "D",
    }

    test_cases = [
        ("192.168.1.1", "A"),
        ("192.168.2.1", "B"),
        ("10.1.1.1", "C"),
        ("172.16.1.1", "D"),
    ]

    for dst_ip, expected in test_cases:
        result = forward_packet(dst_ip, forwarding_table)
        print(f"forward_packet({dst_ip}) = {result} (expected: {expected})")
