"""Matplotlib-only utilities to save confusion matrices and label distribution plots."""
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

def save_confusion_matrix(estimator, X, y_true, title="Confusion Matrix", out_path="results/confusion_matrix.png", labels=None):
    fig, ax = plt.subplots(figsize=(6, 5))
    disp = ConfusionMatrixDisplay.from_estimator(estimator, X, y_true, labels=labels, ax=ax)
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

def save_label_distribution(series, title="Label Distribution", out_path="results/label_distribution.png", rotation=0):
    counts = series.value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(counts.index.astype(str), counts.values)
    ax.set_title(title)
    ax.set_xlabel("Label")
    ax.set_ylabel("Count")
    ax.tick_params(axis='x', rotation=rotation)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
