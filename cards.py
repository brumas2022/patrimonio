import streamlit as st 
import pandas as pd

st.set_page_config("Novo Sebo", layout="wide")
def card():
    col = st.columns((1,1,1,1))
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">', unsafe_allow_html=True)
    col[0].markdown("""
                <div class="card" style="width: 18rem;">
                     <img src="" class="card-img-top" alt="Testando imagem">
                     <div class="card-body">
                          <h5 class="card-title">Projetos</h5>
                          <p class="card-text">Aqui voce econtrará os projetos atuais</p>
                          <a href="#" style="color:white;text-decoration:None" class="btn btn-primary">Ver projetos</a>
                     </div>
                </div>
                """, 
                unsafe_allow_html=True
                )
    col[1].markdown("""
                <div class="card" style="width: 18rem;">
                     <img src="..." class="card-img-top" alt="...">
                     <div class="card-body">
                          <h5 class="card-title">Betina</h5>
                          <p class="card-text">Filha da Niltinha, femea castrada</p>
                          <a href="http://sebodomarcao.cloud" style="color:white;text-decoration:None" class="btn btn-primary">Ver perfil</a>
                     </div>
                </div>
                """, 
                unsafe_allow_html=True
                )
    col[2].markdown("""
                <div class="card" style="width: 18rem;">
                     <img src="..." class="card-img-top" alt="...">
                     <div class="card-body">
                          <h5 class="card-title">Contratos de Obras</h5>
                          <p class="card-text">Conheça os contratos ativos de obras</p>
                          <a href="#" style="color:white;text-decoration:None" class="btn btn-primary">Pesquise a obra</a>
                     </div>
                </div>
                """, 
                unsafe_allow_html=True
                )
    col[3].markdown("""
                <div class="card" style="width: 18rem;">
                     <img src="..." class="card-img-top" alt="...">
                     <div class="card-body">
                          <h5 class="card-title">Fiscais de Contrato</h5>
                          <p class="card-text">Conheça os fiscais de contratos</p>
                          <a href="#" style="color:white;text-decoration:None" class="btn btn-primary">Conheça os fiscais</a>
                     </div>
                </div>
                """, 
                unsafe_allow_html=True
                )
card()