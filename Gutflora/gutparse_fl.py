import os,pandas as pd,sys
  



if "__main__"==__name__:
   file1=sys.argv[1]
   fastafl=sys.argv[2]
   cudir=os.getcwd() 
   fls=[f for f in os.listdir(cudir+"/dataGut") if f.endswith("Final_max_result.txt")] 
   for i,f in enumerate(fls):
      if i ==0:
        df=pd.read_csv(cudir+"/dataGut/"+f,sep="\t")
      else:
        df1=pd.read_csv(cudir+"/dataGut/"+f,sep="\t")
        df=df.append(df1)
   df.to_csv(cudir+"/"+fastafl+"/"+fastafl+"_gutFlora_final_fl.txt",sep="\t") 
   
