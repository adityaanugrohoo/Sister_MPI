# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika rank ke 0 maka akan mengirimkan pesan ke proses yang mempunyai rank 1 sampai size yang ditentukan
if rank == 0:
	for i in range(1, size):
		sendMsg = "Hello, rank "+str(i)+", ini pesan dari rank " + str(rank)
		comm.send(sendMsg, dest=i)

# jika bukan rank 0, maka menerima pesan yang berasal dari proses dengan rank 0
else:
	recvMsg = comm.recv(source=0)
	print (recvMsg)