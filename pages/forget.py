import streamlit as st
import re
import data.data as dd
import time

# 设置注册的标签页
st.set_page_config(
    page_title="私人助手找回密码页",
    page_icon="😀"
)
# 设置页面的标题
st.title("私人助手找回密码页 👏")

# 设置注册页面的组件
username = st.text_input("请输入手机号")
password = st.text_input("请输入密码",type="password")
repass = st.text_input("请再次输入密码",type="password")
verify = st.text_input("验证码")

verifyFlag = st.button("修改密码")
# 登录按钮
loginFlag = st.button("已有账号？点击登录")

def verify(username,password,repass):
    if username and password and repass:
        result = dd.query_user_by_username(username)
        if result is None:
            st.error("用户不存在，请前往注册")
        else:
            if password == repass:
                dd.update_password_by_username(username,password)
                st.success("修改成功！")
                time.sleep(1)
                st.switch_page("login.py")
            else:
                st.error("两次密码不一致")
    else:
        st.error("请务必填写相关注册信息")
# 定义一个注册函数
if verifyFlag:
    verify(username,password,repass)
if loginFlag:
    # 如果要跳转到系统的首页，前面不能加pages
    st.switch_page("login.py")