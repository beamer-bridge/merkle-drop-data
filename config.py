# configuration file for use with merkle-drop
#
# To use this. run the following:
#
#   pip install git+https://github.com/trustlines-protocol/merkle-drop.git
#   gunicorn -c config.py merkle_drop.server:app
#
# Please visit https://github.com/trustlines-protocol/merkle-drop for
# more information

import merkle_drop.server

bind = "0.0.0.0:8080"
airdrop_filename = "airdrop.csv"

workers = 4
max_requests = 500


def on_starting(server):
    merkle_drop.server.init_gunicorn_logging()
    merkle_drop.server.init_cors(origins="*")
    merkle_drop.server.init(
        airdrop_filename
    )