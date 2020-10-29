def mergeall():
    import pandas as pd
    # Change the data in .txt file to the same format with other .csv files
    file1=pd.read_csv('C:/Users/lenovo/Documents/FE595-HW3/result.txt', sep=("---"), header=None)
    file1[0] = file1[0].str[6:]
    file1[1] = file1[1].str[9:]
    file1.rename(columns={0:'name',1:'purpose'}, inplace = True)
    
    file2=pd.read_csv('C:/Users/lenovo/Documents/FE595-HW3/result.csv')
    
    file3=pd.read_csv('C:/Users/lenovo/Documents/FE595-HW3/company_list.csv')
    
    file4=pd.read_csv('C:/Users/lenovo/Documents/FE595-HW3/Mydata.csv')
    del file4['Unnamed: 0']
    file4.rename(columns={'Company name':'name','Company purpose':'purpose'}, inplace = True)
    
    file5=pd.read_csv('C:/Users/lenovo/Documents/FE595-HW3/FE595Data1.csv')
    
    file=pd.concat([file1,file2])
    file=pd.concat([file,file3])
    file=pd.concat([file,file4])
    file=pd.concat([file,file5])
    
    file=file.reset_index(drop=True)
    file.to_csv("Allcompanies.csv", index=False, encoding="utf-8")


if __name__ == "__main__":
    mergeall()
