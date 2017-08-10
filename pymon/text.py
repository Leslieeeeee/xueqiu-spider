import jieba

seg_list = jieba.cut_for_search("<p>今日，沪指上涨0.08%，报收3241点；深成指上涨0.11%，报收10543点；创业板下跌0.01%，报收1957点。从盘面上看，家用电器、环保、航运、小金属等板块涨幅居前；种植业、西安自贸区、大飞机、人工智能等板块跌幅居前。据羽时炼金术涨跌背离得出需要警惕5只股票：002437.SZ &nbsp;誉衡药业、600315.SH上海家化、600346.SH恒力股份、000908.SZ &nbsp; &nbsp; 景峰医药、600308.SH华泰股份；值得关注5只股：600383.SH金地集团、600666.SH奥瑞德、000620.SZ新华联、600165.SH新日恒力、002511.SZ中顺洁柔</p><p><img class=\"ke_img\" src=\"//xqimg.imedao.com/15ad206cd716d763fde817d3.png!custom.jpg\" ></p><p><img class=\"ke_img\" src=\"//xqimg.imedao.com/15ad20715d56d213fe08f9eb.png!custom.jpg\" ></p><p><img class=\"ke_img\" src=\"//xqimg.imedao.com/15ad2073da86d253fe7b6bef.png!custom.jpg\" ></p>")
print("Default Mode:", "/ ".join(seg_list)) #精确模式
