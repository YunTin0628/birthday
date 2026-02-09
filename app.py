import streamlit as st
from PIL import Image
import time

# -----------------------------------------------------------------------------
# 1. 網頁基本設定
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🎂",
    layout="centered"
)

# -----------------------------------------------------------------------------
# 2. CSS 美化設計 (新增部分)
#    這裡設定了動態漸層背景、玻璃卡片樣式、按鈕樣式
# -----------------------------------------------------------------------------
def set_bg_hack():
    st.markdown(
        """
        <style>
        /* 全域背景：粉紫暖色調流動漸層 */
        .stApp {
            background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #a18cd1);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* 玻璃擬態卡片樣式 (半透明白底 + 陰影) */
        .glass-card {
            background: rgba(255, 255, 255, 0.6);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
        }

        /* 按鈕美化 */
        .stButton>button {
            background-color: #ff7675;
            color: white;
            border-radius: 25px;
            border: none;
            padding: 10px 25px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #d63031;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }

        /* 標題字型優化 */
        h1, h2, h3 {
            color: #2d3436;
            font-family: 'Helvetica Neue', sans-serif;
        }
        
        /* 隱藏預設選單 */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

# 執行 CSS 設定
set_bg_hack()

# -----------------------------------------------------------------------------
# 3. 定義狀態 (Session State)
# -----------------------------------------------------------------------------
if 'gift_opened' not in st.session_state:
    st.session_state['gift_opened'] = False

# -----------------------------------------------------------------------------
# 4. 定義兩個頁面函數
# -----------------------------------------------------------------------------

def show_cover_page():
    """ 這是剛進來時看到的神秘封面 """
    # 使用空白讓版面往下推一點
    st.write("")
    st.write("")
    
    # 用玻璃卡片包住標題
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("🎁 有一份專屬於妳的禮物...")
    st.write("To: My Dearest")
    
    # 封面動圖
    st.image("https://media.giphy.com/media/l4KibWpBGWchSqCRy/giphy.gif", width=300) 
    
    st.write(" ")
    st.write("準備好解鎖回憶了嗎？")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 按鈕區 (置中處理)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 點我拆開禮物 ✨", use_container_width=True):
            st.session_state['gift_opened'] = True
            st.rerun()

def show_main_content():
    """ 這是禮物被拆開後的內容 """
    
    # 第一次進入主頁面時放特效
    if 'balloons_shown' not in st.session_state:
        st.balloons()
        st.session_state['balloons_shown'] = True

    # 頂部標題區 (用卡片包起來)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.title("🎉 親愛的，生日快樂！")
    st.write("雖然我們才在一起 5 個月，但每一個時刻都值得紀念。")
    st.markdown('</div>', unsafe_allow_html=True)

    # 側邊欄 (不需要卡片樣式，保持原樣即可，但可以加個圖片檢查)
    st.sidebar.title("💖 關於我們")
    st.sidebar.info("在一起的時間：5 個月")
    try:
        st.sidebar.image("images/cover.jpg", caption="❤️ 我們")
    except:
        pass

    # 時間軸 Tabs
    st.write("### 📅 我們的這 5 個月")
    
    # 這裡將內容分頁
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["第1個月", "第2個月", "第3個月", "第4個月", "未來"])

    def show_photo_card(image_path, title, caption):
        """ 輔助函式：顯示帶有樣式的照片卡片 """
        # 開始卡片
        st.markdown(f'<div class="glass-card"><h4>{title}</h4>', unsafe_allow_html=True)
        try:
            img = Image.open(image_path)
            st.image(img, caption=caption, use_container_width=True)
        except FileNotFoundError:
            st.warning(f"找不到圖片: {image_path}")
        # 結束卡片
        st.markdown('</div>', unsafe_allow_html=True)

    with tab1:
        st.write(" ") # 增加一點間距
        st.write("還記得第一個月，我們剛開始認識...")
        show_photo_card("images/image1.jpg", "📍 起點：相遇", "這是我們第一次...")

    with tab2:
        st.write(" ")
        st.write("第二個月，我們去了好多地方...")
        show_photo_card("images/image2.jpg", "🚀 加溫：越來越熟", "那天的天氣很好...")

    with tab3:
        st.write(" ")
        st.write("第三個月，發生了一件好笑的事...")
        show_photo_card("images/image6.jpg", "✨ 閃光：甜蜜回憶", "這張照片裡的妳笑得很開心")

    with tab4:
        st.write(" ")
        st.write("第四個月，雖然忙碌，但只要見到面就很安心。")
        show_photo_card("images/image4.jpg", "🏠 日常：習慣有妳", "平淡但幸福的日常")

    with tab5:
        st.write(" ")
        st.write("第五個月，也就是現在。祝妳生日快樂！")
        show_photo_card("images/image5.jpg", "🎁 現在與未來", "未完待續...")

    st.divider()

    # 信件區 (用卡片包起來)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("💌 給妳的一封信")
    letter_content = """
親愛的，

雖然我不擅長做手工卡片，
但我擅長寫程式，所以我把心意寫進了 Code 裡。

這 5 個月來謝謝妳的包容和陪伴，
希望未來的每一個生日，我都能陪在妳身邊。

愛妳的男友 上
    """
    st.text_area("（心裡話）", letter_content, height=250, disabled=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 增加一個「重頭再來」的按鈕
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 重新封裝禮物", use_container_width=True):
            st.session_state['gift_opened'] = False
            if 'balloons_shown' in st.session_state:
                del st.session_state['balloons_shown']
            st.rerun()

# -----------------------------------------------------------------------------
# 5. 主程式邏輯控制
# -----------------------------------------------------------------------------
if not st.session_state['gift_opened']:
    show_cover_page()
else:
    show_main_content()