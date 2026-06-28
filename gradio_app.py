# pyrefly: ignore [missing-import]
import gradio as gr

def greet(name):
    return "Hello!, welcome to Gradio"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
