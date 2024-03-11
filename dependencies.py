# import numpy, pandas, matplotlib, pytorch, pytorch distributions and sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import torch.distributions as dist
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import jax.tree_util as jtu
# Display the animation in the Jupyter Notebook
from IPython.display import HTML
import torch.nn as nn
import torch.nn.functional as F
import streamlit as st
from matplotlib.animation import FuncAnimation
from tqdm.auto import trange, tqdm
import streamlit as st
import imageio
from PIL import Image
from io import BytesIO