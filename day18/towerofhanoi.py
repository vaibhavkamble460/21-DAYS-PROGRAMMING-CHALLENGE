def tower(n,source,destination,auxillary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return

    tower(n-1,source,auxillary,destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    tower(n-1,auxillary,destination,source)


n=4
tower(n,'A','B','C')