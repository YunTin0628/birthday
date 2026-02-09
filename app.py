import streamlit as st
import streamlit.components.v1 as components
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
        "image": "images/image10.jpg",
        "desc": "我們的旅程從這裡開始，這裡是我們最溫暖的小窩。"
    },
    {
        "name": "第二站：南寮",
        "image": "images/image1.jpg",
        "desc": "還記得那天我們去海邊吹風，雖然風有點大，但心情很放鬆。"
    },
    {
        "name": "第三站：板橋耶誕城",
        "image": "images/image4.jpg",
        "desc": "在滿滿的燈光下，妳的笑容比聖誕樹還要耀眼。"
    },
    {
        "name": "終點站：回到新竹的家",
        "image": "images/image17.jpg",
        "desc": "繞了一圈，發現最想去的地方，其實就是有妳在的身邊。"
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
# 4. 輔助函式：強制滾動到頂部 (JavaScript Hack - 暴力版)
# -----------------------------------------------------------------------------
def scroll_to_top():
    """
    這個 JavaScript 會嘗試抓取所有可能的滾動容器，全部設為 0。
    """
    js = """
    <script>
        // 方案 1: 針對 Streamlit 主視圖容器 (最常見)
        var viewContainer = window.parent.document.querySelector("[data-testid='stAppViewContainer']");
        if (viewContainer) {
            viewContainer.scrollTo({top: 0, behavior: 'instant'});
        }
        
        // 方案 2: 針對傳統 .main 容器
        var main = window.parent.document.querySelector(".main");
        if (main) {
            main.scrollTo({top: 0, behavior: 'instant'});
        }
        
        // 方案 3: 針對整個視窗
        window.parent.window.scrollTo({top: 0, behavior: 'instant'});
    </script>
    """
    components.html(js, height=0)

# -----------------------------------------------------------------------------
# 5. 核心魔法：CSS 手刻飛機進度條動畫
# -----------------------------------------------------------------------------
def play_flight_animation():
    placeholder = st.empty()
    animation_duration = 3.5
    
    with placeholder.container():
        # 這裡也要呼叫一次 scroll_to_top，確保動畫是在最上面播放
        scroll_to_top()
        
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
# 6. 頁面邏輯
# -----------------------------------------------------------------------------

def show_ticket():
    scroll_to_top()
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown(f"""
    <div class="boarding-pass">
        <div class="pass-header"><h2>BOARDING PASS ✈️</h2></div>
        <div class="pass-body">
            <div class="pass-row">
                <div><div class="pass-label">PASSENGER</div><div class="pass-value">最愛的妳 ❤️</div></div>
                <div style="text-align:right;"><div class="pass-label">FLIGHT</div><div class="pass-value">LOVE-520</div></div>
            </div>
            <div class="pass-row">
                <div><div class="pass-label">FROM</div><div class="pass-value">我們的開始</div></div>
                <div style="text-align:right;"><div class="pass-label">TO</div><div class="pass-value">永遠的未來</div></div>
            </div>
            <div class="pass-row">
                <div><div class="pass-label">DATE</div><div class="pass-value">2023.TODAY</div></div>
                <div style="text-align:right;"><div class="pass-label">SEAT</div><div class="pass-value">1A (My Heart)</div></div>
            </div>
            <hr style="border-top: 2px dashed #ccc; margin: 20px 0;">
            <p style="text-align:center; color:#888; font-size:14px;">*此旅程將帶妳從新竹出發，找回我們的回憶*</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🛫 CHECK IN (出發)", type="primary"):
            play_flight_animation()
            st.session_state.stage = 1
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def show_journey_step(index):
    scroll_to_top()
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    current_data = destinations[index - 1]
    
    st.progress(index / len(destinations), text=f"飛行進度: 第 {index} 站 / 共 {len(destinations)} 站")
    
    st.markdown(f"""<div class="glass-card"><h2 style="color:#2d3436; margin-bottom: 20px;">📍 {current_data['name']}</h2></div>""", unsafe_allow_html=True)
    st.write("")
    try:
        img = Image.open(current_data['image'])
        st.image(img, use_container_width=True)
    except:
        st.warning(f"找不到照片: {current_data['image']}")

    st.write("")
    st.markdown(f"""<div class="glass-card"><p style="font-size:20px; color:#555; line-height: 1.6;">{current_data['desc']}</p></div>""", unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if index < len(destinations):
            if st.button("✈️ 前往下一站"):
                play_flight_animation()
                st.session_state.stage += 1
                st.rerun()
        else:
            if st.button("🏁 抵達終點 (按我)", type="primary"):
                play_flight_animation()
                st.session_state.stage = 999
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def show_final_surprise():
    scroll_to_top()
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
        if st.button("🔄 再飛一次"):
            st.session_state.stage = 0
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. 主程式流程控制
# -----------------------------------------------------------------------------
if st.session_state.stage == 0:
    show_ticket()
elif 1 <= st.session_state.stage <= len(destinations):
    show_journey_step(st.session_state.stage)
elif st.session_state.stage == 999:
    show_final_surprise()