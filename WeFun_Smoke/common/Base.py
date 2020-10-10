
class Context:
    #乐园社区
    server_id = 1216333003035246592
    # 接口测试社区
    api_id = 1277254596447698944
    # 自行创建社区得id
    new_sercer = None
    # 自行创建社区下频道类别ID
    channel_id = None
    Cookie = None



    # 频道发消息--->写死的id
    news_channel = 1262423827544014848

if __name__ == '__main__':

    print(getattr(Context,'new_sercer'))
    print(getattr(Context,))
