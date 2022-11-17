from .base_import import *
from app.util.http_util import *
from lxml import etree
import time


@api_bp.route("/getdata", methods=["POST", "GET"])
def get_sphere_date():
    now_time = time.localtime(time.time())
    year = int(str(now_time[0])[2:])
    sql = "SELECT MAX(ISSUE) FROM ball_history;"
    ret = sql_engine.execute(sql)
    issue = ret.fetchall()
    issue = issue[0][0]
    html = get_html_by_requests("https://datachart.500.com/ssq/history/newinc/history.php?start=%s" % (issue))
    tree = etree.HTML(html)
    line = tree.xpath('//*[@id="tdata"]/tr')
    if (len(line) == 2):
        session = Session()
        newb = Ball_history()
        num = line[0].xpath("td/text()")[0:8]
        if (num[0] == str(issue)):
            num = line[1].xpath("td/text()")[0:8]
        newb.issue = num[0]
        newb.red1 = num[1]
        newb.red2 = num[2]
        newb.red3 = num[3]
        newb.red4 = num[4]
        newb.red5 = num[5]
        newb.red6 = num[6]
        newb.blue = num[7]
        session.add(newb)
        session.commit()
        session.close()
        return str(num)
    return "自己手动点的？是不是傻？"

# 加载权重文件
@api_bp.route("/getdata", methods=["POST", "GET"])
def load_weighted():
    # 本期now 和 after

    return None
