from dependencies import *

def display_gif_frame(gif_path, frame_index):
    try:
        # Read the GIF file
        print("win")
        gif_reader = imageio.get_reader(gif_path)
        # Extract the specific frame
        frame = gif_reader.get_data(frame_index)
        print(frame.shape)
        # save the frame as a png file
        imageio.imwrite('frame.png', frame)
        # Display the extracted frame in Streamlit using NumPy array
        st.image(np.array(frame), caption=f'Frame {frame_index}', use_column_width=True)

    except Exception as e:
        print("lose")
        st.error(f"Error: {e}")

st.header("Uncertainty in Deep Learning for Regresssion.")
names = "Anugu Arun Reddy"
formatted_names = f'<div style="text-align: center;"><strong style="font-size: 17px;">{names}</strong></div>'
st.write(formatted_names, unsafe_allow_html=True)
st.write("\n")
latex_text_0 = r"""In the ever-evolving landscape of deep learning, understanding and quantifying uncertainty are paramount for building robust and reliable models, particularly in regression tasks. This article delves into the intriguing realm of uncertainty in deep learning, exploring three powerful techniques—Gaussian MLP, Deep Ensemble, and MC Dropout. By leveraging these methodologies, we aim to unravel the nuances of uncertainty estimation, shedding light on their applications and contributions to enhancing the reliability of regression models. Join us on this journey as we unravel the intricacies of uncertainty in deep learning and demonstrate the practical implementation of Gaussian MLP, Deep Ensemble, and MC Dropout for more informed and confident regression predictions."""
st.write(latex_text_0)
st.write("""
<div style='text-align: center;'>
    <h3>Gaussian MLP</h3>
</div>
""", unsafe_allow_html=True)

# LaTeX expression
latex_text = r"""
The described neural network model is a type of probabilistic or heteroskedastic regression model. 
In this context, the neural network takes an input variable $ y $ and predicts not only the mean $ \mu $ 
of the conditional distribution $p(y \mid x)$ but also the variance $ \sigma^2 $. The inclusion of variance 
allows the model to capture uncertainty in its predictions, making it particularly useful in scenarios where estimating 
the level of uncertainty is crucial.

This model is commonly employed in tasks where predictions have inherent variability or uncertainty. For instance, in financial 
forecasting, predicting stock prices, or medical diagnostics, the certainty associated with predictions is as important as the 
predictions themselves. By providing both the mean and variance of the predicted distribution, the model can offer a more 
nuanced understanding of the uncertainty associated with its predictions.

The predicted variance can be interpreted as a measure of how much the predicted values are expected to deviate from the mean. 
In situations where having a measure of uncertainty is vital for decision-making, this type of model can provide more informative 
and reliable predictions compared to deterministic models that only output a single point estimate.
"""

st.image("NN_M1.png")

st.write(latex_text)

device = "cpu"

latex_options_HNN = {
    "Option 1": "0.5x^2 + 0.25x^3",
    "Option 2": "(e^x)\sin(3\pi x)",
    "Option 3": "tan^{-1}(x)",
}

selectbox_label_html = f'<div style="text-align: center;"><span style="font-size: 18px;"><strong>Select an option and move the slider to view the visualizations:</strong></span></div>'

# Render the custom HTML as Markdown
st.markdown(selectbox_label_html, unsafe_allow_html=True)

selected_option = st.selectbox("", list(latex_options_HNN.keys()))
# Render the selected option as LaTeX
st.latex(f"Selected\,Option: {latex_options_HNN[selected_option]}")


if selected_option=="Option 1":
    gif_path = 'HNN_1.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 1 Gaussian MLP', 0, total_frames - 1, 23)
    display_gif_frame(gif_path, frame_index)

elif selected_option=="Option 2":
    gif_path = 'HNN_2.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 2 Gaussian MLP', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)

else :
    gif_path = 'HNN_3.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 3 Gaussian MLP', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)

st.write("""
<div style='text-align: center;'>
    <h3>Deep Ensemble</h3>
</div>
""", unsafe_allow_html=True)

st.image("DeepEnsemble.png")

latex_text_2 = r"""
A deep ensemble involves training multiple neural network models independently on the same dataset, leveraging diverse initializations and training samples. Aggregating their predictions enhances model robustness and generalization. This approach is pivotal in capturing nuanced representations of data and mitigating overfitting in complex machine learning tasks.

Deep ensembles are instrumental in tasks requiring precise uncertainty quantification, like medical diagnoses. Their ability to express uncertainty arises from diverse model predictions. This is vital for decision-making in applications where not only accurate predictions but also confidence levels are crucial, enhancing reliability in real-world scenarios.

Deep ensembles contribute to model reliability by mitigating overfitting and capturing comprehensive uncertainty representations. The diversity among models helps in creating robust, trustworthy models. This is especially crucial in applications where prediction errors can have significant consequences, demanding both accurate predictions and nuanced understanding of prediction confidence.
"""

st.write(latex_text_2)

latex_options_DE = {
    "Option 1": "x + 0.3\sin(2\pi x) + 0.3\sin(4\pi x)",
    "Option 2": "0.5(e^x)\sin(2\pi x)",
    "Option 3": "(e^x)\sin(5x + \cos(9x))",
}

selectbox_label_html = f'<div style="text-align: center;"><span style="font-size: 18px;"><strong>Select an option and move the slider to view the visualizations:</strong></span></div>'


# Render the custom HTML as Markdown
st.markdown(selectbox_label_html, unsafe_allow_html=True)

selected_option = st.selectbox(" ", list(latex_options_DE.keys()))
# Render the selected option as LaTeX
st.latex(f"Selected\,Option: {latex_options_DE[selected_option]}")


if selected_option=="Option 1":
    gif_path = 'DEEP_ENSEMBLE_1.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 1 DEEP ENSEMBLE', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)

elif selected_option=="Option 2":
    gif_path = 'DEEP_ENSEMBLE_2.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 2 DEEP ENSEMBLE', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)

else :
    gif_path = 'DEEP_ENSEMBLE_3.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 3 DEEP ENSEMBLE', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)

st.write("""
<div style='text-align: center;'>
    <h3>MC Dropout</h3>
</div>
""", unsafe_allow_html=True)

st.image("MCD.png")

latex_text_3 = r"""
MC Dropout, short for Monte Carlo Dropout, is a powerful technique in the realm of probabilistic machine learning. It involves applying dropout—a regularization method—in a Monte Carlo fashion during both training and inference. By incorporating dropout at test time, MC Dropout facilitates uncertainty estimation, making it a valuable tool for enhancing model robustness and reliability.

MC Dropout introduces an element of stochasticity during training by randomly dropping out (i.e., deactivating) neurons in the neural network. This process prevents the model from relying too heavily on specific features, promoting generalization. Multiple instances of dropout are applied during each training iteration, effectively creating an ensemble of slightly different models.

The key strength of MC Dropout lies in its ability to provide uncertainty estimates for predictions. During inference, the dropout process is retained, and the model is run multiple times with different dropout masks. This results in a collection of predictions, and the variance across these predictions serves as a measure of uncertainty. This uncertainty quantification is particularly beneficial in applications where understanding the reliability of predictions is crucial.
"""

st.write(latex_text_3)


latex_options_MC = {
    "Option 1": "x + 0.3\sin(2\pi x) + 0.3\sin(4\pi x)",
    "Option 2": "0.5(e^x)\sin(2\pi x)",
    "Option 3": "(e^x)\sin(5x + \cos(9x))",
}

selectbox_label_html = f'<div style="text-align: center;"><span style="font-size: 18px;"><strong>Select an option and move the slider to view the visualizations:</strong></span></div>'

# Render the custom HTML as Markdown
st.markdown(selectbox_label_html, unsafe_allow_html=True)

selected_option = st.selectbox("  ", list(latex_options_MC.keys()))
# Render the selected option as LaTeX
st.latex(f"Selected\,Option: {latex_options_MC[selected_option]}")


if selected_option=="Option 1":
    gif_path = 'MC_DROPOUT_1.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 1 MC DROPOUT', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)

elif selected_option=="Option 2":
    gif_path = 'MC_DROPOUT_2.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 2 MC DROPOUT', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)

else :
    gif_path = 'MC_DROPOUT_3.gif'
    total_frames = imageio.get_reader(gif_path).get_length()
    frame_index = st.slider('Move the slider for Option 3 MC DROPOUT', 0, total_frames - 1, 17)
    display_gif_frame(gif_path, frame_index)
