#Below function calculates the pearson correlation between all columns of a dataframe and writes it into csv file, this helps in checking for collinearity.
def calculate_pearson_corr(df):
    from scipy import stats
    import csv
    cols=len(df.columns)
    corr={}
    for i in range(cols):
        col1 = df.columns[i]
        for j in range(cols):
            col2=df.columns[j]
            if(col1!=col2):
                col3=col1+'_'+col2
                col4=col2+'_'+col1
                if str(col3) and str(col4) not in corr:
                    corr["%s"% str(col3)]=stats.pearsonr(df.iloc[:,i], df.iloc[:,j])[0]           
    with open('total_pearson_corr.csv','w') as f:
        w = csv.writer(f)
        w.writerows(corr.items())
    return corr

def calculate_pbs_corr(df):
    from scipy import stats
    import csv
    cols=len(df.columns)
    corr={}
    for i in range(cols):
        col1 = df.columns[i]
        for j in range(cols):
            col2=df.columns[j]
            if(col1!=col2):
                col3=col1+'_'+col2
                col4=col2+'_'+col1
                if str(col3) and str(col4) not in corr:
                    corr["%s"% str(col3)]=stats.pointbiserialr(df.iloc[:,i], df.iloc[:,j])[0]           
    with open('total_pbiserial_corr.csv','w') as f:
        w = csv.writer(f)
        w.writerows(corr.items())
    return corr   
