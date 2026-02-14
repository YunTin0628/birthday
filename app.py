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
        "name": "第一站：我們的開始",
        "album": [
            {
                "image": "images/1.png",
                "desc": "一開始我們是透過這隻狗狗認識的，沒想到他竟然變成我們愛情的起點。當時的我怎麼樣也沒想到這麼可愛的女孩未來會變成我最喜歡的人。謝謝你願意一直陪我聊很多事情，也陪我走過了那段難熬的時間。"
            }
        ]
    },
    {
        "name": "第二站：第一次新竹之旅",
        "album": [
            {
                "image": "images/2.jpg",
                "desc": "在我們考試考完後，終於有時間見面了!這也是我們確認彼此心意後的第一次約會。為了讓你報備，還特地去系館拍照(雖然現在天天去)，然後逛了清交的整個校園，還教你騎了Oloo。"
            },
            {
                "image": "images/image1.jpg",
                "desc": "吃完飯後，我們跑到海邊看夕陽，還差點趕不上，還記得我們一起許願，一起拍照。雖然那天風超級大，大到我們頭髮都亂飄，看著夕陽就覺得一切都好漂亮。"
            },
            {
                "image": "images/image2.jpg",
                "desc": "最後我拿出了凱凱跟情書，還記得你開心的樣子，但我當下超緊張的，還好你喜歡。也在那時候，我答應了要跟你在一起很久很久!後來我們去巨城吃冰和逛街，這一天真的很美好，是我2025最開心的一天。"
            }
        ]
    },
    {
        "name": "第三站：咖啡廳讀書",
        "album": [
            {
                "image": "images/3.jpg",
                "desc": "為了應付接下來的考試，但又很想待在一起，所以我們就約在咖啡廳讀書。還記得那時候的你穿了個裙子，沒想到那會是我好不容易才能看到的。我們一起讀了好久，然後一起吃了好吃的甜點，結束後一起去吃牛肉麵，真的很開心。"
            }
        ]
    },
    {
        "name": "第四站：突然的公園散步",
        "album": [
            {
                "image": "images/image8.jpg",
                "desc": "那天你好不容易來新竹找我住，我們也如償一起去公園散步，一邊散步一邊聊天，有種溫馨的感覺，還一起在盪鞦韆上躺著搖來搖去，真的很開心。"
            }
        ]
    },
    {
        "name": "第五站：中山的耶誕樹",
        "album": [
            {
                "image": "images/image5.jpg",
                "desc": "這天我們決定一起去中山逛街，去之後發現竟然已經有聖誕樹了，於是跟聖誕樹拍了好多照片。"
            },
            {
                "image": "images/image6.jpg",
                "desc": "不管什麼角度的你都讓我覺得好可愛!"
            },
            {
                "image": "images/image7.jpg",
                "desc": "可愛!"
            },
            {
                "image": "images/4.jpg",
                "desc": "這張被你天天拿來罵我，但還是很可愛。"
            },
            {
                "image": "images/5.jpg",
                "desc": "要離開的時候一起吃了冰淇淋，結果沒想到我沒搭上客運，最後在Qtime待了一晚，隔天還直接去考試。之後學乖要先看回去的車了。"
            }
        ]
    },
    {
        "name": "第六站：新竹三天兩夜",
        "album": [
            {
                "image": "images/6.jpg",
                "desc": "當我們終於有三天是可以一直在一起時，決定要好好到處玩，第一天去內灣，屬實沒想到竟然還有可以玩的地方。還用運動幣免費玩了一堆遊戲。但自己玩一定很無聊，還好有你陪我一起玩。"
            },
            {
                "image": "images/image10.jpg",
                "desc": "經過一番努力，獲得了兩隻寶貝。"
            },
            {
                "image": "images/7.jpg",
                "desc": "那天我們一起在房間聊天跟玩，一起吃檸檬千層，我也幫你吹頭髮，還被鄰居敲門，但能跟你抱抱睡真的讓我很安心，希望未來有天能跟你天天抱睡。"
            },
            {
                "image": "images/image9.jpg",
                "desc": "後來我們去吃拉麵，結果要等超久，於是我們跑到竹北遠百，還看到小baby爬爬比賽，真的超可愛。"
            },
            {
                "image": "images/image11.jpg",
                "desc": "兩個不知道拍照要擺什麼pose的人，只好嘟嘴^3^"
            }
        ]
    },
    {
        "name": "第七站：終於來到板橋耶誕城",
        "album": [
            {
                "image": "images/image12.jpg",
                "desc": "雖然臨近期末考了，但我們還是想要去逛耶誕城，於是說好先去圖書館認真讀書。雖然中途在綁帽T的繩子，有時還不認真，但起碼是乖乖讀到晚上，趕快去耶誕城一起逛逛。"
            },
            {
                "image": "images/image14.jpg",
                "desc": "很久違的看到了耶誕城的大聖誕樹，人真的超級多，很難找到適合的時間拍。還被路人問能不能幫忙拍，還是覺得他們一定覺得我拍超醜。但能跟你一起逛然後拍很多照片真的很開心。"
            },
            {
                "image": "images/image13.jpg",
                "desc": "每次都在reels看到很多情侶拍照姿勢，終於有機會實踐了。為了拍出這張算是好看的照片喬了超級久，好好笑。"
            },
            {
                "image": "images/image8.jpg",
                "desc": "幫你拍的絕佳氛圍照，還是被你說不好看，我決定要去認真學拍照。"
            },
            {
                "image": "images/9.jpg",
                "desc": "去你常去的那條街吃布丁跟飯飯，這個韓式拌飯真的超大碗，下次真的要兩個人一起吃一份。"
            }
        ]
    },
    {
        "name": "第八站：舞台劇與廢物媽媽",
        "album": [
            {
                "image": "images/image19.jpg",
                "desc": "一個月前決定一起去看舞台劇，雖然在去看之前去夜市吃了好多東西，還被拍貼機老闆搞到。但是真的很開心也很謝謝你願意陪我去看，儘管你可能看不懂。我也會陪你去做很多你想做的喔。"
            },
            {
                "image": "images/10.jpg",
                "desc": "那天的妳真的超漂亮的，雖然後來要回去時差點出事，等的超級緊張，但還好我們運氣爆棚成功最後兩個上車。"
            },
            {
                "image": "images/image17.jpg",
                "desc": "那時候我們還一起做了熔岩巧克力，算是我們第一次一起做料理，真的超級好吃，一後還要一起做很多甜點或料理喔。"
            },
            {
                "image": "images/11.jpg",
                "desc": "隔天我們去了廢物媽媽育兒農場，原本以為沒什麼，但超級好玩的，還記得餵動物的時候你超怕，還有馬要偷吃，但還是拍到很多可愛的照片，下次在一起去其他地方玩喔。"
            },
            {
                "image": "images/image15.jpg",
                "desc": "最後一起去了南寮漁港，雖然沒吃到那邊的食物，但海邊的風景配你真的很漂亮，約好下次要一起去那邊放風箏跟野餐!"
            }
        ]
    },
    {
        "name": "第九站：聖誕大餐",
        "album": [
            {
                "image": "images/12.jpg",
                "desc": "這是我們一起度過的第一個聖誕節，一起去吃了說很久的烤肉大餐，親手烤給你的肉好吃吧!之後的每個節日我們都要一起過喔!"
            },
            {
                "image": "images/13.jpg",
                "desc": "隔天原本要去吃酵想，一開始跑錯店真的很尷尬，結果還賣完了，只好找另一間來吃，我們還吃不懂生甜甜圈，還好後來找到一間超好吃的!"
            }
        ]
    },
    {
        "name": "第十站：第一次的跨年",
        "album": [
            {
                "image": "images/15.jpg",
                "desc": "來到2025的尾聲了，雖然你還有很多事情，但你還是願意來找我一起跨年，真的很感動，我們一起去看新竹的跨年晚會，好多表演真的都超好看，而且是跟你一起看，最後的煙火真的很美，希望未來的每個跨年都能和你一起度過。"
            },
            {
                "image": "images/14.jpg",
                "desc": "當時我們逛了市集，還一起打彈珠，差點打到不用回家好好笑，你還成功套到兩瓶飲料，打敗我這個從小玩到大的，令人慚愧。"
            },
            {
                "image": "images/16.jpg",
                "desc": "韋禮安應該不會告我肖像權吧"
            }
        ]
    },
    {
        "name": "第十二站：落雨松",
        "album": [
            {
                "image": "images/17.jpg",
                "desc": "雖然我一月一直在準備考試，但你不厭其煩，常常來陪我，甚至跟我一起去看落羽松。真的很謝謝你在我壓力大的時候能陪伴我，給我鼓勵。"
            },
            {
                "image": "images/18.jpg",
                "desc": "對我來說你的存在已經是習慣了，我知道一月的我忙到不能好好陪你，但你還是願意來找我，真的很感動。未來我也會努力在你需要的時候陪伴你，給你鼓勵。"
            }
        ]
    },
    {
        "name": "第十三站：台中之旅",
        "album": [
            {
                "image": "images/19.jpg",
                "desc": "終於我考完試了，於是我們一起去台中玩，不管是吃咖哩，逛草悟道，或是在一中街隨便逛，只要跟你待在一起就都很美好，我也買了很多帥帥的衣服，寶貝的眼光真棒，也買了說了很久的情侶T，以後我們要很常一起穿出門喔。最後經歷了goshare事件，還好沒被收兩萬，真是幸好。"
            }
        ]
    },
    {
        "name": "終點站：我們的未來",
        "album": [
            {
                "image": "images/f1.jpg",
                "desc": "藍寶寶，我很開心能夠在這時候遇到妳，你的存在對我來說就是一道光，照亮了我的生活。"
            },
            {
                "image": "images/f2.jpg",
                "desc": "這趟旅程經歷了很多事情，不管事開心的或是難過的甚至是生氣的，但不管如何，我對你的愛只會隨著時間變多。"
            },
            {
                "image": "images/f3.jpg",
                "desc": "我仍然是一個很不成熟的人，我很常讓你生氣難過哭哭，但我希望你知道，我對你的心意絕對是滿分，無論如何我都會陪在你身邊。"
            },
            {
                "image": "images/f4.jpg",
                "desc": "這趟旅程僅僅四個月，但這不是我們的終點，未來我還會陪你走過很多地方，經歷很多事情。"
            },
            {
                "image": "images/f5.jpg",
                "desc": "也希望你能夠一直陪在我身邊，陪我一起成長，讓我們的心能一直依靠彼此。"
            },
            {
                "image": "images/f6.jpg",
                "desc": "這個禮物希望你會喜歡，也希望能成為我們回憶的一部份，我不是個很懂浪漫的人，所以才希望能盡我所能給你儀式感。"
            },
            {
                "image": "images/f7.jpg",
                "desc": "情人節快樂我最愛的寶寶 你的凱凱上"
            }
        ]
    }
]

# -----------------------------------------------------------------------------
# 2. CSS 樣式設計 (最高防彈級・無破綻置中版)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* 全域背景 */
    .stApp {
        background: linear-gradient(to bottom, #87CEEB, #E0F7FA);
        background-attachment: fixed;
    }
    
    /* === 漂浮愛心特效 CSS === */
    .floating-hearts {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        pointer-events: none; z-index: 0; overflow: hidden;
    }
    .heart {
        position: absolute; bottom: -10%; opacity: 0; font-size: 24px;
        animation-name: floatUp; animation-timing-function: linear; animation-iteration-count: infinite;
    }
    @keyframes floatUp {
        0% { transform: translateY(0) scale(0.5); opacity: 0; }
        10% { opacity: 0.6; }
        80% { opacity: 0.6; }
        100% { transform: translateY(-110vh) scale(1.2); opacity: 0; }
    }

    /* 主要內容容器 */
    .main-container {
        max-width: 800px; margin: 0 auto; padding: 10px; position: relative; z-index: 10; box-sizing: border-box;
    }
    
    /* 卡片設計 */
    .boarding-pass {
        background-color: white; border-radius: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        padding: 0; margin: 20px auto; width: 95%; max-width: 500px; position: relative; z-index: 10;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); border-radius: 20px;
        padding: 20px; margin-top: 20px; width: 100%; box-sizing: border-box;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1); text-align: center; z-index: 10;
    }
    .pass-header { background-color: #FF6B6B; color: white; padding: 15px; text-align: center; border-bottom: 2px dashed #eee; }
    .pass-body { padding: 20px; color: #555; }
    .pass-row { display: flex; justify-content: space-between; margin-bottom: 15px; }
    .pass-label { font-size: 12px; color: #aaa; text-transform: uppercase; }
    .pass-value { font-size: 16px; font-weight: bold; color: #333; }
    
    /* ========================================================
       1. 圖片絕對置中 (雙層 Flex 容器鎖定)
       ======================================================== */
    div[data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 0 auto !important;
    }
    div[data-testid="stImage"] > div {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 0 auto !important;
    }
    div[data-testid="stImage"] img {
        display: block !important;
        margin: 0 auto !important;
        max-width: 100% !important;
        max-height: 60vh !important;
        border-radius: 15px !important;
    }

    /* ========================================================
       2. 全域大按鈕 (起飛、下一站) 絕對置中 + 固定寬度
       ======================================================== */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    div[data-testid="stButton"] > button {
        width: 250px !important;      
        max-width: 80vw !important;   /* 防手機螢幕太小 */
        border-radius: 30px !important;
        font-weight: bold !important;
        padding: 10px 0 !important;
        font-size: 16px !important;
        margin: 0 auto !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    /* ========================================================
       3. 相簿導航列 (同一排 + 60px)
       全場唯一使用 st.columns 的地方
       ======================================================== */
    /* 強制將這個區塊保持同一排、不換行並整體居中 */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; 
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        max-width: 300px !important; /* 將整個導航區塊限制在中間 */
        margin: 10px auto !important;
        gap: 15px !important;
    }

    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
        width: auto !important;
        flex: none !important;
        min-width: 0 !important;
    }

    /* 左、右按鈕容器鎖定 60px */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(1),
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(3) {
        width: 60px !important;
    }

    /* 中間頁碼容器給足 80px 空間，並強制置中 */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(2) {
        width: 80px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }

    /* 覆蓋大按鈕的設定，讓這兩個導航按鈕精準變成 60px 小圓角 */
    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button {
        width: 60px !important;
        min-width: 60px !important;
        padding: 5px 0 !important;
        border-radius: 15px !important;
    }

    /* 隱藏原生元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>

    <div class="floating-hearts">
        <div class="heart" style="left: 10%; animation-duration: 8s; animation-delay: 1s;">❤️</div>
        <div class="heart" style="left: 30%; animation-duration: 12s; animation-delay: 4s;">💖</div>
        <div class="heart" style="left: 70%; animation-duration: 15s; animation-delay: 2s;">❤️</div>
        <div class="heart" style="left: 90%; animation-duration: 10s; animation-delay: 5s;">💗</div>
        <div class="heart" style="left: 15%; animation-duration: 10s; animation-delay: 2.5s;">❤️</div>
        <div class="heart" style="left: 85%; animation-duration: 11s; animation-delay: 0.5s;">💖</div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. 狀態管理
# -----------------------------------------------------------------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 0

if 'prev_stage' not in st.session_state:
    st.session_state.prev_stage = -1

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
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(255, 255, 255, 0.95); z-index: 999999;
                display: flex; flex-direction: column; justify-content: center; align-items: center;
            }}
            .progress-track {{
                width: 80%; max-width: 600px; height: 8px;
                background-color: #e0e0e0; border-radius: 10px;
                position: relative; margin-bottom: 20px;
            }}
            .progress-fill {{
                height: 100%; background: linear-gradient(90deg, #FF6B6B, #FF8E53);
                border-radius: 10px; width: 0%;
                animation: fillProgress {animation_duration}s linear forwards;
            }}
            .airplane-icon {{
                position: absolute; top: -25px; left: 0%; font-size: 30px;
                transform: translateX(-50%) rotate(45deg);
                animation: movePlane {animation_duration}s linear forwards;
            }}
            .loading-text {{
                font-size: 18px; color: #555; font-weight: bold; margin-top: 20px;
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
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
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
                <div><div class="pass-label">DATE</div><div class="pass-value">2026/02/14</div></div>
                <div style="text-align:right;"><div class="pass-label">SEAT</div><div class="pass-value">我的身邊</div></div>
            </div>
            <hr style="border-top: 2px dashed #ccc; margin: 20px 0;">
            <p style="text-align:center; color:#888; font-size:12px;">*此旅程將帶妳出發，找回我們的回憶*</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    if st.button("🛫 起飛", type="primary"):
        play_flight_animation()
        st.session_state.stage = 1
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

def show_journey_step(index):
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    current_data = destinations[index - 1]
    
    st.markdown(f"""<div class="glass-card"><h2 style="color:#2d3436; margin:0;">📍 {current_data['name']}</h2></div>""", unsafe_allow_html=True)
    st.write("")
    
    album = current_data.get("album", [])
    idx_key = f"photo_idx_{index}"
    if idx_key not in st.session_state:
        st.session_state[idx_key] = 0
    current_photo_index = st.session_state[idx_key]
    if current_photo_index >= len(album): current_photo_index = 0
    current_item = album[current_photo_index]
    
    try:
        img = Image.open(current_item['image'])
        st.image(img)
    except:
        st.warning(f"缺少照片: {current_item['image']}")

    # 導航按鈕 (同一排！)
    if len(album) > 1:
        c_prev, c_info, c_next = st.columns(3)
        
        with c_prev:
            if st.button("❮", key=f"prev_{index}"):
                st.session_state[idx_key] = (current_photo_index - 1) % len(album)
                st.rerun()
        
        with c_info:
            # 移除了會干擾排版的 width 設定，讓 CSS 統一接管置中
            st.markdown(f"<div style='text-align:center; color:#aaa; font-weight:bold; font-size:16px;'>{current_photo_index + 1} / {len(album)}</div>", unsafe_allow_html=True)
            
        with c_next:
            if st.button("❯", key=f"next_{index}"):
                st.session_state[idx_key] = (current_photo_index + 1) % len(album)
                st.rerun()

    st.write("")
    st.markdown(f"""
        <div class="glass-card" style="min-height: 100px; padding: 15px;">
            <p style="font-size:18px; color:#555; margin:0; line-height:1.6;">
                {current_item['desc']}
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.write("")

    if index < len(destinations):
        if st.button("✈️ 下一站"):
            play_flight_animation()
            st.session_state.stage += 1
            st.rerun()
    else:
        if st.button("旅程結束", type="primary"):
            play_flight_animation()
            st.session_state.stage = 999
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

def show_final_surprise():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.balloons()
    
    st.markdown("""
        <div class="glass-card">
            <h1 style="color:#FF6B6B; font-size: 32px; margin: 0;">💗 情人節快樂! 💗</h1>
        </div>
    """, unsafe_allow_html=True)
    st.write("")

    final_photo_path = "images/final.jpg" 
    try:
        img = Image.open(final_photo_path)
        st.markdown('<div class="glass-card" style="padding: 10px;">', unsafe_allow_html=True)
        st.image(img)
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.warning(f"找不到最後的照片，請確認 {final_photo_path} 檔案是否存在。")

    st.write("")

    if st.button("🔄 再飛一次"):
        st.session_state.stage = 0
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. 主程式流程控制
# -----------------------------------------------------------------------------
if st.session_state.stage != st.session_state.prev_stage:
    scroll_to_here(0, key=f"force_scroll_top_stage_{st.session_state.stage}")
    st.session_state.prev_stage = st.session_state.stage

if st.session_state.stage == 0:
    show_ticket()
elif 1 <= st.session_state.stage <= len(destinations):
    show_journey_step(st.session_state.stage)
elif st.session_state.stage == 999:
    show_final_surprise()