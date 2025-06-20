import random
import string
from typing import Union, Tuple, List, Dict

# Name Assignment (variables and constants)
MINING_REWARD = 3.125 # TODO: Assign the current bitcoin mining reward
current_block_height = 800_000 # TODO: Assign the current block height as an integer
BTC_TO_SATS = 100_000_000 # TODO: Assign the number of satoshis in one Bitcoin

# Functions
def calculate_total_reward(blocks_mined) -> float:
    """Calculate the total Bitcoin reward for a given number of mined blocks."""
    MINING_REWARD = 3.125
    return blocks_mined * MINING_REWARD


# TODO: Check if fee is between 0.00001 and 0.01 BTC
def is_valid_tx_fee(fee):
    """Return True if the transaction fee is within an acceptable range.
    
    Args:
        fee: Transaction fee in BTC
        
    Returns:
        Boolean indicating whether the fee is valid
    """
    return 0.00001 <= fee <= 0.01

  
# TODO: Compare balance to 50.0 and return result
def is_large_balance(balance):
    """Determine if a wallet balance is considered large.
    
    Args:
        balance: Wallet balance in BTC
        
    Returns:
        True if balance > 50.0 BTC, False otherwise
    """
    return balance > 50.0
  
 # TODO: Calculate fee rate and use if-elif-else to determine priority
def tx_priority(size_bytes, fee_btc):
    """Return the priority of a transaction based on fee rate."""
    fee_rate = fee_btc / size_bytes
    if fee_rate >= 0.00005:
        return "high"
    elif fee_rate >= 0.00001:
        return "medium"
    else:
        return "low"


# TODO: Convert network to lowercase and compare with "mainnet"
def is_mainnet(network):
    """Check if the network is for Bitcoin mainnet.
    
    Args:
        network: String like 'mainnet', 'testnet', 'signet' or 'regtest'
        
    Returns:
        True if mainnet, False otherwise
    """
    return network.lower() == "mainnet"


# TODO: Use comparison chaining to check if 100 <= value <= 200
def is_in_range(value):
    """Check if a value is within the range 100 to 200 (inclusive).
    
    Args:
        value: Numeric value
        
    Returns:
        True if in range, else False
    """
    return 100 <= value <= 200


# TODO: Use the 'is' keyword to compare object identity
def is_same_wallet(wallet1, wallet2):
    """Check if two wallet objects are the same in memory.
    
    Args:
        wallet1: First wallet object
        wallet2: Second wallet object
        
    Returns:
        True if both point to the same object, else False
    """
    return wallet1 is wallet2



# TODO: Strip leading/trailing spaces and convert to lowercase
def normalize_address(address):
    """Normalize a Bitcoin address by stripping whitespace and converting to lowercase.
    
    Args:
        address: Raw address string
        
    Returns:
        Normalized address string
    """
    return address.strip().lower()



def add_utxo(utxos, new_utxo):
    """Add a new UTXO to the list of UTXOs.
    
    Args:
        utxos: List of current UTXOs
        new_utxo: UTXO to add
        
    Returns:
        Updated list of UTXOs
    """
    return utxos + [new_utxo]


# Use a for loop with enumerate to find fee > 0.005 and return index and value
def find_high_fee(fee_list):
    """Find the first transaction with a fee greater than 0.005 BTC.
    
    Args:
        fee_list: List of transaction fees
        
    Returns:
        Tuple of (index, fee) or None if not found
    """
    for index, fee in enumerate(fee_list):
        if fee > 0.005:
            return (index, fee)
    return None


# Return a tuple with wallet name and balance
def get_wallet_details():
    """Return basic wallet details as a tuple.
    
    Returns:
        Tuple containing (wallet_name, balance)
    """
    return ("satoshi_wallet", 50.0)



# TODO: Use dict.get() to return tx status or 'not found' if missing
def get_tx_status(tx_pool, txid):
    """Get the status of a transaction from the mempool.
    
    Args:
        tx_pool: Dictionary of txid -> status
        txid: Transaction ID to check
        
    Returns:
        Status string or 'not found'
    """
    return tx_pool.get(txid, "not found")

# TODO: Unpack wallet_info tuple into name and balance, then format the return string
def unpack_wallet_info(wallet_info):
    """Unpack wallet information from a tuple and return a formatted string.
    
    Args:
        wallet_info: Tuple of (wallet_name, balance)
        
    Returns:
        Formatted string of wallet status
    """
    name, balance = wallet_info
    return f"Wallet {name} has balance: {balance} BTC"


def calculate_sats(btc: float) -> int:
    """Convert BTC to satoshis (1 BTC = 100,000,000 sats).
    
    Args:
        btc: Amount in Bitcoin
        
    Returns:
        Equivalent amount in satoshis
    """
    BTC_TO_SATS = 100_000_000
    return int(btc * BTC_TO_SATS)

 # TODO: Generate a suffix of random alphanumeric characters (length = 32 - length of the prefix)
# TODO: Concatenate the prefix and suffix to form the mock address
def generate_address(prefix: str = "bc1q") -> str:
    """Generate a mock Bitcoin address with given prefix.
    
    Args:
        prefix: Address prefix (default is bech32)
        
    Returns:
        Mock address string of length 32
    """
    length = 32 - len(prefix)
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return prefix + suffix
   

# TODO: Ensure height is an integer
# TODO: Check that height is not negative
# TODO: Check that height is within a realistic range (e.g., <= 800,000)
def validate_block_height(height: Union[int, float, str]) -> Tuple[bool, str]:
    """Validate a Bitcoin block height.
    
    Args:
        height: Block height to validate
        
    Returns:
        Tuple of (is_valid, message)
    """
    if not isinstance(height, int):
        return False, "Block height must be an integer"
    if height < 0:
        return False, "Block height cannot be negative"
    if height > 800_000:
        return False, "Block height seems unrealistic"
    return True, "Valid block height"
   

# TODO: Initialize the base reward for the genesis block in sats
# TODO: Initialize the halving interval approximately every four years in blocks
# TODO: Iterate through each block height, compute halvings, and calculate reward
# TODO: Store results in a dictionary
def halving_schedule(blocks: List[int]) -> Dict[int, int]:
    """Calculate block reward for given block heights based on halving schedule.
    
    Args:
        blocks: List of block heights
        
    Returns:
        Dictionary mapping block heights to their block reward in satoshis
    """
    BTC_TO_SATS = 100_000_000
    HALVING_INTERVAL = 210_000
    GENESIS_REWARD_BTC = 50

    result = {}
    for block in blocks:
        halvings = block // HALVING_INTERVAL
        reward_btc = GENESIS_REWARD_BTC / (2 ** halvings)
        reward_sats = int(reward_btc * BTC_TO_SATS)
        result[block] = reward_sats
    return result

# TODO: Filter UTXOs to those with value >= target
# TODO: Return the one with the smallest value, or {} if none found
def find_utxo_with_min_value(utxos: List[Dict[str, int]], target: int) -> Dict[str, int]:
    """Find the UTXO with minimum value that meets or exceeds target.
    
    Args:
        utxos: List of UTXOs (each with 'value' key in sats)
        target: Minimum target value in sats
        
    Returns:
        UTXO with smallest value >= target, or empty dict if none found
    """
    eligible = [utxo for utxo in utxos if utxo["value"] >= target]
    if not eligible:
        return {}
    return min(eligible, key=lambda x: x["value"])


# TODO: Create a base dictionary with txid and vout
# TODO: Merge any extra keyword arguments into the base
def create_utxo(txid: str, vout: int, **kwargs) -> Dict[str, Union[str, int]]:
    """Create a UTXO dictionary with optional additional fields."""
    base = {"txid": txid, "vout": vout}
    base.update(kwargs)
    return base
 
