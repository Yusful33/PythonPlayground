import pandas as pd
import time
import os.path
#All of the files should be located in C:\Users\FIY716\Documents\Projects\New_Column but below are the full paths for ease of use
#C:\Users\FIY716\Documents\Projects\New_Column\Prod_Debt.xlsx
#C:\Users\FIY716\Documents\Projects\New_Column\QA_Debt.xlsx
#C:\Users\FIY716\Documents\Projects\New_Column\Prod_IP.xlsx
#C:\Users\FIY716\Documents\Projects\New_Column\QA_IP.xlsx
PROD_debt_file = input("Please enter the file path of the Prod Debt file you are looking to compare:")
QA_debt_file = input("Please enter the file path of the QA Debt file you are looking to compare:")
PROD_IP_file = input("Please enter the file path of the Prod IP file you are looking to compare:")
QA_IP_file = input("Please enter the file path of the QA IP file you are looking to compare:")

if os.path.isfile(PROD_debt_file) and os.path.isfile(QA_debt_file) and os.path.isfile(PROD_IP_file) and os.path.isfile(QA_IP_file):
    print("Thank you, please allow a few minutes for the process to complete :)")

    start = time.time()

    df1 = pd.read_excel(PROD_debt_file, index_col=0)
    df2 = pd.read_excel(QA_debt_file, index_col=0)
    df3 = pd.read_excel(PROD_IP_file, index_col=0)
    df4 = pd.read_excel(QA_IP_file, index_col=0)

#The indicator parameter below adds a new column to the merged data set notifying you of which data set the info is comign from
    df_new_ip = df3.merge(df4, on = 'TRD_ID', how='outer', indicator=True)
    df_new_debt = df1.merge(df2, on = 'TRD_ID', how='outer', indicator=True)
#The new column is called "_merge"
    df_common_ip = df_new_ip[df_new_ip['_merge'] == 'both']
    df_common_debt = df_new_debt[df_new_debt['_merge'] == 'both']
#The below now create variables from prod and qa without the common rows between them
    df_prod_debt = df1[(~df1.TRD_ID.isin(df_common_debt.TRD_ID))]
    df_qa_debt = df2[(~df2.TRD_ID.isin(df_common_debt.TRD_ID))]
    df_prod_ip = df3[(~df3.TRD_ID.isin(df_common_ip.TRD_ID))]
    df_qa_ip = df4[(~df4.TRD_ID.isin(df_common_ip.TRD_ID))]
#Displays out the diffs between the two files dataframe(df_po)
    prod_debt = pd.DataFrame(df_prod_debt)
    qa_debt = pd.DataFrame(df_qa_debt)
    prod_ip = pd.DataFrame(df_prod_ip)
    qa_ip = pd.DataFrame(df_qa_ip)
#Converting df to csv
    debt_prod_csv = prod_debt.to_csv(r"C:/Users/FIY716/Documents/Projects/New_Column/Unique_Prod_Debt.csv", index = None, header=True)
    debt_qa_csv = qa_debt.to_csv(r"C:/Users/FIY716/Documents/Projects/New_Column/Unique_QA_Debt.csv", index = None, header=True)
    ip_prod_csv = prod_ip.to_csv(r"C:/Users/FIY716/Documents/Projects/New_Column/Unique_PROD_IP.csv", index = None, header=True)
    ip_qa_csv = qa_ip.to_csv(r"C:/Users/FIY716/Documents/Projects/New_Column/Unique_QA_IP.csv", index = None, header=True)

    print("...............................")
    print('It Took', round(time.time()-start,2), 'seconds for this script to run, thank you for your patience.')
else:
    print("You have not entered in an invalid file path, please try again.")

