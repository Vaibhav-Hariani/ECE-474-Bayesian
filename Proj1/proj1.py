import numpy as np

if __name__ == "__main__":
    means=[0,3,10]
    vars = [np.sqrt(3),2,3]
    NUM_SAMPLES=100000
    ## dims means, vars, samples
    normals = np.random.normal(loc=means, scale=vars, size=(NUM_SAMPLES, len(vars),len(means)))
    ns = [10,20,50]
    ps = [0.5,0.4,0.9]
    binomials = np.random.binomial(n=ns,p=ps, size=(1000, len(ns),len(ps)))
    for m in range(len(means)):
        for v in range(len(vars)):
            print(f"expected Mean {means[m]:.2f}, vars {vars[v]:.2f}, got {np.mean(normals[...,v,m]):.2f}")
            print(f"Binomial Parameters ")