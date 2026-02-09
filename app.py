import streamlit as st
from streamlit_scroll_to_top import scroll_to_here
from PIL import Image
import time

# -----------------------------------------------------------------------------
# 1. 設定與資料準備
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Love Journey", page_icon="✈️", layout="wide")

# === 旅程地點設定 (修改重點：改用 album 結構) ===
destinations = [
    {
        "name": "第一站：新竹的家",
        "album": [
            {
                "image": "images/image10.jpg",
                "desc": "這是我們的起點，還記得那天我們一起窩在沙發上..."
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
        # 這裡示範如何放多張照片配不同文字
        "album": [
            {
                "image": "images/image4.jpg",
                "desc": "耶誕城的燈光好美，但我覺得妳比燈光還美。"
            },
            {
                "image": "images/image1.jpg", # 這裡可以換成另一張照片
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
# 2. CSS 樣式設計
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* 全域背景：天空漸層 */
    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #E0F7FA);
        background-attachment: fixed;
    }
    .main-container {
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* 機票與卡片樣式 */
    .boarding-pass {
        background-color: white;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        padding: 0;
        margin: 20px auto;
        max-width: 500px;
        position: relative;
    }
    .pass-header { background-color: #FF6B6B; color: white; padding: 15px; text-align: center; border-bottom: 2px dashed #eee; }
    .pass-body { padding: 25px; color: #555; }
    .pass-row { display: flex; justify-content: space-between; margin-bottom: 20px; }
    .pass-label { font-size: 14px; color: #aaa; text-transform: uppercase; }
    .pass-value { font-size: 18px; font-weight: bold; color: #333; }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        margin-top: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
    }

    /* 按鈕美化 */
    .stButton>button {
        width: 100%;
        border-radius: 30px;
        font-weight: bold;
        padding: 12px 0;
        font-size: 18px;
        transition: transform 0.2s;
    }
    .stButton>button:hover { transform: scale(1.05); }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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
        # 這裡也要呼叫一次 scroll_to_here，確保動畫是在最上面播放
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
                width: 70%;
                max-width: 600px;
                height: 10px;
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
                font-size: 40px;
                transform: translateX(-50%) rotate(45deg);
                animation: movePlane {animation_duration}s linear forwards;
            }}
            .loading-text {{
                font-size: 24px;
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
    st.write("")
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
                <div><div class="pass-label">DATE</div><div class="pass-value">2026/03/21</div></div>
                <div style="text-align:right;"><div class="pass-label">SEAT</div><div class="pass-value">我的身邊</div></div>
            </div>
            <hr style="border-top: 2px dashed #ccc; margin: 20px 0;">
            <p style="text-align:center; color:#888; font-size:14px;">*此旅程將帶妳出發，找回我們的回憶*</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns([1, 0.2, 1])
    with col2:
        if st.button("🛫 起飛", type="primary", use_container_width=True):
            play_flight_animation()
            st.session_state.stage = 1
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def show_journey_step(index):
    # 使用 stage 作為 key
    scroll_to_here(0, key=f"scroll_step_{index}")
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    current_data = destinations[index - 1]
    
    # 標題
    st.markdown(f"""<div class="glass-card"><h2 style="color:#2d3436; margin:0;">📍 {current_data['name']}</h2></div>""", unsafe_allow_html=True)
    st.write("")
    
    # === 核心相簿邏輯 ===
    album = current_data.get("album", [])
    
    # 1. 初始化這一站的相片索引 (如果還沒有紀錄過，從第 0 張開始)
    # 我們用 f"photo_idx_{index}" 來確保每一站的進度是分開紀錄的
    idx_key = f"photo_idx_{index}"
    if idx_key not in st.session_state:
        st.session_state[idx_key] = 0
    
    current_photo_index = st.session_state[idx_key]
    
    # 確保索引不會超出範圍 (防呆)
    if current_photo_index >= len(album):
        current_photo_index = 0
        
    # 取得當前要顯示的那一組 (照片+文字)
    current_item = album[current_photo_index]
    
    # 2. 顯示照片區域 (包含左右切換按鈕)
    # 版面比例：[按鈕 1] [照片 10] [按鈕 1] -> 按鈕在兩側
    col_prev, col_img, col_next = st.columns([1, 5, 1], gap="small", vertical_alignment="center")
    
    with col_prev:
        # 如果不是第一張，顯示「上一張」按鈕
        if len(album) > 1:
            if st.button("❮", key=f"prev_{index}", help="上一張"):
                # 切換邏輯：減 1，如果小於 0 就跳到最後一張 (循環播放)
                st.session_state[idx_key] = (current_photo_index - 1) % len(album)
                st.rerun()

    with col_img:
        # 顯示照片
        try:
            img = Image.open(current_item['image'])
            # CSS Hack: 強制固定圖片高度，避免切換時版面跳動
            # object-fit: cover 會自動裁切圖片填滿框框
            st.markdown(
                f"""
                <style>
                div[data-testid="stImage"] img {{
                    height: 1000px; 
                    object-fit: cover;
                    border-radius: 15px;
                }}
                /* 手機版適配：高度改為自動或較小 */
                @media (max-width: 600px) {{
                    div[data-testid="stImage"] img {{
                        height: 300px;
                    }}
                }}
                </style>
                """,
                unsafe_allow_html=True,
            )
            st.image(img, use_container_width=True)
        except:
            st.warning(f"缺少照片: {current_item['image']}")

    with col_next:
        # 如果不是最後一張，顯示「下一張」按鈕
        if len(album) > 1:
            if st.button("❯", key=f"next_{index}", help="下一張"):
                # 切換邏輯：加 1，如果超過就跳回第一張
                st.session_state[idx_key] = (current_photo_index + 1) % len(album)
                st.rerun()

    # 3. 顯示對應的文字
    # 這裡會隨著上面的按鈕切換而改變
    st.write("")
    st.markdown(f"""
        <div class="glass-card" style="min-height: 120px; display:flex; align-items:center; justify-content:center;">
            <p style="font-size:20px; color:#555; margin:0;">
                {current_item['desc']}
            </p>
            <br>
            <span style="font-size:12px; color:#aaa; display:block; margin-top:10px;">
                ({current_photo_index + 1} / {len(album)})
            </span>
        </div>
        """, unsafe_allow_html=True)
    st.write("")

    # === 下方按鈕區 (前往下一站) ===
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if index < len(destinations):
            if st.button("✈️ 前往下一站", use_container_width=True):
                play_flight_animation()
                st.session_state.stage += 1
                st.rerun()
        else:
            if st.button("🏁 抵達終點 (按我)", type="primary", use_container_width=True):
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
            <h1 style="color:#FF6B6B; font-size: 40px;">🎂 HAPPY BIRTHDAY! 🎂</h1>
            <p style="font-size: 24px;">親愛的，生日快樂！</p>
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
    st.text_area("", letter, height=350, disabled=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
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