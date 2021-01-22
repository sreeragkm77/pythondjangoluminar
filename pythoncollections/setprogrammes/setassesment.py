student=["sreerag","sibin","sarath","narayanan","jhon","ajay"]
failed=["jhon","ajay"]
sset=set(student)
fset=set(failed)
passed=sset.difference(fset)
print("passed =",passed)