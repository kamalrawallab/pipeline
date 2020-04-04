import os,subprocess

files=[f for f in os.listdir("/home/qwe/RV/tcruzi_strains") if f.endswith(".fasta")]
for fls in files:
    print(fls)
    subprocess.call(["python","blast_prot1.py","/home/qwe/RV/tcruzi_strains/"+fls.strip()],cwd="/home/qwe/RV/tools/Database_Program/vf")
