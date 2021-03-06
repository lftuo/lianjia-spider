#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-10 10:17:51
# @File : LianjiaErShouListSpider.py
# @Software : PyCharm
# 爬取链家二手房列表信息
import requests
from bs4 import BeautifulSoup
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ListSpider(object):



    def get_list_info(self):
        html_str = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
            <meta http-equiv="Cache-Control" content="no-transform"/>
            <meta http-equiv="Cache-Control" content="no-siteapp"/>
            <meta http-equiv="Content-language" content="zh-CN"/>
            <meta name="format-detection" content="telephone=no"/>
            <meta name="applicable-device" content="pc">
            <link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.lianjia.com/gz/ershoufang/ershoufang.html">
            <meta name="mobile-agent" content="format=html5;url=https://m.lianjia.com/gz/ershoufang/">
            <script>
                ljConf = {
                    city_id: '440100',
                    city_abbr: 'gz',
                    city_name: '广州',
                    channel: 'ershoufang',
                    page: 'ershoufang_search',
                    pageConfig: {
                        "ajaxroot": "\/\/ajax.api.lianjia.com\/",
                        "imAppid": "LIANJIA_WEB_20160624",
                        "imAppkey": "6dfdcee27d78b1107fceeca55d80b7bd"
                    },
                    feroot: '//s1.ljcdn.com/feroot/',
                    ucid: '',
                    cdn: '0',
                };
            </script>
        
            <!-- 2017.7.18 开放全国 -->
            <script>
                var _hmt = _hmt || [];
                (function () {
                    var hm = document.createElement("script");
                    hm.src = "https://hm.baidu.com/hm.js?9152f8221cb6243a53c83b956842be8a";
                    var s = document.getElementsByTagName("script")[0];
                    s.parentNode.insertBefore(hm, s);
                })();
            </script>
            <title>【广州二手房_广州二手房出售_广州二手房网】（广州链家网）</title>
            <meta name="description"
                  content="链家广州二手房网,现有广州二手房真实房源14338套.为准备买广州二手房的用户提供广州地图找房、通勤找房等快捷找房工具,方便您更快捷的了解和购买广州二手房.买广州二手房就到广州链家网."/>
            <meta name="keywords" content="广州二手房,广州二手房出售,广州二手房网"/>
            <link href="/favicon.ico" type="image/x-icon" rel=icon>
            <link href="/favicon.ico" type="image/x-icon" rel="shortcut icon">
            <link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/common.css?_v=201709261333487">
            <link rel="stylesheet" href="https://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellList/index.css?_v=201709261333487">
            <!--[if lt IE 9]>
            <script type="text/javascript"
                    src="https://s1.ljcdn.com/feroot/dep/common-require/html5.js?_v=201709261333487"></script><![endif]-->
            <script>
                function RESIZEIMG(b, k, l, m) {
                    var c = b.parentNode;
                    var d = parseInt(c.offsetWidth) || k;
                    var e = parseInt(c.offsetHeight) || l;
                    var f = d / e;
                    var g = b.naturalWidth || b.width;
                    var h = b.naturalHeight || b.height;
                    var i = g / h;
                    var j = "width";
                    if (f < i) {
                        j = "height";
                        try {
                            b.style["left"] = "-" + parseInt(Math.abs((d - (g * e / h)) / 2)) + "px"
                        } catch (e) {
                        }
                    } else if (m) {
                        try {
                            b.style["top"] = "-" + parseInt(Math.abs((e - (h * d / g)) / 2)) + "px"
                        } catch (e) {
                        }
                    }
                    ;b.style[j] = "100%";
                };
            </script>
            <script>
                var _czc = _czc || [];
                _czc.push(["_setAccount", "1254525948"]);
            </script>
        
            <script type="text/javascript">
                var _smq = _smq || [];
                _smq.push(['_setAccount', '41331c2', new Date()]);
                _smq.push(['_setDomainName', 'lianjia.com']);
                _smq.push(['pageview']);
                (function () {
                    var sm = document.createElement('script');
                    sm.type = 'text/javascript';
                    sm.async = true;
                    sm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'cdnmaster.com/sitemaster/collect.js';
                    var s = document.getElementsByTagName('script')[0];
                    s.parentNode.insertBefore(sm, s);
                })();
            </script>
        </head>
        <body>
        <script>
            __STAT_LJ_CONF = {
                params: {
                    ljweb_group: ['SEARCH', 'BIGDATA_PC'],
                    ljweb_id: '',
                    ljweb_mod: '',
                    ljweb_bl: '',
                    ljweb_el: '',
                    ljweb_sl: '',
                    ljweb_index: '',
                    ljweb_value: '',
                    ljweb_url: '',
                    ljweb_ljref: (document.cookie.match(/(?:^| )ljref=([^;]*)(?:;|$)/) || ['', ''])[1],
                    ljweb_sample: (document.cookie.match(/(?:^| )sample_traffic_test=([^;]*)(?:;|$)/) || ['', ''])[1],
                    ljweb_ref: document.referrer,
                    ljweb_cid: '440100',
                    ljweb_channel: 'ershoufang',
                    ljweb_page: 'ershoufang_search',
                    ljweb_source: '',
                    ljweb_stat_id: ''
                }
            };
        
        
            var UT = {
                send: function () {
        
                }
            };
            var LjUserTrack = {
                log: [],
                initInterval: false,
                intervalLog: function () {
                    setTimeout(function () {
                        if (window.$ULOG && $ULOG.send) {
                            for (var i = 0, l = LjUserTrack.log.length; i < l; i++) {
                                LjUserTrack.__send(LjUserTrack.log[i]);
                            }
        
                            for (var m = 0, n = LjUserTrack.logIds.length; m < n; m++) {
                                LjUserTrack.__sendId(LjUserTrack.logIds[m]);
                            }
                        } else {
                            LjUserTrack.intervalLog();
                        }
                    }, 16.7);
                },
                _start_time: +new Date,
                __send: function (data) {
                    var evt_id = data.evt_id || '10043';
                    if ('evt_id' in data) {
                        delete data.evt_id;
                    }
        
                    $ULOG.send(evt_id, {
                        "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid) || "lianjiaweb",
                        "key": window.location.href,
                        "action": data
                    });
                },
                logIds: [],
                __sendId: function (id) {
                    id && $ULOG.send(id, {
                        "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid) || "lianjiaweb",
                        "key": window.location.href
                    });
                },
                sendId: function (id) {
                    if (window.$ULOG && $ULOG.send) {
                        LjUserTrack.__sendId(id);
                    } else {
                        LjUserTrack.logIds.push(id);
        
                        LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());
        
                    }
                },
                send: function (data, el, config) {
        
                    var utConf = __STAT_LJ_CONF;
                    var params = config || utConf.params,
                        win = window,
                        j;
        
                    data.groupIndex = data.ljweb_group || 0;
        
                    if (params) {
                        for (var d in params) {
                            if (params[d] !== j && data[d] === j) {
                                data[d] = params[d];
                            }
                        }
                    }
        
                    if (el) {
                        this.checkClick(el, data);
                    }
        
                    data.ljweb_group = params['ljweb_group'][data.groupIndex || 0];
        
                    delete data.groupIndex;
        
                    if (data.typ) {
                        data.ljweb_bl = (data.ljweb_bl || '') + '_' + data.typ;
                        delete data.typ;
                    }
        
                    if (window.$ULOG && $ULOG.send) {
                        LjUserTrack.__send(data);
                    } else {
                        LjUserTrack.log.push(data);
        
                        LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());
        
                    }
        
                },
                checkClick: function (el, data) {
        
                    var TAG_LINK = 'A';
                    var href = '';
                    var elParent = null;
        
                    href = (el.tagName.toUpperCase() === TAG_LINK ? el.getAttribute("href", 2) : '');
                    if (!href && (elParent = el.parentNode) && elParent.nodeType === 1) {
                        href = (elParent.tagName.toUpperCase() === TAG_LINK ? elParent.getAttribute("href", 2) : '');
                    }
        
                    if (href) {
                        data.ljweb_url = href;
                    } else {
                        data.ljweb_url = data.ljweb_url
                            || el.getAttribute("data-log_url")
                            || (elParent = el.parentNode || el).getAttribute("data-log_url")
                            || (
                                (elParent = elParent.parentNode || elParent)
                                && (elParent.nodeType === 1)
                                && elParent.getAttribute("data-log_url")
                            )
                            || "";
                    }
        
                    this.attr(el, data);
        
                },
                path: function () {
        
                },
                attr: function (el, data) {
                    var modId = el.getAttribute("log-mod");
                    var blAttr = el.getAttribute("data-bl");
                    var elAttr = el.getAttribute("data-el");
                    var slAttr = el.getAttribute("data-sl");
                    var InAttr = el.getAttribute("data-log_index");
                    var valAttr = el.getAttribute("data-log_value");
                    var idAttr = el.getAttribute("data-log_id");
                    var groupAttr = el.getAttribute("data-log_group");
                    var sourceAttr = el.getAttribute("data-log_source");
                    var statIdAttr = el.getAttribute("data-log_statId");
                    var evtId = el.getAttribute("data-log_evtid");
        
                    data.ljweb_bl = data.ljweb_bl || blAttr || '';
                    data.ljweb_el = data.ljweb_el || elAttr || '';
                    data.ljweb_sl = data.ljweb_sl || slAttr || '';
                    data.ljweb_index = data.ljweb_index || InAttr || '';
                    data.ljweb_value = data.ljweb_value || valAttr || '';
                    data.ljweb_id = data.ljweb_id || idAttr || '';
                    data.ljweb_source = data.ljweb_source || sourceAttr || '';
                    data.ljweb_stat_id = data.ljweb_stat_id || statIdAttr || 0;
                    data.groupIndex = data.groupIndex || groupAttr || 0;
                    data.evt_id = data.evt_id || evtId || '';
        
                    if (!modId) {
                        if (el.parentNode && el.parentNode.nodeType === 1 && el.parentNode.tagName.toUpperCase() !== 'BODY') {
                            this.attr(el.parentNode, data);
                        }
                    } else {
                        data.ljweb_mod = modId;
                    }
                }
            };
        
            ;
            ;(function () {
                var isW3c = !!document.addEventListener;
        
                LjUserTrack.send({
                    ljweb_mod: 'pv',
                    ljweb_group: 1
                });
        
                /*window[isW3c ? 'addEventListener' : 'attachEvent'](
                (isW3c ? '': 'on') + 'beforeunload',
                function(e) {
                    var _end_time = +new Date;
                    UT.send({type: 'show', subtype: 'stay', time: (_end_time-UT._start_time)/1000});
                },
                false);*/
            })();
        
        
        </script>
        <div class="banner">
            <div class="container">
                <ul class="channelList">
                    <li><a href="//www.lianjia.com/ershoufang.html">首页</a></li>
                    <li class="selected"><a href="https://gz.lianjia.com/ershoufang/ershoufang.html">二手房</a></li>
                    <li class=""><a href="http://gz.fang.lianjia.com/ershoufang.html">新房</a></li>
                    <li class=""><a href="https://gz.lianjia.com/zufang/ershoufang.html">租房</a></li>
                    <li rel="nofollow" class=""><a href="http://you.lianjia.com/ershoufang.html">旅居</a></li>
                    <li class=""><a href="https://us.lianjia.com">海外</a></li>
                    <li class=""><a href="https://gz.lianjia.com/xiaoqu/ershoufang.html">小区</a></li>
                    <li class=""><a href="https://gz.lianjia.com/jingjiren/ershoufang.html">经纪人</a></li>
                    <li class=""><a href="https://gz.lianjia.com/wenda/ershoufang.html">指南</a>
                        <div class="childList"><a href="https://gz.lianjia.com/wenda/ershoufang.html">问答</a><a
                                href="https://news.lianjia.com/gz/baike/ershoufang.html">百科</a></div>
                    </li>
                    <li class=""><a href="https://gz.lianjia.com/tool.html" target="_blank">工具</a></li>
                    <li class=""><a href="https://gz.lianjia.com/yezhu/ershoufang.html" target="_blank">业主</a></li>
                </ul>
                <div class="banner-right">
                    <div class="login" id="userInfoContainer"><i></i><a
                            href="https://upassport.lianjia.com/login?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fgz.lianjia.com%252Fershoufang%252F"
                            id="loginBtn" rel="nofollow">登录</a>/<a
                            href="https://passport.lianjia.com/register/resources/lianjia/register.html?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttps%253A%252F%252Fgz.lianjia.com%252Fershoufang%252F"
                            id="registerBtn" rel="nofollow">注册</a></div>
                    <div class="phone"><i></i><span>热线电话1010-9666</span></div>
                </div>
            </div>
        </div>
        
        
        <script type="text/template" id="userInfoTpl">
            <i></i>
            <%if(isAgent){%>
            <a id="userNameContainer" href="<%=$.env.fixedUrl('//agent.lianjia.com/')%>"><%=username%></a>
            <%}else{%>
            <a id="userNameContainer" href="<%=$.env.fixedUrl('//user.lianjia.com/')%>" rel="nofollow"><%=username%></a>
            <%}%>
            <span id="tipContainer"></span>
            &nbsp;&nbsp;<a href="<%=logoutUrl%>">退出</a>
            <span id="pushNewsListContainer"></span>
        </script>
        <script type="text/template" id="pushNewsListTpl">
            <div class="pushNewsList">
                <%for(var i in group_by_type){%>
                <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
                <a href="<%=pushMsgMap[i].url%>"><%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%></a>
                <%}%>
                <%}%>
            </div>
        </script>
        
        <div class="header">
            <div class="menu">
                <div class="menuLeft"><a href="/ershoufang/" class="logo"></a>
                    <ul class="typeList">
                        <li class="selected"><a href="/ershoufang/" title="广州在售二手房">在售</a></li>
                        <li><a href="/chengjiao/" title="广州成交二手房">成交</a></li>
                        <li><a href="/xiaoqu/" title="广州小区二手房">小区</a></li>
                        <li><a href="/ditu/" title="广州地图找房二手房" target="_blank">地图找房</a></li>
                    </ul>
                </div>
                <div class="app"><a href="//www.lianjia.com/client/ershoufang.html" target="_blank"><i></i>下载链家APP<span
                        class="layer-qrcode"><span class="icon-qrcode"><img width="124" height="124"
                                                                            src="/ershoufang.html/ajax.api.lianjia.com/qr/getDownloadQr?location=menu_app&ljweb_channel_key=ershoufang_search"
                                                                            alt="下载链家app"></span><span
                        class="txt">使用链家APP</span><span class="sub-txt">随时随地查看新上房源</span></span></a></div>
            </div>
            <div class="search">
                <div class="input" log-mod="search">
                    <form id="searchForm" action='/ershoufang/rs'><input type="text" id="searchInput" value=""
                                                                         autocomplete="off">
                        <div class="inputRightPart">
                            <div class="save" id="savedSearchMsg"><span id="savedSearchCount">0</span>条已保存搜索<span
                                    id="savedSearchArrow" class="downArrow"></span></div>
                            <button type='submit' class="searchButton" data-bl="search" data-el="search">&nbsp;<i></i>&nbsp;
                            </button>
                        </div>
                    </form>
                    <div class="searchMsg" id="searchMsgContainer"></div>
                </div>
            </div>
        </div>
        
        
        <script type="text/template" id="hotSearchTpl">
            <div class="searchMsgTitle">
                <span class="searchMsgName">热门搜索</span>
            </div>
            <ul data-bl="sug" data-el="history">
                <%for(var i =0; i < list.length; i++){%>
                <li>
                    <a role="addHistory" href="<%=list[i].url%>" data-log_index="<%=i+1%>" data-log_value="<%=list[i].string%>"
                       class="sug--search_item">
                        <span class="msgListTitle" role="historyKey"><%=list[i].string%></span>
                    </a>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="searchHistoryTpl">
            <div class="searchMsgTitle">
                <span class="searchMsgName">搜索历史</span>
                <div class="searchMsgTitleRightPart">
                    <a href="#" id="clearSearchHistory" class="manage">清除历史记录</a>
                </div>
            </div>
            <ul data-bl="sug" data-el="history">
                <%for(var i = 0; i < list.length; i++){%>
                <li>
                    <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>"
                       data-log_value="<%=$.encodeHTML(list[i].name)%>" class="sug--search_item">
                        <span class="msgListTitle" role="historyKey"><%=$.encodeHTML(list[i].name)%></span>
                        <%if(list[i].newCount) {%>
                        <span class="msgListAdd"><%=list[i].newCount%>套新增房源</span>
                        <%}%>
                    </a>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="searchSuggestionTpl">
            <div class="searchMsgTitle">
                <span class="searchMsgName">你可能在找</span>
            </div>
            <ul data-bl="sug" data-el="sug">
                <%for(var i = 0;i < list.length;i++){%>
                <li>
                    <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>" data-log_value="<%=list[i].title%>">
                <span class="msgListTitle">
                  <span role="historyKey"><%=list[i].title%></span>
                  <%if(list[i].region){%>
                    <span class="msgListArea"><%=list[i].region%></span>
                  <%}%>
                </span>
                        <%if(type === 'sell'){%>
                        <span class="msgListAdd">约<%=list[i].count%>套在售</span>
                        <%}else if(type === 'deal'){%>
                        <span class="msgListAdd">约<%=list[i].count%>套成交</span>
                        <%}%>
                    </a>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="savedSearchTpl">
            <div class="searchMsgTitle">
                <span class="searchMsgName">已保存搜索</span>
                <div class="searchMsgTitleRightPart">
                    <%if(totalCount){%>
                    <a class="totalNew">查看<%=totalCount%>套新增房源</a>
                    <%}%>
                    <a href="<%=userCenterUrl%>" class="manage">管理</a>
                </div>
            </div>
            <ul data-bl="sug" data-el="history">
                <%for(var i = 0; i < savedData.length; i++){
                var title = savedData[i].query ? savedData[i].query + '&nbsp;' : '';
                title = title + savedData[i].title.join('&nbsp;');
                %>
                <li>
                    <a href="<%=savedData[i].url%>" role="savedSearch" data-log_index="<%=i+1%>" data-log_value="<%=title%>"
                       class="sug--search_item">
                        <span class="msgListTitle"><%=title%></span>
                        <%if(savedData[i].unread && savedData[i].unread !== 0){%>
                        <span class="msgListAdd">新增<%=savedData[i].unread%>套</span>
                        <%}%>
                    </a>
                </li>
                <%}%>
            </ul>
        </script>
        
        <script>
            var hotSearchData = {
                channel: [{
                    "name": "\u4e8c\u624b\u623f",
                    "action": "ershoufang",
                    "channel": "ershoufang",
                    "checked": 1,
                    "tipsHot": {
                        "query": [{
                            "string": "\u78a7\u6842\u56ed\u51e4\u51f0\u57ce",
                            "url": "http:\/\/gz.lianjia.com\/ershoufang\/c2111103316652\/"
                        }, {
                            "string": "\u91d1\u78a7\u82b1\u56ed",
                            "url": "http:\/\/gz.lianjia.com\/ershoufang\/c2111103316673\/"
                        }, {
                            "string": "\u9a8f\u666f\u82b1\u56ed",
                            "url": "http:\/\/gz.lianjia.com\/ershoufang\/c2111103317119\/"
                        }, {
                            "string": "\u7f57\u9a6c\u5bb6\u56ed",
                            "url": "http:\/\/gz.lianjia.com\/ershoufang\/c2111103317093\/"
                        }, {
                            "string": "1\u53f7\u7ebf\u5730\u94c1\u623f",
                            "url": "http:\/\/gz.lianjia.com\/ditiefang\/li110460679\/"
                        }, {
                            "string": "5\u53f7\u7ebf\u5730\u94c1\u623f",
                            "url": "http:\/\/gz.lianjia.com\/ditiefang\/li110460685\/"
                        }],
                        "tips": "\u8bf7\u8f93\u5165\u533a\u57df\u3001\u5546\u5708\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"
                    }
                }, {
                    "name": "\u5c0f\u533a",
                    "action": "xiaoqu",
                    "channel": "xiaoqu",
                    "checked": 0,
                    "tipsHot": {
                        "query": [{
                            "string": "\u78a7\u6842\u56ed\u51e4\u51f0\u57ce",
                            "url": "http:\/\/gz.lianjia.com\/xiaoqu\/2111103316652\/"
                        }, {
                            "string": "\u91d1\u78a7\u82b1\u56ed",
                            "url": "http:\/\/gz.lianjia.com\/xiaoqu\/2111103316673\/"
                        }, {
                            "string": "\u9a8f\u666f\u82b1\u56ed",
                            "url": "http:\/\/gz.lianjia.com\/xiaoqu\/2111103317119\/"
                        }, {
                            "string": "\u7f57\u9a6c\u5bb6\u56ed",
                            "url": "http:\/\/gz.lianjia.com\/xiaoqu\/2111103317093\/"
                        }, {"string": "\u661f\u6cb3\u6e7e", "url": "http:\/\/gz.lianjia.com\/xiaoqu\/2111103316631\/"}],
                        "tips": "\u8bf7\u8f93\u5165\u5c0f\u533a\u540d\u5f00\u59cb\u67e5\u627e\u5c0f\u533a"
                    }
                }, {
                    "name": "\u65b0\u623f",
                    "action": "loupan",
                    "channel": "xinfang",
                    "checked": 0,
                    "tipsHot": {"query": [], "tips": "\u8bf7\u8f93\u5165\u697c\u76d8\u540d\u79f0\u5f00\u59cb\u627e\u623f"}
                }, {
                    "name": "\u79df\u623f",
                    "action": "zufang",
                    "channel": "zufang",
                    "checked": 0,
                    "tipsHot": {
                        "query": [{
                            "string": "\u78a7\u6842\u56ed\u51e4\u51f0\u57ce",
                            "url": "http:\/\/gz.lianjia.com\/zufang\/c2111103316652\/"
                        }, {
                            "string": "\u661f\u6cb3\u6e7e",
                            "url": "http:\/\/gz.lianjia.com\/zufang\/c2111103316631\/"
                        }, {
                            "string": "\u96c5\u5c45\u4e50\u82b1\u56ed",
                            "url": "http:\/\/gz.lianjia.com\/zufang\/c2111103316648\/"
                        }, {
                            "string": "\u6653\u6e2f\u6e7e",
                            "url": "http:\/\/gz.lianjia.com\/zufang\/c2111103317137\/"
                        }, {
                            "string": "5\u53f7\u7ebf\u79df\u623f",
                            "url": "http:\/\/gz.lianjia.com\/ditiezufang\/li110460685\/"
                        }, {
                            "string": "2\u53f7\u7ebf\u79df\u623f",
                            "url": "http:\/\/gz.lianjia.com\/ditiezufang\/li110460680\/"
                        }],
                        "tips": "\u8bf7\u8f93\u5165\u533a\u57df\u3001\u5546\u5708\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"
                    }
                }, {
                    "name": "\u7ecf\u7eaa\u4eba",
                    "action": "jingjiren",
                    "channel": "jingjiren",
                    "checked": 0,
                    "tipsHot": {
                        "query": [],
                        "tips": "\u8bf7\u8f93\u5165\u5546\u5708\u3001\u5c0f\u533a\u6216\u7ecf\u7eaa\u4eba\u7684\u59d3\u540d\u3001\u7535\u8bdd..."
                    }
                }],
                curChannel: 'ershoufang'
            };
        </script>
        <div class="m-filter">
            <div class="position">
                <dl>
                    <h2>
                        <dt title="广州在售位置">位置</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/" id="areaTab" class="selected" title="广州二手房">
                            区域<span class="arrow"></span>
                        </a>
                        <a href="/ditiefang/" id="subwayTab" title="广州地铁找房">
                            地铁线<span class="arrow"></span>
                        </a>
                    </dd>
                </dl>
                <dl>
                    <dt></dt>
                    <dd>
                        <!-- 区域 -->
                        <div data-role="ershoufang">
                            <div>
                                <a href="/ershoufang/tianhe/" title="广州天河在售二手房 ">天河</a>
                                <a href="/ershoufang/yuexiu/" title="广州越秀在售二手房 ">越秀</a>
                                <a href="/ershoufang/liwan/" title="广州荔湾在售二手房 ">荔湾</a>
                                <a href="/ershoufang/haizhu/" title="广州海珠在售二手房 ">海珠</a>
                                <a href="/ershoufang/panyu/" title="广州番禺在售二手房 ">番禺</a>
                                <a href="/ershoufang/baiyun/" title="广州白云在售二手房 ">白云</a>
                                <a href="/ershoufang/huangpugz/" title="广州黄埔在售二手房 ">黄埔</a>
                                <a href="/ershoufang/conghua/" title="广州从化在售二手房 ">从化</a>
                                <a href="/ershoufang/zengcheng/" title="广州增城在售二手房 ">增城</a>
                                <a href="/ershoufang/huadou/" title="广州花都在售二手房 ">花都</a>
                                <a href="/ershoufang/nansha/" title="广州南沙在售二手房 ">南沙</a>
                            </div>
                        </div>
                        <!-- 地铁 -->
                        <div data-role="ditiefang" style="display:none;">
                            <div>
                                <a href="/ditiefang/li110460679/" title="广州1号线在售二手房 ">1号线</a>
                                <a href="/ditiefang/li110460680/" title="广州2号线在售二手房 ">2号线</a>
                                <a href="/ditiefang/li110460681/" title="广州3号线在售二手房 ">3号线</a>
                                <a href="/ditiefang/li110460684/" title="广州3号线北延段在售二手房 ">3号线北延段</a>
                                <a href="/ditiefang/li110460682/" title="广州4号线在售二手房 ">4号线</a>
                                <a href="/ditiefang/li110460685/" title="广州5号线在售二手房 ">5号线</a>
                                <a href="/ditiefang/li110460683/" title="广州6号线在售二手房 ">6号线</a>
                                <a href="/ditiefang/li2116865044761163/" title="广州7号线在售二手房 ">7号线</a>
                                <a href="/ditiefang/li110460686/" title="广州8号线在售二手房 ">8号线</a>
                                <a href="/ditiefang/li110460688/" title="广州apm线在售二手房 ">apm线</a>
                                <a href="/ditiefang/li110460687/" title="广州广佛线在售二手房 ">广佛线</a>
                            </div>
                        </div>
                        <!-- 学区 -->
                    </dd>
                </dl>
            </div>
        
            <div class="list-more">
                <dl class=" hasmore">
                    <h2>
                        <dt title="广州售价在售二手房">售价</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/p1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">100万以下</span>
                        </a>
                        <a href="/ershoufang/p2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">100-120万</span>
                        </a>
                        <a href="/ershoufang/p3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">120-150万</span>
                        </a>
                        <a href="/ershoufang/p4/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">150-200万</span>
                        </a>
                        <a href="/ershoufang/p5/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">200-300万</span>
                        </a>
                        <a href="/ershoufang/p6/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">300-500万</span>
                        </a>
                        <a href="/ershoufang/p7/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">500万以上</span>
                        </a>
                        <span class="customFilter mt" data-role="price">
                        <input type="text" role="minValue" value="">
                        <span>-</span>
                        <input type="text" role="maxValue" value="">&nbsp;
                                          <span>万</span>
                                        <button class="btn-range hide" data-url="/ershoufang/bp{min}ep{max}/">确定</button>
                      </span>
                        <span class="btn-showmore">+ 更多及自定义</span>
                    </dd>
                </dl>
                <dl class=" hasmore">
                    <h2>
                        <dt title="广州面积在售二手房">面积</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/a1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">40平以下</span>
                        </a>
                        <a href="/ershoufang/a2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">40-60平</span>
                        </a>
                        <a href="/ershoufang/a3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">60-80平</span>
                        </a>
                        <a href="/ershoufang/a4/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">80-100平</span>
                        </a>
                        <a href="/ershoufang/a5/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">100-120平</span>
                        </a>
                        <a href="/ershoufang/a6/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">120-144平</span>
                        </a>
                        <a href="/ershoufang/a7/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">144平以上</span>
                        </a>
                        <span class="customFilter mt" data-role="area">
                        <input type="text" role="minValue" value="">
                        <span>-</span>
                        <input type="text" role="maxValue" value="">&nbsp;
                                          <span>平</span>
                                        <button class="btn-range hide" data-url="/ershoufang/ba{min}ea{max}/">确定</button>
                      </span>
                        <span class="btn-showmore">+ 更多及自定义</span>
                    </dd>
                </dl>
                <dl class=" ">
                    <h2>
                        <dt title="广州房型在售二手房">房型</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/l1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">一室</span>
                        </a>
                        <a href="/ershoufang/l2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">二室</span>
                        </a>
                        <a href="/ershoufang/l3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">三室</span>
                        </a>
                        <a href="/ershoufang/l4/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">四室</span>
                        </a>
                        <a href="/ershoufang/l5/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">五室</span>
                        </a>
                        <a href="/ershoufang/l6/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">五室以上</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州用途在售二手房">用途</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/sf1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">普通住宅</span>
                        </a>
                        <a href="/ershoufang/sf2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">商住两用</span>
                        </a>
                        <a href="/ershoufang/sf3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">别墅</span>
                        </a>
                        <a href="/ershoufang/sf4/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">四合院</span>
                        </a>
                        <a href="/ershoufang/sf5/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">其他</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州权属在售二手房">权属</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/dp1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">商品房</span>
                        </a>
                        <a href="/ershoufang/dp2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">公房</span>
                        </a>
                        <a href="/ershoufang/dp3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">经适房</span>
                        </a>
                        <a href="/ershoufang/dp4/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">其他</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州楼层在售二手房">楼层</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/lc1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">低楼层</span>
                        </a>
                        <a href="/ershoufang/lc2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">中楼层</span>
                        </a>
                        <a href="/ershoufang/lc3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">高楼层</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州朝向在售二手房">朝向</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/f1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">朝东</span>
                        </a>
                        <a href="/ershoufang/f2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">朝南</span>
                        </a>
                        <a href="/ershoufang/f3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">朝西</span>
                        </a>
                        <a href="/ershoufang/f4/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">朝北</span>
                        </a>
                        <a href="/ershoufang/f5/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">南北</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州楼龄在售二手房">楼龄</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/y1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">5年以内</span>
                        </a>
                        <a href="/ershoufang/y2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">10年以内</span>
                        </a>
                        <a href="/ershoufang/y3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">15年以内</span>
                        </a>
                        <a href="/ershoufang/y4/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">20年以内</span>
                        </a>
                        <a href="/ershoufang/y5/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">20年以上</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州类型在售二手房">类型</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/bt1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">塔楼</span>
                        </a>
                        <a href="/ershoufang/bt2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">板楼</span>
                        </a>
                        <a href="/ershoufang/bt3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">板塔结合</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州电梯在售二手房">电梯</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/ie2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">有电梯</span>
                        </a>
                        <a href="/ershoufang/ie1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">无电梯</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide " data-role="hide-row">
                    <h2>
                        <dt title="广州装修在售二手房">装修</dt>
                    </h2>
                    <dd>
                        <a href="/ershoufang/de1/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">精装修</span>
                        </a>
                        <a href="/ershoufang/de2/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">普通装修</span>
                        </a>
                        <a href="/ershoufang/de3/" class="" rel="nofollow">
                            <span class="checkbox "></span>
                            <span class="name">毛坯房</span>
                        </a>
                    </dd>
                </dl>
                <dl class="hide otherItem" data-role="hide-row">
                    <dt class="other">其他</dt>
                    <dd>
                        <form id="otherSearchForm">
                            <input class="inp-search" type="text" value="" placeholder="在结果中搜索">
                            <button type="submit" class="btn-search">确定</button>
                        </form>
                    </dd>
                </dl>
            </div>
            <div class="more btn-more">更多选项<span class="arrow"></span></div>
        </div>
        <div class="content "><!-- 左侧内容 -->
            <div class="leftContent">
                <div class="orderFilter">
                    <div class="orderTag">
                        <ul>
                            <li class='selected'><h3><a href="/ershoufang/">默认排序</span></a></h3></li>
                            <li><h3><a href="/ershoufang/co32/">最新</span></a></h3></li>
                            <li><h3><a href="/ershoufang/co21/">总价</a></h3></li>
                            <li><h3><a href="/ershoufang/co41/">房屋单价</a></h3></li>
                            <li><h3><a href="/ershoufang/co11/">面积</a></h3></li>
                            <li><h3><a href="/ershoufang/co52/">带看较多</span></a></h3></li>
                        </ul>
                        <div class="orderType" id="switchView"><span class="list" title="列表模式"></span><span class="img"
                                                                                                            title="大图模式"></span>
                        </div>
                    </div>
                    <div class="filterAgain">
                        <div class="title">筛选：</div>
                        <ul>
                            <li><h3><a href="/ershoufang/ty1/"><span class="checkbox"></span>满两年</a></h3></li>
                            <li><h3><a href="/ershoufang/mw1/"><span class="checkbox"></span>满五年</a></h3></li>
                            <li><h3><a href="/ershoufang/tt2/"><span class="checkbox"></span>新上</a></h3></li>
                            <li>
                                <h3><a href="/ershoufang/tt4/"><span class="checkbox"></span>随时看房
                                    <div class="info"><i></i>
                                        <div class="infoContent min-wid">经纪人持有该房源钥匙，您可以随时预约看房</div>
                                    </div>
                                </a></h3>
                            </li>
                            <li><h3><a href="/ershoufang/hu1/"><span class="checkbox"></span>不看商业类</a></h3></li>
                            <li><h3><a href="/ershoufang/nb1/"><span class="checkbox"></span>不看地下室</a></h3></li>
                            <li><h3><a href="/ershoufang/ng1/"><span class="checkbox"></span>不看车位</a></h3></li>
                        </ul>
                    </div>
                </div>
                <div class="resultDes clear"><h2 class="total fl">共找到<span> 14338 </span>套广州二手房</h2>
                    <div class="button fr"></div>
                </div>
                <div id="newAddHouseContainer"></div>
                <div class="listContentLine"></div>
                <ul class="sellListContent" log-mod="list">
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003046161.html" target="_blank"
                                         data-log_index="1" data-el="ershoufang" data-housecode="GZ0003046161" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15064922588699_3635136054_10.jpg.280x210.jpg.232x174.jpg"
                                                         alt="豪景花园 采光好 格局方正"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003046161.html"
                                                  target="_blank" data-log_index="1" data-el="ershoufang"
                                                  data-housecode="GZ0003046161" data-is_focus="" data-sl="">豪景花园 采光好 格局方正</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103317018/ershoufang.html" target="_blank" data-log_index="1"
                                        data-el="region">豪景花园 </a> | 4室1厅 | 106.21平米 | 东 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共19层)2007年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/yueken/ershoufang.html" target="_blank">粤垦</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>30人关注 / 共17次带看 / 1个月以前发布</div>
                            <div class="tag"><span class="subway">距离6号线天平架站861米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>370</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003046161" data-rid="2111103317018" data-price="34837">
                                    <span>单价34837元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003046161"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003046161" log-mod="GZ0003046161"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003039466.html" target="_blank"
                                         data-log_index="2" data-el="ershoufang" data-housecode="GZ0003039466" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15063068002098_1546536019_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="华南碧桂园 翠云山 六米阳光"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003039466.html"
                                                  target="_blank" data-log_index="2" data-el="ershoufang"
                                                  data-housecode="GZ0003039466" data-is_focus="" data-sl="">华南碧桂园 翠云山 六米阳光</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238336866/ershoufang.html" target="_blank"
                                        data-log_index="2" data-el="region">华南碧桂园翠云山 </a> | 3室2厅 | 110平米 | 北 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共18层)2001年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/huanan1/ershoufang.html" target="_blank">华南</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>25人关注 / 共37次带看 / 1个月以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>328</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003039466" data-rid="2110343238336866" data-price="29819">
                                    <span>单价29819元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003039466"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003039466" log-mod="GZ0003039466"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003036437.html" target="_blank"
                                         data-log_index="3" data-el="ershoufang" data-housecode="GZ0003036437" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15071932585910_4274381609_9.jpg.280x210.jpg.232x174.jpg"
                                                         alt="万科城市花园 小三房 方正实用 带花园"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003036437.html"
                                                  target="_blank" data-log_index="3" data-el="ershoufang"
                                                  data-housecode="GZ0003036437" data-is_focus="" data-sl="">万科城市花园 小三房 方正实用
                                带花园</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103319400/ershoufang.html" target="_blank" data-log_index="3"
                                        data-el="region">万科城市花园 </a> | 3室2厅 | 92平米 | 东南 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共18层)2003年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/qufu/ershoufang.html" target="_blank">区府</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>43人关注 / 共41次带看 / 3个月以前发布</div>
                            <div class="tag"><span class="subway">距离5号线文冲站791米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>335</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003036437" data-rid="2111103319400" data-price="36414">
                                    <span>单价36414元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003036437"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003036437" log-mod="GZ0003036437"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002550957.html" target="_blank"
                                         data-log_index="4" data-el="ershoufang" data-housecode="GZ0002550957" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15049153960030_4082207787_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="珠江帝景苑克莱公寓 高层五房 业主诚心售"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002550957.html"
                                                  target="_blank" data-log_index="4" data-el="ershoufang"
                                                  data-housecode="GZ0002550957" data-is_focus="" data-sl="">珠江帝景苑克莱公寓 高层五房
                                业主诚心售</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238861344/ershoufang.html" target="_blank"
                                        data-log_index="4" data-el="region">珠江帝景苑克莱国际公寓灏景轩 </a> | 5室3厅 | 238平米 | 西 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共32层)2007年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/chigang/ershoufang.html" target="_blank">赤岗</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>176人关注 / 共146次带看 / 一年前发布</div>
                            <div class="tag"><span class="subway">距离3号线广州塔站801米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>1500</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002550957" data-rid="2110343238861344" data-price="63026">
                                    <span>单价63026元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002550957"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002550957" log-mod="GZ0002550957"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002235949.html" target="_blank"
                                         data-log_index="5" data-el="ershoufang" data-housecode="GZ0002235949" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15054598163237_3604462117_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="南向 三房 全新装修 即买即住"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002235949.html"
                                                  target="_blank" data-log_index="5" data-el="ershoufang"
                                                  data-housecode="GZ0002235949" data-is_focus="" data-sl="">南向 三房 全新装修 即买即住</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103318219/ershoufang.html" target="_blank" data-log_index="5"
                                        data-el="region">方圆月岛 </a> | 3室2厅 | 133平米 | 南 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共46层)2009年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/zhujiangxinchengzhong/ershoufang.html"
                                        target="_blank">珠江新城中</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>257人关注 / 共374次带看 / 一年前发布</div>
                            <div class="tag"><span class="subway">距离5号线猎德站277米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>1236.9</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002235949" data-rid="2111103318219" data-price="93000">
                                    <span>单价93000元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002235949"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002235949" log-mod="GZ0002235949"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003039386.html" target="_blank"
                                         data-log_index="6" data-el="ershoufang" data-housecode="GZ0003039386" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15063904373605_1404126879_8.jpg.280x210.jpg.232x174.jpg"
                                                         alt="侨源山庄 电梯三房两卫 环境优美舒适"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003039386.html"
                                                  target="_blank" data-log_index="6" data-el="ershoufang"
                                                  data-housecode="GZ0003039386" data-is_focus="" data-sl="">侨源山庄 电梯三房两卫
                                环境优美舒适</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238599319/ershoufang.html" target="_blank"
                                        data-log_index="6" data-el="region">侨源山庄雅侨楼 </a> | 3室2厅 | 86.7平米 | 东 | 简装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共9层)1998年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/yueken/ershoufang.html" target="_blank">粤垦</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>21人关注 / 共19次带看 / 1个月以前发布</div>
                            <div class="tag"><span class="subway">距离6号线燕塘站917米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>330</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003039386" data-rid="2110343238599319" data-price="38063">
                                    <span>单价38063元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003039386"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003039386" log-mod="GZ0003039386"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003095769.html" target="_blank"
                                         data-log_index="7" data-el="ershoufang" data-housecode="GZ0003095769" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15075167295421_1624133473_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="华南碧桂园 装修保养好 望花园单位"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003095769.html"
                                                  target="_blank" data-log_index="7" data-el="ershoufang"
                                                  data-housecode="GZ0003095769" data-is_focus="" data-sl="">华南碧桂园 装修保养好
                                望花园单位</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238599480/ershoufang.html" target="_blank"
                                        data-log_index="7" data-el="region">华南碧桂园芳翠苑 </a> | 3室2厅 | 107平米 | 北 | 简装
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共7层)2001年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/huanan1/ershoufang.html" target="_blank">华南</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>7人关注 / 共19次带看 / 21天以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>320</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003095769" data-rid="2110343238599480" data-price="29907">
                                    <span>单价29907元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003095769"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003095769" log-mod="GZ0003095769"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003124674.html" target="_blank"
                                         data-log_index="8" data-el="ershoufang" data-housecode="GZ0003124674" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15072608765325_3902805584_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="锦绣生态园菁华轩 大两房出售"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003124674.html"
                                                  target="_blank" data-log_index="8" data-el="ershoufang"
                                                  data-housecode="GZ0003124674" data-is_focus="" data-sl="">锦绣生态园菁华轩
                                大两房出售</a><span class="new tagBlock">新上</span></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238860898/ershoufang.html" target="_blank"
                                        data-log_index="8" data-el="region">锦绣生态园菁华轩 </a> | 2室2厅 | 71平米 | 西北 | 其他
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共6层)2001年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/zhongcun/ershoufang.html" target="_blank">钟村</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>34人关注 / 共13次带看 / 4天以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>150</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003124674" data-rid="2110343238860898" data-price="21127">
                                    <span>单价21127元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003124674"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003124674" log-mod="GZ0003124674"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002839515.html" target="_blank"
                                         data-log_index="9" data-el="ershoufang" data-housecode="GZ0002839515" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15059670313675_1144949460_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="芳草园 精装三房 大型花园小区 安静"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002839515.html"
                                                  target="_blank" data-log_index="9" data-el="ershoufang"
                                                  data-housecode="GZ0002839515" data-is_focus="" data-sl="">芳草园 精装三房 大型花园小区
                                安静</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238337003/ershoufang.html" target="_blank"
                                        data-log_index="9" data-el="region">芳草园A区 </a> | 3室2厅 | 117.05平米 | 北 | 简装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共30层)2004年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/tianhebei/ershoufang.html" target="_blank">天河北</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>42人关注 / 共45次带看 / 3个月以前发布</div>
                            <div class="tag"><span class="subway">距离3号线华师站899米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>850</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002839515" data-rid="2110343238337003" data-price="72619">
                                    <span>单价72619元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002839515"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002839515" log-mod="GZ0002839515"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002716501.html" target="_blank"
                                         data-log_index="10" data-el="ershoufang" data-housecode="GZ0002716501" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15075937630086_2045152478_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="一尺山居高层三房 过五年住房"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002716501.html"
                                                  target="_blank" data-log_index="10" data-el="ershoufang"
                                                  data-housecode="GZ0002716501" data-is_focus="" data-sl="">一尺山居高层三房 过五年住房</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238861405/ershoufang.html" target="_blank"
                                        data-log_index="10" data-el="region">广州雅居乐花园一尺山居 </a> | 3室2厅 | 100平米 | 西南 | 精装
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共23层)2010年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/huanan1/ershoufang.html" target="_blank">华南</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>231人关注 / 共162次带看 / 一年前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>370</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002716501" data-rid="2110343238861405" data-price="37000">
                                    <span>单价37000元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002716501"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002716501" log-mod="GZ0002716501"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003120690.html" target="_blank"
                                         data-log_index="11" data-el="ershoufang" data-housecode="GZ0003120690" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15074452071424_276707174_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="东华花园 实用三房 楼梯房"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003120690.html"
                                                  target="_blank" data-log_index="11" data-el="ershoufang"
                                                  data-housecode="GZ0003120690" data-is_focus="" data-sl="">东华花园 实用三房 楼梯房</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103317784/ershoufang.html" target="_blank" data-log_index="11"
                                        data-el="region">东华花园 </a> | 3室2厅 | 89.83平米 | 东北 | 其他
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共6层)2004年建板楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/shiqiao1/ershoufang.html" target="_blank">市桥</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>31人关注 / 共14次带看 / 7天以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>216</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003120690" data-rid="2111103317784" data-price="24046">
                                    <span>单价24046元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003120690"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003120690" log-mod="GZ0003120690"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003118304.html" target="_blank"
                                         data-log_index="12" data-el="ershoufang" data-housecode="GZ0003118304" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15068527485452_4226758728_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="云苑新村 精装两房 电梯中层"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003118304.html"
                                                  target="_blank" data-log_index="12" data-el="ershoufang"
                                                  data-housecode="GZ0003118304" data-is_focus="" data-sl="">云苑新村 精装两房 电梯中层</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238337411/ershoufang.html" target="_blank"
                                        data-log_index="12" data-el="region">广园云苑新村云苑一街 </a> | 2室1厅 | 75.52平米 | 南 北 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共9层)1999年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/guangyuanlu/ershoufang.html" target="_blank">广园路</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>12人关注 / 共13次带看 / 9天以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>250</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003118304" data-rid="2110343238337411" data-price="33104">
                                    <span>单价33104元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003118304"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003118304" log-mod="GZ0003118304"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003095718.html" target="_blank"
                                         data-log_index="13" data-el="ershoufang" data-housecode="GZ0003095718" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15070859735228_3898183923_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="金道花园 温馨电梯两房 配套完善"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003095718.html"
                                                  target="_blank" data-log_index="13" data-el="ershoufang"
                                                  data-housecode="GZ0003095718" data-is_focus="" data-sl="">金道花园 温馨电梯两房 配套完善</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238860941/ershoufang.html" target="_blank"
                                        data-log_index="13" data-el="region">金道花园金光大街 </a> | 2室2厅 | 76.73平米 | 西北 | 其他 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共22层)2000年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/hedong1/ershoufang.html" target="_blank">鹤洞</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>26人关注 / 共20次带看 / 18天以前发布</div>
                            <div class="tag"><span class="subway">距离1号线西朗站458米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>228</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003095718" data-rid="2110343238860941" data-price="29715">
                                    <span>单价29715元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003095718"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003095718" log-mod="GZ0003095718"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002243262.html" target="_blank"
                                         data-log_index="14" data-el="ershoufang" data-housecode="GZ0002243262" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15059608286235_2344523344_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="旭景家园 温馨三房 安静望花园"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002243262.html"
                                                  target="_blank" data-log_index="14" data-el="ershoufang"
                                                  data-housecode="GZ0002243262" data-is_focus="" data-sl="">旭景家园 温馨三房 安静望花园</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238336991/ershoufang.html" target="_blank"
                                        data-log_index="14" data-el="region">旭景家园A区 </a> | 3室2厅 | 83.51平米 | 东 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共15层)2002年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/dongpu/ershoufang.html" target="_blank">东圃</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>407人关注 / 共261次带看 / 一年前发布</div>
                            <div class="tag"><span class="subway">距离4号线车陂站0米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>320</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002243262" data-rid="2110343238336991" data-price="38319">
                                    <span>单价38319元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002243262"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002243262" log-mod="GZ0002243262"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003110306.html" target="_blank"
                                         data-log_index="15" data-el="ershoufang" data-housecode="GZ0003110306" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15067496664172_819370801_8.jpg.280x210.jpg.232x174.jpg"
                                                         alt="翠湖山庄 东向望花园 户型方正 满五一套"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003110306.html"
                                                  target="_blank" data-log_index="15" data-el="ershoufang"
                                                  data-housecode="GZ0003110306" data-is_focus="" data-sl="">翠湖山庄 东向望花园 户型方正
                                满五一套</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103316919/ershoufang.html" target="_blank" data-log_index="15"
                                        data-el="region">翠湖山庄 </a> | 3室2厅 | 132.8平米 | 东北 | 其他 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共17层)1999年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/tianhegongyuan/ershoufang.html" target="_blank">天河公园</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>9人关注 / 共7次带看 / 13天以前发布</div>
                            <div class="tag"><span class="subway">距离5号线科韵路站0米</span><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>608</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003110306" data-rid="2111103316919" data-price="45784">
                                    <span>单价45784元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003110306"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003110306" log-mod="GZ0003110306"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003134466.html" target="_blank"
                                         data-log_index="16" data-el="ershoufang" data-housecode="GZ0003134466" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15075361725236_2154835435_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="康裕园 装修保养好  南向三房"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003134466.html"
                                                  target="_blank" data-log_index="16" data-el="ershoufang"
                                                  data-housecode="GZ0003134466" data-is_focus="" data-sl="">康裕园 装修保养好
                                南向三房</a><span class="new tagBlock">新上</span></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238599658/ershoufang.html" target="_blank"
                                        data-log_index="16" data-el="region">康裕园十街 </a> | 3室2厅 | 94平米 | 南 | 精装 | 无电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共7层)1993年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/shiqiao1/ershoufang.html" target="_blank">市桥</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>2人关注 / 共14次带看 / 4天以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>215</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003134466" data-rid="2110343238599658" data-price="22873">
                                    <span>单价22873元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003134466"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003134466" log-mod="GZ0003134466"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003020216.html" target="_blank"
                                         data-log_index="17" data-el="ershoufang" data-housecode="GZ0003020216" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15059520280054_1261460881_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="怡港花园 东南向大三房 高层"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003020216.html"
                                                  target="_blank" data-log_index="17" data-el="ershoufang"
                                                  data-housecode="GZ0003020216" data-is_focus="" data-sl="">怡港花园 东南向大三房 高层</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238861055/ershoufang.html" target="_blank"
                                        data-log_index="17" data-el="region">怡港花园怡康楼 </a> | 3室2厅 | 105.77平米 | 东南 | 其他 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共17层)1999年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/qufu/ershoufang.html" target="_blank">区府</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>0人关注 / 共18次带看 / 2个月以前发布</div>
                            <div class="tag"><span class="subway">距离5号线大沙地站930米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>472</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003020216" data-rid="2110343238861055" data-price="44626">
                                    <span>单价44626元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003020216"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003020216" log-mod="GZ0003020216"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003030524.html" target="_blank"
                                         data-log_index="18" data-el="ershoufang" data-housecode="GZ0003030524" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15072480680304_1108727891_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="郎晴居二期 高层南向望江 全景无遮挡"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003030524.html"
                                                  target="_blank" data-log_index="18" data-el="ershoufang"
                                                  data-housecode="GZ0003030524" data-is_focus="" data-sl="">郎晴居二期 高层南向望江
                                全景无遮挡</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238336809/ershoufang.html" target="_blank"
                                        data-log_index="18" data-el="region">朗晴居二期 </a> | 3室2厅 | 96.61平米 | 南 | 其他 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共32层)2000年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/binjiangzhong/ershoufang.html" target="_blank">滨江中</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>46人关注 / 共22次带看 / 1个月以前发布</div>
                            <div class="tag"><span class="subway">距离2号线市二宫站901米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>530</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003030524" data-rid="2110343238336809" data-price="54860">
                                    <span>单价54860元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003030524"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003030524" log-mod="GZ0003030524"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002722805.html" target="_blank"
                                         data-log_index="19" data-el="ershoufang" data-housecode="GZ0002722805" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15061443356763_3297881531_2.jpg.280x210.jpg.232x174.jpg"
                                                         alt="聚德花园 2000年楼龄 南向电梯两房"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002722805.html"
                                                  target="_blank" data-log_index="19" data-el="ershoufang"
                                                  data-housecode="GZ0002722805" data-is_focus="" data-sl="">聚德花园 2000年楼龄
                                南向电梯两房</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103317803/ershoufang.html" target="_blank" data-log_index="19"
                                        data-el="region">聚德花园 </a> | 2室1厅 | 60.5平米 | 南 | 其他 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共9层)1997年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/chigang/ershoufang.html" target="_blank">赤岗</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>247人关注 / 共122次带看 / 5个月以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>220</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002722805" data-rid="2111103317803" data-price="36364">
                                    <span>单价36364元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002722805"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002722805" log-mod="GZ0002722805"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003082596.html" target="_blank"
                                         data-log_index="20" data-el="ershoufang" data-housecode="GZ0003082596" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15058841456454_1054810473_4.jpg.280x210.jpg.232x174.jpg"
                                                         alt="白云明珠广场 新精装修 房入房两房 总价"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003082596.html"
                                                  target="_blank" data-log_index="20" data-el="ershoufang"
                                                  data-housecode="GZ0003082596" data-is_focus="" data-sl="">白云明珠广场 新精装修 房入房两房
                                总价</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103831540/ershoufang.html" target="_blank" data-log_index="20"
                                        data-el="region">机场路华明街白云明珠广场 </a> | 2室1厅 | 48.27平米 | 北 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共14层)1996年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/jichanglu/ershoufang.html" target="_blank">机场路</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>20人关注 / 共44次带看 / 11个月以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>160</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003082596" data-rid="2111103831540" data-price="33147">
                                    <span>单价33147元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003082596"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003082596" log-mod="GZ0003082596"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002641636.html" target="_blank"
                                         data-log_index="21" data-el="ershoufang" data-housecode="GZ0002641636" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15061445444671_2045145643_5.jpg.280x210.jpg.232x174.jpg"
                                                         alt="金碧花园三期 安静望花园 户型好 地铁口"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002641636.html"
                                                  target="_blank" data-log_index="21" data-el="ershoufang"
                                                  data-housecode="GZ0002641636" data-is_focus="" data-sl="">金碧花园三期 安静望花园 户型好
                                地铁口</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238860931/ershoufang.html" target="_blank"
                                        data-log_index="21" data-el="region">金碧花园第三金碧 </a> | 3室2厅 | 104平米 | 北 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共32层)2000年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/jinbi/ershoufang.html" target="_blank">金碧</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>45人关注 / 共19次带看 / 一年前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>470</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002641636" data-rid="2110343238860931" data-price="45193">
                                    <span>单价45193元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002641636"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002641636" log-mod="GZ0002641636"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003119717.html" target="_blank"
                                         data-log_index="22" data-el="ershoufang" data-housecode="GZ0003119717" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15071733425803_756564045_2.jpg.280x210.jpg.232x174.jpg"
                                                         alt="侨怡苑 电梯两房 配套完善"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003119717.html"
                                                  target="_blank" data-log_index="22" data-el="ershoufang"
                                                  data-housecode="GZ0003119717" data-is_focus="" data-sl="">侨怡苑 电梯两房 配套完善</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103317324/ershoufang.html" target="_blank" data-log_index="22"
                                        data-el="region">侨怡苑 </a> | 2室2厅 | 97.36平米 | 北 | 简装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共21层)1992年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/tiyuzhongxin/ershoufang.html" target="_blank">体育中心</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>4人关注 / 共8次带看 / 8天以前发布</div>
                            <div class="tag"><span class="subway">距离3号线北延段林和西站563米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>560</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003119717" data-rid="2111103317324" data-price="57519">
                                    <span>单价57519元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003119717"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003119717" log-mod="GZ0003119717"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002876762.html" target="_blank"
                                         data-log_index="23" data-el="ershoufang" data-housecode="GZ0002876762" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15075196101200_1740456339_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="江南新村 户型方正 交通方便"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002876762.html"
                                                  target="_blank" data-log_index="23" data-el="ershoufang"
                                                  data-housecode="GZ0002876762" data-is_focus="" data-sl="">江南新村 户型方正 交通方便</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238337180/ershoufang.html" target="_blank"
                                        data-log_index="23" data-el="region">江南新村2街 </a> | 2室2厅 | 73.89平米 | 西 | 其他
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共7层)1998年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/shiqiao1/ershoufang.html" target="_blank">市桥</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>282人关注 / 共65次带看 / 2个月以前发布</div>
                            <div class="tag"><span class="subway">距离3号线市桥站1056米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>123</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002876762" data-rid="2110343238337180" data-price="16647">
                                    <span>单价16647元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002876762"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002876762" log-mod="GZ0002876762"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002889862.html" target="_blank"
                                         data-log_index="24" data-el="ershoufang" data-housecode="GZ0002889862" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15073455492846_186427962_4.jpg.280x210.jpg.232x174.jpg"
                                                         alt="下塘西路 大院管理 实用两房"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002889862.html"
                                                  target="_blank" data-log_index="24" data-el="ershoufang"
                                                  data-housecode="GZ0002889862" data-is_focus="" data-sl="">下塘西路 大院管理 实用两房</a>
                            </div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103831612/ershoufang.html" target="_blank" data-log_index="24"
                                        data-el="region">下塘西路 </a> | 2室1厅 | 58平米 | 东南 | 简装
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>高楼层(共9层)1993年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/lujing/ershoufang.html" target="_blank">麓景</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>6人关注 / 共21次带看 / 3个月以前发布</div>
                            <div class="tag"><span class="subway">距离5号线小北站612米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>190</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002889862" data-rid="2111103831612" data-price="32759">
                                    <span>单价32759元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002889862"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002889862" log-mod="GZ0002889862"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003002081.html" target="_blank"
                                         data-log_index="25" data-el="ershoufang" data-housecode="GZ0003002081" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15052097305865_451519294_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="协和新世界 正宗的一房一厅 花园小区"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003002081.html"
                                                  target="_blank" data-log_index="25" data-el="ershoufang"
                                                  data-housecode="GZ0003002081" data-is_focus="" data-sl="">协和新世界 正宗的一房一厅
                                花园小区</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103319393/ershoufang.html" target="_blank" data-log_index="25"
                                        data-el="region">协和新世界 </a> | 1室1厅 | 47平米 | 北 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共32层)2008年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/tianhebei/ershoufang.html" target="_blank">天河北</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>23人关注 / 共24次带看 / 1个月以前发布</div>
                            <div class="tag"><span class="subway">距离3号线华师站902米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>360</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003002081" data-rid="2111103319393" data-price="76596">
                                    <span>单价76596元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003002081"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003002081" log-mod="GZ0003002081"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003067932.html" target="_blank"
                                         data-log_index="26" data-el="ershoufang" data-housecode="GZ0003067932" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15058749683053_646047184_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="时代玫瑰园 大三房 南向望花园 厅出阳台"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003067932.html"
                                                  target="_blank" data-log_index="26" data-el="ershoufang"
                                                  data-housecode="GZ0003067932" data-is_focus="" data-sl="">时代玫瑰园 大三房 南向望花园
                                厅出阳台</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103316672/ershoufang.html" target="_blank" data-log_index="26"
                                        data-el="region">时代玫瑰园 </a> | 3室2厅 | 119.97平米 | 南 | 其他 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共16层)2008年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/baiyundadaobei/ershoufang.html" target="_blank">白云大道北</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>22人关注 / 共6次带看 / 25天以前发布</div>
                            <div class="tag"><span class="subway">距离2号线黄边站290米</span><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>490</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003067932" data-rid="2111103316672" data-price="40844">
                                    <span>单价40844元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003067932"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003067932" log-mod="GZ0003067932"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003123281.html" target="_blank"
                                         data-log_index="27" data-el="ershoufang" data-housecode="GZ0003123281" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15075205841071_1251151652_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="赤岗路 格局方正 带入户花园 门口停车"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003123281.html"
                                                  target="_blank" data-log_index="27" data-el="ershoufang"
                                                  data-housecode="GZ0003123281" data-is_focus="" data-sl="">赤岗路 格局方正 带入户花园
                                门口停车</a><span class="new tagBlock">新上</span></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238336869/ershoufang.html" target="_blank"
                                        data-log_index="27" data-el="region">毛纺小区赤岗东三街 </a> | 2室2厅 | 65.87平米 | 南 北 | 精装
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>低楼层(共8层)1990年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/chigang/ershoufang.html" target="_blank">赤岗</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>9人关注 / 共5次带看 / 6天以前发布</div>
                            <div class="tag"><span class="subway">距离8号线赤岗站783米</span><span class="taxfree">房本满五年</span><span
                                    class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>230</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003123281" data-rid="2110343238336869" data-price="34918">
                                    <span>单价34918元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003123281"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003123281" log-mod="GZ0003123281"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003010812.html" target="_blank"
                                         data-log_index="28" data-el="ershoufang" data-housecode="GZ0003010812" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15061444129147_3206384675_1.jpg.280x210.jpg.232x174.jpg"
                                                         alt="自在城市花园 温馨三房 望花园单位"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003010812.html"
                                                  target="_blank" data-log_index="28" data-el="ershoufang"
                                                  data-housecode="GZ0003010812" data-is_focus="" data-sl="">自在城市花园 温馨三房
                                望花园单位</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238337314/ershoufang.html" target="_blank"
                                        data-log_index="28" data-el="region">自在城市花园自在华庭 </a> | 3室2厅 | 104.65平米 | 东北 | 精装 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共10层)2004年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/huanan1/ershoufang.html" target="_blank">华南</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>9人关注 / 共36次带看 / 1个月以前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>310</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003010812" data-rid="2110343238337314" data-price="29623">
                                    <span>单价29623元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003010812"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003010812" log-mod="GZ0003010812"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0003075949.html" target="_blank"
                                         data-log_index="29" data-el="ershoufang" data-housecode="GZ0003075949" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15056983223678_2657937683_5.jpg.280x210.jpg.232x174.jpg"
                                                         alt="云山居 简装三房 东南向 户型方正"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0003075949.html"
                                                  target="_blank" data-log_index="29" data-el="ershoufang"
                                                  data-housecode="GZ0003075949" data-is_focus="" data-sl="">云山居 简装三房 东南向
                                户型方正</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2110343238337239/ershoufang.html" target="_blank"
                                        data-log_index="29" data-el="region">云山居 </a> | 3室2厅 | 102平米 | 东南 | 简装 | 无电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共6层)2000年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/baiyundadaobei/ershoufang.html" target="_blank">白云大道北</a></div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>14人关注 / 共12次带看 / 一年前发布</div>
                            <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>270</span>万</div>
                                <div class="unitPrice" data-hid="GZ0003075949" data-rid="2110343238337239" data-price="26471">
                                    <span>单价26471元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0003075949"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0003075949" log-mod="GZ0003075949"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                    <li class="clear"><a class="img " href="https://gz.lianjia.com/ershoufang/GZ0002989763.html" target="_blank"
                                         data-log_index="30" data-el="ershoufang" data-housecode="GZ0002989763" data-is_focus=""
                                         data-sl=""><img class="lj-lazy"
                                                         src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                         data-original="https://image1.ljcdn.com/mytophomeimg/15067724063730_2843163645_7.jpg.280x210.jpg.232x174.jpg"
                                                         alt="骏逸苑，地铁口，南向三房，诚心放卖"></a>
                        <div class="info clear">
                            <div class="title"><a class="" href="https://gz.lianjia.com/ershoufang/GZ0002989763.html"
                                                  target="_blank" data-log_index="30" data-el="ershoufang"
                                                  data-housecode="GZ0002989763" data-is_focus=""
                                                  data-sl="">骏逸苑，地铁口，南向三房，诚心放卖</a></div>
                            <div class="address">
                                <div class="houseInfo"><span class="houseIcon"></span><a
                                        href="https://gz.lianjia.com/xiaoqu/2111103317024/ershoufang.html" target="_blank" data-log_index="30"
                                        data-el="region">骏逸苑 </a> | 3室2厅 | 107平米 | 南 | 其他 | 有电梯
                                </div>
                            </div>
                            <div class="flood">
                                <div class="positionInfo"><span class="positionIcon"></span>中楼层(共9层)2000年建塔楼 - <a
                                        href="https://gz.lianjia.com/ershoufang/zhujiangxinchengdong/ershoufang.html" target="_blank">珠江新城东</a>
                                </div>
                            </div>
                            <div class="followInfo"><span class="starIcon"></span>35人关注 / 共22次带看 / 1个月以前发布</div>
                            <div class="tag"><span class="subway">距离5号线科韵路站0米</span><span class="taxfree">房本满五年</span></div>
                            <div class="priceInfo">
                                <div class="totalPrice"><span>718</span>万</div>
                                <div class="unitPrice" data-hid="GZ0002989763" data-rid="2111103317024" data-price="67103">
                                    <span>单价67103元/平米</span></div>
                            </div>
                        </div>
                        <div class="listButtonContainer">
                            <div class="btn-follow followBtn" data-hid="GZ0002989763"><span class="follow-text">关注</span></div>
                            <div class="compareBtn LOGCLICK" data-hid="GZ0002989763" log-mod="GZ0002989763"
                                 data-log_evtid="10230">加入对比
                            </div>
                        </div>
                    </li>
                </ul>
                <div class="bigImgList" style="display: none;" log-mod="list">
                    <div class="item" data-houseid="GZ0003046161"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003046161.html"
                                                                     target="_blank" data-bl="list" data-log_index="1"
                                                                     data-housecode="GZ0003046161" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15064922588699_3635136054_10.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003046161"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>370</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003046161.html" target="_blank"
                           data-bl="list" data-log_index="1" data-housecode="GZ0003046161" data-is_focus=""
                           data-el="ershoufang">豪景花园 采光好 格局方正</a>
                        <div class="info">
                            粤垦<span>/</span>4室1厅<span>/</span>106.21平米<span>/</span>东<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离6号线天平架站861米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003039466"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003039466.html"
                                                                     target="_blank" data-bl="list" data-log_index="2"
                                                                     data-housecode="GZ0003039466" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15063068002098_1546536019_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003039466"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>328</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003039466.html" target="_blank"
                           data-bl="list" data-log_index="2" data-housecode="GZ0003039466" data-is_focus=""
                           data-el="ershoufang">华南碧桂园 翠云山 六米阳光</a>
                        <div class="info">华南<span>/</span>3室2厅<span>/</span>110平米<span>/</span>北<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003036437"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003036437.html"
                                                                     target="_blank" data-bl="list" data-log_index="3"
                                                                     data-housecode="GZ0003036437" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15071932585910_4274381609_9.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003036437"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>335</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003036437.html" target="_blank"
                           data-bl="list" data-log_index="3" data-housecode="GZ0003036437" data-is_focus=""
                           data-el="ershoufang">万科城市花园 小三房 方正实用 带花园</a>
                        <div class="info">区府<span>/</span>3室2厅<span>/</span>92平米<span>/</span>东南<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离5号线文冲站791米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002550957"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002550957.html"
                                                                     target="_blank" data-bl="list" data-log_index="4"
                                                                     data-housecode="GZ0002550957" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15049153960030_4082207787_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002550957"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>1500</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002550957.html" target="_blank"
                           data-bl="list" data-log_index="4" data-housecode="GZ0002550957" data-is_focus=""
                           data-el="ershoufang">珠江帝景苑克莱公寓 高层五房 业主诚心售</a>
                        <div class="info">赤岗<span>/</span>5室3厅<span>/</span>238平米<span>/</span>西<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离3号线广州塔站801米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002235949"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002235949.html"
                                                                     target="_blank" data-bl="list" data-log_index="5"
                                                                     data-housecode="GZ0002235949" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15054598163237_3604462117_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002235949"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>1236.9</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002235949.html" target="_blank"
                           data-bl="list" data-log_index="5" data-housecode="GZ0002235949" data-is_focus=""
                           data-el="ershoufang">南向 三房 全新装修 即买即住</a>
                        <div class="info">
                            珠江新城中<span>/</span>3室2厅<span>/</span>133平米<span>/</span>南<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离5号线猎德站277米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003039386"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003039386.html"
                                                                     target="_blank" data-bl="list" data-log_index="6"
                                                                     data-housecode="GZ0003039386" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15063904373605_1404126879_8.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003039386"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>330</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003039386.html" target="_blank"
                           data-bl="list" data-log_index="6" data-housecode="GZ0003039386" data-is_focus=""
                           data-el="ershoufang">侨源山庄 电梯三房两卫 环境优美舒适</a>
                        <div class="info">粤垦<span>/</span>3室2厅<span>/</span>86.7平米<span>/</span>东<span>/</span>简装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离6号线燕塘站917米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003095769"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003095769.html"
                                                                     target="_blank" data-bl="list" data-log_index="7"
                                                                     data-housecode="GZ0003095769" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15075167295421_1624133473_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003095769"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>320</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003095769.html" target="_blank"
                           data-bl="list" data-log_index="7" data-housecode="GZ0003095769" data-is_focus=""
                           data-el="ershoufang">华南碧桂园 装修保养好 望花园单位</a>
                        <div class="info">华南<span>/</span>3室2厅<span>/</span>107平米<span>/</span>北<span>/</span>简装</div>
                        <div class="tag"><span class="taxfree">房本满五年</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003124674"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003124674.html"
                                                                     target="_blank" data-bl="list" data-log_index="8"
                                                                     data-housecode="GZ0003124674" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15072608765325_3902805584_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003124674"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>150</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003124674.html" target="_blank"
                           data-bl="list" data-log_index="8" data-housecode="GZ0003124674" data-is_focus=""
                           data-el="ershoufang">锦绣生态园菁华轩 大两房出售</a>
                        <div class="info">钟村<span>/</span>2室2厅<span>/</span>71平米<span>/</span>西北<span>/</span>其他</div>
                        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002839515"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002839515.html"
                                                                     target="_blank" data-bl="list" data-log_index="9"
                                                                     data-housecode="GZ0002839515" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15059670313675_1144949460_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002839515"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>850</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002839515.html" target="_blank"
                           data-bl="list" data-log_index="9" data-housecode="GZ0002839515" data-is_focus=""
                           data-el="ershoufang">芳草园 精装三房 大型花园小区 安静</a>
                        <div class="info">
                            天河北<span>/</span>3室2厅<span>/</span>117.05平米<span>/</span>北<span>/</span>简装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离3号线华师站899米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002716501"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002716501.html"
                                                                     target="_blank" data-bl="list" data-log_index="10"
                                                                     data-housecode="GZ0002716501" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15075937630086_2045152478_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002716501"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>370</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002716501.html" target="_blank"
                           data-bl="list" data-log_index="10" data-housecode="GZ0002716501" data-is_focus=""
                           data-el="ershoufang">一尺山居高层三房 过五年住房</a>
                        <div class="info">华南<span>/</span>3室2厅<span>/</span>100平米<span>/</span>西南<span>/</span>精装</div>
                        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003120690"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003120690.html"
                                                                     target="_blank" data-bl="list" data-log_index="11"
                                                                     data-housecode="GZ0003120690" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15074452071424_276707174_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003120690"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>216</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003120690.html" target="_blank"
                           data-bl="list" data-log_index="11" data-housecode="GZ0003120690" data-is_focus=""
                           data-el="ershoufang">东华花园 实用三房 楼梯房</a>
                        <div class="info">市桥<span>/</span>3室2厅<span>/</span>89.83平米<span>/</span>东北<span>/</span>其他</div>
                        <div class="tag"><span class="taxfree">房本满五年</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003118304"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003118304.html"
                                                                     target="_blank" data-bl="list" data-log_index="12"
                                                                     data-housecode="GZ0003118304" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15068527485452_4226758728_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003118304"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>250</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003118304.html" target="_blank"
                           data-bl="list" data-log_index="12" data-housecode="GZ0003118304" data-is_focus=""
                           data-el="ershoufang">云苑新村 精装两房 电梯中层</a>
                        <div class="info">广园路<span>/</span>2室1厅<span>/</span>75.52平米<span>/</span>南
                            北<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003095718"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003095718.html"
                                                                     target="_blank" data-bl="list" data-log_index="13"
                                                                     data-housecode="GZ0003095718" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15070859735228_3898183923_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003095718"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>228</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003095718.html" target="_blank"
                           data-bl="list" data-log_index="13" data-housecode="GZ0003095718" data-is_focus=""
                           data-el="ershoufang">金道花园 温馨电梯两房 配套完善</a>
                        <div class="info">
                            鹤洞<span>/</span>2室2厅<span>/</span>76.73平米<span>/</span>西北<span>/</span>其他<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离1号线西朗站458米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002243262"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002243262.html"
                                                                     target="_blank" data-bl="list" data-log_index="14"
                                                                     data-housecode="GZ0002243262" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15059608286235_2344523344_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002243262"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>320</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002243262.html" target="_blank"
                           data-bl="list" data-log_index="14" data-housecode="GZ0002243262" data-is_focus=""
                           data-el="ershoufang">旭景家园 温馨三房 安静望花园</a>
                        <div class="info">东圃<span>/</span>3室2厅<span>/</span>83.51平米<span>/</span>东<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离4号线车陂站0米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003110306"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003110306.html"
                                                                     target="_blank" data-bl="list" data-log_index="15"
                                                                     data-housecode="GZ0003110306" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15067496664172_819370801_8.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003110306"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>608</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003110306.html" target="_blank"
                           data-bl="list" data-log_index="15" data-housecode="GZ0003110306" data-is_focus=""
                           data-el="ershoufang">翠湖山庄 东向望花园 户型方正 满五一套</a>
                        <div class="info">
                            天河公园<span>/</span>3室2厅<span>/</span>132.8平米<span>/</span>东北<span>/</span>其他<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离5号线科韵路站0米</span><span class="taxfree">房本满五年</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003134466"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003134466.html"
                                                                     target="_blank" data-bl="list" data-log_index="16"
                                                                     data-housecode="GZ0003134466" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15075361725236_2154835435_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003134466"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>215</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003134466.html" target="_blank"
                           data-bl="list" data-log_index="16" data-housecode="GZ0003134466" data-is_focus=""
                           data-el="ershoufang">康裕园 装修保养好 南向三房</a>
                        <div class="info">市桥<span>/</span>3室2厅<span>/</span>94平米<span>/</span>南<span>/</span>精装<span>/</span>无电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003020216"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003020216.html"
                                                                     target="_blank" data-bl="list" data-log_index="17"
                                                                     data-housecode="GZ0003020216" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15059520280054_1261460881_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003020216"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>472</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003020216.html" target="_blank"
                           data-bl="list" data-log_index="17" data-housecode="GZ0003020216" data-is_focus=""
                           data-el="ershoufang">怡港花园 东南向大三房 高层</a>
                        <div class="info">
                            区府<span>/</span>3室2厅<span>/</span>105.77平米<span>/</span>东南<span>/</span>其他<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离5号线大沙地站930米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003030524"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003030524.html"
                                                                     target="_blank" data-bl="list" data-log_index="18"
                                                                     data-housecode="GZ0003030524" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15072480680304_1108727891_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003030524"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>530</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003030524.html" target="_blank"
                           data-bl="list" data-log_index="18" data-housecode="GZ0003030524" data-is_focus=""
                           data-el="ershoufang">郎晴居二期 高层南向望江 全景无遮挡</a>
                        <div class="info">
                            滨江中<span>/</span>3室2厅<span>/</span>96.61平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离2号线市二宫站901米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002722805"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002722805.html"
                                                                     target="_blank" data-bl="list" data-log_index="19"
                                                                     data-housecode="GZ0002722805" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15061443356763_3297881531_2.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002722805"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>220</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002722805.html" target="_blank"
                           data-bl="list" data-log_index="19" data-housecode="GZ0002722805" data-is_focus=""
                           data-el="ershoufang">聚德花园 2000年楼龄 南向电梯两房</a>
                        <div class="info">赤岗<span>/</span>2室1厅<span>/</span>60.5平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003082596"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003082596.html"
                                                                     target="_blank" data-bl="list" data-log_index="20"
                                                                     data-housecode="GZ0003082596" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15058841456454_1054810473_4.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003082596"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>160</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003082596.html" target="_blank"
                           data-bl="list" data-log_index="20" data-housecode="GZ0003082596" data-is_focus=""
                           data-el="ershoufang">白云明珠广场 新精装修 房入房两房 总价</a>
                        <div class="info">
                            机场路<span>/</span>2室1厅<span>/</span>48.27平米<span>/</span>北<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002641636"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002641636.html"
                                                                     target="_blank" data-bl="list" data-log_index="21"
                                                                     data-housecode="GZ0002641636" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15061445444671_2045145643_5.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002641636"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>470</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002641636.html" target="_blank"
                           data-bl="list" data-log_index="21" data-housecode="GZ0002641636" data-is_focus=""
                           data-el="ershoufang">金碧花园三期 安静望花园 户型好 地铁口</a>
                        <div class="info">金碧<span>/</span>3室2厅<span>/</span>104平米<span>/</span>北<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003119717"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003119717.html"
                                                                     target="_blank" data-bl="list" data-log_index="22"
                                                                     data-housecode="GZ0003119717" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15071733425803_756564045_2.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003119717"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>560</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003119717.html" target="_blank"
                           data-bl="list" data-log_index="22" data-housecode="GZ0003119717" data-is_focus=""
                           data-el="ershoufang">侨怡苑 电梯两房 配套完善</a>
                        <div class="info">
                            体育中心<span>/</span>2室2厅<span>/</span>97.36平米<span>/</span>北<span>/</span>简装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离3号线北延段林和西站563米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002876762"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002876762.html"
                                                                     target="_blank" data-bl="list" data-log_index="23"
                                                                     data-housecode="GZ0002876762" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15075196101200_1740456339_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002876762"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>123</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002876762.html" target="_blank"
                           data-bl="list" data-log_index="23" data-housecode="GZ0002876762" data-is_focus=""
                           data-el="ershoufang">江南新村 户型方正 交通方便</a>
                        <div class="info">市桥<span>/</span>2室2厅<span>/</span>73.89平米<span>/</span>西<span>/</span>其他</div>
                        <div class="tag"><span class="subway">距离3号线市桥站1056米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002889862"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002889862.html"
                                                                     target="_blank" data-bl="list" data-log_index="24"
                                                                     data-housecode="GZ0002889862" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15073455492846_186427962_4.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002889862"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>190</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002889862.html" target="_blank"
                           data-bl="list" data-log_index="24" data-housecode="GZ0002889862" data-is_focus=""
                           data-el="ershoufang">下塘西路 大院管理 实用两房</a>
                        <div class="info">麓景<span>/</span>2室1厅<span>/</span>58平米<span>/</span>东南<span>/</span>简装</div>
                        <div class="tag"><span class="subway">距离5号线小北站612米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003002081"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003002081.html"
                                                                     target="_blank" data-bl="list" data-log_index="25"
                                                                     data-housecode="GZ0003002081" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15052097305865_451519294_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003002081"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>360</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003002081.html" target="_blank"
                           data-bl="list" data-log_index="25" data-housecode="GZ0003002081" data-is_focus=""
                           data-el="ershoufang">协和新世界 正宗的一房一厅 花园小区</a>
                        <div class="info">天河北<span>/</span>1室1厅<span>/</span>47平米<span>/</span>北<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离3号线华师站902米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003067932"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003067932.html"
                                                                     target="_blank" data-bl="list" data-log_index="26"
                                                                     data-housecode="GZ0003067932" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15058749683053_646047184_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003067932"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>490</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003067932.html" target="_blank"
                           data-bl="list" data-log_index="26" data-housecode="GZ0003067932" data-is_focus=""
                           data-el="ershoufang">时代玫瑰园 大三房 南向望花园 厅出阳台</a>
                        <div class="info">
                            白云大道北<span>/</span>3室2厅<span>/</span>119.97平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离2号线黄边站290米</span><span class="taxfree">房本满五年</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003123281"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003123281.html"
                                                                     target="_blank" data-bl="list" data-log_index="27"
                                                                     data-housecode="GZ0003123281" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15075205841071_1251151652_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003123281"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>230</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003123281.html" target="_blank"
                           data-bl="list" data-log_index="27" data-housecode="GZ0003123281" data-is_focus=""
                           data-el="ershoufang">赤岗路 格局方正 带入户花园 门口停车</a>
                        <div class="info">赤岗<span>/</span>2室2厅<span>/</span>65.87平米<span>/</span>南 北<span>/</span>精装</div>
                        <div class="tag"><span class="subway">距离8号线赤岗站783米</span><span class="taxfree">房本满五年</span><span
                                class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003010812"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003010812.html"
                                                                     target="_blank" data-bl="list" data-log_index="28"
                                                                     data-housecode="GZ0003010812" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15061444129147_3206384675_1.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003010812"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>310</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003010812.html" target="_blank"
                           data-bl="list" data-log_index="28" data-housecode="GZ0003010812" data-is_focus=""
                           data-el="ershoufang">自在城市花园 温馨三房 望花园单位</a>
                        <div class="info">
                            华南<span>/</span>3室2厅<span>/</span>104.65平米<span>/</span>东北<span>/</span>精装<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0003075949"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0003075949.html"
                                                                     target="_blank" data-bl="list" data-log_index="29"
                                                                     data-housecode="GZ0003075949" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15056983223678_2657937683_5.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0003075949"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>270</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0003075949.html" target="_blank"
                           data-bl="list" data-log_index="29" data-housecode="GZ0003075949" data-is_focus=""
                           data-el="ershoufang">云山居 简装三房 东南向 户型方正</a>
                        <div class="info">
                            白云大道北<span>/</span>3室2厅<span>/</span>102平米<span>/</span>东南<span>/</span>简装<span>/</span>无电梯
                        </div>
                        <div class="tag"><span class="taxfree">房本满五年</span><span class="haskey">随时看房</span></div>
                    </div>
                    <div class="item" data-houseid="GZ0002989763"><a class="img"
                                                                     href="https://gz.lianjia.com/ershoufang/GZ0002989763.html"
                                                                     target="_blank" data-bl="list" data-log_index="30"
                                                                     data-housecode="GZ0002989763" data-is_focus=""
                                                                     data-el="ershoufang"><img class="lj-lazy"
                                                                                               src="https://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=201709261333487"
                                                                                               data-original="https://image1.ljcdn.com/mytophomeimg/15067724063730_2843163645_7.jpg.280x210.jpg.437x300.jpg">
                        <div class="btn-follow follow" data-hid="GZ0002989763"><span class="star"></span><span
                                class="follow-text">关注</span></div>
                        <div class="leftArrow"><span></span></div>
                        <div class="rightArrow"><span></span></div>
                        <div class="price"><span>718</span>万</div>
                    </a><a class="title" href="https://gz.lianjia.com/ershoufang/GZ0002989763.html" target="_blank"
                           data-bl="list" data-log_index="30" data-housecode="GZ0002989763" data-is_focus=""
                           data-el="ershoufang">骏逸苑，地铁口，南向三房，诚心放卖</a>
                        <div class="info">
                            珠江新城东<span>/</span>3室2厅<span>/</span>107平米<span>/</span>南<span>/</span>其他<span>/</span>有电梯
                        </div>
                        <div class="tag"><span class="subway">距离5号线科韵路站0米</span><span class="taxfree">房本满五年</span></div>
                    </div>
                </div><!-- 无搜索结果 -->
                <div id="noResultPush"></div>
                <div class="contentBottom clear">
                    <div class="crumbs fl"><a href="/">链家网广州站</a><span>&nbsp;&gt;&nbsp;</span>
                        <h1><a href="/ershoufang/">广州二手房</a></h1></div>
                    <div class="page-box fr">
                        <div class="page-box house-lst-page-box" comp-module='page' page-url="/ershoufang/pg{page}/"
                             page-data='{"totalPage":100,"curPage":1}'></div>
        
        
                    </div>
                </div>
                <div style="display:none;"><p></p>
                    <p></p>
                    <p></p></div>
            </div><!-- 右侧sidebar -->
            <div class="rightLayout">
                <div class="rightContent">
                    <div class="map">
                        <div class="pic"></div>
                        <button id="btn-map">试试地图找房</button>
                    </div>
                    <div class="price" id='priceSideBarContainer' log-mod="recommand_price"></div>
                    <div class="suggestAgent" id='suggestAgentContainer' log-mod="ershoufang_list_recommend-agent"></div>
                    <div class="suggestHouse" id="suggestHouseContainer" log-mod="recommand_house"></div>
                    <div class="suggestCommunity" id="suggestCommunityContainer"
                         log-mod="ershoufang_list_recommend-community"></div>
                    <div class="wenda zixun" id="pushZixunContainer" log-mod="recommand_zixun"></div>
                    <div class="wenda SCROLLVIEWLOG" id="pushWendaContainer" log-mod="recommand_wenda"></div>
                    <div class="wenda SCROLLVIEWLOG" id="pushBaikeContainer" log-mod="recommand_baike"></div>
                    <div class="download">
                        <div class="title">下载链家APP</div>
                        <div class="qr-code"><img width="94" height="94"
                                                  src="/ershoufang.html/ajax.api.lianjia.com/qr/getDownloadQr?location=right&ljweb_channel_key=ershoufang_search"
                                                  alt="下载链家app">
                            <div class="text"><p>扫描上方二维码</p>
                                <p>随时查看新房源</p>
                                <p class="get-more"><a href="/ershoufang.html/www.lianjia.com/client">了解更多<img width="9" height="9"
                                                                                                               src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEUAAACcn6Gfn5+an5+bnqCbnqGfn5+cn6EV6DbuAAAAB3RSTlMA0BAw8LAgvf5k9AAAAEdJREFUKM9jIBOkBqMJhBcqoAmUC6EKmJSjKWEWR1eiiK6ECZsSA3QlzuhKSihRghDA0EJ/BWIoCgzh4YMIZALRYBrMQAkAAF5bGMBkrwzqAAAAAElFTkSuQmCC"></a>
                                </p></div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="clear:both"></div>
        </div>
        <div id="pushCommunity" class="pushCommunity" log-mod="ershoufang_list_recommend-community"></div>
        <div id="newHousePush" class="newHousePush"></div>
        <div class="saveMegmask"></div>
        <div class="saveok">
            <div class="fl"></div>
            <div class="fr"><span>已成功保存搜索条件！</span>
                <p>您可在搜索框右侧下拉列表中快速使用该条件。该条件有新房源出现时，我们将会用站内提醒的方式来通知您</p><label class="close">确定</label></div>
        </div>
        <div class="saveerror">
            <div class="fl"></div>
            <div class="fr"><span>你的搜索条件已达到上限！</span>
                <p>您可在搜索框右侧下拉列表中快速使用该条件。该条件有新房源出现时，我们将会用站内提醒的方式来通知您。</p><a href="//user.lianjia.com/site/searchlist/ershoufang.html"
                                                                           rel="nofollow">个人中心</a><label
                        class="close">取消</label></div>
        </div>
        <div class="pagination_group_a"><a href="/ershoufang/"></a><a href="/ershoufang/pg2/"></a><a
                href="/ershoufang/pg3/"></a><a href="/ershoufang/pg4/"></a><a href="/ershoufang/pg5/"></a><a
                href="/ershoufang/pg6/"></a><a href="/ershoufang/pg7/"></a><a href="/ershoufang/pg8/"></a><a
                href="/ershoufang/pg9/"></a><a href="/ershoufang/pg10/"></a></div>
        <div class="footer">
            <div class="wrapper">
                <div class="f-title">
                    <div class="fl">
                        <ul>
                            <li><a href="https://www.lianjia.com/zhuanti/home/ershoufang.html" rel="nofollow" target="_blank">了解链家</a></li>
                            <li><a href="https://gz.lianjia.com/about/aboutlianjia/ershoufang.html" rel="nofollow" target="_blank">关于链家</a>
                            </li>
                            <li><a href="https://gz.lianjia.com/about/contactus/ershoufang.html" rel="nofollow" target="_blank">联系我们</a></li>
                            <li><a href="https://join.lianjia.com/ershoufang.html" rel="nofollow" target="_blank">加入我们</a></li>
                            <li><a href="https://www.lianjia.com/privacy/ershoufang.html" rel="nofollow" target="_blank">隐私声明</a></li>
                            <li><a href="https://gz.lianjia.com/sitemap/ershoufang.html" target="_blank">网站地图</a></li>
                            <li><a href="https://www.lianjia.com/notice/7.html" rel="nofollow" target="_blank">友情链接</a></li>
                            <li><a href="https://agent.lianjia.com/ershoufang.html" rel="nofollow" target="_blank">经纪人登录</a></li>
                        </ul>
                    </div>
                    <div class="fr">官方客服 1010 9666</div>
                </div>
                <div class="lianjia-link-box">
                    <div class="fl">
                        <div class="tab"><span
                                class="hover">城市二手房</span><span>房产资讯</span><span>城区二手房</span><span>城区租房</span><span>城区小区</span><span>热门小区</span><span>热门问答</span><span>热门百科</span><span>合作与友情链接</span>
                        </div>
                        <div class="link-list">
                            <div>
                                <dd><a target="_blank" href="https://bj.lianjia.com/ershoufang.html">北京房产网</a><a target="_blank"
                                                                                                                 href="https://gz.lianjia.com/ershoufang.html">广州房产网</a><a
                                        target="_blank" href="https://sz.lianjia.com/ershoufang.html">深圳房产网</a><a target="_blank"
                                                                                                                  href="https://tj.lianjia.com/ershoufang.html">天津房产网</a><a
                                        target="_blank" href="https://cd.lianjia.com/ershoufang.html">成都房产网</a><a target="_blank"
                                                                                                                  href="https://nj.lianjia.com/ershoufang.html">南京房产网</a><a
                                        target="_blank" href="https://hz.lianjia.com/ershoufang.html">杭州房产网</a><a target="_blank"
                                                                                                                  href="https://qd.lianjia.com/ershoufang.html">青岛房产网</a><a
                                        target="_blank" href="https://dl.lianjia.com/ershoufang.html">大连房产网</a><a target="_blank"
                                                                                                                  href="https://xm.lianjia.com/ershoufang.html">厦门房产网</a><a
                                        target="_blank" href="https://wh.lianjia.com/ershoufang.html">武汉房产网</a><a target="_blank"
                                                                                                                  href="https://cq.lianjia.com/ershoufang.html">重庆房产网</a><a
                                        target="_blank" href="https://cs.lianjia.com/ershoufang.html">长沙房产网</a><a target="_blank"
                                                                                                                  href="https://jn.lianjia.com/ershoufang.html">济南房产网</a><a
                                        target="_blank" href="https://fs.lianjia.com/ershoufang.html">佛山房产网</a><a target="_blank"
                                                                                                                  href="https://dg.lianjia.com/ershoufang.html">东莞房产网</a><a
                                        target="_blank" href="https://yt.lianjia.com/ershoufang.html">烟台房产网</a><a target="_blank"
                                                                                                                  href="https://zs.lianjia.com/ershoufang.html">中山房产网</a><a
                                        target="_blank" href="https://zh.lianjia.com/ershoufang.html">珠海房产网</a><a target="_blank"
                                                                                                                  href="https://hui.lianjia.com/ershoufang.html">惠州房产网</a><a
                                        target="_blank" href="https://sy.lianjia.com/ershoufang.html">沈阳房产网</a><a target="_blank"
                                                                                                                  href="https://hf.lianjia.com/ershoufang.html">合肥房产网</a><a
                                        target="_blank" href="https://zz.lianjia.com/ershoufang.html">郑州房产网</a></dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="https://news.lianjia.com/ershoufang.html">房产资讯</a><a target="_blank"
                                                                                                                  href="https://news.lianjia.com/bj/ershoufang.html">北京房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/bj/baike/ershoufang.html">北京房产百科</a><a target="_blank"
                                                                                                                              href="https://bj.lianjia.com/wenda/ershoufang.html">北京房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/ershoufang.html">广州房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/gz/baike/ershoufang.html">广州房产百科</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/ershoufang.html">广州房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/sz/ershoufang.html">深圳房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/sz/baike/ershoufang.html">深圳房产百科</a><a target="_blank"
                                                                                                                              href="https://sz.lianjia.com/wenda/ershoufang.html">深圳房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/tj/ershoufang.html">天津房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/tj/baike/ershoufang.html">天津房产百科</a><a
                                        target="_blank" href="https://tj.lianjia.com/wenda/ershoufang.html">天津房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/cd/ershoufang.html">成都房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/cd/baike/ershoufang.html">成都房产百科</a><a target="_blank"
                                                                                                                              href="https://cd.lianjia.com/wenda/ershoufang.html">成都房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/nj/ershoufang.html">南京房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/nj/baike/ershoufang.html">南京房产百科</a><a
                                        target="_blank" href="https://nj.lianjia.com/wenda/ershoufang.html">南京房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/hz/ershoufang.html">杭州房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/hz/baike/ershoufang.html">杭州房产百科</a><a target="_blank"
                                                                                                                              href="https://hz.lianjia.com/wenda/ershoufang.html">杭州房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/qd/ershoufang.html">青岛房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/qd/baike/ershoufang.html">青岛房产百科</a><a
                                        target="_blank" href="https://qd.lianjia.com/wenda/ershoufang.html">青岛房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/dl/ershoufang.html">大连房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/dl/baike/ershoufang.html">大连房产百科</a><a target="_blank"
                                                                                                                              href="https://dl.lianjia.com/wenda/ershoufang.html">大连房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/xm/ershoufang.html">厦门房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/xm/baike/ershoufang.html">厦门房产百科</a><a
                                        target="_blank" href="https://news.lianjia.com/wh/ershoufang.html">武汉房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/wh/baike/ershoufang.html">武汉房产百科</a><a
                                        target="_blank" href="https://news.lianjia.com/cq/ershoufang.html">重庆房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/cq/baike/ershoufang.html">重庆房产百科</a><a
                                        target="_blank" href="https://cq.lianjia.com/wenda/ershoufang.html">重庆房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/cs/ershoufang.html">长沙房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/cs/baike/ershoufang.html">长沙房产百科</a><a target="_blank"
                                                                                                                              href="https://cs.lianjia.com/wenda/ershoufang.html">长沙房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/jn/ershoufang.html">济南房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/jn/baike/ershoufang.html">济南房产百科</a><a
                                        target="_blank" href="https://jn.lianjia.com/wenda/ershoufang.html">济南房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/fs/ershoufang.html">佛山房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/fs/baike/ershoufang.html">佛山房产百科</a><a target="_blank"
                                                                                                                              href="https://fs.lianjia.com/wenda/ershoufang.html">佛山房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/dg/ershoufang.html">东莞房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/dg/baike/ershoufang.html">东莞房产百科</a><a
                                        target="_blank" href="https://dg.lianjia.com/wenda/ershoufang.html">东莞房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/xa/ershoufang.html">西安房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/xa/baike/ershoufang.html">西安房产百科</a><a target="_blank"
                                                                                                                              href="https://news.lianjia.com/sjz/ershoufang.html">石家庄房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/sjz/baike/ershoufang.html">石家庄房产百科</a><a target="_blank"
                                                                                                                                href="https://sjz.lianjia.com/wenda/ershoufang.html">石家庄房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/yt/ershoufang.html">烟台房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/yt/baike/ershoufang.html">烟台房产百科</a><a
                                        target="_blank" href="https://news.lianjia.com/sy/ershoufang.html">沈阳房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/sy/baike/ershoufang.html">沈阳房产百科</a><a
                                        target="_blank" href="https://sy.lianjia.com/wenda/ershoufang.html">沈阳房产知识</a><a target="_blank"
                                                                                                                         href="https://news.lianjia.com/hf/ershoufang.html">合肥房产资讯</a><a
                                        target="_blank" href="https://news.lianjia.com/hf/baike/ershoufang.html">合肥房产百科</a><a target="_blank"
                                                                                                                              href="https://hf.lianjia.com/wenda/ershoufang.html">合肥房产知识</a><a
                                        target="_blank" href="https://news.lianjia.com/zz/ershoufang.html">郑州房产资讯</a><a target="_blank"
                                                                                                                        href="https://news.lianjia.com/zz/baike/ershoufang.html">郑州房产百科</a>
                                </dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="https://gz.lianjia.com/ershoufang/liwan/ershoufang.html">荔湾二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/yuexiu/ershoufang.html">越秀二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/haizhu/ershoufang.html">海珠二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/tianhe/ershoufang.html">天河二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/baiyun/ershoufang.html">白云二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/huangpugz/ershoufang.html">黄埔二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/panyu/ershoufang.html">番禺二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/huadou/ershoufang.html">花都二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/nansha/ershoufang.html">南沙二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/zengcheng/ershoufang.html">增城二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/ershoufang/conghua/ershoufang.html">从化二手房</a></dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="https://gz.lianjia.com/zufang/liwan/ershoufang.html">荔湾租房</a><a target="_blank"
                                                                                                                             href="https://gz.lianjia.com/zufang/yuexiu/ershoufang.html">越秀租房</a><a
                                        target="_blank" href="https://gz.lianjia.com/zufang/haizhu/ershoufang.html">海珠租房</a><a target="_blank"
                                                                                                                               href="https://gz.lianjia.com/zufang/tianhe/ershoufang.html">天河租房</a><a
                                        target="_blank" href="https://gz.lianjia.com/zufang/baiyun/ershoufang.html">白云租房</a><a target="_blank"
                                                                                                                               href="https://gz.lianjia.com/zufang/huangpugz/ershoufang.html">黄埔租房</a><a
                                        target="_blank" href="https://gz.lianjia.com/zufang/panyu/ershoufang.html">番禺租房</a><a target="_blank"
                                                                                                                              href="https://gz.lianjia.com/zufang/huadou/ershoufang.html">花都租房</a><a
                                        target="_blank" href="https://gz.lianjia.com/zufang/nansha/ershoufang.html">南沙租房</a><a target="_blank"
                                                                                                                               href="https://gz.lianjia.com/zufang/zengcheng/ershoufang.html">增城租房</a><a
                                        target="_blank" href="https://gz.lianjia.com/zufang/conghua/ershoufang.html">从化租房</a></dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="https://gz.lianjia.com/xiaoqu/liwan/ershoufang.html">荔湾小区</a><a target="_blank"
                                                                                                                             href="https://gz.lianjia.com/xiaoqu/yuexiu/ershoufang.html">越秀小区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/haizhu/ershoufang.html">海珠小区</a><a target="_blank"
                                                                                                                               href="https://gz.lianjia.com/xiaoqu/tianhe/ershoufang.html">天河小区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/baiyun/ershoufang.html">白云小区</a><a target="_blank"
                                                                                                                               href="https://gz.lianjia.com/xiaoqu/huangpugz/ershoufang.html">黄埔小区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/panyu/ershoufang.html">番禺小区</a><a target="_blank"
                                                                                                                              href="https://gz.lianjia.com/xiaoqu/huadou/ershoufang.html">花都小区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/nansha/ershoufang.html">南沙小区</a><a target="_blank"
                                                                                                                               href="https://gz.lianjia.com/xiaoqu/zengcheng/ershoufang.html">增城小区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/conghua/ershoufang.html">从化小区</a></dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238599618/ershoufang.html">白云高尔夫花园西区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238860934/ershoufang.html">金海岸花园聚湖</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238861338/ershoufang.html">和辉花园叠翠园</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238336826/ershoufang.html">五一新村二街北</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316733/ershoufang.html">黄金广场</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103318141/ershoufang.html">梅宾东公安宿舍</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103319007/ershoufang.html">京溪尚苑</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103319257/ershoufang.html">富力盈丰大厦</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103831657/ershoufang.html">六榕路</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238861177/ershoufang.html">华南碧桂园岭御苑</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103318455/ershoufang.html">盛大蓝庭</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238861093/ershoufang.html">锦绣半岛金月湾</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316814/ershoufang.html">金逸雅居</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238599610/ershoufang.html">丰年华庭芳邻美地</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238336959/ershoufang.html">荔港南湾B区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238598821/ershoufang.html">广州星河湾荟心园</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316569/ershoufang.html">南北广场</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103318880/ershoufang.html">天河峰景大厦</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103831699/ershoufang.html">越秀北路</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316413/ershoufang.html">东成花苑</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238861743/ershoufang.html">羊城花园趣苑</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316779/ershoufang.html">绿茵翠庭</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238598814/ershoufang.html">广州星河湾怡心园</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238599585/ershoufang.html">保利西海岸英伦堡花园</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316754/ershoufang.html">中兴花园</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103317852/ershoufang.html">岭南雅院</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103317566/ershoufang.html">晓港花苑</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343239123007/ershoufang.html">碧桂园凤凰城凤雅苑</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316960/ershoufang.html">陶瓷大厦</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316867/ershoufang.html">花地城广场</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238337522/ershoufang.html">盈翠华庭翠逸居</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238336541/ershoufang.html">保利世纪绿洲一期</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238337521/ershoufang.html">盈彩美居云彩轩</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238336935/ershoufang.html">旭景家园C区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103316740/ershoufang.html">中信乐涛苑</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238337530/ershoufang.html">晓港湾晓城大厦</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238599206/ershoufang.html">罗马家园威尼斯庭</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238860879/ershoufang.html">锦丽居三期锦绣星城</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2110343238336906/ershoufang.html">新世界逸彩庭园E区</a><a
                                        target="_blank" href="https://gz.lianjia.com/xiaoqu/2111103319231/ershoufang.html">佳润临江上品</a></dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b1001/ershoufang.html">房价行情</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b1002/ershoufang.html">购房建议</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b1003/ershoufang.html">购房资质</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b1004/ershoufang.html">买房风险</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b1005/ershoufang.html">二手房</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b1006/ershoufang.html">新房</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b1007/ershoufang.html">海外买房</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b2001/ershoufang.html">税费计算</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b2002/ershoufang.html">认购签约</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b2003/ershoufang.html">资金监管</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b2004/ershoufang.html">过户流程</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b2005/ershoufang.html">入住交接</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b3001/ershoufang.html">房屋估价</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b3002/ershoufang.html">卖房流程</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b3003/ershoufang.html">出售方案</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b3004/ershoufang.html">业主风险</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b3005/ershoufang.html">卖旧买新</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b5001/ershoufang.html">贷款利率</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b5002/ershoufang.html">首付月供</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b5003/ershoufang.html">贷款流程</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b5004/ershoufang.html">住房公积金</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b5005/ershoufang.html">商业贷款</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b5006/ershoufang.html">融资借款</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b5007/ershoufang.html">金融方案</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b6001/ershoufang.html">房产政策</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b6002/ershoufang.html">法律纠纷</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b6003/ershoufang.html">保障住房</a><a
                                        target="_blank" href="https://gz.lianjia.com/wenda/liebiao/b6004/ershoufang.html">其他</a></dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="https://news.lianjia.com/gz/baike/0033/ershoufang.html">房产政策</a><a target="_blank"
                                                                                                                                href="https://news.lianjia.com/gz/baike/0034/ershoufang.html">房价行情</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0035/ershoufang.html">购房建议</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0036/ershoufang.html">购房资质</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0037/ershoufang.html">房屋贷款</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0038/ershoufang.html">融资借款</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0039/ershoufang.html">保障住房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0040/ershoufang.html">产权/变更</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0041/ershoufang.html">法律纠纷</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0042/ershoufang.html">房屋装修</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0043/ershoufang.html">其他</a><a target="_blank"
                                                                                                                               href="https://news.lianjia.com/gz/baike/0044/ershoufang.html">准备买房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0045/ershoufang.html">看房/选房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0046/ershoufang.html">签约/定房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0047/ershoufang.html">全款/贷款</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0048/ershoufang.html">缴税/过户</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0049/ershoufang.html">入住/交接</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0050/ershoufang.html">买房风险</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0051/ershoufang.html">准备买房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0052/ershoufang.html">看房/选房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0053/ershoufang.html">认购新房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0054/ershoufang.html">签约/定房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0055/ershoufang.html">全款/贷款</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0056/ershoufang.html">收房/验房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0057/ershoufang.html">装修/入住</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0058/ershoufang.html">退房/维权</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0059/ershoufang.html">各国概况</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0060/ershoufang.html">计划买房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0061/ershoufang.html">签约定房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0062/ershoufang.html">银行贷款</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0063/ershoufang.html">交易过户</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0064/ershoufang.html">房屋代理</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0066/ershoufang.html">准备卖房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0067/ershoufang.html">产权核验</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0068/ershoufang.html">收定金/签约</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0069/ershoufang.html">分步收款</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0070/ershoufang.html">缴税/过户</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0071/ershoufang.html">交房须知</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0072/ershoufang.html">卖房风险</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0073/ershoufang.html">准备换房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0074/ershoufang.html">换房方案</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0075/ershoufang.html">卖旧/买新</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0076/ershoufang.html">金融方案</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0077/ershoufang.html">缴税/过户</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0078/ershoufang.html">交房/收房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0079/ershoufang.html">换房风险</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0080/ershoufang.html">学区政策</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0081/ershoufang.html">入学条件</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0082/ershoufang.html">选学区房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/0083/ershoufang.html">学区房风险</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/00779/ershoufang.html">找房看房</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/00780/ershoufang.html">签约付款</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/00781/ershoufang.html">物业交割</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/00782/ershoufang.html">租房纠纷</a><a
                                        target="_blank" href="https://news.lianjia.com/gz/baike/00783/ershoufang.html">我是房东</a></dd>
                            </div>
                            <div>
                                <dd><a target="_blank" href="http://guangzhou.liebiao.com/ershoufang/">广州二手房</a><a
                                        target="_blank" href="http://www.homekoo.com/ttm_wofang">榻榻米</a><a target="_blank"
                                                                                                           href="http://www.9998.tv/comity/">酒行业协会</a><a
                                        target="_blank" href="http://guangzhou.anjuke.com/sale/">广州二手房</a><a target="_blank"
                                                                                                             href="https://www.tujia.com/guangzhou_gongyu/">途家广州公寓住宿</a><a
                                        target="_blank" href="https://www.xin.com/guangzhou/">广州二手车</a><a target="_blank"
                                                                                                          href="http://www.mayi.com/xilinguole/">锡林郭勒日租房</a><a
                                        target="_blank" href="http://www.mayi.com/shenyang/">沈阳日租房</a><a target="_blank"
                                                                                                         href="http://www.lianjia.com/ershoufang.html">房产网</a><a
                                        target="_blank" href="http://m.lianjia.com/gz/ershoufang.html">手机广州房产网</a></dd>
                            </div>
                        </div>
                    </div>
                    <div class="clear"></div>
                </div>
                <div class="bottom">
                    <div class="copyright fl">链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | © Copyright©2010-2017
                        链家网Lianjia.com版权所有
                    </div>
                    <div style="width:300px;color: #888c8e;font-size: 12px;line-height: 20px;"><a target="_blank"
                                                                                                  href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019"
                                                                                                  style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img
                            src="https://s1.ljcdn.com/feroot/pc/asset/img/home/beian.png?_v=201709261333487""
                        style="float:left;"><p
                                style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px;color: #888c8e;">京公网安备
                            11010802024019号</p></a></div>
                </div>
            </div>
        </div>
        
        <script src="https://s1.ljcdn.com/feroot/pc/asset/base/fe.js?_v=201709261333487"></script>
        <script src="https://s1.ljcdn.com/feroot/pc/asset/common/common.js?_v=201709261333487"></script>
        <div style="display:none">
            <script src="https://s1.ljcdn.com/feroot/dep/ljanalytics.js?_v=201709261333487"></script>
        </div>
        <div id="only" data-city="gz" data-page="ershoufang_search"></div>
        <script>var path = 'https://s1.ljcdn.com/feroot/pc/asset?_v=201709261333487'.split("?");
        require.config({
            baseUrl: path[0],
            paths: {
                'echarts': '../../dep/echarts-1.4.1/build/echarts',
                'echarts/chart/bar': '../../dep/echarts-1.4.1/build/echarts',
                'echarts/chart/line': '../../dep/echarts-1.4.1/build/echarts',
                'echarts/chart/pie': '../../dep/echarts-1.4.1/build/echarts',
                'echarts3': '../../dep/echarts3/echarts3',
                'common': 'common',
                'jquery-ui': '../../dep/jquery-ui/jquery-ui.min',
                'zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'
            },
            urlArgs: path[1]
        });
        var feData = {
            "cityName": "北京",
            "getFavHouseUrl": "/api/gethousefav",
            "setFavHouseUrl": "/api/sethousefav",
            "getLastSearch": "/api/getlastsearch",
            "getCommunityHistory": "/api/getcommunityhistory",
            "verifyHouse": "/api/verifyHouse",
            "getUser": "/api/getUser",
            "verifyCode": "/api/getVerifyCode",
            "complaint": "/api/complaint",
            "getDecoration": "/api/getDecoration",
            "trendData": "/site/getpicinfo"
        }</script>
        <script type="text/template" id="priceSideBarTpl">
            <%if(tag !== 'school'){%>
            <div class="title"><%=name%>最新参考均价</div>
            <div class="priceMap" id="priceChartContainer"></div>
            <a href="<%=fangjia_url%>" class="unitPrice" target="_blank">
                <span><%=month_trans%></span>元/平米
            </a>
            <div class="info">
                <a href="<%=fangjia_url%>" target="_blank">环比上月均价<%=month_trans_ratio>=0?'上涨':'下降'%> <%=month_trans_ratio%>%</a>
                <a href="<%=chengjiao_url%>" target="_blank">/ 近90天成交<%=sold_90_day%>套</a>
                <%if(tag === '小区'){%>
                <div>
                    <a class="cardMoreDetail" href="<%=url%>" target="_blank">查看小区详情>></a>
                </div>
                <%}%>
            </div>
            <%}else{%>
            <a class="title" href="<%=url%>" target="_blank"><%=name%></a>
            <div class="unitPrice school">
                <span><%=min_unit_price%></span>万元起
            </div>
            <div class="info">
                <a href="<%=url%>" target="_blank">本学区目前有在售二手房<%=sell_num%>套，划片小区<%=resblock_nums%>个</a>
                <a class="cardMoreDetail" href="<%=url%>" target="_blank">查看学区详情>></a>
            </div>
            <%}%>
        </script>
        
        <script type="text/template" id="suggestAgentTpl">
            <div class="title">推荐置业顾问</div>
            <div class="agent">
                <a class="img <%= (desc.search('学区') > -1) ? '': 'LOGVIEW LOGCLICK'%>" href="<%=url%>" target="_blank"
                   data-bl="agent_<%= (desc.search('学区') > -1) ? 'school': 'community'%>" data-el="<%=ucid%>"
                   data-log_id="20001">
                    <img src="<%=photo_url%>" alt="">
                </a>
                <div class="info">
                    <div class="name">
                        <a href="<%=url%>" target="_blank"
                           data-bl="agent_<%= (desc.search('学区') > -1) ? 'school': 'community'%>" data-el="<%=ucid%>"
                           class="<%= (desc.search('学区') > -1) ? '': 'LOGCLICK'%>" data-log_id="20001"><%=name%></a>
                        <a class="lianjiaim-createtalk <%= (desc.search('学区') > -1) ? '': 'LOGCLICK'%>"
                           style="padding: 1px 0 !important;" title="在线咨询" data-role="lianjiaim-createtalk"
                           data-ucid="<%=ucid%>" data-bl="agentim_<%= (desc.search('学区') > -1) ? 'school': 'community'%>"
                           data-el="<%=ucid%>" data-log_id="20001"></a>
                    </div>
                    <div class="phone"><%=phone%></div>
                </div>
            </div>
            <div class="agentInfo" title="<%=desc%>"><%=formatDesc%></div>
        </script>
        <script type="text/template" id="suggestHouseTpl">
            <a class="img" href="<%=url%>" target="_blank" data-bl="list" data-log_index="<%=index+1%>">
                <img src="<%=img_url%>" alt="">
                <div class="cover"></div>
                <div class="title">
                    <span><%=title%></span>&nbsp;
                </div>
            </a>
            <div class="pointContainer">
                <%for(var i = 0; i < total; i++){%>
                <%if(index === i){%>
                <span data-index="<%=i%>" class="point selected"></span>
                <%}else{%>
                <span data-index="<%=i%>" class="point"></span>
                <%}%>
                <%}%>
            </div>
        </script>
        <script type="text/template" id="suggestCommunityTpl">
            <div class="title">小区推荐</div>
            <ul>
                <%for(var i = 0; i < list.length; i++){%>
                <li>
                    <a href="<%=list[i].url%>" class="img LOGVIEW LOGCLICK" data-log_id="30001" target="_blank"
                       data-log_index="<%=i+1%>"
                       data-bl="<%=$.trim($('.list-more dl:first dt').text()) === '小区' ? 'community' : 'bizcircle'%>"
                       data-el="">
                        <%if(list[i].pic) {%>
                        <img src="<%=list[i].picUri%>.280x210.jpg">
                        <%}else{%>
                        <span class="noimg">暂无图片</span>
                        <%}%>
                        <div class="price">
                            <%if(list[i].price!=0 && list[i].price) {%><%=parseFloat(list[i].price,
                            10).toFixed()%>元/平<%}else{%>暂无均价<%}%>
                        </div>
                    </a>
                    <div class="info clear">
                        <a href="<%=list[i].url%>" target="_blank" class="fl"><%=list[i].name%></a>
                        <div class="fr"><%=list[i].sellNum%>套在售</div>
                    </div>
                    <div class="desc"><%=list[i].desc%></div>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="pushZhuanjiaTpl">
            <span class="name">推荐学区顾问</span>
            <span class="fl pic">
            <img src='<%=list.photoPath%>'>
          </span>
            <span class="fl">
            <a href="<%=list.agentUrl%>" target="_blank"><%=list.name%></a>
            <a class="lianjiaim-createtalk" style="display: none;" title="在线咨询" data-role="lianjiaim-createtalk"
               data-ucid="<%=list.agent_ucid%>"></a>
            <p class="tel"><%=list.phoneNumber%></p>
          </span>
            <p class="tips">
                <%=list.desc%>
            </p>
        </script>
        
        <script type="text/template" id="pushXuexiaoTpl">
            <div class="title"><%=data.regionName%>近期热门学校</div>
            <ul>
                <% var list = data.list;for(var i = 0;i < list.length; i++){%>
                <li class="li<%=i%>">
                    <i></i>
                    <a class="info" href="<%=list[i].viewUrl%>" target="_blank"><%=list[i].schoolName%></a>
                    <span><%=list[i].viewCount%>浏览</span>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="pushChenjiaoTpl">
            <div class="title"><%=data.regionName%>近期成交</div>
            <ul>
                <% var list = data.list; for(var i = 0;i < list.length; i++){%>
                <li class="li<%=i%>">
                    <i></i>
                    <a class="info" href="<%=list[i].viewUrl%>" target="_blank"><%=list[i].schoolName%></a>
                    <span><%=list[i].dealCount%>套</span>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="pushXuequTpl">
            <div class="title">热点精选</div>
            <ul>
                <%for(var i = 0;i < list.length; i++){%>
                <li>
                    <a class="info" href="<%=list[i].pc_url%>" target="_blank"><%=list[i].title%></a>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="pushZixunTpl">
            <div class="title">热点精选</div>
            <ul>
                <%for(var i = 0;i < list.length; i++){%>
                <li>
                    <a class="info" href="<%=list[i].url%>" target="_blank" data-bl="list" data-log_index="<%=i+1%>">
                        <i class="opt<%=i%>"><%=i+1%></i><span><%=list[i].question_title%></span>
                    </a>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="pushWendaTpl">
            <div class="title">热门问答</div>
            <ul>
                <%for(var i = 0;i < list.length; i++){%>
                <li>
                    <a class="info" href="<%=list[i].url%>" target="_blank" data-bl="list" data-log_index="<%=i+1%>"><%=list[i].question_title%></a>
                    <span class="answer_count"><%=list[i].answer_count%>个回答 / </span><span
                        class="time"><%=list[i].mtime%></span>
                </li>
                <%}%>
            </ul>
        </script>
        <script type="text/template" id="pushBaikeTpl">
            <div class="list-baike">
                <div class="title">热门百科
                    <a href="<%=baike_data['more_url']%>" class="btn-more" target="_blank">更多</a>
                </div>
                <div class="bd">
                    <%for(var i = 0;i < baike_data['data'].length; i++){%>
                    <div class="item"><a href="<%=baike_data['data'][i].url%>" target="_blank" class="tit"><%=baike_data['data'][i].title%></a>
                        <div class="sub-tit"><%=baike_data['data'][i].summary%></div>
                        <span class="arrow"></span></div>
                    <%}%>
                </div>
            </div>
        </script>
        <script type="text/template" id="newAddHouseTpl">
            <div class="newAddHouse">
                自从您上次浏览（<%=time%>）之后，该搜索条件下新增加了<%=count%>套房源
                <a href="<%=url%>" class="LOGNEWERSHOUFANGSHOW" <%=logText%>><%=linkText%></a>
                <span class="newHouseRightClose">x</span>
            </div>
        </script>
        <script type="text/template" id="pushXinfangTpl">
            <div class="newHousePushContainer">
                <h3>推荐楼盘</h3>
                <ul log-mod="ershoufang_list_newHouseRecommand">
                    <%for(var i = 0; i < list.length; i++){%>
                    <li>
                        <a class="pic LOGVIEW LOGCLICK" href="<%=list[i].view_url%>" target="_blank" data-bl="list"
                           data-log_id="40001" data-el="<%=strategy_version%>" data-log_index="<%=i+1%>">
                            <span class="bg"></span>
                            <%if(list[i].cover_pic){%>
                            <img src="<%=list[i].cover_pic%>.218x150.jpg">
                            <%}else{%>
                            <div class="mark"></div>
                            <%}%>
                            <div class="description"><%=list[i].district_name%>－<%=list[i].resblock_name%></div>
                        </a>
                        <%if(list[i].rooms){%>
                        <p class="area">
                            <%=list[i].rooms%>
                            <%if(list[i].min_frame_area != '' && list[i].max_frame_area != ''){%>
                            &nbsp;-&nbsp;
                            <%=list[i].min_frame_area%>~<%=list[i].max_frame_area%>平
                            <%}%>
                        </p>
                        <%}%>
                        <div class="price">
                            <%if(list[i].show_price && list[i].show_price != 0){%>
                            <i><%=list[i].show_price%></i>
                            <%=list[i].show_price_unit%>
                            <%}else{%>
                            价格待定
                            <%}%>
                        </div>
                    </li>
                    <%}%>
                </ul>
            </div>
        </script>
        
        <script type="text/javascript">
            require(['ershoufang/sellList/index'], function (main) {
                main({
                    sidebar: {
                        "type": "city",
                        "cityId": 440100,
                        "uuid": "bb946daf-c78f-497e-8ae3-d5ac3d2d4604",
                        "ucid": null,
                        "id": 440100
                    },
                    url: '/web/ershoufang/sidebar',
                    xuequUrl: '/web/ershoufang/sidebarxuequ',
                    ifXuqu: "\/ershoufang\/",
                    ids: 'GZ0003046161,GZ0003039466,GZ0003036437,GZ0002550957,GZ0002235949,GZ0003039386,GZ0003095769,GZ0003124674,GZ0002839515,GZ0002716501,GZ0003120690,GZ0003118304,GZ0003095718,GZ0002243262,GZ0003110306,GZ0003134466,GZ0003020216,GZ0003030524,GZ0002722805,GZ0003082596,GZ0002641636,GZ0003119717,GZ0002876762,GZ0002889862,GZ0003002081,GZ0003067932,GZ0003123281,GZ0003010812,GZ0003075949,GZ0002989763',
                    SIRKeyword: "",
                    count: 14338,
                    pageNum: 1,
                    cid: null,
                    bid: null,
                    ucid: '',
                    uuid: 'bb946daf-c78f-497e-8ae3-d5ac3d2d4604',
                    loadingImg: 'https://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellDetail/img/loading.gif?_v=201709261333487',
                    qrImg: '//ajax.api.lianjia.com/qr/getDownloadQr'
                });
        
            });
        
        
            ;
            ;+function () {
                LjUserTrack.send({
                    "ljweb_id": "10001",
                    "ljweb_mod": "ershoufang_list_view",
                    "ljweb_bl": "spk_0",
                    "ljweb_el": "14338",
                    "ljweb_value": "",
                });
                var isHaveAgentCard = false
                var clickLinkBl = 'list';
                var resblockId = '';
                if (isHaveAgentCard) {
                    clickLinkBl = 'list_have_sem_card';
                    resblockId = ""
                }
                $(document.body).on("click", "[data-el='ershoufang']", function () {
                    var $m = $(this);
                    LjUserTrack.send({
                        "ljweb_id": "10002",
                        "ljweb_mod": "ershoufang_list_list",
                        "ljweb_bl": clickLinkBl,
                        "ljweb_el": "ershoufang",
                        "ljweb_index": $m.attr("data-log_index"),
                        "ljweb_url": $m.attr("href"),
                        "ljweb_value": resblockId,
                        "ljweb_is_focus": $m.attr("data-is_focus") || 0,
                        "ljweb_house_code": $m.attr('data-housecode')
                    });
        
                });
        
                $(document.body).on("mousedown", ".input [data-bl='sug'] [data-log_value]", function () {
                    var $m = $(this);
                    var actionId = $m.closest('[data-bl="sug"]').attr("data-el") === 'history' ? '10004' : '10003';
                    LjUserTrack.send({
                        "ljweb_id": actionId,
                        "ljweb_mod": "ershoufang_list_search",
                        "ljweb_bl": "search",
                        "ljweb_el": $m.attr("data-log_value"),
                        "ljweb_index": $m.attr("data-log_index"),
                        "ljweb_value": $.trim($("#searchInput").val()),
                        "ljweb_url": $m.attr("href")
                    });
                });
                $("#searchForm").on("submit", function () {
                    var $m = $(this);
                    LjUserTrack.send({
                        "ljweb_id": "10008",
                        "ljweb_mod": "ershoufang_list_search",
                        "ljweb_bl": "search",
                        "ljweb_value": $.trim($("#searchInput").val())
                    });
                });
        
            }();
        </script>
        <script>require(['common/suggestion'], function (suggestion) {
            window.defaultSuggest = suggestion.init({
                requestOptions: {cityId: '440100', cityName: '广州'},
                url: '/api/headerSearch?channel=ershoufang&q=',
                main: '#keyword-box',
                appendTo: '#suggest-cont',
                redirect: true
            });
        });</script>
        <div class="loninContaner">
            <div class="overlay_bg"></div>
            <div class="panel_login animated" id="dialog">
                <div class="panel_info"><i class="close_login">&times</i>
                    <div class="panel_tab">
                        <div class="title">
                            <div class="fl">账号密码登录</div>
                        </div>
                        <div class="clear"></div>
                        <div id="con_login_user">
                            <form action="" method="post">
                                <ul>
                                    <li class="item border-t userName"><input type="text" class="the_input topSpecial users"
                                                                              placeholder="请输入手机号" maxlength="11"/></li>
                                    <li class="item border-b pwd"><input type="password" class="the_input password"
                                                                         maxlength="20" placeholder="请输入登录密码"/><em
                                            class="password-view"></em></li>
                                    <li class="item checkVerimg" style="display:none;"><input type="text"
                                                                                              class="the_input ver-img"
                                                                                              maxlength="6"
                                                                                              placeholder="请输入验证码"/><img
                                            class="verImg"></li>
                                    <li class="item drag" style="display:none;">
                                        <div id="drag"></div>
                                    </li>
                                    <li class="show-error">
                                        <dd>用户名或密码错误</dd>
                                    </li>
                                    <li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox"
                                                                                                              name="remember"
                                                                                                              value="1"
                                                                                                              class="mind-login"
                                                                                                              checked/></span>下次自动登录</label><a
                                            href="javascript:;" rel="nofollow" class="toforget">忘记密码</a></li>
                                    <li class="li_btn"><a class="login-user-btn"/>登录</a></li>
                                    <li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a>
                                    </li>
                                </ul>
                            </form>
                        </div>
                        <div id="con_login_agent" class="undis">
                            <form action="" method="post">
                                <ul>
                                    <li class="item">
                                        <dd></dd>
                                        <input type="text" class="the_input users" placeholder="输入经纪人ID号码"/></li>
                                    <li class="item"><input type="password" class="the_input password" placeholder="登录密码"/></li>
                                    <li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox"
                                                                                                              name="remember"
                                                                                                              value="1"
                                                                                                              class="mind-login"
                                                                                                              checked/></span>下次自动登录</label><a
                                            href="https://passport.lianjDia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/"
                                            rel="nofollow">忘记密码</a></li>
                                    <li><input class="login-agent-btn" value="立即登录"/></li>
                                </ul>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="registered"></div>
            </div>
            <div class="panel_login animated" id="dialog_tel">
                <div class="panel_info"><i class="close_login">&times</i>
                    <div class="panel_tab">
                        <div class="title">
                            <div class="fl">手机快捷登录</div>
                            <div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div>
                        </div>
                        <div class="clear"></div>
                        <div id="con_login_user_tel">
                            <form action="" method="post">
                                <ul>
                                    <li class="item border-t userName"><input type="text" class="the_input topSpecial users_tel"
                                                                              maxlength="11" placeholder="请输入手机号"/></li>
                                    <!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> -->
                                    <li class="item checkVerimg" style=""><input type="text" class="the_input ver-img"
                                                                                 maxlength="6" placeholder="请输入验证码"/><img
                                            class="verImg"></li>
                                    <li class="item border-b Verify"><input type="text" class="the_input verifycode"
                                                                            maxlength="6" placeholder="请输入短信验证码"/><a
                                            class="send_verify_code" id="send_verify_code_tel" href="javascript:;"
                                            rel="nofollow"><em>获取验证码</em></a></li>
                                    <li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;"
                                        rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li>
                                    <li class="show-error">
                                        <dd>用户名或密码错误</dd>
                                    </li>
                                    <li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox"
                                                                                                              name="remember"
                                                                                                              value="1"
                                                                                                              class="mind-login"
                                                                                                              checked/></span>下次自动登录</label>
                                    </li>
                                    <li class="li_btn"><a class="login-user-tel-btn"/>登录</a></li>
                                    <li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a>
                                    </li>
                                </ul>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="registered"></div>
            </div>
            <div class="panel_login animated" id="dialog_reg">
                <div class="panel_info"><i class="close_login">&times</i>
                    <div class="panel_tab">
                        <div class="title">
                            <div class="fl">手机号码注册</div>
                            <label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow"
                                                                    class="tologin">去登录</a></label></div>
                        <div class="clear"></div>
                        <div id="con_login_user_reg">
                            <form action="" method="post">
                                <ul>
                                    <li class="item border-t userName"><input type="text" class="the_input topSpecial users_reg"
                                                                              maxlength="11" placeholder="请输入手机号"/></li>
                                    <li class="item checkVerimg" style=""><input type="text" class="the_input ver-img"
                                                                                 maxlength="6" placeholder="请输入验证码"/><img
                                            class="verImg"></li>
                                    <li class="item border-c Verify"><input type="text" class="the_input verifycode"
                                                                            maxlength="6" placeholder="请输入短信验证码"/><a
                                            class="send_verify_code" id="send_verify_code_reg" href="javascript:;"
                                            rel="nofollow"><em>获取验证码</em></a></li>
                                    <li class="item border-b pwd"><input type="password" class="the_input password_reg"
                                                                         maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"/><em
                                            class="password-view"></em></li>
                                    <li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;"
                                        rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a></li>
                                    <li class="show-error">
                                        <dd>用户名或密码错误</dd>
                                    </li>
                                    <li class="li_01"><label class="checkbox-btn"><span class="active"><input type="checkbox"
                                                                                                              name="read"
                                                                                                              value="1"
                                                                                                              class="read-protocol"
                                                                                                              checked/></span>我已阅读并同意</label><a
                                            class="toprotocol" href="/ershoufang.html/www.lianjia.com/zhuanti/protocol" target="_blank">《链家用户使用协议》</a>
                                    </li>
                                    <li class="li_btn"><a class="register-user-btn"/>注册</a></li>
                                </ul>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="registered"></div>
            </div>
            <div class="panel_login animated" id="dialog_forget">
                <div class="panel_info"><i class="close_login">&times</i>
                    <div class="panel_tab">
                        <div class="title">
                            <div class="fl">找回密码</div>
                        </div>
                        <div class="clear"></div>
                        <div id="con_forget_user_tel" class="con_forget_user_tel">
                            <form action="" method="post">
                                <ul>
                                    <li class="item border-t userName"><input type="text"
                                                                              class="the_input topSpecial user_forget_phone"
                                                                              placeholder="请输入手机号" maxlength="11"/></li>
                                    <li class="item checkVerimg" style=""><input type="text" class="the_input ver-img"
                                                                                 maxlength="6" placeholder="请输入验证码"/><img
                                            class="verImg"></li>
                                    <li class="item border-b Verify"><input type="text" class="the_input verifycode"
                                                                            maxlength="6" placeholder="请输入短信验证码"/><a
                                            class="send_verify_code" id="send_verify_code_forget" href="javascript:;"
                                            rel="nofollow"><em>获取验证码</em></a></li>
                                    <li class="item border-t pwd" style="margin-top:-1px;"><input type="password"
                                                                                                  class="the_input password_reg"
                                                                                                  maxlength="20"
                                                                                                  placeholder="请输入密码（最少8位，数字+字母）"/><em
                                            class="password-view"></em></li>
                                    <li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a
                                            class="voice_a">发送语音验证码</a></li>
                                    <li class="show-error">
                                        <dd>用户名或密码错误</dd>
                                    </li>
                                    <li class="li_btn"><a class="user-forget"/>修改密码</a></li>
                                </ul>
                            </form>
                        </div>
                        <div id="con_forget_user_pw" class="con_forget_user_pw">
                            <form action="" method="post">
                                <ul>
                                    <li class="item border-t pwd"><input type="password" class="the_input password_reg"
                                                                         maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"/><em
                                            class="password-view"></em></li>
                                    <li class="show-error">
                                        <dd>用户名或密码错误</dd>
                                    </li>
                                    <li class="li_btn"><a class="modify-user-pswd"/>修改密码</a></li>
                                </ul>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="registered"></div>
            </div>
        </div>
        <!-- LianjiaIM Style -->
        <link property='stylesheet' rel="stylesheet"
              href="https://s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?_v=201709261333487"/>
        <script src="//s1.ljcdn.com/web-im-sdk/static/0.9/ljim-core.min.js?_v=20171010"></script>
        <script>(function () {
            var imConf = {
                "ajaxroot": "\/\/ajax.api.lianjia.com\/",
                "imAppid": "LIANJIA_WEB_20160624",
                "imAppkey": "6dfdcee27d78b1107fceeca55d80b7bd"
            };
            $.listener.on('userInfo', function (data) {
                if (data.code === 1) {
                    data.ucid = '';
                }
                require(['lianjiaIM/lianjiaim'], function (LianjiaIM) {
                    var ljim = new LianjiaIM({
                        appid: imConf.imAppid,
                        appkey: imConf.imAppkey,
                        userData: data,
                        staticRoot: 'https://s1.ljcdn.com/feroot/?_v=201709261333487'
                    });
                });
            });
        })();</script>
        <script type="text/javascript">var advert = 'https://s1.ljcdn.com/feroot/pc/asset/common/advert.js?_v=201709261333487';
        $.listener.on('userInfo', function (data) {
            window.loginData = data;
        });
        var mvl = document.createElement('script');
        mvl.type = 'text/javascript';
        mvl.async = true;
        mvl.src = advert;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(mvl, s);
        </script>
        <script type="text/javascript">(function () {
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            } else {
                bp.src = 'http://push.zhanzhang.baidu.com/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();</script><!--cookie mapping--><img
                src='https://cm.e.qq.com/cm.fcg?u=248b9273a849b4bc2bfa58b70247d90a&t=1507603325&p=5c75b4c74c2c2bdd920800e36eb777af&platform=PC&gdt_dspid=4169211&gdt_dsp_checksum=5c75b4c74c2c2bdd920800e36eb777af&gdt_dsp_timestamp=1507603325'
                alt="cookie_mapping_url" style="display: none;"></body>
        </html>
        """

        # 获取二手房列表信息
        # url = "https://gz.lianjia.com/ershoufang/"
        #url = "http://localhost:63342/lianjia-spider/data/ershoufang.html?_ijt=4jal28moed8rj6sqpn1835poh"
        #user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"
        #headers = {'User-Agent': user_agent}
        #r = requests.get(url, headers=headers)

        soup = BeautifulSoup(html_str, 'lxml', from_encoding='utf-8')
        soup.find_all(class_="clear")
        print soup.find_all(class_="clear")


    def list_spider(self):
        spider = ListSpider()
        print ""

if __name__ == '__main__':
    spider = ListSpider()
    spider.get_list_info()
