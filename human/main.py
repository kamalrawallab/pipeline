import os,subprocess

files=[f for f in os.listdir("/home/qwe/Desktop/human_dataset") if f.endswith(".fasta")]
for fls in files:
    print(fls)
    subprocess.call(["python","blast_prot1.py","/home/qwe/Desktop/human_dataset/"+fls.strip()],cwd="/home/qwe/RV/tools/Database_Program/human")
