import subprocess
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt


def plot_variacao():
    fig = plt.figure(figsize=(16, 8))
    plt.title('Variação do ping', fontdict={"fontsize": 18})
    plt.axhline(y=30, color='r', linestyle='-')
    sns.lineplot(data=df, x='time', y='ping')
    plt.savefig('variacao.png')


def plot_abaixo_de_trinta():
    fig1 = plt.figure(figsize=(16, 8))
    fig1 = plt.title('Cade os 30 de ping?', fontdict={"fontsize": 18})
    fig1 = sns.countplot(data=df, x='lentidao')
    plt.savefig('count.png')


if __name__ == '__main__':
    subprocess.call(['bash', 'ping.sh'])

    sns.set_theme(style="darkgrid")

    columns_name = ['host', 'time', 'ping']
    columns_types = {'time': "datetime64[ns]"}

    df = pd.read_csv('results.csv', header=None, names=columns_name)

    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['time'] = [x.strftime('%M:%S:%f') for x in df['time']]
    df['lentidao'] = ['acima de 30' if x > 30 else 'abaixo de 30' for x in df['ping']]

    plot_variacao()
    plot_abaixo_de_trinta()


