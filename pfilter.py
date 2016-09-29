from mpi4py import MPI

def pfilter(predicate, items, callback, root=0):
	comm = MPI.COMM_WORLD # cluster/pool of nodes
	rank = comm.Get_rank() # current node's ID

	if rank == root: # base node
		work = items # hold the items to send out
	else:
	    work = None

	# distribute items evenly across nodes in comm
	# assign to item locally
	item = comm.scatter(work, root=root)

	# send all boolean-item pairs back to root
	results = comm.gather((predicate(item), item), root=root)

	# wait until all processes reach this point
	comm.Barrier()

	if rank == root:
		# only root gets the gathered pairs
		callback([item for keep, item in results if keep])

pfilter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5], print)