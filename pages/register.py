import streamlit as st
import re
import data.data as dd
import time
import backgroud.backgroud as bg
# 背景色

# 设置注册的标签页
st.set_page_config(
    page_title="私人助手注册页",
    page_icon="😀"
)
# 设置页面的标题
st.title("私人助手注册页 👏")

# 设置注册页面的组件
username = st.text_input("请输入手机号")
password = st.text_input("请输入密码",type="password")
repass = st.text_input("请再次输入密码",type="password")
registerFlag = st.button("注册")
# 登录按钮
loginFlag = st.button("已有账号？点击登录")

# 定义一个注册函数
def register(username,password,repass):
    # 1、校验三个信息是否填写
    if username and password and repass:
        #2、校验用户名的长度是否为11位 并且是否为手机号 正则表达式
        if re.match('^(13|15|17|18|19)[0-9]{9}$', username):
            #3、查看两次密码是否一致 并且密码长度必须大于等于8位
            if password == repass and len(password) >=8:
                # 4、查询数据库是否有重复信息
                if dd.query_user_by_username(username):
                    st.error("用户已注册，请勿重复注册！")
                else:
                    dd.add_user(username, password)
                    st.success("注册成功")
                    time.sleep(2)
                    st.switch_page("login.py")
            else:
                st.error("两次密码不一致或者密码长度字段不足8位")
        else:
            st.error("手机号格式不正确")

    else:
        st.error("请务必填写相关注册信息")


# 点击注册按钮之后，需要将用户输入的用户名、密码、确认密码全部拿到，
# 先校验信息是否填写，检验两次密码是否一致 校验账号是否在数据库存在，
# 如果都校验成功，需要添加到数据库 然后再跳转到登录界面
if registerFlag:
    register(username, password, repass)

# 这是是当点击登录按钮之后需要跳转到登录界面
if loginFlag:
    # 如果要跳转到系统的首页，前面不能加pages
    st.switch_page("login.py")

bg.main_bg('image/register.jpg')