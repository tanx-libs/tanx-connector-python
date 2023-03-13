from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brine_wrapper import client  # noqa: E402
from src.brine_wrapper.blockchain_utils import sign_msg  # noqa: E402

load_dotenv()
private_key = os.environ['PRIVATE_KEY']
eth_address = os.environ['ETH_ADDRESS']

Client = client.Client()

Client.complete_login(eth_address, private_key)

nonce = Client.create_order_nonce('btcusdt', 'market', 29580.51, 'buy', 0.0001)

print(Client.sign_msg_hash(nonce['payload'], private_key))



