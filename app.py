import gradio as gr

def perform(input1):

    resultados = []

    for i in range (1, input1):
        a = (fizzbuzz(i))
        print(a)

        resultados.append(a)
 
    return resultados

def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0: 
        return "FizzBuzz"
    elif numero % 3 == 0: 
        return "Fizz"
    elif numero % 5 == 0: 
        return "Buzz"
    else: 
        return numero

with gr.Blocks() as demo: 

    input_texto = gr.Number(label="¿Cuantos números quieres revisar?")
    #input_imagen_original = gr.Image()
    #input_video_destino = gr.Video()
    btn = gr.Button(value="Submit")
    output_texto = gr.Text()

    #Actions
    btn.click(perform, inputs=[input_texto], outputs=[output_texto])

demo.launch()    
    
