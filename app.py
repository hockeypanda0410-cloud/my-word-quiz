import streamlit as st
import pandas as pd
import random

# 1. 앱 페이지 설정
st.set_page_config(page_title="영단어 야르!", page_icon="📖")

# 제목 출력
st.title("🔥 영단어 외우기 야르!")
st.write("구글 스프레드시트에서 만든 CSV 파일을 업로드해서 공부해보세요.")

# 2. CSV 파일 업로드 기능
uploaded_file = st.file_uploader("단어장(CSV) 파일을 선택하세요", type="csv")

if uploaded_file is not None:
    # 엑셀(CSV) 읽기
    df = pd.read_csv(uploaded_file)
    
    # 세션 상태(데이터 저장소) 초기화
    # 버튼을 누를 때마다 화면이 새로고침되는데, 데이터를 유지하기 위해 사용합니다.
    if 'current_word' not in st.session_state:
        st.session_state.current_word = None
    if 'show_meaning' not in st.session_state:
        st.session_state.show_meaning = False

    # 3. 단어 뽑기 버튼
    if st.button("새로운 단어 뽑기 🎲"):
        # 무작위로 행 하나 선택
        st.session_state.current_word = df.sample(n=1).iloc[0]
        st.session_state.show_meaning = False # 새로운 단어니까 뜻은 가림

    # 4. 화면에 단어 표시
    if st.session_state.current_word is not None:
        st.markdown("---")
        # 'word' 열의 데이터 출력
        st.subheader(f"단어: {st.session_state.current_word['word']}")
        
        # 뜻 보기 버튼
        if st.button("뜻 확인하기 👀"):
            st.session_state.show_meaning = True
        
        # 뜻 표시 (뜻 보기 버튼을 눌렀을 때만 나타남)
        if st.session_state.show_meaning:
            # 'meaning' 열의 데이터 출력
            st.info(f"뜻: {st.session_state.current_word['meaning']}")
            
else:
    st.info("먼저 CSV 파일을 업로드해주세요. 엑셀의 첫 줄은 'word', 'meaning'이어야 합니다.")

# 하단 도움말
with st.expander("사용 방법 도움말"):
    st.write("""
    1. 구글 스프레드시트에서 A1에 'word', B1에 'meaning'을 적습니다.
    2. 그 아래에 단어와 뜻을 채웁니다.
    3. [파일] -> [다운로드] -> [CSV]로 저장합니다.
    4. 이 앱에 그 파일을 올리고 공부를 시작하세요!
    """)
