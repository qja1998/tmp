import streamlit as st
from streamlit_folium import folium_static

from func.map_vis import bj_navi, togo_count, not_togo_count, fest_togo_count, fest_not_togo_count, fest_visit_count, wkd_visit_count, nationwide_plot



# 열 수를 정의 (그리드 형태로 표시하기 위해)
num_columns1 = 1  # 예시로 2개의 열로 설정
num_columns2 = 2

# 지도 크기 설정
map_width = 665
map_width2 = 300
map_height = 400
map_height2 = 400

map_list = [bj_navi, togo_count, not_togo_count, fest_togo_count, fest_not_togo_count, fest_visit_count, wkd_visit_count]

# 방문건수구간이 5인 경우 라벨 붙이기
for i, map_func in enumerate(map_list):
    columns1 = st.columns(num_columns1)
    columns2 = st.columns(num_columns2)

    col1 = columns1[i % num_columns1]  # 그리드 형태로 배치
    with col1:
        m, title = map_func("tt")

        # Expander의 크기는 내부의 콘텐츠 크기에 의해 자동으로 결정됨
        with st.expander(title, expanded=False):  # 기본적으로 접힌 상태            
            # 지도의 크기를 설정 (Expander 크기와 동일하게 맞춤)
            folium_static(m, width=map_width, height=map_height)

    col2_1 = columns2[(i*2) % num_columns2]
    col2_2 = columns2[(i*2) % num_columns2 + 1]
    with col2_1:
        m, title = map_func("g")

        # Expander의 크기는 내부의 콘텐츠 크기에 의해 자동으로 결정됨
        with st.expander(title, expanded=False):  # 기본적으로 접힌 상태            
            # 지도의 크기를 설정 (Expander 크기와 동일하게 맞춤)
            folium_static(m, width=map_width2, height=map_height2)
    
    with col2_2:
        m, title = map_func("b")

        # Expander의 크기는 내부의 콘텐츠 크기에 의해 자동으로 결정됨
        with st.expander(title, expanded=False):  # 기본적으로 접힌 상태            
            # 지도의 크기를 설정 (Expander 크기와 동일하게 맞춤)
            folium_static(m, width=map_width2, height=map_height2)


m, title = nationwide_plot()

with st.expander(title, expanded=False):  # 기본적으로 접힌 상태            
    # 지도의 크기를 설정 (Expander 크기와 동일하게 맞춤)
    folium_static(m, width=map_width, height=map_height)