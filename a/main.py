import requests
from pprint import pprint
from typing import Dict, Any

HOST = "https://api.spacetraders.io/v2"
TOKEN = "YOUR_TOKEN"


def register_new_agent(callsign: str, faction: str) -> Dict[str, Any]:
    """Register a new agent with the given callsign and faction.

    Args:
        callsign (str): The callsign, or unique identifier, for the agent.
        faction (str): The faction the agent belongs to.

    Returns:
        Dict[str, Any]: The JSON response from the API. The response will contain the agent's unique token for future API calls.
    """
    url = f"{HOST}/register"
    headers = {"Content-Type": "application/json"}
    json = {"symbol": callsign, "faction": faction}
    response = requests.post(url=url, headers=headers, json=json)
    return response.json()


def get_headquarters_details() -> Dict[str, Any]:
    """Get the details of the headquarters for the agent

    Returns:
        Dict[str, Any]: The JSON response from the API. The response will contain the details of the headquarters.
    """
    # IMPLEMENT FUNCTION HERE

    # STEP 1: Using the token retrieved from register_new_agent(), make a request for your agent's profile to get the headquarters's waypoint symbol.

    # STEP 2: Using your token and the headerquarters's waypoint symbol, make a request to get the waypoint's details.
    
    return None


def accept_first_contract() -> Dict[str, Any]:
    """Accept the first contract available to the agent

    Returns:
        Dict[str, Any]: The JSON response from the API. The response will contain the details of the contract accepted.
    """
    # IMPLEMENT FUNCTION HERE

    # STEP 1: Using the token retrieved from register_new_agent(), make a request to get the list of available contracts.

    # STEP 2: Using your token and the contract ID, make a request to accept the contract.
    
    return None


def find_first_shipyard() -> str:
    """Find the waypoint of the first shipyard in the system where the agent's headquarters is located.

    Returns:
        str: The symbol of the first shipyard found in the system.
    """
    # IMPLEMENT FUNCTION HERE

    # STEP 1: Using the token retrieved from register_new_agent(),

    # STEP 2: Using your token and the system symbol, make a request to get the list of waypoints in the system with the trait "SHIPYARD". Return the first shipyard found.
    
    return None


if __name__ == "__main__":
    # PERFORM FUNCTION CALLS HERE
    # pprint(register_new_agent("YOUR_CALLSIGN", "COSMIC"))
    pass
