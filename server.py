import random
from pyecharts import Line, Kline, Grid
from pyecharts_javascripthon.api import TRANSLATOR
from pyecharts import Scatter3D
from flask import Flask, render_template
import time
"""
Windows 系统
set FLASK_APP=server.py
flask run
"""

app = Flask(__name__)


REMOTE_HOST = "https://pyecharts.github.io/assets/js"



@app.route("/")
def hello():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    # s3d = scatter3d()
    # return render_template(
    #     "bbspyecharts.html",
    #     myechart=s3d.render_embed(),
    #     host=REMOTE_HOST,
    #     script_list=s3d.get_js_dependencies(),
    # )

    _bar = data_mix()# bar_chart()
    javascript_snippet = TRANSLATOR.translate(_bar.options)

    return render_template(
        "bbsResize.html",
        chart_id=_bar.chart_id,
        host=REMOTE_HOST,
        renderer=_bar.renderer,
        my_width="100%",
        my_height=600,
        custom_function=javascript_snippet.function_snippet,
        options=javascript_snippet.option_snippet,
        script_list=_bar.get_js_dependencies(),
    )


def bar_chart():
    # bar = Bar("我的第一个图表", "这里是副标题")
    # bar.add(
    #     "服装"
    #     , ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    #     , [5, 20, 36, 10, 75, 90]
    # )

    # attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    # v1 = [5, 20, 36, 10, 75, 90]
    # v2 = [10, 25, 8, 60, 20, 80]
    # bar = Bar("柱状图数据堆叠示例")
    # bar.add("商家A", attr, v1, is_stack=True)
    # bar.add("商家B", attr, v2, is_stack=True)
    # return bar

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", height=720)
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)

    line = Line("折线图示例", title_top="50%")
    attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    line.add(
        "最高气温",
        attr,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        attr,
        [1, -2, 2, 5, 3, 2, 0],
        mark_point=["max", "min"],
        mark_line=["average"],
        legend_top="50%",
    )

    grid = Grid()
    grid.add(bar, grid_bottom="60%")
    grid.add(line, grid_top="60%")
    return grid

def data_mix():
    # control charts together
    # 设置 dataZoom 控制索引
    line = Line("折线图示例", width=1200, height=700)
    # attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    attr = ["2018/5/{}".format(i + 1) for i in range(31)]
    line.add(
        "最高气温",
        attr,
        [11, 11, 15, 13, 12, 13, 10, 11, 15, 13, 12, 13, 10, 11, 15, 13, 12, 13, 10, 10, 12, 13, 10, 11, 15, 13, 12, 13, 10, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        attr,
        [1, -2, 2, 5, 3, 2, 0, -2, 2, 5, 3, 2, 0, -2, 2, 5, 3, 2, 0, -2, 2, 5, 3, 2, 0, 2, 0, 2, -2, 2, -2],
        mark_point=["max", "min"],
        legend_top="50%",
        mark_line=["average"],
        # 设置 dataZoom 控制索引为 0,1 的 x 轴，即第一个和第二个
        is_datazoom_show=True,
        datazoom_xaxis_index=[0, 1],
    )

    v1 = [
        [2320.26, 2320.26, 2287.3, 2362.94],
        [2300, 2291.3, 2288.26, 2308.38],
        [2295.35, 2346.5, 2295.35, 2345.92],
        [2347.22, 2358.98, 2337.35, 2363.8],
        [2360.75, 2382.48, 2347.89, 2383.76],
        [2383.43, 2385.42, 2371.23, 2391.82],
        [2377.41, 2419.02, 2369.57, 2421.15],
        [2425.92, 2428.15, 2417.58, 2440.38],
        [2411, 2433.13, 2403.3, 2437.42],
        [2432.68, 2334.48, 2427.7, 2441.73],
        [2430.69, 2418.53, 2394.22, 2433.89],
        [2416.62, 2432.4, 2414.4, 2443.03],
        [2441.91, 2421.56, 2418.43, 2444.8],
        [2420.26, 2382.91, 2373.53, 2427.07],
        [2383.49, 2397.18, 2370.61, 2397.94],
        [2378.82, 2325.95, 2309.17, 2378.82],
        [2322.94, 2314.16, 2308.76, 2330.88],
        [2320.62, 2325.82, 2315.01, 2338.78],
        [2313.74, 2293.34, 2289.89, 2340.71],
        [2297.77, 2313.22, 2292.03, 2324.63],
        [2322.32, 2365.59, 2308.92, 2366.16],
        [2364.54, 2359.51, 2330.86, 2369.65],
        [2332.08, 2273.4, 2259.25, 2333.54],
        [2274.81, 2326.31, 2270.1, 2328.14],
        [2333.61, 2347.18, 2321.6, 2351.44],
        [2340.44, 2324.29, 2304.27, 2352.02],
        [2326.42, 2318.61, 2314.59, 2333.67],
        [2314.68, 2310.59, 2296.58, 2320.96],
        [2309.16, 2286.6, 2264.83, 2333.29],
        [2282.17, 2263.97, 2253.25, 2286.33],
        [2255.77, 2270.28, 2253.31, 2276.22],
    ]
    kline = Kline("K 线图示例", title_top="50%")
    kline.add(
        "日K",
        ["2018/5/{}".format(i + 1) for i in range(31)],
        v1,
        is_datazoom_show=True,
    )

    grid = Grid()
    grid.add(line, grid_top="60%")
    grid.add(kline, grid_bottom="60%")
    return grid

def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ]
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D

def generate_3d_random_point():
    return [
        random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
    ]

if __name__ == '__main__':
    print('===start===')
    app.run(debug=True)  # threaded=True,
    print('===end===')