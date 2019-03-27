from merkletools import MerkleTools 




with open('currentMempool.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    data=data[1:-1]
    temp= data.replace('"',"")


mempool = list(map(str, temp.split(",")))



mt = MerkleTools(hash_type="sha256")


s=input("Enter txn id to check:")

txn= str(s)


for i in range(len(mempool)):
	mt.add_leaf(mempool[i])


mt.make_tree()

proof=mt.get_proof(mempool.index(txn)+1)


if mt.validate_proof(proof, mt.get_leaf(mempool.index(txn)+1), mt.get_merkle_root())==True:
	print("Transaction is in mempool")
	print("Witness:", proof)

else:
	print("Transaction not in mempool")

