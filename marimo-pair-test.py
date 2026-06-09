import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd

    mutations = pd.read_csv("missense-mutations.csv")
    mo.ui.table(mutations)
    return mo, pd


@app.cell
def _(mo, pd):
    wightman_amygdala = pd.read_csv("wightman_Brain_Amygdala.csv")
    mo.ui.table(wightman_amygdala)
    return (wightman_amygdala,)


@app.cell
def _(wightman_amygdala):
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt


    def plot_numeric_scatter_matrix(df):
        numeric_df = df.select_dtypes(include="number").dropna(axis=1, how="all")
        axes = scatter_matrix(
            numeric_df,
            alpha=0.15,
            diagonal="hist",
            figsize=(14, 14),
            marker=".",
            hist_kwds={"bins": 30},
        )
        fig = axes[0, 0].get_figure()
        fig.suptitle("Wightman Brain Amygdala: Numeric Columns", y=1.02)
        fig.tight_layout()
        return fig


    plot_numeric_scatter_matrix(wightman_amygdala)
    return (plt,)


@app.cell(hide_code=True)
def _(plt, wightman_amygdala):
    import numpy as np


    def plot_pvalue_distribution(df):
        pvalue_data = df["pvalue"].where(df["pvalue"] > 0).dropna()
        pvalue_bins = np.logspace(
            np.log10(pvalue_data.min()),
            np.log10(pvalue_data.max()),
            40,
        )

        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.hist(
            pvalue_data,
            bins=pvalue_bins,
            color="#2f6f73",
            edgecolor="white",
            linewidth=0.6,
        )
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title("Distribution of pvalue")
        ax.set_xlabel("pvalue")
        ax.set_ylabel("Gene count")
        ax.grid(True, which="both", alpha=0.25)
        fig.tight_layout()
        return fig


    fig_pvalue = plot_pvalue_distribution(wightman_amygdala)
    fig_pvalue
    return (fig_pvalue,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's write something!
    """)
    return


@app.cell(hide_code=True)
def _(fig_pvalue, mo):
    mo.md(f"""
    Something
    {mo.as_html(fig_pvalue)}
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
