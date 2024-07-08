import streamlit as st
import data.data as dd
import datetime
import time
import backgroud.backgroud as bg
# 背景色

st.set_page_config(
    page_title="chatbot",
)
user_id = st.session_state.user_id # 用户id就是某一个用户的唯一标识
username = st.session_state.username
# f"字符串{变量名}"
st.title("AI智能助手 👏")
st.subheader(f"欢迎{username}使用")
st.text("这是一个AI助手，可以回答你的任何问题，请尽情使用吧！")
message = "预 计 吕 梁 地 区 将 有 小 雨 转 多 云 的 天 气 变 化 。 这 意 味 着 在 白 天 或 夜 晚 的 某个 时 间 段 内 可 能 会 有 小 雨 ， 但 随 后 天 气 将 转 为 多 云 。 温 度 范 围 ： 明 天 的 气 温 预 计 在 18℃ 到 29℃ 之 间 ， 相 对 较 为 宜 人 。 风 力 与 风 向 ： 预 计 明 天 将 有 东 南 风 ， 且 风 力 小 于 3 级 ， 这 意 味 着 风 势 较 为 温 和 ， 不 会 对 日 常 生 活 造 成 太 大 影 响 。 空 气 质 量 ： 空 气 质 量 预 测 为 良 ， 这 意 味 着 空 气 中 的 污 染 物 浓 度 较 低 ， 对 人 体 健 康 的 影 响 较 小 。"
def ai_response():
    for word in message.split():
        yield word+" "
        time.sleep(0.1)
# 创建一个聊天输入框 接受用户输入的问题
problem = st.chat_input("请输入你的问题")
if problem:
    # 展示一个聊天信息 chat_message是一个聊天信息的展示组件，如果组件中增加信息，需要通过如下语法来完成
    dd.add_chat_message(user_id,problem,"user",datetime.datetime.now())
    with st.chat_message("user"):
        st.write(problem)
    # AI回复一下
    with st.chat_message("assistant"):
        dd.add_chat_message(user_id, message, "assistant", datetime.datetime.now())
        # write写出的数据是直接一下全部输出了 一般输出应该都是流式输出
        # write写出一个字符串即可，write_stream中不能放字符串 而应该是一个迭代器
        response = ai_response()
        st.write_stream(response)
remove = st.button("清屏")
if remove:
    st.switch_page("pages/chatbot2.py")

bg.main_bg('image/chatbot.jpg')

