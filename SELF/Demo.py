import streamlit as st

st.set_page_config(layout='wide')

col1, col2, col3,col4,col5,col6= st.columns([1,3,1,0.25,0.25,0.5]) #st.columns(5)


##st.markdown("<h1 style='text-align: center; color: Black;'>Saama Stremlit Demo</h1>", unsafe_allow_html=True)

##st.header('This is a header with a divider', divider='rainbow')
##st.header('_Streamlit_ is :blue[cool] :sunglasses:')


with col1:
   st.image('Saama_Logo.jpg', caption='Great Place To Work', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

with col2:
   st.markdown("<h1 style='text-align: center; color: black;'>STREAMLIT DEMO</h1>", unsafe_allow_html=True) 

with col3:
    text_search = st.text_input("", value="Search")

with col4:
   st.image('notification icon.png', caption=None, width=50, use_column_width=False, clamp=False, channels="RGB", output_format="always")

with col5:
   st.image('Task Icon.jpg', caption=None, width=50, use_column_width=False, clamp=False, channels="RGB", output_format="always")

with col6:
   st.image('user profile icon.jpg', caption=None, width=50, use_column_width=False, clamp=False, channels="RGB", output_format="always")


#with st.columns(3)[1]:
 #   st.markdown("<h1 style='text-align: center; color: Black;'>Saama Stremlit Demo</h1>", unsafe_allow_html=True)

#style = "<style>h1 {text-align: center;}</style>"
#st.markdown(style, unsafe_allow_html=True)
#.header("Saama Stremlit Demo")

st.markdown("This is Streamlit Demo App")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
#st.markdown("Here's a bouquet &mdash;\
 #           :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)