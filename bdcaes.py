from supabase import create_client, Client
import requests
import streamlit as st


supabase: Client = create_client('https://ibhcxtnwnonsnycfgjay.supabase.co',
                                     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImliaGN4dG53bm9uc255Y2ZnamF5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NTE1Mzk2MiwiZXhwIjoyMDEwNzI5OTYyfQ.W9t9sqi_odq3kV2WovKCVfMXcFGprFOgai9Us9_rTQA')

resposta = supabase.table("caninos").select("nome").execute()
resposta1 = supabase.table("caninos").select("id").execute()
resposta
st.write(resposta)
st.write(resposta1)

res = supabase.storage.from_('Meninos').get_public_url('Femeas/Betina.jpg')
st.image(str(res))

#editor = requests.get("https://ibhcxtnwnonsnycfgjay.supabase.co")
#print(editor)