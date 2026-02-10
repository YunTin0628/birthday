import streamlit as st
from streamlit_scroll_to_top import scroll_to_here
from PIL import Image
import time

# -----------------------------------------------------------------------------
# 1. 設定與資料準備
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Love Journey", page_icon="✈️", layout="wide")

# === 旅程地點設定 ===
destinations = [
    {
        "name": "第一站：新竹的家",
        "album": [
            {
                "image": "images/1.png",
                "desc": "一開始我們是透過這隻狗狗認識的，沒想到牠竟然是我們愛情的起點！"
                "當時的我怎麼樣也沒想到這麼可愛的女孩未來會變成我最喜歡的人。"
                "謝謝你願意一直陪我聊很多事情，也陪我走過了那段難熬的時間。"
            }
        ]
    },
    {
        "name": "第二站：南寮",
        "album": [
            {
                "image": "images/image1.jpg",
                "desc": "風很大的南寮，妳的頭髮都被吹亂了，但笑得很開心。"
            }
        ]
    },
    {
        "name": "第三站：板橋耶誕城",
        "album": [
            {
                "image": "images/image4.jpg",
                "desc": "耶誕城的燈光好美，但我覺得妳比燈光還美。"
            },
            {
                "image": "images/image1.jpg", 
                "desc": "逛累了我們去吃了那間很好吃的餐廳，下次再去吃吧！"
            }
        ]
    },
    {
        "name": "終點站：回到新竹的家",
        "album": [
            {
                "image": "images/image17.jpg",
                "desc": "繞了一圈，發現最想去的地方，其實就是有妳在的身邊。"
            }
        ]
    },
]

# -----------------------------------------------------------------------------
# 2. CSS 樣式設計 (包含手機版優化)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* 全域背景 */
    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #E0F7FA);
        background-attachment: fixed;
    }
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 10px; /* 增加內距避免貼邊 */
    }
    
    /* 機票樣式 - 手機版優化 */
    .boarding-pass {
        background-color: white;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        padding: 0;
        margin: 20px auto;
        width: 95%;        /* 手機上佔寬度 95% */
        max-width: 500px;  /* 電腦上最大 500px */
        position: relative;
    }
    
    /* 玻璃卡片 - 手機版優化 */
    .glass-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;       /* 手機版縮小內距 */
        margin-top: 20px;
        width: 100%;         /* 強制不超出螢幕 */
        box-sizing: border-box; /* 確保 padding 不會撐大寬度 */
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
    }

    .pass-header { background-color: #FF6B6B; color: white; padding: 15px; text-align: center; border-bottom: 2px dashed #eee; }
    .pass-body { padding: 20px; color: #555; }
    .pass-row { display: flex; justify-content: space-between; margin-bottom: 15px; }
    
    /* 字體大小響應式調整 */
    .pass-label { font-size: 12px; color: #aaa; text-transform: uppercase; }
    .pass-value { font-size: 16px; font-weight: bold; color: #333; }
    
    /* 按鈕美化 */
    .stButton>button {
        width: 100%;
        border-radius: 30px;
        font-weight: bold;
        padding: 10px 0;
        font-size: 16px;
        transition: transform 0.2s;
    }
    .stButton>button:hover { transform: scale(1.05); }
    
    /* 隱藏 Streamlit 原生元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* === 手機版專用調整 (@media) === */
    @media (max-width: 600px) {
        h2 { font-size: 24px !important; }
        p { font-size: 16px !important; }
        .pass-body { padding: 15px; }
        .glass-card { padding: 15px; margin-top: 15px; }
        
        /* 強制修正圖片容器高度，避免手機版太長 */
        div[data-testid="stImage"] img {
            max-height: 300px !important;
            object-fit: cover;
        }
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. 狀態管理
# -----------------------------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 0

# -----------------------------------------------------------------------------
# 4. 核心魔法：CSS 手刻飛機進度條動畫
# -----------------------------------------------------------------------------
def play_flight_animation():
    placeholder = st.empty()
    animation_duration = 3.5
    
    with placeholder.container():
        scroll_to_here(0, key=f"scroll_anim_{time.time()}")
        
        st.markdown(f"""
            <style>
            .flight-overlay {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(255, 255, 255, 0.95);
                z-index: 999999;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }}
            .progress-track {{
                width: 80%; /* 手機版寬一點 */
                max-width: 600px;
                height: 8px;
                background-color: #e0e0e0;
                border-radius: 10px;
                position: relative;
                margin-bottom: 20px;
            }}
            .progress-fill {{
                height: 100%;
                background: linear-gradient(90deg, #FF6B6B, #FF8E53);
                border-radius: 10px;
                width: 0%;
                animation: fillProgress {animation_duration}s linear forwards;
            }}
            .airplane-icon {{
                position: absolute;
                top: -25px;
                left: 0%;
                font-size: 30px; /* 手機版飛機稍微小一點 */
                transform: translateX(-50%) rotate(45deg);
                animation: movePlane {animation_duration}s linear forwards;
            }}
            .loading-text {{
                font-size: 18px;
                color: #555;
                font-weight: bold;
                margin-top: 20px;
                animation: fadeText 1s infinite alternate;
            }}
            @keyframes fillProgress {{ 0% {{ width: 0%; }} 100% {{ width: 100%; }} }}
            @keyframes movePlane {{ 0% {{ left: 0%; }} 100% {{ left: 100%; }} }}
            @keyframes fadeText {{ from {{ opacity: 0.6; }} to {{ opacity: 1; }} }}
            </style>
            <div class="flight-overlay">
                <div class="progress-track">
                    <div class="progress-fill"></div>
                    <div class="airplane-icon">✈️</div>
                </div>
                <div class="loading-text">正在飛往下一站...</div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(animation_duration)
        
    placeholder.empty()

# -----------------------------------------------------------------------------
# 5. 頁面邏輯
# -----------------------------------------------------------------------------

def show_ticket():
    scroll_to_here(0, key="scroll_ticket")
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.write("")
    
    # 這裡的 HTML 已經配合上面的 CSS 手機版優化了
    st.markdown(f"""
    <div class="boarding-pass">
        <div class="pass-header"><h2>BOARDING PASS ✈️</h2></div>
        <div class="pass-body">
            <div class="pass-row">
                <div><div class="pass-label">PASSENGER</div><div class="pass-value">藍悅慈</div></div>
                <div style="text-align:right;"><div class="pass-label">FLIGHT</div><div class="pass-value">LOVE-99</div></div>
            </div>
            <div class="pass-row">
                <div><div class="pass-label">FROM</div><div class="pass-value">我們的開始</div></div>
                <div style="text-align:right;"><div class="pass-label">TO</div><div class="pass-value">我們的未來</div></div>
            </div>
            <div class="pass-row">
                <div><div class="pass-label">DATE</div><div class="pass-value">2026/02/14</div></div>
                <div style="text-align:right;"><div class="pass-label">SEAT</div><div class="pass-value">我的身邊</div></div>
            </div>
            <hr style="border-top: 2px dashed #ccc; margin: 20px 0;">
            <p style="text-align:center; color:#888; font-size:12px;">*此旅程將帶妳出發，找回我們的回憶*</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    # 手機版按鈕置中優化
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🛫 起飛", type="primary", use_container_width=True):
            play_flight_animation()
            st.session_state.stage = 1
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def show_journey_step(index):
    scroll_to_here(0, key=f"scroll_step_{index}")
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    current_data = destinations[index - 1]
    
    st.markdown(f"""<div class="glass-card"><h2 style="color:#2d3436; margin:0;">📍 {current_data['name']}</h2></div>""", unsafe_allow_html=True)
    st.write("")
    
    # === 相簿邏輯 ===
    album = current_data.get("album", [])
    idx_key = f"photo_idx_{index}"
    if idx_key not in st.session_state:
        st.session_state[idx_key] = 0
    current_photo_index = st.session_state[idx_key]
    if current_photo_index >= len(album): current_photo_index = 0
    current_item = album[current_photo_index]
    
    # 1. 顯示照片 (CSS Hack 確保圖片在手機上不會過大)
    try:
        img = Image.open(current_item['image'])
        st.markdown(
            f"""
            <style>
            div[data-testid="stImage"] img {{
                max-height: 1000px;
                width: 100%;
                object-fit: cover;
                border-radius: 15px;
            }}
            /* 手機上再縮小一點，避免滑動太長 */
            @media (max-width: 600px) {{
                div[data-testid="stImage"] img {{
                    max-height: 300px;
                }}
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        # 用一個中間的 column 來限制圖片最大寬度
        # 手機版 [0.1, 10, 0.1] 會讓圖片幾乎滿版
        # 電腦版 [1, 3, 1] 會讓圖片適中
        # 這裡我們用 [1, 10, 1] 讓 CSS 去控制最大高度即可
        c1, c2, c3 = st.columns([1, 20, 1]) 
        with c2:
            st.image(img, use_container_width=True)
    except:
        st.warning(f"缺少照片: {current_item['image']}")

    # 2. 導航按鈕 (移到照片下方)
    # 版面：[上一張] [頁碼] [下一張]
    if len(album) > 1:
        # 使用 gap="small" 讓按鈕緊湊一點
        b_prev, b_info, b_next = st.columns([1, 2, 1], gap="small", vertical_alignment="center")
        
        with b_prev:
            if st.button("❮", key=f"prev_{index}", use_container_width=True):
                st.session_state[idx_key] = (current_photo_index - 1) % len(album)
                st.rerun()
        
        with b_info:
            st.markdown(f"<p style='text-align:center; color:#aaa; margin:0;'>{current_photo_index + 1} / {len(album)}</p>", unsafe_allow_html=True)
            
        with b_next:
            if st.button("❯", key=f"next_{index}", use_container_width=True):
                st.session_state[idx_key] = (current_photo_index + 1) % len(album)
                st.rerun()

    # 3. 文字內容
    st.write("")
    st.markdown(f"""
        <div class="glass-card" style="min-height: 100px; padding: 15px;">
            <p style="font-size:18px; color:#555; margin:0; line-height:1.6;">
                {current_item['desc']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.write("")

    # 下一步按鈕
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if index < len(destinations):
            if st.button("✈️ 下一站", use_container_width=True):
                play_flight_animation()
                st.session_state.stage += 1
                st.rerun()
        else:
            if st.button("🏁 抵達終點", type="primary", use_container_width=True):
                play_flight_animation()
                st.session_state.stage = 999
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def show_final_surprise():
    scroll_to_here(0, key="scroll_final")
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.balloons()
    st.markdown("""
        <div class="glass-card">
            <h1 style="color:#FF6B6B; font-size: 32px;">🎂 HAPPY BIRTHDAY! 🎂</h1>
            <p style="font-size: 20px;">親愛的，生日快樂！</p>
            <br>
            <img src="https://media.giphy.com/media/l0Iy4ppWvwQ4SXPxK/giphy.gif" width="100%" style="border-radius:10px;">
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("### 💌 給妳的一封信")
    letter = """
    親愛的，
    
    這趟旅程雖然短暫，就像我們這 5 個月一樣，
    從新竹出發，去了好多地方，最後又回到了溫暖的家。
    
    謝謝妳出現在我的生命裡。
    希望這張「沒有期限的機票」，
    能讓我陪妳去更多更多的地方。
    
    愛妳的男友 上
    """
    st.text_area("", letter, height=300, disabled=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 再飛一次", use_container_width=True):
            st.session_state.stage = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. 主程式流程控制
# -----------------------------------------------------------------------------
if st.session_state.stage == 0:
    show_ticket()
elif 1 <= st.session_state.stage <= len(destinations):
    show_journey_step(st.session_state.stage)
elif st.session_state.stage == 999:
    show_final_surprise()