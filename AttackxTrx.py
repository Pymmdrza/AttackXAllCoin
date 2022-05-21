import bit
from bit import *
from bit.format import bytes_to_wif
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base

import json
import random
import requests
from lxml import html
from rich import print
from rich.panel import Panel
from hdwallet import HDWallet
from rich.console import Console
from hdwallet.symbols import TRX as trx

console = Console(safe_box="None")


def HASH160(pubk_bytes):
	return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest()).digest()


x = int(input('[*] Min Num : 1 --------------------------------------------------------------------------------->> '))
y = int(input('[*] Max Num : 115792089237316195423570985008687907852837564279074904382605163141518161494336 ---->> '))
F = []
P = x


def trxbal(trx_addr):
	block = requests.get("https://apilist.tronscan.org/api/account?address=" + trx_addr)
	res = block.json()
	balances = dict(res)["balances"][0]["amount"]
	return balances


z = 1
w = 0
while P < y:
	P += 1
	ran = P
	pk = Key.from_int(ran)
	key = Key.from_int(ran)
	hasher = key.to_hex()
	PRIVATE_KEY = str(hasher)
	trx1: HDWallet = HDWallet(symbol=trx)
	trx1.from_private_key(private_key=PRIVATE_KEY)
	trx_addr = trx1.p2pkh_address()
	trxbalx = trxbal(trx_addr)
	amount_trx = '0.000000'
	if str(trxbalx) != str(amount_trx):
		console.print(
			'[white on green]TRX Address: [white on red1]' + str(trx_addr) + '[/][gold1 on black]   BALANCE: [white]' +
			str(trxbalx) + '[/]\n[blue]KEY: ' + str(PRIVATE_KEY) + '[/]')
		z += 1
		w += 1
		f = open("TrxNewWiner.txt", "a")
		f.write('\n' + str(trx_addr) + '     BALANCE:' + str(trxbalx) + '\nPrivateKey:' + str(PRIVATE_KEY) + '\n-----------------[ '
		                                                                                                     'Mmdrza.Com '
		                                                                                                     ']-------------------')
		f.close()
	
	
	else:
		console.print(str(z) + '[gold1]  Win:[white]' + str(w) + '[gold1]  TRX Address: [red1]' + str(trx_addr) + '[/][gold1]   BALANCE: [white]' + str(
			trxbalx) + '[/]')
		z += 1
