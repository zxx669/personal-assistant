import streamlit as st
import data.data as dd
user_id = st.session_state.user_id # 用户id就是某一个用户的唯一标识
username = st.session_state.username
# f"字符串{变量名}"
st.title("AI智能助手 👏")
st.subheader(f"欢迎{username}使用")
st.text("这是一个AI助手，可以回答你的任何问题，请尽情使用吧！")

# 渲染私人助手界面的时候，应该查询当前用户的历史聊天记录，用于进行界面的渲染
list = dd.query_message_by_user_id(user_id=user_id)
if list:
    #{"message_id":xx,"user_id":xx,message:xxx,role:xxx,message_time:xxx"}
    for msg in list:
        with st.chat_message(msg["role"]):
            st.write(msg["message"])
else:
    # 如果当前用户和AI助手没有任何的聊天记录，需要给他一个默认的助手欢迎语
    with st.chat_message("assistant"):
        st.write("我是你的智能AI助手，可以回答你的任何问题，请问你有什么问题？")

# 创建一个聊天输入框 接受用户输入的问题
problem = st.chat_input("请输入你的问题")




