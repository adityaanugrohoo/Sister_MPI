# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import random

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank=comm.Get_rank()

# dapatkan total proses berjalan
size=comm.Get_size()

# generate angka integer secara random untuk setiap proses
angka = random.randint(0,100)
print ("Rank %d memiliki nilai : %d" %(rank, angka))

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
	sum = 0
	for i in range(1,size):
		sum += comm.recv(source=i)
	print ("Jumlah seluruh nilai yaitu = %d" %(sum))

# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
	comm.send(angka, dest=0)