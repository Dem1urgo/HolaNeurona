import streamlit as st


# importamos la libreria

st.title("Neurona")
# titulo de la pagina

st.image("https://concepto.de/wp-content/uploads/2018/09/neuronas2-e1537381557413.jpg",
            width=400)

st.header('Ejemplo de una neurona con diferentes modificaciones')
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y un sesgo"])


with tab1:
    st.header('Un peso y una entrada')
    peso = st.slider('Introduce el peso', 0., 10.)
    entrada = st.number_input('Escribe la entrada')
    if st.button("Calcula la salida", key='b1'):
        resultado = peso * entrada
        st.text(f'El resultado es  {resultado}')

with tab2:
    
    st.header('Dos entradas y con sus respectivos pesos')

    col1, col2 = st.columns(2)

    with col1:
        peso1 = st.slider('Introduce el peso', 0., 10., key='w0')
        entrada1 = st.number_input('Escribe la entrada', key='x0')
        
    
    with col2:
        peso2 = st.slider('Introduce el peso', 0., 10., key='w1')
        entrada2 = st.number_input('Escribe la entrada', key='x1')
        
    
    if st.button("Calcula la salida", key='b2'):
        resultado = (peso1 * entrada1) + (peso2 * entrada2)
        st.text(f'El resultado es {resultado}')
        
    
with tab3:
    st.header('Tres entradas y un sesgo')

    col1, col2, col3 = st.columns(3)

    with col1:
        peso1 = st.slider('Introduce el peso', 0., 10., key='w01')
        entrada1 = st.number_input('Escribe la entrada', key='x01')
    
    with col2:
        peso2 = st.slider('Introduce el peso', 0., 10., key='w02')
        entrada2 = st.number_input('Escribe la entrada', key='x02')

    with col3:
        peso3 = st.slider('Introduce el peso', 0., 10., key='w03')
        entrada3 = st.number_input('Escribe la entrada', key='x03')
       


    sesgo = st.number_input('Introde el sesgo')
       
    if st.button("Calcula la salida", key='b3'):
        resultado = (peso1 * entrada1) + (peso2 * entrada2) + (peso3 * entrada3) + sesgo
        st.text(f'El resultado es {resultado}')
