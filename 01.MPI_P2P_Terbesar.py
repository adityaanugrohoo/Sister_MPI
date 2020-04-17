#!/usr/bin/env python
# coding: utf-8

# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika rank terbesar, maka akan mengirimkan pesan ke proses yang mempunyai rank 0 sampai rank terbesar-1
if rank == size-1:
    for i in range(0, size-1):
        sendMsg = "Hai Rank "+str(i)+", ini pesan dari rank " + str(rank)
        comm.send(sendMsg, dest=i)
# jika bukan rank terbesar, maka akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    recvMsg = comm.recv(source=size-1)
    print (recvMsg)





