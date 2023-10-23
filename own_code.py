import gradio_util as util
import gradio as gr


#hello_demo = gr.Interface(fn=util.hello_greet, inputs="text", outputs="text")
    
demo = gr.Interface(fn=util.interface_greet,
                    inputs=["text", "checkbox", gr.Slider(0, 100)],
                    outputs=["text",'number'],
)
demo.launch()