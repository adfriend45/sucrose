F90 = mpif90 -I/usr/local/software/spack/spack-views/.rhel8-icelake-202110272/uxqqj4xcjrltatqgtuoi2hp46uabtzom/intel-oneapi-mpi-2021.4.0/intel-2021.4.0/kypfgtnfzspxoby7tqy7yt6ykejpwk5n/mpi/2021.4.0/

FFLAGS = -r4 -O2
LDFLAGS = -lnetcdff

SRC = \
	sucrose.f90

OBJ = $(SRC:.f90=.o)

sucrose.exe : $(OBJ)
	$(F90) $(FFLAGS) -o sucrose.exe $(OBJ) $(LDFLAGS)

# Main routine
sucrose.o : sucrose.f90
	$(F90) $(FFLAGS) -c sucrose.f90

#Subroutines
	
#Modules
