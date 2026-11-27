
np.var(x) where x is some np.array computes the var

but np.var(x,ddof=1) computes a different value as now we divide by 1/n-1 and not 1/n


mean_x = np.mean(x) will compute the sample mean of the array, this is why it's important to use np.var(x , ddof=1) to compute the sample variance instead as it's a more representative value for the data. 