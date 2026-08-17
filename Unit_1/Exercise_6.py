#Q6 Write a program to illustrate the use of tuples and sets with basic operation

uidai_no=(123456123452,123456123452,545445636264)
unique_no=set(uidai_no) # dupilicate adhar will be removed

uidai_no=unique_no
print(uidai_no)

print("Basic Operation In Tuple And Set".center(50,'-'))

no=(1,2,3,5,8,9,7,6)
# find index of target value
print(no.index(8))


