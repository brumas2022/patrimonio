import streamlit as st 
import pandas as pd

st.set_page_config("Novo Sebo", layout="wide")

def abertura():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
                <nav class="navbar navbar-expand-lg bg-body-tertiary">
                  <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                          <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href="#">Link</a>
                        </li>
                        <li class="nav-item dropdown">
                          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Dropdown
                          </a>
                          <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                          </ul>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                        </li>
                      </ul>
                      <form class="d-flex" role="search">
                        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                        <button class="btn btn-outline-success" type="submit">Search</button>
                      </form>
                    </div>
                  </div>
                </nav>
                """, unsafe_allow_html=True)
def card():
    col = st.columns((1,1,1,1))
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">', unsafe_allow_html=True)
    col[0].markdown("""
                <div class="card" style="width: 18rem;">
                     <img src="https://sebodomarcao-w9epafmc27rcklcpym2lou.streamlit.app/~/+/media/fc89f99ec2a55668e059f101e3248301d4494bf7c10c4cb8b438b9c2.jpg" class="card-img-top-bottom" alt="Testando imagem">
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
                     <img src="https://sebodomarcao-w9epafmc27rcklcpym2lou.streamlit.app/~/+/media/fc89f99ec2a55668e059f101e3248301d4494bf7c10c4cb8b438b9c2.jpg" class="card-img-top" alt="...">
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
                     <img src="Gemini_Generated_Image_jwkry5jwkry5jwkr.jpg" class="card-img-top" alt="...">
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
                     <img src="https://sebodomarcao-w9epafmc27rcklcpym2lou.streamlit.app/~/+/media/fc89f99ec2a55668e059f101e3248301d4494bf7c10c4cb8b438b9c2.jpg" class="card-img-top" alt="...">
                     <div class="card-body">
                          <h5 class="card-title">Fiscais de Contrato</h5>
                          <p class="card-text">Conheça os fiscais de contratos</p>
                          <a href="#" style="color:white;text-decoration:None" class="btn btn-primary">Conheça os fiscais</a>
                     </div>
                </div>
                """, 
                unsafe_allow_html=True
                )

abertura()
card()