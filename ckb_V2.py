import pandas as pd

def gene_variant():
    df = pd.read_html(f'https://ckb.jax.org/gene/show?geneId={gene_ID}')
    df1 = df[2]
    df2 = pd.DataFrame(df1)
    table_data = df2.to_csv(f'{gene_ID}_gene_variant.csv', index=False)
    return table_data
    
def category_variant():
    df = pd.read_html(f'https://ckb.jax.org/gene/show?geneId={gene_ID}&tabType=CATEGORY_VARIANTS')
    df1 = df[2]
    df2 = pd.DataFrame(df1)
    table_data = df2.to_csv(f'{gene_ID}_category_variant.csv', index=False)
    return table_data
    
def moleecular_profiles():
    df = pd.read_html(f'https://ckb.jax.org/gene/show?geneId={gene_ID}&tabType=MOLECULAR_PROFILES')
    df1 = df[2]
    df2 = pd.DataFrame(df1)
    table_data = df2.to_csv(f'{gene_ID}_moleecular_profiles.csv', index=False)
    return table_data
    
def gene_level_evidence():
    df = pd.read_html(f'https://ckb.jax.org/gene/show?geneId={gene_ID}&tabType=GENE_LEVEL_EVIDENCE')
    df1 = df[2]
    df2 = pd.DataFrame(df1)
    table_data = df2.to_csv(f'{gene_ID}_gene_level_evidence.csv', index=False)
    return table_data

gene_ID = input('Enter gene ID here:')
gene_variant()
category_variant()
moleecular_profiles()
gene_level_evidence()
print('All tables downloaded')
    
