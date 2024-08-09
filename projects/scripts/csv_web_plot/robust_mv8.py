import pandas as pd
import numpy as np
import os 
import random 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
from cvxopt import matrix, solvers
import cvxpy as cp

plt.rcParams['figure.figsize'] = [15, 5]


def get_data(file_name):
    path = os.path.join(os.getcwd(), file_name)
    try:
        df = pd.read_csv(path)
        df = df.pivot_table(index=['year', 'month'], columns = 'ticker_new', values='ret')
        df.reset_index(inplace=True)
        return df
    except pd.errors.ParserError as e:
        df = pd.read_csv(path, skiprows=3)
        first_non_numeric_index = None
        for index, value in df['Unnamed: 0'].items():
            if not is_numeric(value):
                first_non_numeric_index = index
                break
        
        df = df[:first_non_numeric_index]
        df['year'] = df['Unnamed: 0'].astype(str).str[:4]
        df['month'] = df['Unnamed: 0'].astype(str).str[4:6]
        df.drop(columns=['Unnamed: 0'], inplace=True)

        for column in df.columns:
            if column != 'year' and column != 'month':
                df[column] = df[column].astype(float)
            else: 
                
                df[column] = df[column].astype(int)
        df['RF'] = df['RF'] / 100
        df.drop(columns={'SMB', 'HML'}, inplace = True)
        return df
    

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
   

def get_and_merge(ff_file, etf_file):
    ffdf = get_data(ff_file)
    etfdf = get_data(etf_file)
    df = pd.merge(etfdf, ffdf, on=['year', 'month'], how='inner')
    df['ym'] = df['year']*100 + df['month']
    df['ym'] = df['ym'].astype(int)
    return df


def sharpe_ratio(x, meandf, covdf, rf): 
    sp = (x@meandf-rf)/np.sqrt(x.T@covdf@x)
    return sp


def mv(df, etflist = ['BNDX', 'SPSM', 'SPMD', 'SPLG', 'VWO', 'VEA', 'MUB', 'EMB'], short = 0, maxuse = 1, normal = 1, startdate = 199302, enddate = 202312):
    gridsize = 50
    try: 
        cdf = df[(df['ym'] >= startdate) & (df['ym'] <= enddate)]
        useretfL = etflist + ['Mkt-RF', 'RF', 'year', 'month', 'ym']
        cdf = cdf[useretfL]
        
        # Indicating whether to use the maximum available data
        if not maxuse: 
            cdf = cdf.dropna()
        cdf.reset_index(inplace = True)
        
        # Calculate the original moments
        meandf = cdf[etflist].mean()
        covdf = cdf[etflist].cov()
        stddf = np.sqrt(cdf[etflist].var())

        # Risk Free Rate
        rf = cdf['RF'].mean()
        
        # Short Selling option
        if not short: 
            shortchoice = 'w/o.'
        else: 
            shortchoice = 'w/.'
        
        # Standard MV Portfolio 
        if normal: 
            if not short: 
                # solve for optimal weight that minimize STD given return
                def solv_x(r, covdf, meandf, etflist): 
                    covmat = matrix(covdf.values)
                    P = matrix(np.zeros(len(etflist)))
                    G = -matrix(np.eye(len(etflist)))
                    h = matrix(0.0, (len(etflist), 1))
                    A = matrix(np.vstack((np.ones(len(etflist)), meandf)))
                    b = matrix([1.0, r])
                    solvers.options['show_progress'] = False
                    solv = solvers.qp(covmat, P, G, h, A, b)
                    x = np.array(solv['x']).flatten()
                    return x
            else: 
                # solve for optimal weight that minimize STD given return, with short selling
                def solv_x(r, covdf, meandf, etflist): 
                    covmat = matrix(covdf.values)
                    P = matrix(np.zeros(len(etflist)))
                    G = None
                    h = None
                    A = matrix(np.vstack((np.ones(len(etflist)), meandf)))
                    b = matrix([1.0, r])
                    solvers.options['show_progress'] = False
                    solv = solvers.qp(covmat, P, G, h, A, b)
                    x = np.array(solv['x']).flatten()
                    return x
            
            # Initiate linspace for return
            minret = meandf.min()
            maxret = meandf.max()
            retspace = np.linspace(minret, maxret, gridsize)
            
            # Weight, Std, and SR calculation
            weightlist = [solv_x(i, covdf, meandf, etflist) for i in retspace]
            stdlist = [np.sqrt(i@covdf@i) for i in weightlist]
            SRlist = [sharpe_ratio(i, meandf, covdf, rf) for i in weightlist]
            
            # Maximum Sharpe Ratio Portfolio
            maxSRW  = np.argmax(SRlist)
            maxSR_ret = weightlist[maxSRW]@meandf
            maxSR_std = np.sqrt(weightlist[maxSRW]@covdf@weightlist[maxSRW])
            
            # Report the MV Portfolio Weight
            print("Max Sharpe Ratio Portfolio Weights: ")
            for i in range(len(etflist)): 
                perctw = weightlist[maxSRW][i] * 100
                print(f"Asset {i+1} - {etflist[i]}: {perctw.round(2)}%")
            
            # Plot
            gl = min(min(stdlist), min(stddf)) * 0.7 * np.sqrt(12)
            gr = max(max(stdlist), max(stddf)) * 1.1 * np.sqrt(12)
            gu = max(max(retspace), max(meandf)) * 1.15 * 12
            gb = min(min(retspace), min(meandf)) * 0.7 * 12
            
            stdlist = [std * np.sqrt(12) for std in stdlist]
            retspace = retspace * 12
            maxSR_ret = maxSR_ret * 12
            maxSR_std = maxSR_std * np.sqrt(12)
            stddf = stddf * np.sqrt(12)
            meandf = meandf * 12
            
            plt.plot(figsize=(15,5))
            plt.plot(stdlist, retspace, linewidth = 1)
            plt.scatter(stddf, meandf, color='purple', marker='o', s=40)
            for i in range(len(etflist)): 
                plt.annotate(etflist[i], (stddf[i], meandf[i]), textcoords="offset points", xytext=(0,10), ha='center')
            plt.scatter(maxSR_std, maxSR_ret, color='red', marker='*', s=110)
            plt.text(maxSR_std, maxSR_ret, s="MVP", horizontalalignment='right', verticalalignment='top', fontsize=10)
            plt.gca().set_xlim(left=0)
            plt.gca().set_ylim(bottom=0)
            plt.xlim(gl, gr)
            plt.ylim(gb, gu)
            plt.title(f'Standard MV Portfolio, {shortchoice} Short Selling, Date Range: {startdate}-{enddate}')
            plt.show()
            
        # Robust MV Portfolio
        else: 
            robw = np.zeros(len(etflist))
            simwdf = np.zeros(gridsize)
            
            # Simulation Parameters Set Up
            Nsim = 100
            iter = 0
            random.seed(123)
            while iter < Nsim: 
                if iter % 10 == 0 and iter > 1: 
                    print(f"Completed {round(iter*100/Nsim)}%")
                simdata = np.random.multivariate_normal(meandf.values, covdf.values, len(cdf))
                simdf = pd.DataFrame(simdata, columns=etflist)
                simmeandf = simdf.mean()
                simcovdf = simdf.cov()
                
                def solv_x(r, simcovdf, simmeandf, etflist): 
                    covmat = matrix(simcovdf.values)
                    P = matrix(np.zeros(len(etflist)))
                    G = -matrix(np.eye(len(etflist)))
                    h = matrix(0.0, (len(etflist), 1))
                    A = matrix(np.vstack((np.ones(len(etflist)), simmeandf)))
                    b = matrix([1.0, r])
                    solvers.options['show_progress'] = False
                    solv = solvers.qp(covmat, P, G, h, A, b)
                    x = np.array(solv['x']).flatten()
                    return x
                
                # Minimum Variance Portfolio 
                def solv_minvar(simcovdf, etflist): 
                    covmat = matrix(simcovdf.values)
                    P = matrix(np.zeros(len(etflist)))
                    G = -matrix(np.eye(len(etflist)))
                    h = matrix(0.0, (len(etflist), 1))
                    A = matrix(1.0, (1, len(etflist)))
                    b = matrix(1.0)
                    solvers.options['show_progress'] = False
                    solv = solvers.qp(covmat, P, G, h, A, b)
                    x = np.array(solv['x']).flatten()
                    return x
                minvar_w = solv_minvar(simcovdf, etflist)
                
                # Maximum Return Portfolio
                def solv_maxret(simmeandf, etflist): 
                    c = -matrix(simmeandf.values)
                    G = matrix(np.vstack((np.ones(len(etflist)), -np.eye(len(etflist)))))
                    h = matrix(np.vstack((np.array([[1]]), np.zeros((len(etflist), 1)))))
                    solvers.options['show_progress'] = False
                    solv = solvers.lp(c, G, h)
                    x = np.array(solv['x']).flatten()
                    return x
                maxret_w = solv_maxret(simmeandf, etflist)
                
                # Initiate the linspace of return
                minret = simmeandf@minvar_w
                # minret = simmeandf.min()
                maxret = simmeandf@maxret_w
                # maxret = simmeandf.max()
                retspace = np.linspace(minret, maxret, gridsize)
                
                # Weight calculation
                weightlist = [solv_x(i, simcovdf, simmeandf, etflist) for i in retspace]
                simwdf = [a + b for a, b in zip(simwdf, weightlist)]
                
                iter = iter + 1
            print("Iteration Completed")
            simwdf = [w/Nsim for w in simwdf]
            
            # Normalize
            efstd = [np.sqrt(12 * w@covdf@w) for w in simwdf]
            efret = [12 * w@meandf for w in simwdf]
            SRlist = [sharpe_ratio(w, meandf, covdf, rf) for w in simwdf]
            maxSR = np.argmax(SRlist)
            maxSR_ret = efret[maxSR]
            maxSR_std = efstd[maxSR]
            robw = simwdf[maxSR]
            
            cml_std = np.linspace(0, efstd[-1], gridsize)
            cml_ret = [std * (maxSR_ret - rf*12)/maxSR_std + rf*12 for std in cml_std]
            
            # Report the MV Portfolio Weight
            print("Robust Max Sharpe Ratio Portfolio Weights: ")
            for i in range(len(etflist)): 
                perct = robw[i] * 100
                print(f"Asset {i+1} - {etflist[i]}: {perct.round(2)}%")
            
            stddf = stddf * np.sqrt(12)
            meandf = meandf * 12 
            
            # Plot
            gl = min(min(efstd), min(stddf)) * 0.7 
            gr = max(max(efstd), max(stddf)) * 1.1 
            gu = max(max(efret), max(meandf)) * 1.15 
            gb = min(min(efret), min(meandf)) * 0.7 
            
            plt.plot(figsize=(15,5))
            plt.plot(efstd, efret, linewidth = 1)
            plt.plot(cml_std, cml_ret, color='red', linewidth = 1)
            plt.scatter(stddf, meandf, color='purple', marker='o', s=40)
            for i in range(len(etflist)): 
                plt.annotate(etflist[i], (stddf[i], meandf[i]), textcoords="offset points", xytext=(0,10), ha='center')
            plt.scatter(maxSR_std, maxSR_ret, color='red', marker='*', s=110)
            plt.text(maxSR_std, maxSR_ret, s="MVP", horizontalalignment='right', verticalalignment='top', fontsize=10)
            plt.gca().set_xlim(left=0)
            plt.gca().set_ylim(bottom=0)
            plt.xlim(gl, gr)
            plt.ylim(gb, gu)
            plt.title(f'Robust MV Portfolio, {shortchoice} Short Selling, Date Range: {startdate}-{enddate}')
            plt.show()
            
    except: 
        print("error")
        # mv(df, etflist, short, 0, normal, startdate, enddate)



ff_file = 'F-F_Research_Data_Factors.csv'
etf_file = 'ETF_returns.csv'
df = get_and_merge(ff_file, etf_file)

etflist = ['BNDX', 'SPSM', 'SPMD', 'SPLG', 'VWO', 'VEA', 'MUB', 'EMB']

# short = 0 (set to zero for not allowing short-sale constraints)
# maxuse = 0 (set to 0 for balanced sample)
# normal = 0 (set to zero for resampling)

mv(df, etflist, 0, 1, 0, 201512, 202312)
