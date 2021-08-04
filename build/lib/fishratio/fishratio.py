# coding=utf-8

# pip install xlrd
# pip install openpyxl
# pip install pandas
# pip install numpy

from operator import index
import pandas as pds
import numpy as npy
import math
import sys

import click
pds.options.mode.chained_assignment = None
@click.command()

@click.option('--input', type=str, default="input.xlsx", nargs=1, 
            help='Full name (path + name + extension) of input file. default="input.xlsx"')
@click.option('--ratio', type=bool, default=True, nargs=1, 
            help='Formula: (species number of genus) / (species number of family) ratio value. default=True')
@click.option('--ln_ratio', type=bool, default=True, nargs=1, 
            help='Formula: Log(e)(ratio value). default=True')
@click.option('--neg_mul', type=bool, default=True, nargs=1, 
            help='Formula: -(ratio x Log(e)(ratio value)). default=True')
@click.option('--output', type=str, default="output.xlsx", nargs=1, 
            help='Full name (path + name + extension) of output file. default="output.xlsx"')

def calculate(input, ratio, ln_ratio, neg_mul, output):
    """
    Description: \n
    Calculate the ratio and logarithmic value of species contained in several genus of a family to all species in this family.

    Examples: \n
    1. Get options and parameters help: \n
    FishRatio --help

    2. Sample command with all default parameters: \n
    FishRatio --input input.xlsx
    \n or \n
    FishRatio --input input.xlsx --ratio true --ln_ratio true --neg_ratio true --output output.xlsx

    3. Only calculate (species number of genus) / (species number of family): \n
    FishRatio --input input.xlsx --ratio true --ln_ratio false --neg_ratio false --output output.xlsx
    """
    df = pds.read_excel(input)
    # print(df, type(df))

    # print(df.iloc[:,0])
    fam_uni = npy.unique(npy.sort(df.iloc[:,0]))
    # print(fam_uni)

    df2 = pds.DataFrame(columns=[df.columns.tolist()[0], df.columns.tolist()[1], df.columns.tolist()[2], 'Ratios', 'LnRatio', 'NegMul'])

    for fam in fam_uni:
        ndf = df.loc[df.iloc[:,0] == fam]
        # print(ndf)
        gen_spe_dic = ndf.set_index([df.columns.tolist()[1]])[df.columns.tolist()[2]].to_dict()
        fam_spe_sum = sum(ndf.iloc[:,2])
        res = []
        ln_res = []
        mul_res = []
        for gen in ndf.iloc[:,1]:
            gen_res = gen_spe_dic[gen] / fam_spe_sum
            res.append(gen_res)
            gen_ln_res = math.log(gen_res, math.e)
            ln_res.append(gen_ln_res)
            gen_mul_res = gen_res * (-(gen_ln_res))
            mul_res.append(gen_mul_res)
        if ratio:
            ndf['Ratios'] = res
        else:
            None
        if ln_ratio:
            ndf['LnRatio'] = ln_res
        else:
            None
        if neg_mul:
            ndf['NegMul'] = mul_res
        else:
            None
        # print(ndf)
        df2 = df2.append(ndf)
        # print(df2)
    df2.to_excel(output, index=None)

# if __name__ == '__main__':
# calculate()