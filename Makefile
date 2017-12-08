GPP=python
CFLAGS=exemplos/ex4.txt
CFILES=main.py
EXECUTABLE=main

all : main 

main: $(CFILES)
	 $(GPP) $(CFILES) $(CFLAGS) 

# run: 
# #	$(NPROOF_FLOP_COUNT) ./$(EXECUTABLE) 100000000
# 	./$(EXECUTABLE) < file.in
