# Import necessary libraries
import gradio as gr
from gramformer import Gramformer

# Install and import Gramformer
gf = Gramformer(models=1, use_gpu=False)  # Instantiate Gramformer with GPU support

# Define a function to correct sentences using Gramformer.
def correct(sentence):
    # Use Gramformer to correct the input sentence.
    corrected_sentences = gf.correct(sentence)
    # Convert the set to a list and get the first element, then convert it to a string.
    corrected_sentence = str(list(corrected_sentences)[0])
    # Return the corrected sentence as a string.
    return corrected_sentence

# Create a Gradio interface with the correction function and a new title.
interface = gr.Interface(
    fn=correct,  # Function for correction
    inputs=gr.Textbox(placeholder="Enter a sentence here..."),  # Input component
    outputs='text',  # Output format
    title='Grammatical Error Correction App'  # New interface title
)

# Launch the Gradio interface locally.
interface.launch()
