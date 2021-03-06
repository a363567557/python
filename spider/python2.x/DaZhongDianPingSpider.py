#!/usr/bin/python
#-*-coding:utf-8-*-

import requests
import json
from lxml import etree
import time
import random

class DaZhongDianPingSpider:

    def login(self,phone,vcode):
        """
            大众点评手机验证码登录
        :param phone:
        :param vcode:
        :return:
        """
        sess = requests.Session()
        headers = {
            "Accept": "* / *",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep - alive",
            "Content - Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": "_lxsdk_cuid=166d35ccccdc8-0fd2565130e023-8383268-144000-166d35ccccec8;" +
                      "_lxsdk=166d35ccccdc8-0fd2565130e023-8383268-144000-166d35ccccec8;" +
                      "_hc.v=2625f114-04d8-4f64-fe6f-92928895794d.1541144367;" +
                      "cy=2;cye=beijing;" +
                      "s_ViewType=10;" +
                      "ua=dpuser_59840002053;" +
                      "ctu=b84da022cc25cc9da5241a1b069ef30317d4969e87e26dbbc62190bc3f1fa4c5;" +
                      "_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic;" +
                      "ctu=37b04f2c26cafd3ecfcaf0f6c68962d2efbaf5c8b02f0d55542ade1d21aab291b5157f74c3cfdde6d8e43a481fa79ce0;" +
                      "_lxsdk_s=166d77243b9-282-2d8-7f5%7C%7C20",
            "Host": "account.dianping.com",
            "Origin": "https://account.dianping.com",
            "Referer": "https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com%2F",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        url = "https://account.dianping.com/account/ajax/mfastlogin"
        body = {"mobile": phone,
                "vcode": vcode,
                "channel": "13",
                "countrycode": "86",
                "type": "304",
                "keepMobile": "off",
                "_token": "eJy9lG1P20AMx79LJHh1as93uTxUQlMQMEKbLKOBiSHEkjS0GW0CSbaWTvvuc470ElA17dWkSv3ZvrPP9r/9pZXuTBtpQCnVbY1oP9OyMQd0YKBVV9oIhA4MmGWZ1GJESzofZ9QUJidaXF6faKNbZlPCTXHXOC7RvgXBDWIZ+h1pkSEynTRfWuziEW1R10/VaDiMkqT4kdeDWRblT1k+HyTFauccZg9ltEonxTzLPyTRchlHyePRaVS9SNe9jN7vAvRwnc3So4doWaWHT2VRF0mxPHqtc1ims6yUxgF3DtgZftbr9Zuq6MLO//qupXzJP+bCVldh0ypYBnbOMPkr8XdkviFdkoUkJNk7wiEz3ZAEipiiZrqmJKslRkERU6QrEorUDeCKjB0xdZfZO+JmW5fpoEgo6qKWIntHgrYd9YnJznFkj3JkNnH94CrEUKDoXNGDIl0RV8QUgaJveyhRtFAU74nOFUV7sqR7ovP/WA1HFvVVRo6vwvCT362hcwDuWQBxECmhxPU+Sicu0Da7UzauEboZNkLARI5STD+hTgkYRjdvU4q6d4DjAdFbDeMEaHfBtonQZW4ULbfIiXvd6gzA6N16Z/NGw9ArI1BcvF/XEgTFJRObBJ/stD+Ctn0wTcJRw9PA8ZsJ1s0Em0l6+B+I8Sqb50jpxSacVsLdevVkG5+Cf/Z1ss2G/vhl9Rx6IpjGX8A7CybhI60tD4KXanNRJxBMIZgsQscPP1Nve8P8ibv2T/zL8XheT+Mb6od+OF6fF973m42/dI7zbJHPtN9/AOI5ZuA="}


        response = sess.post(url, data = body, headers=headers)
        # print response.headers
        print response.text
        # print json.dumps(body)


    def foodList(self):
        """
            大众点评手机验证码登录
        :param phone:
        :param vcode:
        :return:
        """
        sess = requests.Session()
        headers = {
            "Accept": "* / *",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep - alive",
            "Content - Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": "_lxsdk_cuid=166d35ccccdc8-0fd2565130e023-8383268-144000-166d35ccccec8; _lxsdk=166d35ccccdc8-0fd2565130e023-8383268-144000-166d35ccccec8; _hc.v=2625f114-04d8-4f64-fe6f-92928895794d.1541144367; cy=2; cye=beijing; s_ViewType=10; ua=dpuser_59840002053; ctu=b84da022cc25cc9da5241a1b069ef30317d4969e87e26dbbc62190bc3f1fa4c5; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; dper=3243a17e768c1dee519a80b29158322a74be0e09e722feb49021650a87bc981155bbfc51a5c20e7712a5cf9fb1d0c7ed599a0d04129ad8636eeafd2b88dad642e61402366fee1f8e57df12658d20aaccfbf3cf66ea3c0ec9a0fd8fc3a3ef827a; ll=7fd06e815b796be3df069dec7836c3df; uamo=15017328307; _lxsdk_s=166d7a79329-f72-31c-bf3%7C%7C96",
            "Host": "www.dianping.com",
            "Origin": "https://account.dianping.com",
            "Referer": "https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com%2F",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        # url = "http://www.dianping.com/beijing/ch10"
        page = 2
        url = "http://www.dianping.com/beijing/ch10/p%d?aid=92020785&cpt=92020785"

        # body = {"mobile": phone,
        #         "vcode": vcode,
        #         "channel": "13",
        #         "countrycode": "86",
        #         "type": "304",
        #         "keepMobile": "off",
        #         "_token": "eJy9lG1P20AMx79LJHh1as93uTxUQlMQMEKbLKOBiSHEkjS0GW0CSbaWTvvuc470ElA17dWkSv3ZvrPP9r/9pZXuTBtpQCnVbY1oP9OyMQd0YKBVV9oIhA4MmGWZ1GJESzofZ9QUJidaXF6faKNbZlPCTXHXOC7RvgXBDWIZ+h1pkSEynTRfWuziEW1R10/VaDiMkqT4kdeDWRblT1k+HyTFauccZg9ltEonxTzLPyTRchlHyePRaVS9SNe9jN7vAvRwnc3So4doWaWHT2VRF0mxPHqtc1ims6yUxgF3DtgZftbr9Zuq6MLO//qupXzJP+bCVldh0ypYBnbOMPkr8XdkviFdkoUkJNk7wiEz3ZAEipiiZrqmJKslRkERU6QrEorUDeCKjB0xdZfZO+JmW5fpoEgo6qKWIntHgrYd9YnJznFkj3JkNnH94CrEUKDoXNGDIl0RV8QUgaJveyhRtFAU74nOFUV7sqR7ovP/WA1HFvVVRo6vwvCT362hcwDuWQBxECmhxPU+Sicu0Da7UzauEboZNkLARI5STD+hTgkYRjdvU4q6d4DjAdFbDeMEaHfBtonQZW4ULbfIiXvd6gzA6N16Z/NGw9ArI1BcvF/XEgTFJRObBJ/stD+Ctn0wTcJRw9PA8ZsJ1s0Em0l6+B+I8Sqb50jpxSacVsLdevVkG5+Cf/Z1ss2G/vhl9Rx6IpjGX8A7CybhI60tD4KXanNRJxBMIZgsQscPP1Nve8P8ibv2T/zL8XheT+Mb6od+OF6fF973m42/dI7zbJHPtN9/AOI5ZuA="}


        # response = sess.post(url, headers=headers)
        # print response.headers
        # print "kaishi"
        # print response.text
        #//div[@class='tit']/div[@class='promo-icon J_promo_icon']/a
        # print json.dumps(body)
        html = """<html>
<head>
    <link rel="icon" type="image/x-icon" href="//www.dpfile.com/app/pc-common/dp_favicon.a4af753914321c8e82e402e2b4be01d7.ico">
    <link rel="shortcut icon" type="image/x-icon" href="//www.dpfile.com/app/pc-common/dp_favicon.a4af753914321c8e82e402e2b4be01d7.ico">
    <title>【北京美食】推荐,美食排行/大全/攻略-大众点评网</title>
        <meta name="Keywords" content="北京美食推荐,美食排行榜,北京美食,美食,美食排行"/>
        <meta name="Description" content="附近好吃的美食有哪些,大众点评为您找到186014家好吃的美食餐厅,找北京美食,就上大众点评"/>
        <meta http-equiv="mobile-agent" content="format=html5; url=https://m.dianping.com/beijing/ch10">
        <link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.dianping.com/beijing/ch10">
    <meta charset="UTF-8"/>
    <script type="text/javascript">
        window._DP_HeaderData = {
            'cityId': '2',                   
            'cityChName': '北京',                 
            'cityEnName': 'beijing',               
            'pageType': 'search',                                           
            'userId': '806549341',                                    
            'userName': 'dpuser_59840002053',                                      
            'searchType': 'category',    
            'shopTypeChName': '美食',  
            'categoryId': '0',
        };
        window.IS_OVERSEAS_CITY = false;
    </script>
    <meta name="lx:category" content="dianping_nova">
    <meta name="lx:appnm" content="dp_pc">
    <meta name="lx:cid" content="c_0pd2xsxh">
    <meta name="lx:autopv" content="off"/>
    <link rel="dns-prefetch" href="//analytics.meituan.net"/>
    <script type="text/javascript">
        !(function (win, doc, ns) {
            var cacheFunName = '_MeiTuanALogObject';
            win[cacheFunName] = ns;
            if (!win[ns]) {
                var _LX = function () {
                    _LX.q.push(arguments);
                    return _LX;
                };
                _LX.q = _LX.q || [];
                _LX.l = +new Date();
                win[ns] = _LX;
            }
        })(window, document, 'LXAnalytics');
        var valLab = {
            "cat_id": window._DP_HeaderData.categoryId,
            "custom": {
                "city_id": window._DP_HeaderData.cityId,
                "user_id": window._DP_HeaderData.userId,
                "category": window._DP_HeaderData.shopTypeChName,
                "page_type": window._DP_HeaderData.searchType,
            }};
        var environment = {
            "uid": window._DP_HeaderData.userId,
            "cityid": window._DP_HeaderData.cityId,
        };
        LXAnalytics('pageView', valLab, environment);
    </script>
    <script src="//analytics.meituan.net/analytics.js" type="text/javascript" charset="utf-8" async defer></script>
    <link rel="canonical" href="http://www.dianping.com/beijing/ch10"  />
    <link rel="stylesheet" type="text/css" href="//www.dpfile.com/app/pc-common/index.min.25debddada2557bc6263bd51a17bfecf.css">
    <script type="text/javascript" src="//www.dpfile.com/app/pc-common/index.min.9863dfcc3f8cc8294df03522920025a9.js" ></script>
<link rel="stylesheet" href="//www.dpfile.com/mod/css-reset/1.0.0/css/index.css" type="text/css"/><link rel="stylesheet" href="//www.dpfile.com/concat/~mod~mbox~1.0.4~css~mbox.css,~mod~easy-login~0.4.39~css~account.css,~mod~easy-login~0.4.39~css~style.css,~mod~css-shop-tag~0.1.3~css~index.css,~mod~css-rating~1.0.2~css~index.css,~mod~main-authbox~1.0.9~css~index.css,~mod~css-shop-tag~1.0.1~css~index.css,~mod~app-midas~0.6.12~css~style.css,~mod~app-main-search~1.2.15~css~index.css" type="text/css"/><script type="text/javascript">
    function hasClass(a,b){return a.className.match(new RegExp("(\\s|^)"+b+"(\\s|$)"))}function addClass(a,b){this.hasClass(a,b)||(a.className+=" "+b)}function removeClass(a,b){if(hasClass(a,b)){var c=new RegExp("(\\s|^)"+b+"(\\s|$)");a.className=a.className.replace(c," ")}}function isOnlyOneLine(a){for(var b=a.length,c=0,d=0,e=0;b>c;c++){if(d=a[c].offsetLeft,e>d)return!1;e=d}return!0}function injectSecondaryNav(a,b){var d,e,c=getSecondaryNav(a);c&&(d=getLastDomIndexOfCurLine(b),e=b.length-1,e>d&&a.insertBefore(c,b[d+1]))}function getSecondaryNav(a){var c,b=a.getElementsByTagName("div");if(b&&b.length>0)for(c=b.length-1;c>=0;c--)if("common"==b[c].getAttribute("data-type"))return b[c];return null}function getCurDomIndex(a){for(var b=0,c=a.length;c>b;b++)if(/(^|\s)cur(\s|$)/.test(a[b].className))return b;return-1}function getLastDomIndexOfCurLine(a){for(var b=0,c=0,d=getCurDomIndex(a);d<a.length;d++){if(c=a[d].offsetLeft,b>c)return d-1;b=c}return a.length-1}function getLastDomOfFirstLine(a){var d,e,f,b=a.getElementsByTagName("a"),c=[];if(b)for(d=0;d<b.length;d++)"1"==b[d].getAttribute("data-rank")&&c.push(b[d]);if(isOnlyOneLine(c))return c[c.length-1];for(e=0,f=0,d=0,d=0;d<c.length;d++){if(f=c[d].offsetLeft,e>f)return c[d-1];e=f}}function isCurExist(a){for(var b=a.length,c=!0,d=0;b>d&&!hasClass(a[d],"cur");d++)d==b-1&&(c=!1);return c}function isCurDomInFirstLine(a){var d,b=0,c=0;for(d=0;d<a.length;d++){if(c=a[d].offsetLeft,/(^|\s)cur(\s|$)/.test(a[d].className))return!0;if(b>c)return!1;b=c}}function getLastDomIndexOfFirstLine(a){for(var b=0,c=0,d=0;d<a.length;d++){if(c=a[d].offsetLeft,b>c)return d-1;b=c}return a.length-1}function injectTheMoreLinkDom(a,b){var c,d,e,f,g;if(isCurDomInFirstLine(b)&&(c=getLastDomIndexOfFirstLine(b),d=b.length-1,d>c))for(e=document.createElement("A"),f=document.createElement("I"),f.setAttribute("class","packdown-arrow"),e.setAttribute("class","J_packdown packdown-sear"),e.appendChild(document.createTextNode("更多")),e.appendChild(f),a.insertBefore(e,b[c]),g=c;g<b.length;g++)addClass(b[g],"Hide")}function more(a){var d,e,b=a.getElementsByTagName("a"),c=[];if(b)for(d=0;d<b.length;d++)"1"==b[d].getAttribute("data-rank")&&c.push(b[d]);e=isOnlyOneLine(c),e||(injectSecondaryNav(a,c),injectTheMoreLinkDom(a,c))}function moreInner(a){var b,c,d,e,f,g;if(a&&(b=a.getElementsByTagName("a"),!isOnlyOneLine(b)&&(!isCurExist(b)||isCurDomInFirstLine(b))&&(c=getLastDomIndexOfFirstLine(b),d=b.length-1,d>c))){for(e=c;e<b.length;e++)addClass(b[e],"Hide");f=document.createElement("A"),g=document.createElement("I"),g.setAttribute("class","packdown-arrow"),f.setAttribute("class","J_navpackdown packdown-sear"),f.appendChild(document.createTextNode("更多")),f.appendChild(g),a.insertBefore(f,b[c])}}
</script>
<script type="text/javascript">
    function hasClass(obj, cls) {
        return obj.className.match(new RegExp("(\\s|^)" + cls + "(\\s|$)"));
    }
    function addClass(obj, cls) {
        if (!this.hasClass(obj, cls)) obj.className += " " + cls;
    }
    function removeClass(ele, cls) {
        if (hasClass(ele, cls)) {
            var reg = new RegExp("(\\s|^)" + cls + "(\\s|$)");
            ele.className = ele.className.replace(reg, " ");
        }
    }
    function setAttribute(o, a, v) {
        if (typeof o != 'object' || typeof a != 'string') return;
        a == 'class' ? o.className = v : o.setAttribute(a, v);
    }
    // 获取cookie
    function getCookie(name) {
        var cookieName = encodeURIComponent(name) + '=';
        var cookieStart = document.cookie.indexOf(cookieName);
        var cookieValue = null;
        if (cookieStart > -1) {
            var cookieEnd = document.cookie.indexOf(';', cookieStart);
            if (cookieEnd == -1) {
                cookieEnd = document.cookie.length;
            }
            cookieValue = decodeURIComponent(document.cookie.substring(cookieStart + cookieName.length, cookieEnd));
        }
        return cookieValue;
    }
    function isSetBtnMore(doms) {
        var len = doms.length,
                left = 0,
                preLeft = 0,
                line = 0;
        for (var i = 0; i < len; i++) {
            left = doms[i].offsetLeft;
            if (left < preLeft) line++;
            if (line > 1) return true;
            preLeft = left;
        }
        return false;
    }
    function setBtnMore(box, type) {
        var btnMore = document.createElement("a"),
                btnMoreIcon = document.createElement("i");

        switch (type) {
            case 'down':
                setAttribute(btnMoreIcon, "class", "icon-arr-extend");
                setAttribute(btnMore, 'class', "more J_packdown");
                btnMore.appendChild(document.createTextNode("更多"));
                break;
            case 'up':
                setAttribute(btnMoreIcon, "class", "icon-arr-packup");
                setAttribute(btnMore, 'class', "more J_packup");
                btnMore.appendChild(document.createTextNode("收起"));
                break;
        }
        setAttribute(btnMore, "href", "javascript:;");
        btnMore.appendChild(btnMoreIcon);
        box.appendChild(btnMore);
    }
    function more(container, opt) {
        if (!container) {
            return;
        }
        var all = container.getElementsByTagName('a'),
                doms = [];
        if (all) {
            for (var i = 0; i < all.length; i++) {
                doms.push(all[i]);
            }
        }
        var isSetBtnMoreResult = isSetBtnMore(doms);
        if (isSetBtnMoreResult) {
            addClass(container, 'nc-more');

            var len = doms.length,
                    left = 0,
                    preLeft = 0,
                    line = 0,
                    curNum = -1,
                    arrSecNum = [];
            // 查找cur所在位置&&确定第三行开始得位置
            for (var i = 0; i < len; i++) {
                left = doms[i].offsetLeft;
                if (left < preLeft) line++;
                if (doms[i].className == 'cur') curNum = i;
                if (line == 2) arrSecNum.push(i);
                preLeft = left;
            }

            if (opt == 'down' || curNum < arrSecNum[0] || curNum == -1) {
                setBtnMore(container, 'down');
                for (var i = arrSecNum[0]; i < len; i++) {
                    addClass(doms[i], 'Hide');
                }
            } else if (curNum >= arrSecNum[0]) {
                setBtnMore(container, 'up');
            }
        }
    }
</script>
    <script>
        (function(){
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https'){
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            }
            else{
                bp.src = 'http://push.zhanzhang.baidu.com/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
    </script>
</head>
<body>
    <!--页头部分-->
    <div class="header-container"><div id="top-nav" class="top-nav"> <div class="top-nav-container clearfix"> <div class="group mini-logo Hide"> <a rel="nofollow" target="_blank" class="item" href="http://www.dianping.com"><i class="icon-logo"></i>大众点评首页</a> </div> <div class="group quick-menu "> <a rel="nofollow" class="item write-dp" href="http://www.dianping.com/addreview/list">写点评</a> <span class="seprate">|</span> <span class="login-container J-login-container"> <a rel="nofollow" class="item " href="http://account.dianping.com/login" data-click-name="login">你好，请登录</a> <a rel="nofollow" class="item login" href="https://account.dianping.com/reg" data-click-name="reg">免费注册</a> </span> <span class="seprate">|</span> <a rel="nofollow" href="http://www.dianping.com/member/myinfo" class="item J-my-center-trigger">个人中心<i class="icon i-arrow"></i></a> <span class="seprate">|</span> <a target="_blank" class="item J-shop-serve-trigger">商户服务<i class="icon i-arrow"></i></a> <span class="seprate">|</span> <a target="_blank" class="item J-help-trigger">帮助中心<i class="icon i-arrow"></i></a> <span class="seprate">|</span> <a target="_blank" class="item J-brower-trigger Hide">最近浏览<i class="icon i-arrow"></i></a> <a target="_blank" class="item J-site-trigger">网站导航<i class="icon i-arrow"></i></a> </div> <div class="panel my-center J-my-center-target Hide"> </div> <div class="panel my-center J-shop-serve-target Hide"> <a rel="nofollow" target="_blank" href="https://e.dianping.com/" data-click-name="shop-center">商户中心</a> <a rel="nofollow" target="_blank" href="https://e.dianping.com/claimcpc/page/index?source=dp" data-click-name="shop-coop">商户合作</a> <a rel="nofollow" class="shop-item" target="_blank" href="http://wang.dianping.com" data-click-name="wang">旺铺宝</a> <a rel="nofollow" target="_blank" href="https://daili.meituan.com/?comeFrom=dpwebMenu" data-click-name="daili">招募餐饮代理</a> <a rel="nofollow" target="_blank" href="http://www.dianping.com/apollo/agent/index?source=dppc" data-click-name="apollo">招募非餐饮代理</a> </div> <div class="panel my-center J-help-target Hide"> <a rel="nofollow" target="_blank" href="http://www.dianping.com/help/center" data-click-name="useragreement">平台规则</a> <a rel="nofollow" target="_blank" href="http://kf.dianping.com" data-click-name="kf">联系客服</a> </div> <div class="panel site-nav J-site-target Hide"> </div> </div> </div>
<div id="logo-input" class="logo-input food-conf">
    <div class="logo-input-container clearfix">
<a title="大众点评网" href="/" class="logo logo-food"></a> <a target="_blank" class="city J-city"><span class="map-icon"></span><span>北京</span><i class="icon i-arrow"></i></a> <div class="city-list J-city-list Hide"> <div class="group clearfix"> <h3 class="title">国内城市</h3> <div> <a href="//www.dianping.com/shanghai/food" class="city-item">上海</a> <a href="//www.dianping.com/beijing/food" class="city-item">北京</a> <a href="//www.dianping.com/guangzhou/food" class="city-item">广州</a> <a href="//www.dianping.com/shenzhen/food" class="city-item">深圳</a> <a href="//www.dianping.com/tianjin/food" class="city-item">天津</a> <a href="//www.dianping.com/hangzhou/food" class="city-item">杭州</a> <a href="//www.dianping.com/nanjing/food" class="city-item">南京</a> <a href="//www.dianping.com/suzhou/food" class="city-item">苏州</a> <a href="//www.dianping.com/chengdu/food" class="city-item">成都</a> <a href="//www.dianping.com/wuhan/food" class="city-item">武汉</a> <a href="//www.dianping.com/chongqing/food" class="city-item">重庆</a> <a href="//www.dianping.com/xian/food" class="city-item">西安</a> </div> </div> <div class="group clearfix"> <h3 class="title">国外城市</h3> <div> <a href="//www.dianping.com/tokyo" class="city-item">东京</a> <a href="//www.dianping.com/seoul" class="city-item">首尔</a> <a href="//www.dianping.com/bangkok" class="city-item">曼谷</a> <a href="//www.dianping.com/paris" class="city-item">巴黎</a> </div> </div> <a class="all" href="//www.dianping.com/citylist">更多城市 ></a> </div>
<div class="search-box"> <div class="search-bar "> <span class="search-container clearfix"> <i class="i-search"></i> <span> <input id="J-search-input" class="J-search-input" x-webkit-speech="" x-webkit-grammar="builtin:translate" data-s-pattern="https://www.dianping.com/search/keyword/{0}/{1}_" data-s-epattern="https://www.dianping.com/beijing/{0}" data-s-cateid="0" data-s-cityid="1" type="text" placeholder="搜索商户名、地址、菜名、外卖等" autocomplete="off" /> </span> <span class="search-bnt-panel"> <a target="_blank" class="search-btn search-channel-bnt J-search-btn" id="J-channel-bnt" data-s-chanid="10">搜美食</a> <a target="_blank" class="search-btn search-all-bnt J-search-btn" id="J-all-btn" data-s-chanid="0">搜全站</a> </span> </span> <p class="hot-search J-hot-search"> </p> </div> </div> <div class="qrcode-container"> <i class="close"></i> <div class="qrcode"> <p class="qrcode-text">手机点评</p> <div class="qrcode-img"></div> </div> </div>    </div>
</div>


<div id="cate-channel" class="cate-container channel-cate-container food-conf">
<div class="nav-header"> <div class="navbar"> <span class="cate-item all-cate J-all-cate">全部美食分类 <i class="primary-more"></i> </span> <a target="_blank" class="cate-item other-cate " href="http://t.dianping.com/beijing" data-click-title="row-nav" data-click-name="团购">团购</a> <a target="_blank" class="cate-item other-cate " href="http://s.dianping.com/event/beijing" data-click-title="row-nav" data-click-name="霸王餐">霸王餐</a> <i class = "hot-icon"></i> <a target="_blank" class="cate-item other-cate " href="http://s.dianping.com/beijing/group?utm_source=dp_pc_food" data-click-title="row-nav" data-click-name="社区论坛">社区论坛</a> </div> </div> <div class="gradient"></div>
<div id="cate-index" class="cate-index"> <div class="navwrap"> <div id="nav" > <div class="cate-nav J-cate-nav Hidden"> <ul class="first-cate J-primary-menu"> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">异国料理</a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g116" data-category="food.excticfood" data-click-title="second" data-click-name="g116"><span>西餐</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g113" data-category="food.excticfood" data-click-title="second" data-click-name="g113"><span>日本菜</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.food.excticfood" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">异国料理</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g116" data-category="food.excticfood" data-click-name="g116">西餐</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g113" data-category="food.excticfood" data-click-name="g113">日本菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g114" data-category="food.excticfood" data-click-name="g114">韩国料理</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g115" data-category="food.excticfood" data-click-name="g115">东南亚菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g111" data-category="food.excticfood" data-click-name="g111">自助餐</a> </div> </div> </div> </div> </li> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">中式料理</a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g110" data-category="food.chinesefood" data-click-title="second" data-click-name="g110"><span>火锅</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g101" data-category="food.chinesefood" data-click-title="second" data-click-name="g101"><span>本帮江浙菜</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.food.chinesefood" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">中式料理</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g110" data-category="food.chinesefood" data-click-name="g110">火锅</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g101" data-category="food.chinesefood" data-click-name="g101">本帮江浙菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g102" data-category="food.chinesefood" data-click-name="g102">川菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g103" data-category="food.chinesefood" data-click-name="g103">粤菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g104" data-category="food.chinesefood" data-click-name="g104">湘菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g3243" data-category="food.chinesefood" data-click-name="g3243">新疆菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g248" data-category="food.chinesefood" data-click-name="g248">云南菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g106" data-category="food.chinesefood" data-click-name="g106">东北菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g105" data-category="food.chinesefood" data-click-name="g105">贵州菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g26481" data-category="food.chinesefood" data-click-name="g26481">西北菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g107" data-category="food.chinesefood" data-click-name="g107">台湾菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g247" data-category="food.chinesefood" data-click-name="g247">江西菜</a> </div> </div> </div> </div> </li> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">小吃夜宵</a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g508" data-category="food.snack" data-click-title="second" data-click-name="g508"><span>烧烤</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g251" data-category="food.snack" data-click-title="second" data-click-name="g251"><span>海鲜</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.food.snack" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">小吃夜宵</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g508" data-category="food.snack" data-click-name="g508">烧烤</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g251" data-category="food.snack" data-click-name="g251">海鲜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g219" data-category="food.snack" data-click-name="g219">小龙虾</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g203" data-category="food.snack" data-click-name="g203">蟹宴</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g112" data-category="food.snack" data-click-name="g112">小吃快餐</a> </div> </div> </div> </div> </li> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">饮品甜点</a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g132" data-category="food.dessert" data-click-title="second" data-click-name="g132"><span>咖啡厅</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g117" data-category="food.dessert" data-click-title="second" data-click-name="g117"><span>面包甜点</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.food.dessert" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">饮品甜点</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g132" data-category="food.dessert" data-click-name="g132">咖啡厅</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g117" data-category="food.dessert" data-click-name="g117">面包甜点</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g34014" data-category="food.dessert" data-click-name="g34014">下午茶</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g34015" data-category="food.dessert" data-click-name="g34015">Brunch</a> </div> </div> </div> </div> </li> <li class="first-item"> <div class="primary-container"> <span class="span-container"> <a target="_blank" class="index-title">其他</a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g109" data-category="food.others" data-click-title="second" data-click-name="g109"><span>素菜</span></a> <a target="_blank" class="index-item" href="http://www.dianping.com/beijing/ch10/g215" data-category="food.others" data-click-title="second" data-click-name="g215"><span>面馆</span></a> </span> </div> <div class="sec-cate Hide" data-category="cate.food.others" > <div class="groups"> <div class="group"> <div class="sec-title"> <span class="channel-title" href="">其他</span> </div> <div class="sec-items"> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g109" data-category="food.others" data-click-name="g109">素菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g215" data-category="food.others" data-click-name="g215">面馆</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g1783" data-category="food.others" data-click-name="g1783">家常菜</a> <a target="_blank" class="second-item" href="http://www.dianping.com/beijing/ch10/g118" data-category="food.others" data-click-name="g118">其他</a> </div> </div> </div> </div> </li> </ul> </div> </div> </div> </div></div></div>
    <div class="section Fix J-shop-search">
        




            <div class="bread J_bread">

                        
                                <span>
                                    <a itemscope itemtype="http://data-vocabulary.org/Breadcrumb"  data-ga-index="1"
                                         href="/beijing/ch10" itemprop="url">
                                        <span itemprop="title">
                                            北京美食
                                        </span>
                                    </a>
                                </span>


            </div>



        <div class="navigation">
        <!-- 频道 -->
<!-- 频道 end -->

<!-- 分类 -->
<div class="nav-category J_filter_category">
    <h4>分类:</h4>
    <a href="http://www.dianping.com/beijing/ch10" class="def cur" data-cat-id="0" data-click-name="select_cate_all_click"><span>不限</span></a>
    <div class="nc-contain">
        <div class="con">
            <div id="classfy" class="nc-items">
                <a href="http://www.dianping.com/beijing/ch10/g508"  data-cat-id="508" data-click-name="select_cate_烧烤_click"><span>烧烤</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g117"  data-cat-id="117" data-click-name="select_cate_面包甜点_click"><span>面包甜点</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g110"  data-cat-id="110" data-click-name="select_cate_火锅_click"><span>火锅</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g112"  data-cat-id="112" data-click-name="select_cate_小吃快餐_click"><span>小吃快餐</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g111"  data-cat-id="111" data-click-name="select_cate_自助餐_click"><span>自助餐</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g113"  data-cat-id="113" data-click-name="select_cate_日本菜_click"><span>日本菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g116"  data-cat-id="116" data-click-name="select_cate_西餐_click"><span>西餐</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g34014"  data-cat-id="34014" data-click-name="select_cate_下午茶_click"><span>下午茶</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g311"  data-cat-id="311" data-click-name="select_cate_北京菜_click"><span>北京菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g114"  data-cat-id="114" data-click-name="select_cate_韩国料理_click"><span>韩国料理</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g115"  data-cat-id="115" data-click-name="select_cate_东南亚菜_click"><span>东南亚菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g118"  data-cat-id="118" data-click-name="select_cate_其他美食_click"><span>其他美食</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g103"  data-cat-id="103" data-click-name="select_cate_粤菜_click"><span>粤菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g102"  data-cat-id="102" data-click-name="select_cate_川菜_click"><span>川菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g251"  data-cat-id="251" data-click-name="select_cate_海鲜_click"><span>海鲜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g219"  data-cat-id="219" data-click-name="select_cate_小龙虾_click"><span>小龙虾</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g104"  data-cat-id="104" data-click-name="select_cate_湘菜_click"><span>湘菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g248"  data-cat-id="248" data-click-name="select_cate_云南菜_click"><span>云南菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g1817"  data-cat-id="1817" data-click-name="select_cate_粉面馆_click"><span>粉面馆</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g101"  data-cat-id="101" data-click-name="select_cate_江浙菜_click"><span>江浙菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g4473"  data-cat-id="4473" data-click-name="select_cate_烤鱼_click"><span>烤鱼</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g3243"  data-cat-id="3243" data-click-name="select_cate_新疆菜_click"><span>新疆菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g106"  data-cat-id="106" data-click-name="select_cate_东北菜_click"><span>东北菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g109"  data-cat-id="109" data-click-name="select_cate_素菜_click"><span>素菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g34032"  data-cat-id="34032" data-click-name="select_cate_人气餐厅_click"><span>人气餐厅</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g1845"  data-cat-id="1845" data-click-name="select_cate_俄罗斯菜_click"><span>俄罗斯菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g26482"  data-cat-id="26482" data-click-name="select_cate_徽菜_click"><span>徽菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g105"  data-cat-id="105" data-click-name="select_cate_贵州菜_click"><span>贵州菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g34055"  data-cat-id="34055" data-click-name="select_cate_早茶_click"><span>早茶</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g250"  data-cat-id="250" data-click-name="select_cate_创意菜_click"><span>创意菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g26483"  data-cat-id="26483" data-click-name="select_cate_鲁菜_click"><span>鲁菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g246"  data-cat-id="246" data-click-name="select_cate_湖北菜_click"><span>湖北菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g26481"  data-cat-id="26481" data-click-name="select_cate_西北菜_click"><span>西北菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g1783"  data-cat-id="1783" data-click-name="select_cate_家常菜_click"><span>家常菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g1338"  data-cat-id="1338" data-click-name="select_cate_私房菜_click"><span>私房菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g107"  data-cat-id="107" data-click-name="select_cate_台湾菜_click"><span>台湾菜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g2714"  data-cat-id="2714" data-click-name="select_cate_水果生鲜_click"><span>水果生鲜</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g33759"  data-cat-id="33759" data-click-name="select_cate_食品保健_click"><span>食品保健</span></a>
                <a href="http://www.dianping.com/beijing/ch10/g34236"  data-cat-id="34236" data-click-name="select_cate_饮品店_click"><span>饮品店</span></a>
            </div>

        </div>
    </div>
</div>
<!-- 分类 end -->





<!-- 推荐 -->
<div class="nav-category J_filter_recomm">
    <h4>推荐:</h4>
    <a href="http://www.dianping.com/beijing/ch10" data-click-name="select_rec_all_click" data-cat-id="0" class="def cur"><span>不限</span></a>
    <div class="nc-contain">
        <div class="con">
            <div id="recom-food" class="nc-items">
                <a rel="nofollow" data-click-name="select_rec_意大利面_click" data-cat-id="355" href="http://www.dianping.com/beijing/ch10/q355" ><span>意大利面</span></a>
                <a rel="nofollow" data-click-name="select_rec_色拉_click" data-cat-id="354" href="http://www.dianping.com/beijing/ch10/q354" ><span>色拉</span></a>
                <a rel="nofollow" data-click-name="select_rec_响油鳝糊_click" data-cat-id="469" href="http://www.dianping.com/beijing/ch10/q469" ><span>响油鳝糊</span></a>
                <a rel="nofollow" data-click-name="select_rec_虾饺皇_click" data-cat-id="89" href="http://www.dianping.com/beijing/ch10/q89" ><span>虾饺皇</span></a>
                <a rel="nofollow" data-click-name="select_rec_哈根达斯_click" data-cat-id="238" href="http://www.dianping.com/beijing/ch10/q238" ><span>哈根达斯</span></a>
                <a rel="nofollow" data-click-name="select_rec_牛排_click" data-cat-id="243" href="http://www.dianping.com/beijing/ch10/q243" ><span>牛排</span></a>
                <a rel="nofollow" data-click-name="select_rec_松鼠桂鱼_click" data-cat-id="475" href="http://www.dianping.com/beijing/ch10/q475" ><span>松鼠桂鱼</span></a>
            </div>
        </div>
    </div>
</div>

<!-- 推荐 end -->

<script type="text/javascript">
    more(document.getElementById('classfy'));
    more(document.getElementById('classfy-sub'));
    more(document.getElementById('recom-food'));
</script>
        <div class="nav-category nav-tabs J_filter_region">
        <h4>地点:</h4>
        <a href="http://www.dianping.com/beijing/ch10" class="def cur"><span>不限</span></a>
        <div class="nc-contain">
            <div id='J_nav_tabs' class="tabs">
                <a href="javascript:;" nav="#nav-tab|0|0" data-click-name="select_reg_hot_click" data-click-title="hot"><span class="tit">热门商区</span></a>
                <a href="javascript:;" nav="#nav-tab|0|1" data-click-name="select_reg_biz_click" data-click-title="biz"><span class="tit">行政区</span></a>
                    <a href="javascript:;" nav="#nav-tab|0|2" data-click-name="select_reg_metro_click" data-click-title="metro"><span class="tit">地铁线</span></a>
            </div>
            <div id="J_nt_items" class="con">
                <div id="bussi-nav" class="nc-items">
                        <a href="http://www.dianping.com/beijing/ch10/r2578" data-cat-id="2578" data-click-name="select_reg_hot_click" data-click-title="国贸" ><span>国贸</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2580" data-cat-id="2580" data-click-name="select_reg_hot_click" data-click-title="三里屯" ><span>三里屯</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r23023" data-cat-id="23023" data-click-name="select_reg_hot_click" data-click-title="南锣鼓巷/鼓楼东大街" ><span>南锣鼓巷/鼓楼东大街</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1475" data-cat-id="1475" data-click-name="select_reg_hot_click" data-click-title="王府井/东单" ><span>王府井/东单</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1488" data-cat-id="1488" data-click-name="select_reg_hot_click" data-click-title="中关村" ><span>中关村</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1489" data-cat-id="1489" data-click-name="select_reg_hot_click" data-click-title="五道口" ><span>五道口</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1470" data-cat-id="1470" data-click-name="select_reg_hot_click" data-click-title="亚运村" ><span>亚运村</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2872" data-cat-id="2872" data-click-name="select_reg_hot_click" data-click-title="远大路" ><span>远大路</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2588" data-cat-id="2588" data-click-name="select_reg_hot_click" data-click-title="五棵松" ><span>五棵松</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r23002" data-cat-id="23002" data-click-name="select_reg_hot_click" data-click-title="工人体育场" ><span>工人体育场</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1471" data-cat-id="1471" data-click-name="select_reg_hot_click" data-click-title="望京" ><span>望京</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2078" data-cat-id="2078" data-click-name="select_reg_hot_click" data-click-title="大望路" ><span>大望路</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1495" data-cat-id="1495" data-click-name="select_reg_hot_click" data-click-title="航天桥" ><span>航天桥</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1466" data-cat-id="1466" data-click-name="select_reg_hot_click" data-click-title="朝外大街" ><span>朝外大街</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r1469" data-cat-id="1469" data-click-name="select_reg_hot_click" data-click-title="亮马桥/三元桥" ><span>亮马桥/三元桥</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r23010" data-cat-id="23010" data-click-name="select_reg_hot_click" data-click-title="蓝色港湾" ><span>蓝色港湾</span></a>
                </div>
                <div id="region-nav" class="nc-items">
                            <a href="http://www.dianping.com/beijing/ch10/r16" data-cat-id="16" data-click-name="select_reg_biz_click" data-click-title="西城区" ><span>西城区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r17" data-cat-id="17" data-click-name="select_reg_biz_click" data-click-title="海淀区" ><span>海淀区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r15" data-cat-id="15" data-click-name="select_reg_biz_click" data-click-title="东城区" ><span>东城区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r328" data-cat-id="328" data-click-name="select_reg_biz_click" data-click-title="石景山区" ><span>石景山区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r14" data-cat-id="14" data-click-name="select_reg_biz_click" data-click-title="朝阳区" ><span>朝阳区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r20" data-cat-id="20" data-click-name="select_reg_biz_click" data-click-title="丰台区" ><span>丰台区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r9158" data-cat-id="9158" data-click-name="select_reg_biz_click" data-click-title="顺义区" ><span>顺义区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r9157" data-cat-id="9157" data-click-name="select_reg_biz_click" data-click-title="房山区" ><span>房山区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r5952" data-cat-id="5952" data-click-name="select_reg_biz_click" data-click-title="大兴区" ><span>大兴区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r5950" data-cat-id="5950" data-click-name="select_reg_biz_click" data-click-title="昌平区" ><span>昌平区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/r5951" data-cat-id="5951" data-click-name="select_reg_biz_click" data-click-title="通州区" ><span>通州区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/c434" data-cat-id="434" data-click-name="select_reg_biz_click" data-click-title="密云区" ><span>密云区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/c4453" data-cat-id="4453" data-click-name="select_reg_biz_click" data-click-title="怀柔区" ><span>怀柔区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/c4455" data-cat-id="4455" data-click-name="select_reg_biz_click" data-click-title="平谷区" ><span>平谷区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/c435" data-cat-id="435" data-click-name="select_reg_biz_click" data-click-title="延庆区" ><span>延庆区</span></a>
                            <a href="http://www.dianping.com/beijing/ch10/c4454" data-cat-id="4454" data-click-name="select_reg_biz_click" data-click-title="门头沟区" ><span>门头沟区</span></a>
                </div>
                <div id="metro-nav" class="nc-items">
                        <a href="http://www.dianping.com/beijing/ch10/r82085" data-cat-id="82085" data-click-name="select_reg_metro_click" data-click-title="16号线" ><span>16号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2179" data-cat-id="2179" data-click-name="select_reg_metro_click" data-click-title="1号线" ><span>1号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2180" data-cat-id="2180" data-click-name="select_reg_metro_click" data-click-title="2号线" ><span>2号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r3057" data-cat-id="3057" data-click-name="select_reg_metro_click" data-click-title="4号线" ><span>4号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2181" data-cat-id="2181" data-click-name="select_reg_metro_click" data-click-title="5号线" ><span>5号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r8095" data-cat-id="8095" data-click-name="select_reg_metro_click" data-click-title="6号线" ><span>6号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r66748" data-cat-id="66748" data-click-name="select_reg_metro_click" data-click-title="7号线" ><span>7号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r7643" data-cat-id="7643" data-click-name="select_reg_metro_click" data-click-title="8号线" ><span>8号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r7644" data-cat-id="7644" data-click-name="select_reg_metro_click" data-click-title="9号线" ><span>9号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2507" data-cat-id="2507" data-click-name="select_reg_metro_click" data-click-title="10号线" ><span>10号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r2182" data-cat-id="2182" data-click-name="select_reg_metro_click" data-click-title="13号线" ><span>13号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r8687" data-cat-id="8687" data-click-name="select_reg_metro_click" data-click-title="14号线" ><span>14号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r6962" data-cat-id="6962" data-click-name="select_reg_metro_click" data-click-title="15号线" ><span>15号线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r6961" data-cat-id="6961" data-click-name="select_reg_metro_click" data-click-title="昌平线" ><span>昌平线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r6965" data-cat-id="6965" data-click-name="select_reg_metro_click" data-click-title="亦庄线" ><span>亦庄线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r6963" data-cat-id="6963" data-click-name="select_reg_metro_click" data-click-title="房山线" ><span>房山线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r8195" data-cat-id="8195" data-click-name="select_reg_metro_click" data-click-title="八通线" ><span>八通线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r8196" data-cat-id="8196" data-click-name="select_reg_metro_click" data-click-title="机场线" ><span>机场线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r85496" data-cat-id="85496" data-click-name="select_reg_metro_click" data-click-title="S1线" ><span>S1线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r85812" data-cat-id="85812" data-click-name="select_reg_metro_click" data-click-title="西郊线" ><span>西郊线</span></a>
                        <a href="http://www.dianping.com/beijing/ch10/r85819" data-cat-id="85819" data-click-name="select_reg_metro_click" data-click-title="燕房线" ><span>燕房线</span></a>
                </div>


            </div>
        </div>
    </div>
    <!-- 地点 end -->
<!-- navigation end -->
<script type="text/javascript">
    more(document.getElementById('bussi-nav'));
    more(document.getElementById('bussi-nav-sub'));
    more(document.getElementById('region-nav'));
    more(document.getElementById('region-nav-sub'));
    more(document.getElementById('metro-nav'));
    more(document.getElementById('metro-nav-sub'));
     (function(){
            var tabs = document.getElementById('J_nav_tabs').getElementsByTagName('a'),
                doms = document.getElementById('J_nt_items').getElementsByTagName('div'),
                curIndex = 0,
                items = document.getElementById('J_nt_items').getElementsByTagName('a');

            var tagOpenFlag = false;



            // 获取跳转过来得nav
            if (getCookie('showNav') != null) {
                curIndex = getCookie('showNav').substr(getCookie('showNav').length - 1, getCookie('showNav').length);
                try {
                    curIndex = parseInt(curIndex);
                    if (isNaN(curIndex)) {
                        curIndex = 0;
                    }
                } catch (e) {
                    curIndex = 0;
                    document.cookie = 'showNav=' + tabs[0].getAttribute('nav');
                }
            }

            for(var i=0; i<items.length; i++) {
                 items[i].onclick = function () {
                     for(var dataTT=0; dataTT<tabs.length; dataTT++) {
                         if(hasClass(tabs[dataTT],'cur')){
                             document.cookie = 'showNav=' + tabs[dataTT].getAttribute('nav');
                         }
                     }
                 }
            }

            // set doms hide
            for (var dataTmp = 0; dataTmp < doms.length; dataTmp++) {
                addClass(doms[dataTmp], 'Hide');
            }
            (function(j) {
                if(doms[j] != null && doms.length > 0) {
                    var curEle = doms[j].id,
                            initNavEle = document.getElementById(curEle);

                    if (initNavEle.getElementsByTagName('a').length == 0) {
                        addClass(tabs[j], 'Hide');
                        j += 1;
                    }
                    curSubName = doms[j].id + '-sub';
//                curSubName = doms[j].getAttribute('id') + '-sub';


                    if (document.getElementById(curSubName)) {
                        removeClass(document.getElementById(curSubName), 'Hide');
                    } else {
                        j = 0;
                    }

                    addClass(tabs[j], 'cur');
                    removeClass(doms[j], 'Hide');

                    for (var i = 0; i < tabs.length; i++) {
                        if (doms[i].getElementsByTagName('a').length == 0) {
                            addClass(tabs[i], 'Hide');
                        }
                    }
                }
            })(curIndex);
        })();
</script>
        </div>
        <div class="content-wrap">
            <div class="shop-wrap">
                <div class="content">
                        <div class="filter-box J_filter_box">
    <!-- classify -->
    <div class="filt-classify">
        <a href="http://www.dianping.com/beijing/ch10/m3" rel="nofollow" data-click-name="filter_booking_click" class=" "><i class="icon-check"></i>有团购<i class="icon-hot"></i></a>

        <a href="http://www.dianping.com/beijing/ch10/m5" rel="nofollow" data-click-name="filter_price_click" class=" " ><i class="icon-check"></i>可订座</a>

        <a href="http://www.dianping.com/beijing/ch10/m6" rel="nofollow" class=" "><i class="icon-check"></i>可外卖</a>
    </div>
    <!-- classify end -->
    <!-- service -->
    <div class="filt-service">
        <ul>
            <li><a href="http://www.dianping.com/beijing/ch10" rel="nofollow" class="cur" data-click-name="sort_default_click">智能</a><em class="sep">|</em></li>
            <li><a href="http://www.dianping.com/beijing/ch10/o3" rel="nofollow"  data-click-name="sort_review_click">好评<i class="icon-arr-down"></i></a><em class="sep">|</em></li>
            <li><a href="http://www.dianping.com/beijing/ch10/o2" rel="nofollow"  data-click-name="sort_hot_click">人气<i class="icon-arr-down"></i></a><em class="sep">|</em></li>
                <li><a href="http://www.dianping.com/beijing/ch10/o4" rel="nofollow"  data-click-name="sort_custom_口味_click">口味<i class="icon-arr-down"></i></a><em class="sep">|</em></li>
                <li class="fs-slt">
                    <a href="##"  >其他排序<i class="icon-arr-extend"></i></a>
                    <em class="sep">|</em>
                    <div class="slt-list">
                        <span class="tit">其他排序<i class="icon-arr-packup"></i></span>
                                <a href="http://www.dianping.com/beijing/ch10/o11" rel="nofollow" data-order="2" data-click-name="sort_other_点评最多_click">点评最多</a>
                                <a href="http://www.dianping.com/beijing/ch10/o5" rel="nofollow" data-order="2" data-click-name="sort_other_环境最佳_click">环境最佳</a>
                                <a href="http://www.dianping.com/beijing/ch10/o6" rel="nofollow" data-order="2" data-click-name="sort_other_服务最佳_click">服务最佳</a>
                                <a href="http://www.dianping.com/beijing/ch10/o13" rel="nofollow" data-order="2" data-click-name="sort_other_预订优先_click">预订优先</a>
                    </div>
                </li>

            <li class="fs-slt">
                <a  href="##" class="fs-price-tit " ><span class="avgprice"> 人均<i class="icon-arr-extend"></i></span></a>
                <div class="slt-list per-capita">
                    <span class="tit">人均<i class="icon-arr-packup"></i></span>

                    <a href="http://www.dianping.com/beijing/ch10/o9" data-click-name="sort_avgprice_max_click" rel="nofollow" title="">人均最高</a>
                    <a href="http://www.dianping.com/beijing/ch10/o8" data-click-name="sort_avgprice_min_click" rel="nofollow" title="">人均最低</a>

                    <div class="ipt-price J_bar-range">
                        <span class="i-box"><span class="icon">¥</span><input class="J_range-min" type="text" value=""></span>
                        <span>-</span>
                        <span class="i-box"><span class="icon">¥</span><input class="J_range-max" type="text" value=""></span>
                        <div class="btn-box">
                            <a href="javascript:void(0);" data-click-name="sort_avgprice_custom_click" title="" class="confirm J_range-btn" data-url="/beijing/ch10/{0}">确定</a>
                            <a href="javascript:void(0);" title="" class="reset J_range-reset">重置</a>
                        </div>
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <!-- service end -->
    <a href="http://www.dianping.com/search/map/category/2/10" rel="nofollow" target="_blank" class="map"><i class="icon-map"></i></a>
</div>
                    
<div class="shop-list J_shop-list shop-all-list" id="shop-all-list">
  <ul>
  <li class="" data-midas="sver%3D2%26ad_ci%3DmmGX23iicHdxKI-GyMghWT5jc9mIZF0J8geGSVWS7Ovn78Mn128OgO4Fu08wbUClIrsWRngn782t%26ad_v%3D1%26ad_cj%3DmmGX23iwrMshTraBRyAmBfiVwnywFKmpj1ERJ68EUf_A5s_iUQlL6vDFE7OFkdto7MoKjxGcY5LUjm4m_bzqmv7YIUlvTsABN-GkLA13HxxyP8iHzbOlbMOyQe_bUyQAAgz7lWFBs18wV02GPjQTIxP44p3Im_6ZXaIXw9ZKMESK15QBaAlBwhZwK1G8ntxrAAWYIvYZBw">
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/92020785" data-click-name="shop_img_click" data-shopid="92020785"  title="" data-midas-extends="module=5_ad_kwimg" >
        <img title="潮汕古巷牛肉火锅(木樨园店)" alt="潮汕古巷牛肉火锅(木樨园店)" data-src="https://img.meituan.net/msmerchant/3c7ff63071e81e371b76bcf31566d2f21170209.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/3c7ff63071e81e371b76bcf31566d2f21170209.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:1,cl_a:40,cl_k:1272416,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',92020785);" data-click-name="shop_title_click" data-shopid="92020785" data-hippo-type="shop" title="潮汕古巷牛肉火锅(木樨园店)" target="_blank" href="http://www.dianping.com/shop/92020785" data-midas-extends="module=5_ad_kwtitle" >
            <h4>潮汕古巷牛肉火锅(木樨园店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="92020785"
                target="_blank" href="http://t.dianping.com/deal/25340918" title="潮汕古巷牛肉火锅!仅售238元！价值274元的潮汕B套餐，建议3人使用，提供免费WiFi。"  class="igroup" data-midas-extends="module=5_ad_kwicon1"
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="25340918">
              </a>

              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/92020785#promo=0" title=""
                  class="ipromote " 
                  data-click-name="shop_icon_shortdeal_click" data-shopid="92020785"
                  data-midas-extends="module=5_ad_kwicon2"
                ></a>




              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/92020785#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="92020785" class="ibook "
                title="" 
                data-midas-extends="module=5_ad_kwicon4"  >
              </a>


            <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/92020785#waimai" data-click-name="shop_icon_takeaway_click" data-shopid="92020785"
               class="iout " title="本店支持在线下单，足不出户，外送到家！"
                data-midas-extends="module=5_ad_kwicon5">
            </a>
        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b67633981" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="92020785"
              data-midas-extends="module=5_ad_kwbranch">
          分店
          </a>

            <a target="_blank" href="http://www.dianping.com/business" data-click-name="shop_icon_ad_click" data-shopid="92020785" class="search-ad" data-midas-extends="module=5_ad_kwtg">广告</a>

      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str45" title="准五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/92020785#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="92020785" target="_blank" module="list-readreview" data-midas-extends="module=5_ad_kwreview"
              rel="nofollow">
              <b>528</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/92020785" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="92020785" target="_blank" rel="nofollow" data-midas-extends="module=5_ad_kwprice">
            人均
            <b>￥106</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g110" data-click-name="shop_tag_cate_click" data-shopid="92020785" data-midas-extends="module=5_ad_kwcat"><span class="tag">火锅</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r1995" data-click-name="shop_tag_region_click" data-shopid="92020785" data-midas-extends="module=5_ad_kwregion"><span class="tag">洋桥/木樨园</span></a>
        <span class="addr">永外路果园7号楼合生广场4层</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/92020785/dish95779483" data-click-name="shop_tag_dish_click" data-shopid="92020785" target="_blank">鲜牛肉丸</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/92020785/dish133243170" data-click-name="shop_tag_dish_click" data-shopid="92020785" target="_blank">潮汕炸豆皮</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/92020785/dish133243169" data-click-name="shop_tag_dish_click" data-shopid="92020785" target="_blank">吊龙</a>
      </div>

      <span class="comment-list">
        <span >口味<b>8.5</b></span>
        <span >环境<b>8.8</b></span>
        <span >服务<b>8.6</b></span>
      </span>

    </div>


      <div class="svr-info">

            <div deal-type="DEAL_GROUP" class="si-deal d-packup">
            <a href="javascript:void(0);" title="" class="more J_more" data-click-name="shop_groupdeal_more_click"  >更多3单团购<i class="icon-arr-extend"></i></a>
            <a target="_blank" href="http://t.dianping.com/deal/25340918" data-click-name="shop_info_groupdeal_click"  title="团购：潮汕古巷牛肉火锅!仅售238元！价值274元的潮汕B套餐，建议3人使用，提供免费WiFi。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>潮汕古巷牛肉火锅!仅售238元！价值274元的潮汕B套餐，建议3人使用，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/25340922" data-click-name="shop_info_groupdeal_click"  title="团购：潮汕古巷牛肉火锅!仅售288元！最高价值366元的潮汕C套餐，建议4人使用，提供免费WiFi。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>潮汕古巷牛肉火锅!仅售288元！最高价值366元的潮汕C套餐，建议4人使用，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/25340926" data-click-name="shop_info_groupdeal_click"  title="团购：潮汕古巷牛肉火锅!仅售188元！价值202元的潮汕A套餐，建议2人使用，提供免费WiFi。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>潮汕古巷牛肉火锅!仅售188元！价值202元的潮汕A套餐，建议2人使用，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/30311968" data-click-name="shop_info_groupdeal_click"  title="团购：潮汕古巷牛肉火锅!仅售90元！价值100元的代金券1张，全场通用，可叠加使用，可免费使用包间，提供免费WiFi。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>潮汕古巷牛肉火锅!仅售90元！价值100元的代金券1张，全场通用，可叠加使用，可免费使用包间，提供免费WiFi。
            </a>
            </div>
              <a target="_blank" href="http://www.dianping.com/shop/92020785#promo=0" title="" data-midas-extends="module=5_ad_kwdown2" data-click-name="shop_info_promo_click" data-shopid="92020785" class="tuan privilege">
                <span class="tit">优惠：</span>此餐馆有优惠券
              </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/92020785/review" rel="nofollow"  data-midas-extends="module=5_ad_kwfloat1" title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat2" title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="92020785" data-fav-referid="92020785" data-fav-favortype="1" data-name="潮汕古巷牛肉火锅(木樨园店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat3" title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="92020785" data-poi="HETSRDZVVGTGUP" data-address="永外路果园7号楼合生广场4层" data-sname="潮汕古巷牛肉火锅" data-shopid="92020785">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat4" title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="92020785" data-sname="潮汕古巷牛肉火锅" data-url="/search/around/2/0_92020785{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/107151368" data-click-name="shop_img_click" data-shopid="107151368" rel="nofollow" title=""  >
        <img title="第六季自助餐厅(王府井店)" alt="第六季自助餐厅(王府井店)" data-src="https://img.meituan.net/msmerchant/bb3e9741f50274b716c413eb4d21f32c2031694.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/bb3e9741f50274b716c413eb4d21f32c2031694.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:2,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',107151368);" data-click-name="shop_title_click" data-shopid="107151368" data-hippo-type="shop" title="第六季自助餐厅(王府井店)" target="_blank" href="http://www.dianping.com/shop/107151368"  >
            <h4>第六季自助餐厅(王府井店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="107151368"
                target="_blank" href="http://t.dianping.com/deal/33698462" title="第六季自助餐厅!仅售263元！价值269元的单人晚市豪华自助。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="33698462">
              </a>







        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b69719009" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="107151368"
              >
          分店
          </a>


      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/107151368#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="107151368" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>3288</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/107151368" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="107151368" target="_blank" rel="nofollow" >
            人均
            <b>￥250</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g111" data-click-name="shop_tag_cate_click" data-shopid="107151368" ><span class="tag">自助餐</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r1475" data-click-name="shop_tag_region_click" data-shopid="107151368" ><span class="tag">王府井/东单</span></a>
        <span class="addr">东安门大街55号</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/107151368/dish181236137" data-click-name="shop_tag_dish_click" data-shopid="107151368" target="_blank">鲍鱼</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/107151368/dish181357841" data-click-name="shop_tag_dish_click" data-shopid="107151368" target="_blank">大闸蟹</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/107151368/dish180138603" data-click-name="shop_tag_dish_click" data-shopid="107151368" target="_blank">基围虾</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.1</b></span>
        <span >环境<b>9.2</b></span>
        <span >服务<b>9.4</b></span>
      </span>

    </div>


      <div class="svr-info">

            <div deal-type="DEAL_GROUP" class="si-deal d-packup">
            <a href="javascript:void(0);" title="" class="more J_more" data-click-name="shop_groupdeal_more_click"  >更多1单团购<i class="icon-arr-extend"></i></a>
            <a target="_blank" href="http://t.dianping.com/deal/33698462" data-click-name="shop_info_groupdeal_click"  title="团购：第六季自助餐厅!仅售263元！价值269元的单人晚市豪华自助。"
               
               >
                <span class="tit">团购：</span>第六季自助餐厅!仅售263元！价值269元的单人晚市豪华自助。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/33698471" data-click-name="shop_info_groupdeal_click"  title="团购：第六季自助餐厅!仅售244元！价值249元的单人午市豪华自助。"
               
               >
                <span class="tit">团购：</span>第六季自助餐厅!仅售244元！价值249元的单人午市豪华自助。
            </a>
            </div>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/107151368/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="107151368" data-fav-referid="107151368" data-fav-favortype="1" data-name="第六季自助餐厅(王府井店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="107151368" data-poi="HESHUIZVVIHTEF" data-address="东安门大街55号" data-sname="第六季自助餐厅" data-shopid="107151368">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="107151368" data-sname="第六季自助餐厅" data-url="/search/around/2/0_107151368{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/5618484" data-click-name="shop_img_click" data-shopid="5618484" rel="nofollow" title=""  >
        <img title="京兆尹" alt="京兆尹" data-src="https://img.meituan.net/msmerchant/70ec732ce911fd200c895546520dcb10648989.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/70ec732ce911fd200c895546520dcb10648989.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:3,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',5618484);" data-click-name="shop_title_click" data-shopid="5618484" data-hippo-type="shop" title="京兆尹" target="_blank" href="http://www.dianping.com/shop/5618484"  >
            <h4>京兆尹</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="5618484"
                target="_blank" href="http://t.dianping.com/deal/25726575" title="京兆尹!仅售688元！价值860元的双人无限续加下午茶2位，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="25726575">
              </a>







        </div>



      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/5618484#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="5618484" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>7743</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/5618484" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="5618484" target="_blank" rel="nofollow" >
            人均
            <b>￥622</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g109" data-click-name="shop_tag_cate_click" data-shopid="5618484" ><span class="tag">素菜</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r23022" data-click-name="shop_tag_region_click" data-shopid="5618484" ><span class="tag">雍和宫/地坛</span></a>
        <span class="addr">五道营胡同2号</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/5618484/dish309383" data-click-name="shop_tag_dish_click" data-shopid="5618484" target="_blank">糖醋藕小排</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/5618484/dish7693216" data-click-name="shop_tag_dish_click" data-shopid="5618484" target="_blank">金刚沙豆腐</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/5618484/dish188625" data-click-name="shop_tag_dish_click" data-shopid="5618484" target="_blank">百菇卤味饭</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.1</b></span>
        <span >环境<b>9.4</b></span>
        <span >服务<b>9.3</b></span>
      </span>

    </div>


      <div class="svr-info">

            <div deal-type="DEAL_GROUP" class="si-deal d-packup">
            <a href="javascript:void(0);" title="" class="more J_more" data-click-name="shop_groupdeal_more_click"  >更多1单团购<i class="icon-arr-extend"></i></a>
            <a target="_blank" href="http://t.dianping.com/deal/25726575" data-click-name="shop_info_groupdeal_click"  title="团购：京兆尹!仅售688元！价值860元的双人无限续加下午茶2位，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>京兆尹!仅售688元！价值860元的双人无限续加下午茶2位，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/31264304" data-click-name="shop_info_groupdeal_click"  title="团购：京兆尹!仅售588元！价值860元的女王日无限续加自助下午茶2位，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>京兆尹!仅售588元！价值860元的女王日无限续加自助下午茶2位，提供免费WiFi。
            </a>
            </div>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/5618484/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="5618484" data-fav-referid="5618484" data-fav-favortype="1" data-name="京兆尹"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="5618484" data-poi="HERVSUZVVJHTVO" data-address="五道营胡同2号" data-sname="京兆尹" data-shopid="5618484">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="5618484" data-sname="京兆尹" data-url="/search/around/2/0_5618484{keyword}">附近</a>
    </div>

    </li>
  <li class="" data-midas="ad%3D23279008%26productid%3D74%26modelid%3D38%26pctr%3D0.01813344939907545%26sver%3D2%26target_id%3D7722538%26entityid%3D23919667%26slot%3D31%26search_ads_ab%3D465_1%2C160002_0%2C450_1%26userid%3D806549341%26bottomfen%3D100%26config_center_ab%3Ds16-l2-e1%26page_city_id%3D2%26category_id%3D10%26entitytype%3D1%26rmp%3DQBuakgUkUTFz1lYNm13p-pYBCfV-xZugTisocgOfhq0ZbZhCayKCQojC1hUmDOc%26entityplat%3D1%26adshop_id%3D23919667%26request_id%3D385b61bb-6180-4339-8029-38cee879e043">
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/23919667" data-click-name="shop_img_click" data-shopid="23919667"  title="" data-midas-extends="module=5_ad_kwimg" >
        <img title="重来火锅(原记忆老灶火锅)" alt="重来火锅(原记忆老灶火锅)" data-src="http://p1.meituan.net/mogu/32e5bb532433cacd0d8b622efcce2a3249045.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="http://p1.meituan.net/mogu/32e5bb532433cacd0d8b622efcce2a3249045.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:4,cl_a:4,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',23919667);" data-click-name="shop_title_click" data-shopid="23919667" data-hippo-type="shop" title="重来火锅(原记忆老灶火锅)" target="_blank" href="http://www.dianping.com/shop/23919667" data-midas-extends="module=5_ad_kwtitle" >
            <h4>重来火锅(原记忆老灶火锅)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="23919667"
                target="_blank" href="http://t.dianping.com/deal/12696707" title="重来火锅!仅售95元！价值100元的代金券1张，全场通用，可叠加使用，可免费使用包间，提供免费WiFi。"  class="igroup" data-midas-extends="module=5_ad_kwicon1"
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="12696707">
              </a>





              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/23919667#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="23919667" class="ibook "
                title="" 
                data-midas-extends="module=5_ad_kwicon4"  >
              </a>


        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b23919667" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="23919667"
              data-midas-extends="module=5_ad_kwbranch">
          分店
          </a>

            <a target="_blank" href="http://www.dianping.com/business" data-click-name="shop_icon_ad_click" data-shopid="23919667" class="search-ad" data-midas-extends="module=5_ad_kwtg">广告</a>

      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str45" title="准五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/23919667#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="23919667" target="_blank" module="list-readreview" data-midas-extends="module=5_ad_kwreview"
              rel="nofollow">
              <b>1586</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/23919667" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="23919667" target="_blank" rel="nofollow" data-midas-extends="module=5_ad_kwprice">
            人均
            <b>￥94</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g110" data-click-name="shop_tag_cate_click" data-shopid="23919667" data-midas-extends="module=5_ad_kwcat"><span class="tag">火锅</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r1471" data-click-name="shop_tag_region_click" data-shopid="23919667" data-midas-extends="module=5_ad_kwregion"><span class="tag">望京</span></a>
        <span class="addr">望京街9号望京新城B区望京国际商业中心E座1层</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/23919667/dish150970381" data-click-name="shop_tag_dish_click" data-shopid="23919667" target="_blank">鲜鸭血</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/23919667/dish7209052" data-click-name="shop_tag_dish_click" data-shopid="23919667" target="_blank">生抠鲜鸭肠</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/23919667/dish6567683" data-click-name="shop_tag_dish_click" data-shopid="23919667" target="_blank">九宫格红汤锅</a>
      </div>

      <span class="comment-list">
        <span >口味<b>8.5</b></span>
        <span >环境<b>8.7</b></span>
        <span >服务<b>9.0</b></span>
      </span>

    </div>


      <div class="svr-info">

            <div deal-type="DEAL_GROUP" class="si-deal d-packup">
            <a href="javascript:void(0);" title="" class="more J_more" data-click-name="shop_groupdeal_more_click"  >更多2单团购<i class="icon-arr-extend"></i></a>
            <a target="_blank" href="http://t.dianping.com/deal/12696707" data-click-name="shop_info_groupdeal_click"  title="团购：重来火锅!仅售95元！价值100元的代金券1张，全场通用，可叠加使用，可免费使用包间，提供免费WiFi。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>重来火锅!仅售95元！价值100元的代金券1张，全场通用，可叠加使用，可免费使用包间，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/33365291" data-click-name="shop_info_groupdeal_click"  title="团购：重来火锅!仅售188元！最高价值278元的四人餐，可免费使用包间，提供免费WiFi，提供免费停车位。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>重来火锅!仅售188元！最高价值278元的四人餐，可免费使用包间，提供免费WiFi，提供免费停车位。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/33429757" data-click-name="shop_info_groupdeal_click"  title="团购：重来火锅!仅售98元！最高价值192元的双人餐，可免费使用包间，提供免费WiFi，提供免费停车位。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>重来火锅!仅售98元！最高价值192元的双人餐，可免费使用包间，提供免费WiFi，提供免费停车位。
            </a>
            </div>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/23919667/review" rel="nofollow"  data-midas-extends="module=5_ad_kwfloat1" title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat2" title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="23919667" data-fav-referid="23919667" data-fav-favortype="1" data-name="重来火锅(原记忆老灶火锅)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat3" title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="23919667" data-poi="HESJCGZVVTCCSK" data-address="望京街9号望京新城B区望京国际商业中心E座1层" data-sname="重来火锅" data-shopid="23919667">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat4" title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="23919667" data-sname="重来火锅" data-url="/search/around/2/0_23919667{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/69719009" data-click-name="shop_img_click" data-shopid="69719009" rel="nofollow" title=""  >
        <img title="第六季自助餐厅(西三环店)" alt="第六季自助餐厅(西三环店)" data-src="https://img.meituan.net/msmerchant/bb3e9741f50274b716c413eb4d21f32c2031694.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/bb3e9741f50274b716c413eb4d21f32c2031694.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:5,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',69719009);" data-click-name="shop_title_click" data-shopid="69719009" data-hippo-type="shop" title="第六季自助餐厅(西三环店)" target="_blank" href="http://www.dianping.com/shop/69719009"  >
            <h4>第六季自助餐厅(西三环店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="69719009"
                target="_blank" href="http://t.dianping.com/deal/33698518" title="第六季自助餐厅!仅售263元！价值269元的晚市豪华自助餐，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="33698518">
              </a>







        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b69719009" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="69719009"
              >
          分店
          </a>


      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/69719009#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="69719009" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>8556</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/69719009" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="69719009" target="_blank" rel="nofollow" >
            人均
            <b>￥259</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g111" data-click-name="shop_tag_cate_click" data-shopid="69719009" ><span class="tag">自助餐</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r1494" data-click-name="shop_tag_region_click" data-shopid="69719009" ><span class="tag">紫竹桥</span></a>
        <span class="addr">西三环北路21号久凌大厦北楼二层</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/69719009/dish9333279" data-click-name="shop_tag_dish_click" data-shopid="69719009" target="_blank">鲍鱼</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/69719009/dish9333273" data-click-name="shop_tag_dish_click" data-shopid="69719009" target="_blank">三文鱼</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/69719009/dish10442600" data-click-name="shop_tag_dish_click" data-shopid="69719009" target="_blank">水果</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.1</b></span>
        <span >环境<b>9.1</b></span>
        <span >服务<b>9.2</b></span>
      </span>

    </div>


      <div class="svr-info">

            <div deal-type="DEAL_GROUP" class="si-deal d-packup">
            <a href="javascript:void(0);" title="" class="more J_more" data-click-name="shop_groupdeal_more_click"  >更多1单团购<i class="icon-arr-extend"></i></a>
            <a target="_blank" href="http://t.dianping.com/deal/33698518" data-click-name="shop_info_groupdeal_click"  title="团购：第六季自助餐厅!仅售263元！价值269元的晚市豪华自助餐，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>第六季自助餐厅!仅售263元！价值269元的晚市豪华自助餐，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/33698523" data-click-name="shop_info_groupdeal_click"  title="团购：第六季自助餐厅!仅售244元！价值249元的午市豪华自助餐，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>第六季自助餐厅!仅售244元！价值249元的午市豪华自助餐，提供免费WiFi。
            </a>
            </div>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/69719009/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="69719009" data-fav-referid="69719009" data-fav-favortype="1" data-name="第六季自助餐厅(西三环店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="69719009" data-poi="HEICSHZVVHAARC" data-address="西三环北路21号久凌大厦北楼二层" data-sname="第六季自助餐厅" data-shopid="69719009">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="69719009" data-sname="第六季自助餐厅" data-url="/search/around/2/0_69719009{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/93389432" data-click-name="shop_img_click" data-shopid="93389432" rel="nofollow" title=""  >
        <img title="行运打边炉(三元里店)" alt="行运打边炉(三元里店)" data-src="https://img.meituan.net/msmerchant/e651e730511cc4db0fefa290f72afb892572782.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/e651e730511cc4db0fefa290f72afb892572782.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:6,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',93389432);" data-click-name="shop_title_click" data-shopid="93389432" data-hippo-type="shop" title="行运打边炉(三元里店)" target="_blank" href="http://www.dianping.com/shop/93389432"  >
            <h4>行运打边炉(三元里店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="93389432"
                target="_blank" href="http://t.dianping.com/deal/27836352" title="行运打边炉!仅售90元！价值100元的代金券1张，除酒水外全场通用，可叠加使用2张，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="27836352">
              </a>





              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/93389432#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="93389432" class="ibook "
                title="" 
                  >
              </a>


        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b93389432" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="93389432"
              >
          分店
          </a>


      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/93389432#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="93389432" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>2817</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/93389432" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="93389432" target="_blank" rel="nofollow" >
            人均
            <b>￥283</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g110" data-click-name="shop_tag_cate_click" data-shopid="93389432" ><span class="tag">火锅</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r1469" data-click-name="shop_tag_region_click" data-shopid="93389432" ><span class="tag">亮马桥/三元桥</span></a>
        <span class="addr">三元里街16号</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/93389432/dish102623354" data-click-name="shop_tag_dish_click" data-shopid="93389432" target="_blank">金牌花胶鸡煲</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/93389432/dish102876121" data-click-name="shop_tag_dish_click" data-shopid="93389432" target="_blank">招牌黄金泡饭</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/93389432/dish102870212" data-click-name="shop_tag_dish_click" data-shopid="93389432" target="_blank">手打金沙牛丸</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.1</b></span>
        <span >环境<b>8.8</b></span>
        <span >服务<b>8.6</b></span>
      </span>

    </div>


      <div class="svr-info">

            <a target="_blank" href="http://t.dianping.com/deal/27836352" data-click-name="shop_info_groupdeal_click"  title="团购：行运打边炉!仅售90元！价值100元的代金券1张，除酒水外全场通用，可叠加使用2张，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>行运打边炉!仅售90元！价值100元的代金券1张，除酒水外全场通用，可叠加使用2张，提供免费WiFi。
            </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/93389432/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="93389432" data-fav-referid="93389432" data-fav-favortype="1" data-name="行运打边炉(三元里店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="93389432" data-poi="HESTGJZVVRJEVC" data-address="三元里街16号" data-sname="行运打边炉" data-shopid="93389432">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="93389432" data-sname="行运打边炉" data-url="/search/around/2/0_93389432{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/95137467" data-click-name="shop_img_click" data-shopid="95137467" rel="nofollow" title=""  >
        <img title="第六季自助餐厅(甜水园店)" alt="第六季自助餐厅(甜水园店)" data-src="https://img.meituan.net/msmerchant/bb3e9741f50274b716c413eb4d21f32c2031694.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/bb3e9741f50274b716c413eb4d21f32c2031694.png%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:7,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',95137467);" data-click-name="shop_title_click" data-shopid="95137467" data-hippo-type="shop" title="第六季自助餐厅(甜水园店)" target="_blank" href="http://www.dianping.com/shop/95137467"  >
            <h4>第六季自助餐厅(甜水园店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="95137467"
                target="_blank" href="http://t.dianping.com/deal/33698530" title="第六季自助餐厅!仅售263元！价值269元的晚市豪华自助餐，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="33698530">
              </a>







        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b69719009" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="95137467"
              >
          分店
          </a>


      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/95137467#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="95137467" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>4317</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/95137467" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="95137467" target="_blank" rel="nofollow" >
            人均
            <b>￥252</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g111" data-click-name="shop_tag_cate_click" data-shopid="95137467" ><span class="tag">自助餐</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r23000" data-click-name="shop_tag_region_click" data-shopid="95137467" ><span class="tag">甜水园</span></a>
        <span class="addr">甜水园街甜水园北里16号楼甜水园图书市场一层南侧</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/95137467/dish102576320" data-click-name="shop_tag_dish_click" data-shopid="95137467" target="_blank">鲍鱼</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/95137467/dish102576319" data-click-name="shop_tag_dish_click" data-shopid="95137467" target="_blank">基围虾</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/95137467/dish102750558" data-click-name="shop_tag_dish_click" data-shopid="95137467" target="_blank">皮皮虾</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.1</b></span>
        <span >环境<b>9.1</b></span>
        <span >服务<b>9.3</b></span>
      </span>

    </div>


      <div class="svr-info">

            <div deal-type="DEAL_GROUP" class="si-deal d-packup">
            <a href="javascript:void(0);" title="" class="more J_more" data-click-name="shop_groupdeal_more_click"  >更多1单团购<i class="icon-arr-extend"></i></a>
            <a target="_blank" href="http://t.dianping.com/deal/33698530" data-click-name="shop_info_groupdeal_click"  title="团购：第六季自助餐厅!仅售263元！价值269元的晚市豪华自助餐，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>第六季自助餐厅!仅售263元！价值269元的晚市豪华自助餐，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/33698534" data-click-name="shop_info_groupdeal_click"  title="团购：第六季自助餐厅!仅售244元！价值249元的午市豪华自助餐，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>第六季自助餐厅!仅售244元！价值249元的午市豪华自助餐，提供免费WiFi。
            </a>
            </div>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/95137467/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="95137467" data-fav-referid="95137467" data-fav-favortype="1" data-name="第六季自助餐厅(甜水园店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="95137467" data-poi="HETWATZVVRIVEB" data-address="甜水园街甜水园北里16号楼甜水园图书市场一层南侧" data-sname="第六季自助餐厅" data-shopid="95137467">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="95137467" data-sname="第六季自助餐厅" data-url="/search/around/2/0_95137467{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/74597797" data-click-name="shop_img_click" data-shopid="74597797" rel="nofollow" title=""  >
        <img title="重八牛府(花乡奥莱店)" alt="重八牛府(花乡奥莱店)" data-src="https://img.meituan.net/msmerchant/4e66ed833469f000b6d9aa2b3ec7456e529475.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/4e66ed833469f000b6d9aa2b3ec7456e529475.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:8,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',74597797);" data-click-name="shop_title_click" data-shopid="74597797" data-hippo-type="shop" title="重八牛府(花乡奥莱店)" target="_blank" href="http://www.dianping.com/shop/74597797"  >
            <h4>重八牛府(花乡奥莱店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="74597797"
                target="_blank" href="http://t.dianping.com/deal/2308261" title="重八牛府!仅售86元！价值100元的代金劵1张，全场通用，可叠加使用，可免费使用包间。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="2308261">
              </a>

              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/74597797#promo=0" title=""
                  class="ipromote " 
                  data-click-name="shop_icon_shortdeal_click" data-shopid="74597797"
                  
                ></a>




              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/74597797#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="74597797" class="ibook "
                title="" 
                  >
              </a>


        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b17677116" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="74597797"
              >
          分店
          </a>


      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/74597797#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="74597797" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>2660</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/74597797" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="74597797" target="_blank" rel="nofollow" >
            人均
            <b>￥101</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g110" data-click-name="shop_tag_cate_click" data-shopid="74597797" ><span class="tag">火锅</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r7040" data-click-name="shop_tag_region_click" data-shopid="74597797" ><span class="tag">花乡</span></a>
        <span class="addr">南四环西路76号7号楼304</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/74597797/dish130178367" data-click-name="shop_tag_dish_click" data-shopid="74597797" target="_blank">重八招牌手打牛丸（鲜肉现打）</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/74597797/dish38906218" data-click-name="shop_tag_dish_click" data-shopid="74597797" target="_blank">重八独家秘制牛丸鸳鸯锅</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/74597797/dish38906305" data-click-name="shop_tag_dish_click" data-shopid="74597797" target="_blank">嫩牛肉</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.2</b></span>
        <span >环境<b>9.2</b></span>
        <span >服务<b>9.3</b></span>
      </span>

    </div>


      <div class="svr-info">

            <a target="_blank" href="http://t.dianping.com/deal/2308261" data-click-name="shop_info_groupdeal_click"  title="团购：重八牛府!仅售86元！价值100元的代金劵1张，全场通用，可叠加使用，可免费使用包间。"
               
               >
                <span class="tit">团购：</span>重八牛府!仅售86元！价值100元的代金劵1张，全场通用，可叠加使用，可免费使用包间。
            </a>
              <a target="_blank" href="http://www.dianping.com/shop/74597797#promo=0" title=""  data-click-name="shop_info_promo_click" data-shopid="74597797" class="tuan privilege">
                <span class="tit">优惠：</span>此餐馆有优惠券
              </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/74597797/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="74597797" data-fav-referid="74597797" data-fav-favortype="1" data-name="重八牛府(花乡奥莱店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="74597797" data-poi="HESJUCZVVEEVBS" data-address="南四环西路76号7号楼304" data-sname="重八牛府" data-shopid="74597797">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="74597797" data-sname="重八牛府" data-url="/search/around/2/0_74597797{keyword}">附近</a>
    </div>

    </li>
  <li class="" data-midas="ad%3D23238415%26productid%3D74%26modelid%3D38%26pctr%3D0.025808469246437312%26sver%3D2%26target_id%3D7642012%26entityid%3D69619894%26slot%3D31%26search_ads_ab%3D465_1%2C160002_0%2C450_1%26userid%3D806549341%26bottomfen%3D100%26config_center_ab%3Ds16-l2-e1%26page_city_id%3D2%26category_id%3D10%26entitytype%3D1%26rmp%3DvdACD_wgXtvNEvPkJ-Lc3LuQFw3SXxZhzozV6azSFCAmu8X3crLFuWsV2cxRXA%26entityplat%3D1%26adshop_id%3D69619894%26request_id%3D385b61bb-6180-4339-8029-38cee879e043">
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/69619894" data-click-name="shop_img_click" data-shopid="69619894"  title="" data-midas-extends="module=5_ad_kwimg" >
        <img title="那味道串串香(中粮万科长阳半岛店)" alt="那味道串串香(中粮万科长阳半岛店)" data-src="http://qcloud.dpfile.com/pc/kCqv69V2vl_bZ9B7VUYkFTh2TcG8I5KN5vQd95-7sPKozkitQKqHlrJgLKwbanFcs9bU8u7TlyVW3ovyQ7Jtmw.jpg"
           src="http://qcloud.dpfile.com/pc/kCqv69V2vl_bZ9B7VUYkFTh2TcG8I5KN5vQd95-7sPKozkitQKqHlrJgLKwbanFcs9bU8u7TlyVW3ovyQ7Jtmw.jpg"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:9,cl_a:4,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',69619894);" data-click-name="shop_title_click" data-shopid="69619894" data-hippo-type="shop" title="那味道串串香(中粮万科长阳半岛店)" target="_blank" href="http://www.dianping.com/shop/69619894" data-midas-extends="module=5_ad_kwtitle" >
            <h4>那味道串串香(中粮万科长阳半岛店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="69619894"
                target="_blank" href="http://t.dianping.com/deal/22414649" title="那味道串串香!仅售13.8元！价值20元的特色串串20份，提供免费WiFi。"  class="igroup" data-midas-extends="module=5_ad_kwicon1"
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="22414649">
              </a>







        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b66588330" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="69619894"
              data-midas-extends="module=5_ad_kwbranch">
          分店
          </a>

            <a target="_blank" href="http://www.dianping.com/business" data-click-name="shop_icon_ad_click" data-shopid="69619894" class="search-ad" data-midas-extends="module=5_ad_kwtg">广告</a>

      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str40" title="四星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/69619894#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="69619894" target="_blank" module="list-readreview" data-midas-extends="module=5_ad_kwreview"
              rel="nofollow">
              <b>231</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/69619894" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="69619894" target="_blank" rel="nofollow" data-midas-extends="module=5_ad_kwprice">
            人均
            <b>￥61</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g110" data-click-name="shop_tag_cate_click" data-shopid="69619894" data-midas-extends="module=5_ad_kwcat"><span class="tag">火锅</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r30781" data-click-name="shop_tag_region_click" data-shopid="69619894" data-midas-extends="module=5_ad_kwregion"><span class="tag">长阳镇</span></a>
        <span class="addr">长阳镇长阳路中粮万科长阳半岛广场4层</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/69619894/dish14295375" data-click-name="shop_tag_dish_click" data-shopid="69619894" target="_blank">麻辣牛肉</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/69619894/dish14230391" data-click-name="shop_tag_dish_click" data-shopid="69619894" target="_blank">秘制酱料</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/69619894/dish14337533" data-click-name="shop_tag_dish_click" data-shopid="69619894" target="_blank">鸳鸯锅</a>
      </div>

      <span class="comment-list">
        <span >口味<b>7.9</b></span>
        <span >环境<b>8.1</b></span>
        <span >服务<b>8.5</b></span>
      </span>

    </div>


      <div class="svr-info">

            <a target="_blank" href="http://t.dianping.com/deal/22414649" data-click-name="shop_info_groupdeal_click"  title="团购：那味道串串香!仅售13.8元！价值20元的特色串串20份，提供免费WiFi。"
               
               data-midas-extends="module=5_ad_kwdown1">
                <span class="tit">团购：</span>那味道串串香!仅售13.8元！价值20元的特色串串20份，提供免费WiFi。
            </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/69619894/review" rel="nofollow"  data-midas-extends="module=5_ad_kwfloat1" title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat2" title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="69619894" data-fav-referid="69619894" data-fav-favortype="1" data-name="那味道串串香(中粮万科长阳半岛店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat3" title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="69619894" data-poi="HERRFTZVUWSIVB" data-address="长阳镇长阳路中粮万科长阳半岛广场4层" data-sname="那味道串串香" data-shopid="69619894">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat4" title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="69619894" data-sname="那味道串串香" data-url="/search/around/2/0_69619894{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/507576" data-click-name="shop_img_click" data-shopid="507576" rel="nofollow" title=""  >
        <img title="满福楼" alt="满福楼" data-src="https://img.meituan.net/msmerchant/54111d58a8253c8ac59665f1adf95642463892.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/54111d58a8253c8ac59665f1adf95642463892.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:10,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',507576);" data-click-name="shop_title_click" data-shopid="507576" data-hippo-type="shop" title="满福楼" target="_blank" href="http://www.dianping.com/shop/507576"  >
            <h4>满福楼</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="507576"
                target="_blank" href="http://t.dianping.com/deal/31579061" title="满福楼!仅售156元！最高价值196元的双人套餐，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="31579061">
              </a>





              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/507576#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="507576" class="ibook icon-only"
                title="" 
                  >
              </a>


            <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/507576#waimai" data-click-name="shop_icon_takeaway_click" data-shopid="507576"
               class="iout icon-only" title="本店支持在线下单，足不出户，外送到家！"
                >
            </a>
        </div>



      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/507576#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="507576" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>18275</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/507576" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="507576" target="_blank" rel="nofollow" >
            人均
            <b>￥121</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g110" data-click-name="shop_tag_cate_click" data-shopid="507576" ><span class="tag">火锅</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r1466" data-click-name="shop_tag_region_click" data-shopid="507576" ><span class="tag">朝外大街</span></a>
        <span class="addr">朝阳门外大街8号蓝岛大厦东区六层</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/507576/dish43827" data-click-name="shop_tag_dish_click" data-shopid="507576" target="_blank">手切鲜羊肉</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/507576/dish444769" data-click-name="shop_tag_dish_click" data-shopid="507576" target="_blank">冻羊肉</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/507576/dish821413" data-click-name="shop_tag_dish_click" data-shopid="507576" target="_blank">纯鲜墨鱼丸</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.1</b></span>
        <span >环境<b>9.1</b></span>
        <span >服务<b>9.1</b></span>
      </span>

    </div>


      <div class="svr-info">

            <div deal-type="DEAL_GROUP" class="si-deal d-packup">
            <a href="javascript:void(0);" title="" class="more J_more" data-click-name="shop_groupdeal_more_click"  >更多2单团购<i class="icon-arr-extend"></i></a>
            <a target="_blank" href="http://t.dianping.com/deal/31579061" data-click-name="shop_info_groupdeal_click"  title="团购：满福楼!仅售156元！最高价值196元的双人套餐，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>满福楼!仅售156元！最高价值196元的双人套餐，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/31634799" data-click-name="shop_info_groupdeal_click"  title="团购：满福楼!仅售356元！最高价值444元的畅销午市四人套餐，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>满福楼!仅售356元！最高价值444元的畅销午市四人套餐，提供免费WiFi。
            </a>
            <a target="_blank" href="http://t.dianping.com/deal/33327284" data-click-name="shop_info_groupdeal_click"  title="团购：满福楼!仅售95元！价值100元的必吃榜代金券1张，全场通用，可叠加使用，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>满福楼!仅售95元！价值100元的必吃榜代金券1张，全场通用，可叠加使用，提供免费WiFi。
            </a>
            </div>
          <a target="_blank" href="http://www.dianping.com/shop/507576" data-click-name="shop_info_takeway_click" data-shopid="507576" title="外送：本店支持在线下单，足不出户，外送到家！" class="tuan privilege">
            <span class="tit">外送：</span>本店支持在线下单，足不出户，外送到家！
          </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/507576/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="507576" data-fav-referid="507576" data-fav-favortype="1" data-name="满福楼"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="507576" data-poi="HETFIJZVVJRRTC" data-address="朝阳门外大街8号蓝岛大厦东区六层" data-sname="满福楼" data-shopid="507576">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="507576" data-sname="满福楼" data-url="/search/around/2/0_507576{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/69788171" data-click-name="shop_img_click" data-shopid="69788171" rel="nofollow" title=""  >
        <img title="就三桌涮肉馆" alt="就三桌涮肉馆" data-src="https://img.meituan.net/msmerchant/4db646d79454542d435643a2bd6db8e786426.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/4db646d79454542d435643a2bd6db8e786426.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:11,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',69788171);" data-click-name="shop_title_click" data-shopid="69788171" data-hippo-type="shop" title="就三桌涮肉馆" target="_blank" href="http://www.dianping.com/shop/69788171"  >
            <h4>就三桌涮肉馆</h4>
        </a>


        <div class="promo-icon J_promo_icon">


              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/69788171#promo=0" title=""
                  class="ipromote icon-only" 
                  data-click-name="shop_icon_shortdeal_click" data-shopid="69788171"
                  
                ></a>




              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/69788171#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="69788171" class="ibook icon-only"
                title="" 
                  >
              </a>


            <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/69788171#waimai" data-click-name="shop_icon_takeaway_click" data-shopid="69788171"
               class="iout icon-only" title="本店支持在线下单，足不出户，外送到家！"
                >
            </a>
        </div>



      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/69788171#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="69788171" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>1045</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/69788171" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="69788171" target="_blank" rel="nofollow" >
            人均
            <b>￥104</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g110" data-click-name="shop_tag_cate_click" data-shopid="69788171" ><span class="tag">火锅</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r23020" data-click-name="shop_tag_region_click" data-shopid="69788171" ><span class="tag">798/大山子</span></a>
        <span class="addr">草场地艺术区114号村委会西</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/69788171/dish221639" data-click-name="shop_tag_dish_click" data-shopid="69788171" target="_blank">手切羊肉</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/69788171/dish8100243" data-click-name="shop_tag_dish_click" data-shopid="69788171" target="_blank">鲜毛肚</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/69788171/dish120972037" data-click-name="shop_tag_dish_click" data-shopid="69788171" target="_blank">手工虾滑</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.1</b></span>
        <span >环境<b>9.0</b></span>
        <span >服务<b>9.1</b></span>
      </span>

    </div>


      <div class="svr-info">

              <a target="_blank" href="http://www.dianping.com/shop/69788171#promo=0" title=""  data-click-name="shop_info_promo_click" data-shopid="69788171" class="tuan ">
                <span class="tit">优惠：</span>此餐馆有优惠券
              </a>
          <a target="_blank" href="http://www.dianping.com/shop/69788171" data-click-name="shop_info_takeway_click" data-shopid="69788171" title="外送：本店支持在线下单，足不出户，外送到家！" class="tuan privilege">
            <span class="tit">外送：</span>本店支持在线下单，足不出户，外送到家！
          </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/69788171/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="69788171" data-fav-referid="69788171" data-fav-favortype="1" data-name="就三桌涮肉馆"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="69788171" data-poi="HESVAJZVVTVGWL" data-address="草场地艺术区114号村委会西" data-sname="就三桌涮肉馆" data-shopid="69788171">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="69788171" data-sname="就三桌涮肉馆" data-url="/search/around/2/0_69788171{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/111599817" data-click-name="shop_img_click" data-shopid="111599817" rel="nofollow" title=""  >
        <img title="香守" alt="香守" data-src="https://img.meituan.net/msmerchant/6f9162ac5468f0888b6525326781c32f578514.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/6f9162ac5468f0888b6525326781c32f578514.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:12,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',111599817);" data-click-name="shop_title_click" data-shopid="111599817" data-hippo-type="shop" title="香守" target="_blank" href="http://www.dianping.com/shop/111599817"  >
            <h4>香守</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="111599817"
                target="_blank" href="http://t.dianping.com/deal/33998871" title="香守!仅售458元！最高价值736元的带妹.带哥吃鸡宴，建议2人使用，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="33998871">
              </a>





              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/111599817#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="111599817" class="ibook icon-only"
                title="" 
                  >
              </a>


        </div>



      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/111599817#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="111599817" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>134</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/111599817" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="111599817" target="_blank" rel="nofollow" >
            人均
            <b>￥420</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g251" data-click-name="shop_tag_cate_click" data-shopid="111599817" ><span class="tag">海鲜</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r2078" data-click-name="shop_tag_region_click" data-shopid="111599817" ><span class="tag">大望路</span></a>
        <span class="addr">华贸广场路华贸jw万豪酒店2层</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/111599817/dish185379240" data-click-name="shop_tag_dish_click" data-shopid="111599817" target="_blank">花胶走地鸡汤</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/111599817/dish191638761" data-click-name="shop_tag_dish_click" data-shopid="111599817" target="_blank">潮州手工牛肉丸</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/111599817/dish191537871" data-click-name="shop_tag_dish_click" data-shopid="111599817" target="_blank">酱料9宫格</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.3</b></span>
        <span >环境<b>9.4</b></span>
        <span >服务<b>9.3</b></span>
      </span>

    </div>


      <div class="svr-info">

            <a target="_blank" href="http://t.dianping.com/deal/33998871" data-click-name="shop_info_groupdeal_click"  title="团购：香守!仅售458元！最高价值736元的带妹.带哥吃鸡宴，建议2人使用，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>香守!仅售458元！最高价值736元的带妹.带哥吃鸡宴，建议2人使用，提供免费WiFi。
            </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/111599817/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="111599817" data-fav-referid="111599817" data-fav-favortype="1" data-name="香守"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="111599817" data-poi="HEUGWAZVVRCRJY" data-address="华贸广场路华贸jw万豪酒店2层" data-sname="香守" data-shopid="111599817">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="111599817" data-sname="香守" data-url="/search/around/2/0_111599817{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/19210686" data-click-name="shop_img_click" data-shopid="19210686" rel="nofollow" title=""  >
        <img title="罗兰湖餐厅" alt="罗兰湖餐厅" data-src="http://p1.meituan.net/apiback/330bdb70e0cb114c01f153958a7a52f59990739.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="http://p1.meituan.net/apiback/330bdb70e0cb114c01f153958a7a52f59990739.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:13,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',19210686);" data-click-name="shop_title_click" data-shopid="19210686" data-hippo-type="shop" title="罗兰湖餐厅" target="_blank" href="http://www.dianping.com/shop/19210686"  >
            <h4>罗兰湖餐厅</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="19210686"
                target="_blank" href="http://t.dianping.com/deal/33797635" title="罗兰湖餐厅!仅售68元！最高价值84元的精品单人下午茶，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="33797635">
              </a>







        </div>



      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/19210686#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="19210686" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>4683</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/19210686" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="19210686" target="_blank" rel="nofollow" >
            人均
            <b>￥215</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g118" data-click-name="shop_tag_cate_click" data-shopid="19210686" ><span class="tag">其他美食</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r2583" data-click-name="shop_tag_region_click" data-shopid="19210686" ><span class="tag">酒仙桥</span></a>
        <span class="addr">芳园西路6号</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/19210686/dish160091" data-click-name="shop_tag_dish_click" data-shopid="19210686" target="_blank">大蒜牛扒</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/19210686/dish190185" data-click-name="shop_tag_dish_click" data-shopid="19210686" target="_blank">烤鳗鱼</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/19210686/dish14991788" data-click-name="shop_tag_dish_click" data-shopid="19210686" target="_blank">加州阳光卷</a>
      </div>

      <span class="comment-list">
        <span >口味<b>8.6</b></span>
        <span >环境<b>9.3</b></span>
        <span >服务<b>9.1</b></span>
      </span>

    </div>


      <div class="svr-info">

            <a target="_blank" href="http://t.dianping.com/deal/33797635" data-click-name="shop_info_groupdeal_click"  title="团购：罗兰湖餐厅!仅售68元！最高价值84元的精品单人下午茶，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>罗兰湖餐厅!仅售68元！最高价值84元的精品单人下午茶，提供免费WiFi。
            </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/19210686/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="19210686" data-fav-referid="19210686" data-fav-favortype="1" data-name="罗兰湖餐厅"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="19210686" data-poi="HESUBHZVVSRISJ" data-address="芳园西路6号" data-sname="罗兰湖餐厅" data-shopid="19210686">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="19210686" data-sname="罗兰湖餐厅" data-url="/search/around/2/0_19210686{keyword}">附近</a>
    </div>

    </li>
  <li class="" data-midas="ad%3D23413167%26productid%3D74%26modelid%3D38%26pctr%3D0.02761233432224966%26sver%3D2%26target_id%3D7983937%26entityid%3D22740088%26slot%3D31%26search_ads_ab%3D465_1%2C160002_0%2C450_1%26userid%3D806549341%26bottomfen%3D100%26config_center_ab%3Ds16-l2-e1%26page_city_id%3D2%26category_id%3D10%26entitytype%3D1%26rmp%3DMW1raDUduy8jgLEsj0iruNw1O2QlKCzeNoRS9gBv67FFoRKuWkHhYN7Hm5OP97I%26entityplat%3D1%26adshop_id%3D22740088%26request_id%3D385b61bb-6180-4339-8029-38cee879e043">
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/22740088" data-click-name="shop_img_click" data-shopid="22740088"  title="" data-midas-extends="module=5_ad_kwimg" >
        <img title="炙子革命老北京炙子烤肉(鼓楼店)" alt="炙子革命老北京炙子烤肉(鼓楼店)" data-src="https://img.meituan.net/msmerchant/e75fc1ffac7cfb8381113d28542ddd45279932.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/e75fc1ffac7cfb8381113d28542ddd45279932.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:14,cl_a:4,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',22740088);" data-click-name="shop_title_click" data-shopid="22740088" data-hippo-type="shop" title="炙子革命老北京炙子烤肉(鼓楼店)" target="_blank" href="http://www.dianping.com/shop/22740088" data-midas-extends="module=5_ad_kwtitle" >
            <h4>炙子革命老北京炙子烤肉(鼓楼店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">






              <a rel="nofollow" target="_blank" href="http://www.dianping.com/shop/22740088#reserve"
                data-click-name="shop_icon_booking_click" data-shopid="22740088" class="ibook "
                title="" 
                data-midas-extends="module=5_ad_kwicon4"  >
              </a>


        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b10013328" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="22740088"
              data-midas-extends="module=5_ad_kwbranch">
          分店
          </a>

            <a target="_blank" href="http://www.dianping.com/business" data-click-name="shop_icon_ad_click" data-shopid="22740088" class="search-ad" data-midas-extends="module=5_ad_kwtg">广告</a>

      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str45" title="准五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/22740088#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="22740088" target="_blank" module="list-readreview" data-midas-extends="module=5_ad_kwreview"
              rel="nofollow">
              <b>3223</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/22740088" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="22740088" target="_blank" rel="nofollow" data-midas-extends="module=5_ad_kwprice">
            人均
            <b>￥92</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g508" data-click-name="shop_tag_cate_click" data-shopid="22740088" data-midas-extends="module=5_ad_kwcat"><span class="tag">烧烤</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r2595" data-click-name="shop_tag_region_click" data-shopid="22740088" data-midas-extends="module=5_ad_kwregion"><span class="tag">什刹海</span></a>
        <span class="addr">旧鼓楼大街铃铛胡同25号</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/22740088/dish28226" data-click-name="shop_tag_dish_click" data-shopid="22740088" target="_blank">肥瘦羊肉</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/22740088/dish28227" data-click-name="shop_tag_dish_click" data-shopid="22740088" target="_blank">酸梅汤</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/22740088/dish41854582" data-click-name="shop_tag_dish_click" data-shopid="22740088" target="_blank">蒜香肥牛</a>
      </div>

      <span class="comment-list">
        <span >口味<b>8.8</b></span>
        <span >环境<b>8.5</b></span>
        <span >服务<b>8.7</b></span>
      </span>

    </div>



    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/22740088/review" rel="nofollow"  data-midas-extends="module=5_ad_kwfloat1" title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat2" title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="22740088" data-fav-referid="22740088" data-fav-favortype="1" data-name="炙子革命老北京炙子烤肉(鼓楼店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat3" title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="22740088" data-poi="HERIEFZVVIUBGU" data-address="旧鼓楼大街铃铛胡同25号" data-sname="炙子革命老北京炙子烤肉" data-shopid="22740088">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow" data-midas-extends="module=5_ad_kwfloat4" title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="22740088" data-sname="炙子革命老北京炙子烤肉" data-url="/search/around/2/0_22740088{keyword}">附近</a>
    </div>

    </li>
  <li class="" >
    <div class="pic" >
      <a onclick="LXAnalytics('moduleClick', 'shoppic')" target="_blank" href="http://www.dianping.com/shop/18146141" data-click-name="shop_img_click" data-shopid="18146141" rel="nofollow" title=""  >
        <img title="小吊梨汤(新奥店)" alt="小吊梨汤(新奥店)" data-src="https://img.meituan.net/msmerchant/145b42d9d98350ef9ecf93e92b5cb07829099.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"
           src="https://img.meituan.net/msmerchant/145b42d9d98350ef9ecf93e92b5cb07829099.jpg%40340w_255h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"/>
      </a>
    </div>

    <div class="txt">
      <div class="tit">
        <a onclick="LXAnalytics('moduleClick', 'shopname');document.hippo.ext({cl_i:15,query_id:'385b61bb-6180-4339-8029-38cee879e043'}).mv('cl_to_s',18146141);" data-click-name="shop_title_click" data-shopid="18146141" data-hippo-type="shop" title="小吊梨汤(新奥店)" target="_blank" href="http://www.dianping.com/shop/18146141"  >
            <h4>小吊梨汤(新奥店)</h4>
        </a>


        <div class="promo-icon J_promo_icon">

              <a rel="nofollow" data-click-name="shop_group_icon_click" data-shopid="18146141"
                target="_blank" href="http://t.dianping.com/deal/34056728" title="小吊梨汤!仅售97元！价值100元的代金券1张，全场通用，可叠加使用，提供免费WiFi。"  class="igroup" 
                data-hippo-dealgrp_type="" data-hippo-dealgrp_id="34056728">
              </a>







        </div>

          <a onclick="LXAnalytics('moduleClick', 'shopbranch')" target="_blank"
              link rel="alternate" media="only screen and (max-width: 640px)"
              href="http://www.dianping.com/brands/b2355826" module="list-branch"
              data-click-name="shop_branch_click" class="shop-branch" data-shopid="18146141"
              >
          分店
          </a>


      </div>

      <div class="comment">
        <span class="sml-rank-stars sml-str50" title="五星商户"></span>

          <a onclick="LXAnalytics('moduleClick', 'shopreview')" href="http://www.dianping.com/shop/18146141#comment" class="review-num" data-click-name="shop_iwant_review_click" data-shopid="18146141" target="_blank" module="list-readreview" 
              rel="nofollow">
              <b>15888</b>
条点评</a>

        <em class="sep">|</em>
        <a onclick="LXAnalytics('moduleClick', 'shopprice')" href="http://www.dianping.com/shop/18146141" class="mean-price" data-click-name="shop_avgprice_click" data-shopid="18146141" target="_blank" rel="nofollow" >
            人均
            <b>￥86</b>
            </span>
        </a>

      </div>

      <div class="tag-addr">
        <a href = "http://www.dianping.com/beijing/ch10/g311" data-click-name="shop_tag_cate_click" data-shopid="18146141" ><span class="tag">北京菜</span></a>
        <em class="sep">|</em>
        <a href = "http://www.dianping.com/beijing/ch10/r1470" data-click-name="shop_tag_region_click" data-shopid="18146141" ><span class="tag">亚运村</span></a>
        <span class="addr">湖景东路9号新奥购物中心B1层</span>
      </div>

      <div class="recommend">
          <span>推荐菜：</span>
            <a class="recommend-click" href="http://www.dianping.com/shop/18146141/dish18921" data-click-name="shop_tag_dish_click" data-shopid="18146141" target="_blank">小吊梨汤</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/18146141/dish18919" data-click-name="shop_tag_dish_click" data-shopid="18146141" target="_blank">干酪鱼</a>
            <a class="recommend-click" href="http://www.dianping.com/shop/18146141/dish18916" data-click-name="shop_tag_dish_click" data-shopid="18146141" target="_blank">梨球果仁虾</a>
      </div>

      <span class="comment-list">
        <span >口味<b>9.0</b></span>
        <span >环境<b>9.0</b></span>
        <span >服务<b>9.1</b></span>
      </span>

    </div>


      <div class="svr-info">

            <a target="_blank" href="http://t.dianping.com/deal/34056728" data-click-name="shop_info_groupdeal_click"  title="团购：小吊梨汤!仅售97元！价值100元的代金券1张，全场通用，可叠加使用，提供免费WiFi。"
               
               >
                <span class="tit">团购：</span>小吊梨汤!仅售97元！价值100元的代金券1张，全场通用，可叠加使用，提供免费WiFi。
            </a>
      </div>

    <div class="operate J_operate Hide">
          <a target="_blank" href="http://www.dianping.com/shop/18146141/review" rel="nofollow"   title=""  class="o-remark" data-click-name="shop_review_click"><i></i><span>写点评</span></a>
          <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-favor J_o-favor" data-click-name="shop_favor_click" data-shopid="18146141" data-fav-referid="18146141" data-fav-favortype="1" data-name="小吊梨汤(新奥店)"><i></i><span>收藏</span></a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-map J_o-map" data-click-name="shop_map_click" data-shopid="18146141" data-poi="HEJBSFZVVRDGWD" data-address="湖景东路9号新奥购物中心B1层" data-sname="小吊梨汤" data-shopid="18146141">地图</a>
      <span class="line">|</span>
      <a href="javascript:void(0);" rel="nofollow"  title="" class="o-nearby J_o-nearby" data-click-name="shop_nearby_click" data-shopid="18146141" data-sname="小吊梨汤" data-url="/search/around/2/0_18146141{keyword}">附近</a>
    </div>

    </li>
  </ul>
</div>
                </div>
                    



	<div class="page">


					<a class="cur">1</a>
					<a href="http://www.dianping.com/beijing/ch10/p2?aid=92020785&cpt=92020785" data-ga-page="2" class="PageLink" title="2">2</a>
					<a href="http://www.dianping.com/beijing/ch10/p3?aid=92020785&cpt=92020785" data-ga-page="3" class="PageLink" title="3">3</a>
					<a href="http://www.dianping.com/beijing/ch10/p4?aid=92020785&cpt=92020785" data-ga-page="4" class="PageLink" title="4">4</a>
					<a href="http://www.dianping.com/beijing/ch10/p5?aid=92020785&cpt=92020785" data-ga-page="5" class="PageLink" title="5">5</a>
					<a href="http://www.dianping.com/beijing/ch10/p6?aid=92020785&cpt=92020785" data-ga-page="6" class="PageLink" title="6">6</a>
					<a href="http://www.dianping.com/beijing/ch10/p7?aid=92020785&cpt=92020785" data-ga-page="7" class="PageLink" title="7">7</a>
					<a href="http://www.dianping.com/beijing/ch10/p8?aid=92020785&cpt=92020785" data-ga-page="8" class="PageLink" title="8">8</a>
					<a href="http://www.dianping.com/beijing/ch10/p9?aid=92020785&cpt=92020785" data-ga-page="9" class="PageLink" title="9">9</a>

				<span class="PageMore">...</span>
			<a href="http://www.dianping.com/beijing/ch10/p50?aid=92020785&cpt=92020785" data-ga-page="50" class="PageLink" title="50">50</a>

			<a href="http://www.dianping.com/beijing/ch10/p2?aid=92020785&cpt=92020785" data-ga-page="2" class="next" title="下一页">下一页</a>
	</div>



<div class="sear-result no-result">
   <h4>商户没有被收录？</h4>
   <div class="other-way">
    <a href="http://www.dianping.com/addshop/2_?k=" class="" id="popMbox">添加商户</a>
   </div>
   <div class="evaluation J_evaluation">
    您对搜索结果：<a href="javascript:void(0);" rel="nofollow" class="y J_good choice"><i></i>满意</a><a href="javascript:void(0);" rel="nofollow"  class="n J_no choice"><i></i>不满</a>
    <div class="y-result y-first J_sucTip Hide"><i></i>非常感谢对大众点评的支持</div>
    <div class="y-result y-second Hide J_sucTip"><i></i>请勿重复提交</div>
    <div class="no-box msg-box J_user-advice Hide">
     <h4>遇到什么问题？</h4>
     <i class="close" data-click-name="nobox_quit_click"></i>
     <div class="" data-click-name="nobox_textarea_click">
      <textarea>请输入...</textarea>
     </div>
     <div class="btn">
      <a href="javascript:void(0);" class="del" data-click-name="nobox_cancel_click">取消</a>
      <a href="javascript:void(0);" class="save" data-click-name="nobox_confirm_click">提交</a>
     </div>
    </div>
   </div>
  </div>


<section class="foot-links">
        <!--品牌馆新增底部内链-->
        <!--全国大全-->
        <!--同城推荐-->
            <dl class="linksItem">
                <dt class="b-left">
                <p>北京美食介绍:</p>
                </dt>
                <dd class="b-right">
                    <p>大众点评北京美食频道为您提供北京美食排行榜等相关信息，为您提供最全的北京美食相关信息，找美食就上大众点评
                    </p>
                </dd>
            </dl>
        <!--城市推荐菜-->
        <!--城市美食-->
        <!--生活导航-->

        <!--热门城市-->
        <!--品牌馆新增底部内链-->
        <!--全国大全-->
        <!--同城推荐-->
            <dl class="linksItem J-city-link">

                <dt class="b-left">
                <p>北京美食大全:</p>
                </dt>
                <dd class="b-right">
                    <ul class="characters J-city-char">
                            <li><span>7</span></li>
                            <li><span>A</span></li>
                            <li><span>B</span></li>
                            <li><span>C</span></li>
                            <li><span>D</span></li>
                            <li><span>F</span></li>
                            <li><span>G</span></li>
                            <li><span>H</span></li>
                            <li><span>J</span></li>
                            <li><span>K</span></li>
                            <li><span>L</span></li>
                            <li><span>M</span></li>
                            <li><span>N</span></li>
                            <li><span>P</span></li>
                            <li><span>Q</span></li>
                            <li><span>R</span></li>
                            <li><span>S</span></li>
                            <li><span>T</span></li>
                            <li><span>W</span></li>
                            <li><span>X</span></li>
                            <li><span>Y</span></li>
                            <li><span>Z</span></li>
                    </ul>
                    <div class="content city-content">
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23020" data-click-name="footer_nav_col_click" target="_blank">北京798/大山子美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1473" data-click-name="footer_nav_col_click" target="_blank">北京安贞美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1478" data-click-name="footer_nav_col_click" target="_blank">北京安定门美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1490" data-click-name="footer_nav_col_click" target="_blank">北京北太平庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1492" data-click-name="footer_nav_col_click" target="_blank">北京北下关美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2592" data-click-name="footer_nav_col_click" target="_blank">北京北大地美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2870" data-click-name="footer_nav_col_click" target="_blank">北京北苑家园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23003" data-click-name="footer_nav_col_click" target="_blank">北京百子湾美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23006" data-click-name="footer_nav_col_click" target="_blank">北京北京欢乐谷美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23008" data-click-name="footer_nav_col_click" target="_blank">北京北京东站美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23016" data-click-name="footer_nav_col_click" target="_blank">北京北沙滩美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23024" data-click-name="footer_nav_col_click" target="_blank">北京北新桥/簋街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23036" data-click-name="footer_nav_col_click" target="_blank">北京北京西站/六里桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23043" data-click-name="footer_nav_col_click" target="_blank">北京北七家美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r85513" data-click-name="footer_nav_col_click" target="_blank">北京北关美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1466" data-click-name="footer_nav_col_click" target="_blank">北京朝外大街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1467" data-click-name="footer_nav_col_click" target="_blank">北京朝阳公园/团结湖美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1474" data-click-name="footer_nav_col_click" target="_blank">北京朝阳其它美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1479" data-click-name="footer_nav_col_click" target="_blank">北京朝阳门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1504" data-click-name="footer_nav_col_click" target="_blank">北京崇文门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2876" data-click-name="footer_nav_col_click" target="_blank">北京菜市口美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2880" data-click-name="footer_nav_col_click" target="_blank">北京草桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5955" data-click-name="footer_nav_col_click" target="_blank">北京昌平镇美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23001" data-click-name="footer_nav_col_click" target="_blank">北京慈云寺/八里庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23004" data-click-name="footer_nav_col_click" target="_blank">北京传媒大学/二外美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23019" data-click-name="footer_nav_col_click" target="_blank">北京常营美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r30781" data-click-name="footer_nav_col_click" target="_blank">北京长阳镇美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70269" data-click-name="footer_nav_col_click" target="_blank">北京草房美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70618" data-click-name="footer_nav_col_click" target="_blank">北京次渠美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r81430" data-click-name="footer_nav_col_click" target="_blank">北京朝阳公园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r67342" data-click-name="footer_nav_col_click" target="_blank">北京城关镇美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1477" data-click-name="footer_nav_col_click" target="_blank">北京东四美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1486" data-click-name="footer_nav_col_click" target="_blank">北京地安门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2066" data-click-name="footer_nav_col_click" target="_blank">北京东直门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2078" data-click-name="footer_nav_col_click" target="_blank">北京大望路美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2581" data-click-name="footer_nav_col_click" target="_blank">北京对外经贸美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2873" data-click-name="footer_nav_col_click" target="_blank">北京德外大街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7041" data-click-name="footer_nav_col_click" target="_blank">北京大红门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7509" data-click-name="footer_nav_col_click" target="_blank">北京东坝美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r12015" data-click-name="footer_nav_col_click" target="_blank">北京定福庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23017" data-click-name="footer_nav_col_click" target="_blank">北京大屯美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23021" data-click-name="footer_nav_col_click" target="_blank">北京东四十条美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23029" data-click-name="footer_nav_col_click" target="_blank">北京大钟寺美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r83304" data-click-name="footer_nav_col_click" target="_blank">北京东大桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r67346" data-click-name="footer_nav_col_click" target="_blank">北京窦店镇美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1482" data-click-name="footer_nav_col_click" target="_blank">北京复兴门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1483" data-click-name="footer_nav_col_click" target="_blank">北京阜成门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1507" data-click-name="footer_nav_col_click" target="_blank">北京方庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1509" data-click-name="footer_nav_col_click" target="_blank">北京丰台其它美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23037" data-click-name="footer_nav_col_click" target="_blank">北京分钟寺/成寿寺美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1493" data-click-name="footer_nav_col_click" target="_blank">北京公主坟/万寿路美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1499" data-click-name="footer_nav_col_click" target="_blank">北京广内大街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1500" data-click-name="footer_nav_col_click" target="_blank">北京广外大街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1924" data-click-name="footer_nav_col_click" target="_blank">北京古城/八角美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2578" data-click-name="footer_nav_col_click" target="_blank">北京国贸美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2584" data-click-name="footer_nav_col_click" target="_blank">北京管庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2590" data-click-name="footer_nav_col_click" target="_blank">北京广渠门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5956" data-click-name="footer_nav_col_click" target="_blank">北京果园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7506" data-click-name="footer_nav_col_click" target="_blank">北京公益西桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r12016" data-click-name="footer_nav_col_click" target="_blank">北京国展美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23002" data-click-name="footer_nav_col_click" target="_blank">北京工人体育场美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23007" data-click-name="footer_nav_col_click" target="_blank">北京高碑店美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23025" data-click-name="footer_nav_col_click" target="_blank">北京光明楼/龙潭湖美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1495" data-click-name="footer_nav_col_click" target="_blank">北京航天桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1498" data-click-name="footer_nav_col_click" target="_blank">北京海淀其它美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2591" data-click-name="footer_nav_col_click" target="_blank">北京和平里美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2597" data-click-name="footer_nav_col_click" target="_blank">北京虎坊桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5953" data-click-name="footer_nav_col_click" target="_blank">北京回龙观美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5961" data-click-name="footer_nav_col_click" target="_blank">北京黄村美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7040" data-click-name="footer_nav_col_click" target="_blank">北京花乡美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70610" data-click-name="footer_nav_col_click" target="_blank">北京槐房万达广场美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r64877" data-click-name="footer_nav_col_click" target="_blank">北京后沙峪美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r67374" data-click-name="footer_nav_col_click" target="_blank">北京河北镇美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1465" data-click-name="footer_nav_col_click" target="_blank">北京建外大街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1472" data-click-name="footer_nav_col_click" target="_blank">北京劲松/潘家园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1476" data-click-name="footer_nav_col_click" target="_blank">北京建国门/北京站美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2583" data-click-name="footer_nav_col_click" target="_blank">北京酒仙桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5960" data-click-name="footer_nav_col_click" target="_blank">北京旧宫美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7521" data-click-name="footer_nav_col_click" target="_blank">北京九棵树美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23988" data-click-name="footer_nav_col_click" target="_blank">北京军博美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86574" data-click-name="footer_nav_col_click" target="_blank">北京居庸关长城美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2879" data-click-name="footer_nav_col_click" target="_blank">北京开阳里美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2881" data-click-name="footer_nav_col_click" target="_blank">北京看丹桥美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1469" data-click-name="footer_nav_col_click" target="_blank">北京亮马桥/三元桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1508" data-click-name="footer_nav_col_click" target="_blank">北京六里桥/丽泽桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1926" data-click-name="footer_nav_col_click" target="_blank">北京鲁谷美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2877" data-click-name="footer_nav_col_click" target="_blank">北京刘家窑美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5957" data-click-name="footer_nav_col_click" target="_blank">北京梨园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7508" data-click-name="footer_nav_col_click" target="_blank">北京卢沟桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r12011" data-click-name="footer_nav_col_click" target="_blank">北京良乡美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23010" data-click-name="footer_nav_col_click" target="_blank">北京蓝色港湾美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23014" data-click-name="footer_nav_col_click" target="_blank">北京立水桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23040" data-click-name="footer_nav_col_click" target="_blank">北京丽泽桥/丰管路美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r85684" data-click-name="footer_nav_col_click" target="_blank">北京龙湖天街购物中心美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86566" data-click-name="footer_nav_col_click" target="_blank">北京莲花山滑雪场场美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2882" data-click-name="footer_nav_col_click" target="_blank">北京模式口美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r12013" data-click-name="footer_nav_col_click" target="_blank">北京马泉营美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23039" data-click-name="footer_nav_col_click" target="_blank">北京马家堡/角门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r25907" data-click-name="footer_nav_col_click" target="_blank">北京马驹桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86572" data-click-name="footer_nav_col_click" target="_blank">北京明十三陵美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r64878" data-click-name="footer_nav_col_click" target="_blank">北京马坡牛栏山美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2596" data-click-name="footer_nav_col_click" target="_blank">北京牛街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23023" data-click-name="footer_nav_col_click" target="_blank">北京南锣鼓巷/鼓楼东大街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23028" data-click-name="footer_nav_col_click" target="_blank">北京南菜园/白纸坊美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23042" data-click-name="footer_nav_col_click" target="_blank">北京南口镇美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23989" data-click-name="footer_nav_col_click" target="_blank">北京农业大学西区美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r64879" data-click-name="footer_nav_col_click" target="_blank">北京南彩美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1923" data-click-name="footer_nav_col_click" target="_blank">北京苹果园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70633" data-click-name="footer_nav_col_click" target="_blank">北京庞各庄美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1503" data-click-name="footer_nav_col_click" target="_blank">北京前门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2589" data-click-name="footer_nav_col_click" target="_blank">北京清河美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2878" data-click-name="footer_nav_col_click" target="_blank">北京青塔美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r22998" data-click-name="footer_nav_col_click" target="_blank">北京青年路美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r67384" data-click-name="footer_nav_col_click" target="_blank">北京青龙湖镇美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23033" data-click-name="footer_nav_col_click" target="_blank">北京人民大学美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1491" data-click-name="footer_nav_col_click" target="_blank">北京苏州桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1496" data-click-name="footer_nav_col_click" target="_blank">北京上地美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1927" data-click-name="footer_nav_col_click" target="_blank">北京石景山其它美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2579" data-click-name="footer_nav_col_click" target="_blank">北京双井美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2580" data-click-name="footer_nav_col_click" target="_blank">北京三里屯美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2585" data-click-name="footer_nav_col_click" target="_blank">北京首都机场美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2586" data-click-name="footer_nav_col_click" target="_blank">北京十八里店美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2587" data-click-name="footer_nav_col_click" target="_blank">北京双榆树美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2595" data-click-name="footer_nav_col_click" target="_blank">北京什刹海美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2871" data-click-name="footer_nav_col_click" target="_blank">北京十里堡美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2875" data-click-name="footer_nav_col_click" target="_blank">北京沙子口美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r12012" data-click-name="footer_nav_col_click" target="_blank">北京孙河美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r22996" data-click-name="footer_nav_col_click" target="_blank">北京四惠美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r22999" data-click-name="footer_nav_col_click" target="_blank">北京石佛营美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23005" data-click-name="footer_nav_col_click" target="_blank">北京双桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23013" data-click-name="footer_nav_col_click" target="_blank">北京十里河美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23026" data-click-name="footer_nav_col_click" target="_blank">北京沙滩/美术馆灯市口美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23032" data-click-name="footer_nav_col_click" target="_blank">北京四季青美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23041" data-click-name="footer_nav_col_click" target="_blank">北京顺义美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23044" data-click-name="footer_nav_col_click" target="_blank">北京沙河美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70275" data-click-name="footer_nav_col_click" target="_blank">北京石榴庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r83302" data-click-name="footer_nav_col_click" target="_blank">北京世贸天阶美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86568" data-click-name="footer_nav_col_click" target="_blank">北京上方山国家森林公园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86575" data-click-name="footer_nav_col_click" target="_blank">北京十三陵水库美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r64880" data-click-name="footer_nav_col_click" target="_blank">北京石园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r64881" data-click-name="footer_nav_col_click" target="_blank">北京宋庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r67376" data-click-name="footer_nav_col_click" target="_blank">北京十渡镇美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70132" data-click-name="footer_nav_col_click" target="_blank">北京宋家庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70191" data-click-name="footer_nav_col_click" target="_blank">北京芍药居美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1505" data-click-name="footer_nav_col_click" target="_blank">北京天坛美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5954" data-click-name="footer_nav_col_click" target="_blank">北京天通苑美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r22997" data-click-name="footer_nav_col_click" target="_blank">北京太阳宫美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23000" data-click-name="footer_nav_col_click" target="_blank">北京甜水园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23027" data-click-name="footer_nav_col_click" target="_blank">北京陶然亭美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23045" data-click-name="footer_nav_col_click" target="_blank">北京通州北苑美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86548" data-click-name="footer_nav_col_click" target="_blank">北京土桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r70131" data-click-name="footer_nav_col_click" target="_blank">北京田村美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1471" data-click-name="footer_nav_col_click" target="_blank">北京望京美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1475" data-click-name="footer_nav_col_click" target="_blank">北京王府井/东单美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1489" data-click-name="footer_nav_col_click" target="_blank">北京五道口美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1996" data-click-name="footer_nav_col_click" target="_blank">北京魏公村美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2588" data-click-name="footer_nav_col_click" target="_blank">北京五棵松美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23034" data-click-name="footer_nav_col_click" target="_blank">北京万柳美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23990" data-click-name="footer_nav_col_click" target="_blank">北京武夷花园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r64883" data-click-name="footer_nav_col_click" target="_blank">北京物资学院美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1481" data-click-name="footer_nav_col_click" target="_blank">北京西单美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1484" data-click-name="footer_nav_col_click" target="_blank">北京西直门/动物园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1485" data-click-name="footer_nav_col_click" target="_blank">北京新街口美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1501" data-click-name="footer_nav_col_click" target="_blank">北京宣武门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2593" data-click-name="footer_nav_col_click" target="_blank">北京西四美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5958" data-click-name="footer_nav_col_click" target="_blank">北京新华大街美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7042" data-click-name="footer_nav_col_click" target="_blank">北京小汤山美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7043" data-click-name="footer_nav_col_click" target="_blank">北京西红门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7510" data-click-name="footer_nav_col_click" target="_blank">北京香山美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23009" data-click-name="footer_nav_col_click" target="_blank">北京霄云路美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23015" data-click-name="footer_nav_col_click" target="_blank">北京小营美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23018" data-click-name="footer_nav_col_click" target="_blank">北京小庄/红庙美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23031" data-click-name="footer_nav_col_click" target="_blank">北京西三旗美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23035" data-click-name="footer_nav_col_click" target="_blank">北京学院桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23038" data-click-name="footer_nav_col_click" target="_blank">北京夏家胡同/纪家庙美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r85511" data-click-name="footer_nav_col_click" target="_blank">北京小红门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86567" data-click-name="footer_nav_col_click" target="_blank">北京仙栖洞美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86569" data-click-name="footer_nav_col_click" target="_blank">北京小汤山/央美博艺艺术馆美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86571" data-click-name="footer_nav_col_click" target="_blank">北京霞云岭国家森林公园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r64882" data-click-name="footer_nav_col_click" target="_blank">北京西集美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1470" data-click-name="footer_nav_col_click" target="_blank">北京亚运村美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1497" data-click-name="footer_nav_col_click" target="_blank">北京颐和园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1994" data-click-name="footer_nav_col_click" target="_blank">北京右安门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1995" data-click-name="footer_nav_col_click" target="_blank">北京洋桥/木樨园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2594" data-click-name="footer_nav_col_click" target="_blank">北京月坛美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2872" data-click-name="footer_nav_col_click" target="_blank">北京远大路美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r5959" data-click-name="footer_nav_col_click" target="_blank">北京亦庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r7507" data-click-name="footer_nav_col_click" target="_blank">北京云岗美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23011" data-click-name="footer_nav_col_click" target="_blank">北京燕莎/农业展览馆美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23012" data-click-name="footer_nav_col_click" target="_blank">北京姚家园美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23022" data-click-name="footer_nav_col_click" target="_blank">北京雍和宫/地坛美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r86570" data-click-name="footer_nav_col_click" target="_blank">北京云居滑雪场场美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r67349" data-click-name="footer_nav_col_click" target="_blank">北京阎村镇美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r67350" data-click-name="footer_nav_col_click" target="_blank">北京燕山美食</a></li>
                                    </ul>
                                    <ul class="char-content J-city-content">
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1468" data-click-name="footer_nav_col_click" target="_blank">北京左家庄美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1488" data-click-name="footer_nav_col_click" target="_blank">北京中关村美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r1494" data-click-name="footer_nav_col_click" target="_blank">北京紫竹桥美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r2874" data-click-name="footer_nav_col_click" target="_blank">北京左安门美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r23030" data-click-name="footer_nav_col_click" target="_blank">北京知春路美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10r25600" data-click-name="footer_nav_col_click" target="_blank">北京总部基地美食</a></li>
                                    </ul>
                    </div>
                </dd>
                <p class="moreover J-moreover">更多</p>
            </dl>
        <!--城市推荐菜-->
        <!--城市美食-->
        <!--生活导航-->

        <!--热门城市-->
        <!--品牌馆新增底部内链-->
        <!--全国大全-->
        <!--同城推荐-->
            <dl class="linksItem J-country-link">
                <dt class="b-left">
                <p>美食排行榜:</p>
                </dt>
                <dd class="b-right ">
                    <ul class="characters J-country-char">
                            <li><span>B</span></li>
                            <li><span>C</span></li>
                            <li><span>D</span></li>
                            <li><span>F</span></li>
                            <li><span>G</span></li>
                            <li><span>H</span></li>
                            <li><span>J</span></li>
                            <li><span>K</span></li>
                            <li><span>L</span></li>
                            <li><span>M</span></li>
                            <li><span>N</span></li>
                            <li><span>P</span></li>
                            <li><span>Q</span></li>
                            <li><span>S</span></li>
                            <li><span>T</span></li>
                            <li><span>W</span></li>
                            <li><span>X</span></li>
                            <li><span>Y</span></li>
                            <li><span>Z</span></li>
                    </ul>
                    <div class="content country-content">
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/baotou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">包头美食</a></li>
                                            <li><a href="http://www.dianping.com/beijing/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">北京美食</a></li>
                                            <li><a href="http://www.dianping.com/baoding/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">保定美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/changsha/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">长沙美食</a></li>
                                            <li><a href="http://www.dianping.com/chengdu/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">成都美食</a></li>
                                            <li><a href="http://www.dianping.com/changzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">常州美食</a></li>
                                            <li><a href="http://www.dianping.com/changchun/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">长春美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/dalian/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">大连美食</a></li>
                                            <li><a href="http://www.dianping.com/dongguan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">东莞美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/foshan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">佛山美食</a></li>
                                            <li><a href="http://www.dianping.com/fuzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">福州美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/guiyang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">贵阳美食</a></li>
                                            <li><a href="http://www.dianping.com/guangzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">广州美食</a></li>
                                            <li><a href="http://www.dianping.com/guilin/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">桂林美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/hefei/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">合肥美食</a></li>
                                            <li><a href="http://www.dianping.com/hangzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">杭州美食</a></li>
                                            <li><a href="http://www.dianping.com/huizhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">惠州美食</a></li>
                                            <li><a href="http://www.dianping.com/huaian/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">淮安美食</a></li>
                                            <li><a href="http://www.dianping.com/huhehaote/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">呼和浩特美食</a></li>
                                            <li><a href="http://www.dianping.com/haikou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">海口美食</a></li>
                                            <li><a href="http://www.dianping.com/haerbin/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">哈尔滨美食</a></li>
                                            <li><a href="http://www.dianping.com/handan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">邯郸美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/jining/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">济宁美食</a></li>
                                            <li><a href="http://www.dianping.com/jinan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">济南美食</a></li>
                                            <li><a href="http://www.dianping.com/jilin/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">吉林美食</a></li>
                                            <li><a href="http://www.dianping.com/jinjiang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">晋江美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/kunming/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">昆明美食</a></li>
                                            <li><a href="http://www.dianping.com/kunshan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">昆山美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/linyi/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">临沂美食</a></li>
                                            <li><a href="http://www.dianping.com/lanzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">兰州美食</a></li>
                                            <li><a href="http://www.dianping.com/liuzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">柳州美食</a></li>
                                            <li><a href="http://www.dianping.com/luoyang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">洛阳美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/mianyang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">绵阳美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/nanchang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">南昌美食</a></li>
                                            <li><a href="http://www.dianping.com/nanning/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">南宁美食</a></li>
                                            <li><a href="http://www.dianping.com/nantong/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">南通美食</a></li>
                                            <li><a href="http://www.dianping.com/ningbo/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">宁波美食</a></li>
                                            <li><a href="http://www.dianping.com/nanjing/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">南京美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/pixian/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">郫都区美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/qingdao/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">青岛美食</a></li>
                                            <li><a href="http://www.dianping.com/quanzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">泉州美食</a></li>
                                            <li><a href="http://www.dianping.com/qinhuangdao/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">秦皇岛美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/shuangliu/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">双流区美食</a></li>
                                            <li><a href="http://www.dianping.com/suzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">苏州美食</a></li>
                                            <li><a href="http://www.dianping.com/shenzhen/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">深圳美食</a></li>
                                            <li><a href="http://www.dianping.com/shijiazhuang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">石家庄美食</a></li>
                                            <li><a href="http://www.dianping.com/xiamen/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">厦门美食</a></li>
                                            <li><a href="http://www.dianping.com/shenyang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">沈阳美食</a></li>
                                            <li><a href="http://www.dianping.com/shanghai/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">上海美食</a></li>
                                            <li><a href="http://www.dianping.com/shunde/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">顺德区美食</a></li>
                                            <li><a href="http://www.dianping.com/shantou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">汕头美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/tianjin/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">天津美食</a></li>
                                            <li><a href="http://www.dianping.com/zhejiangtaizhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">台州美食</a></li>
                                            <li><a href="http://www.dianping.com/taiyuan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">太原美食</a></li>
                                            <li><a href="http://www.dianping.com/tangshan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">唐山美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/weifang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">潍坊美食</a></li>
                                            <li><a href="http://www.dianping.com/wulumuqi/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">乌鲁木齐美食</a></li>
                                            <li><a href="http://www.dianping.com/wuhu/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">芜湖美食</a></li>
                                            <li><a href="http://www.dianping.com/wuxi/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">无锡美食</a></li>
                                            <li><a href="http://www.dianping.com/wuhan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">武汉美食</a></li>
                                            <li><a href="http://www.dianping.com/wenzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">温州美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/xuzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">徐州美食</a></li>
                                            <li><a href="http://www.dianping.com/xian/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">西安美食</a></li>
                                            <li><a href="http://www.dianping.com/xiangyang/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">襄阳美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/yantai/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">烟台美食</a></li>
                                            <li><a href="http://www.dianping.com/yinchuan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">银川美食</a></li>
                                            <li><a href="http://www.dianping.com/yangzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">扬州美食</a></li>
                                            <li><a href="http://www.dianping.com/yiwu/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">义乌美食</a></li>
                                    </ul>
                                    <ul class="char-content J-country-content ">
                                            <li><a href="http://www.dianping.com/zhongshan/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">中山美食</a></li>
                                            <li><a href="http://www.dianping.com/zhuhai/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">珠海美食</a></li>
                                            <li><a href="http://www.dianping.com/chongqing/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">重庆美食</a></li>
                                            <li><a href="http://www.dianping.com/zhengzhou/ch10/g10" data-click-name="footer_nav_city_click" starget="_blank">郑州美食</a></li>
                                    </ul>
                    </div>
                </dd>
                <p class="moreover J-moreover">更多</p>
            </dl>
        <!--城市推荐菜-->
        <!--城市美食-->
        <!--生活导航-->

        <!--热门城市-->
        <!--品牌馆新增底部内链-->
        <!--全国大全-->
        <!--同城推荐-->
        <!--城市推荐菜-->
            <dl class="linksItem J-city-food">
                <dt class="b-left">
                <p>北京美食推荐菜:</p>
                </dt>
                <dd class="b-right">
                    <ul class="b-ul char-content">
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q355" data-click-name="footer_nav_click">北京意大利面</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q354" data-click-name="footer_nav_click">北京色拉</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q469" data-click-name="footer_nav_click">北京响油鳝糊</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q89" data-click-name="footer_nav_click">北京虾饺皇</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q238" data-click-name="footer_nav_click">北京哈根达斯</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q243" data-click-name="footer_nav_click">北京牛排</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q475" data-click-name="footer_nav_click">北京松鼠桂鱼</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q239" data-click-name="footer_nav_click">北京冰淇淋</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q353" data-click-name="footer_nav_click">北京披萨</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q711" data-click-name="footer_nav_click">北京黑三剁</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q250" data-click-name="footer_nav_click">北京北极贝</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q307" data-click-name="footer_nav_click">北京烤肉</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q236" data-click-name="footer_nav_click">北京三文鱼</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q14" data-click-name="footer_nav_click">北京咖喱牛腩</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q41" data-click-name="footer_nav_click">北京小笼</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q534" data-click-name="footer_nav_click">北京米酒</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q300" data-click-name="footer_nav_click">北京鳗鱼饭</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q399" data-click-name="footer_nav_click">北京罗非鱼</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q558" data-click-name="footer_nav_click">北京鱼头泡饼</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/q90" data-click-name="footer_nav_click">北京冰火菠萝油</a>
                            </li>
                    </ul>
                </dd>
                <p class="moreover J-moreover showhide" style="visibility: visible;">更多</p>
            </dl>
        <!--城市美食-->
        <!--生活导航-->

        <!--热门城市-->
        <!--品牌馆新增底部内链-->
        <!--全国大全-->
        <!--同城推荐-->
        <!--城市推荐菜-->
        <!--城市美食-->
            <dl class="linksItem J-city-allfood">
                <dt class="b-left">
                <p>北京美食:</p>
                </dt>
                <dd class="b-right">
                    <ul class="b-ul char-content">
                            <li>
                                <a target="_blank" href="/beijing/ch10/g508" data-click-name="footer_nav_click">北京烧烤</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g117" data-click-name="footer_nav_click">北京面包甜点</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g110" data-click-name="footer_nav_click">北京火锅</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g112" data-click-name="footer_nav_click">北京小吃</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g111" data-click-name="footer_nav_click">北京自助餐</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g113" data-click-name="footer_nav_click">北京日本料理</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g116" data-click-name="footer_nav_click">北京西餐</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g34014" data-click-name="footer_nav_click">北京下午茶</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g311" data-click-name="footer_nav_click">北京北京菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g114" data-click-name="footer_nav_click">北京韩国料理</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g115" data-click-name="footer_nav_click">北京东南亚菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g118" data-click-name="footer_nav_click">北京其他美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g103" data-click-name="footer_nav_click">北京粤菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g102" data-click-name="footer_nav_click">北京川菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g251" data-click-name="footer_nav_click">北京海鲜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g219" data-click-name="footer_nav_click">北京小龙虾</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g104" data-click-name="footer_nav_click">北京湘菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g248" data-click-name="footer_nav_click">北京云南菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g1817" data-click-name="footer_nav_click">北京粉面馆</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g101" data-click-name="footer_nav_click">北京江浙菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g4473" data-click-name="footer_nav_click">北京烤鱼</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g3243" data-click-name="footer_nav_click">北京新疆菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g106" data-click-name="footer_nav_click">北京东北菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g109" data-click-name="footer_nav_click">北京素菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g34032" data-click-name="footer_nav_click">北京人气餐厅</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g1845" data-click-name="footer_nav_click">北京俄罗斯菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g26482" data-click-name="footer_nav_click">北京徽菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g105" data-click-name="footer_nav_click">北京贵州菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g34055" data-click-name="footer_nav_click">北京早茶</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g250" data-click-name="footer_nav_click">北京创意菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g26483" data-click-name="footer_nav_click">北京鲁菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g246" data-click-name="footer_nav_click">北京湖北菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g26481" data-click-name="footer_nav_click">北京西北菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g1783" data-click-name="footer_nav_click">北京家常菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g1338" data-click-name="footer_nav_click">北京私房菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g107" data-click-name="footer_nav_click">北京台湾菜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g2714" data-click-name="footer_nav_click">北京水果生鲜</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g33759" data-click-name="footer_nav_click">北京食品保健</a>
                            </li>
                            <li>
                                <a target="_blank" href="/beijing/ch10/g34236" data-click-name="footer_nav_click">北京饮品店</a>
                            </li>
                    </ul>
                </dd>
                <p class="moreover J-moreover showhide" style="visibility: visible;">更多</p>
            </dl>
        <!--生活导航-->

        <!--热门城市-->
        <!--品牌馆新增底部内链-->
        <!--全国大全-->
        <!--同城推荐-->
        <!--城市推荐菜-->
        <!--城市美食-->
        <!--生活导航-->
            <dl class="linksItem J-city-other">
                <dt class="b-left">
                <p>北京生活导航:</p>
                </dt>
                <dd class="b-right">
                    <ul class="b-ul char-content">
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10" data-click-name="footer_nav_click">北京美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch25" data-click-name="footer_nav_click">北京电影演出赛事</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch30" data-click-name="footer_nav_click">北京休闲娱乐</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch60" data-click-name="footer_nav_click">北京酒店</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch50" data-click-name="footer_nav_click">北京丽人</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch15" data-click-name="footer_nav_click">北京K歌</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch45" data-click-name="footer_nav_click">北京运动健身</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch35" data-click-name="footer_nav_click">北京周边游</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch70" data-click-name="footer_nav_click">北京亲子</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch55" data-click-name="footer_nav_click">北京结婚</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch20" data-click-name="footer_nav_click">北京购物</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch95" data-click-name="footer_nav_click">北京宠物</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch80" data-click-name="footer_nav_click">北京生活服务</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch75" data-click-name="footer_nav_click">北京学习培训</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch65" data-click-name="footer_nav_click">北京爱车</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch85" data-click-name="footer_nav_click">北京医疗健康</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch90" data-click-name="footer_nav_click">北京家居</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch40" data-click-name="footer_nav_click">北京宴会</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch33954" data-click-name="footer_nav_click">北京榛果民宿</a>
                            </li>
                    </ul>
                </dd>
                <p class="moreover J-moreover showhide" style="visibility: hidden;">更多</p>
            </dl>

        <!--热门城市-->
        <!--品牌馆新增底部内链-->
        <!--全国大全-->
        <!--同城推荐-->
        <!--城市推荐菜-->
        <!--城市美食-->
        <!--生活导航-->

        <!--热门城市-->
            <dl class="linksItem J-city-hot">
                <dt class="b-left">
                <p>美食 - 热门城市:</p>
                </dt>
                <dd class="b-right">
                    <ul class="b-ul char-content">
                            <li>
                                <a target="_blank" href="http://www.dianping.com/beijing/ch10/g10" data-click-name="footer_nav_click">北京美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/shanghai/ch10/g10" data-click-name="footer_nav_click">上海美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/guangzhou/ch10/g10" data-click-name="footer_nav_click">广州美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/shenzhen/ch10/g10" data-click-name="footer_nav_click">深圳美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/tianjin/ch10/g10" data-click-name="footer_nav_click">天津美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/hangzhou/ch10/g10" data-click-name="footer_nav_click">杭州美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/nanjing/ch10/g10" data-click-name="footer_nav_click">南京美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/jinan/ch10/g10" data-click-name="footer_nav_click">济南美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/chongqing/ch10/g10" data-click-name="footer_nav_click">重庆美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/qingdao/ch10/g10" data-click-name="footer_nav_click">青岛美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/dalian/ch10/g10" data-click-name="footer_nav_click">大连美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/ningbo/ch10/g10" data-click-name="footer_nav_click">宁波美食</a>
                            </li>
                            <li>
                                <a target="_blank" href="http://www.dianping.com/xiamen/ch10/g10" data-click-name="footer_nav_click">厦门美食</a>
                            </li>
                    </ul>
                </dd>
                <p class="moreover J-moreover showhide" style="visibility: visible;">更多</p>
            </dl>
</section>


<div class="J_mkt-group-1"></div>
            </div>
            
        <div class="aside">

    <div class="J_mkt-group-2"></div>
    <div class="J_aside-qrcode"></div>

    <div class="J_midas-3"></div>

        <div class="J_mkt-group-3"></div>
    </div>

        </div>
            <div class="seolist seolist-static">
    <ul>
        相关榜单：<a id="seo-mylist-expand" href="javascript:;" class="packup-seo-icon">
        		        	<i class="packup-seo"></i>
        		        </a>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1166814" title="北京大兴区博物馆排行">北京大兴区博...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1166913" title="北京通州区文化艺术馆排行">北京通州区文...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1166919" title="北京通州区游乐游艺排行">北京通州区游...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167025" title="北京昌平区KTV排行">北京昌平区K...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167038" title="北京昌平区美术展览排行">北京昌平区美...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167145" title="北京房山区景点/郊游排行">北京房山区景...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167146" title="北京房山区公园排行">北京房山区公...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167147" title="北京房山区足浴足疗按摩排行">北京房山区足...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167149" title="北京房山区游乐游艺排行">北京房山区游...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167151" title="北京房山区桌面游戏排行">北京房山区桌...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167152" title="北京房山区演出场馆排行">北京房山区演...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167153" title="北京房山区博物馆排行">北京房山区博...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167191" title="北京房山区儿童游乐场排行">北京房山区儿...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167233" title="北京顺义区电影院排行">北京顺义区电...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167242" title="北京顺义区图书馆排行">北京顺义区图...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167332" title="北京近郊景点/郊游排行">北京近郊景点...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167433" title="北京建外大街文化艺术馆排行">北京建外大街...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167437" title="北京建外大街洗浴中心排行">北京建外大街...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167538" title="北京朝外大街KTV排行">北京朝外大街...</a></li>
                <li><a target="_blank" href="http://www.dianping.com/mylist/1167543" title="北京朝外大街足浴足疗按摩排行">北京朝外大街...</a></li>
    </ul>
</div>

        <a href="#top" class="to-top J_to-top Hide"><i></i></a>
    </div>
    <div class="footer-container"><div id="channel-footer" class="channel-footer"> <p class="links"> <a target="_blank" href="//www.dianping.com/help/center/rule?name=about1" rel="nofollow">关于大众点评</a>| <a target="_blank" href="https://dpapp-appeal.meituan.com/#/shopCreditRegulationPC" rel="nofollow">诚信公约</a>| <a target="_blank" href="//www.dianping.com/help" rel="nofollow">网站帮助</a>| <a target="_blank" href="//www.dianping.com/sitemap/c1c10">网站地图</a>| <a target="_blank" href="//www.dianping.com/business/" rel="nofollow">推广服务</a>| <a target="_blank" href="//www.dianping.com/help/center/rule?name=media1" rel="nofollow">媒体报道</a>| <a target="_blank" href="http://careers.dianping.com" rel="nofollow">人才招聘</a>| <!--新增footer links--> <span class="links-container"> <a class="ext-links" href="javascript:void(0);" rel="nofollow">最新咨询</a>| </span> <a target="_blank" href="//www.dianping.com/forum" rel="nofollow">站务论坛</a>| <a target="_blank" href="//www.dianping.com/help/center/rule?name=about4" rel="nofollow">联系我们</a>| <a target="_blank" href="http://developer.dianping.com" rel="nofollow">开发者</a>| <a target="_blank" href="https://developer.meituan.com/?applyFrom=dianping_c_pc_busines" rel="nofollow">聚宝盆餐饮开放平台</a> </p> <!--新增 footer links 面板--> <div class="ext-container Hide"> <div class="link-items Hide"> <a target="_blank" href="//www.dianping.com/home-tuku"><span>家装图库</span></a> <a target="_blank" href="//m.dianping.com/home-tuku"><span>家装图库手机版</span></a> <a target="_blank" href="//www.dianping.com/jiehun/wenda"><span>结婚资讯</span></a> <a target="_blank" href="//www.dianping.com/plastic/item"><span>整形项目大全</span></a> <a target="_blank" href="//www.dianping.com/movie"><span>点评电影</span></a> </div> </div> <p class="rights"> <span style="margin-right:10px;">©2003-2018 dianping.com, All Rights Reserved.</span> <span>本站发布的所有内容，未经许可，不得转载，详见 <a rel="nofollow" class="G" href="//www.dianping.com/help/center/rule?name=base2">《知识产权声明》</a>。 </span> </p> </div> <script> (function(){var h=navigator.userAgent;var i=navigator.appName;var b=i.indexOf("Microsoft Internet Explorer")!==-1;if(!b){return false}var d=/MSIE (\d+).0/g;var e=d.exec(h);if(e&&e.length&&e[1]<9){var j='<div class="browser-overlay"></div><div id="browser-ie-con" class="browser-ie-con"><div id="browser-close" class="close">×</div><div class="browser-download chrome"><a href="//www.google.cn/chrome/browser/desktop/index.html?utm_dp" target="_black" title="chrome"></a></div><div class="browser-download firefox"><a href="//www.firefox.com.cn/download/?utm_dp" target="_black" title="firefox"></a></div></div>';var f=document.createElement("div");f.id="browser-update-ie";f.className="browser-update-ie";f.innerHTML=j;document.body.appendChild(f);var a=document.documentElement.clientWidth||document.body.clientWidth;var c=document.getElementById("browser-ie-con").offsetWidth;var g=(a-c)/2;document.getElementById("browser-ie-con").style.left=g+"px";document.getElementById("browser-close").attachEvent("onclick",function(){document.getElementById("browser-update-ie").style.display="none"},false)}})(); </script></div>
<script src="//www.dpfile.com/mod/neuron/7.1.4/neuron.js" id="neuron-js"></script><script>neuron.config({path: "//www.dpfile.com/mod", loaded:["app-midas@0.6.12","app-midas@0.6.12/js/mkt.js","app-main-search@1.2.15","pic-monitor@0.1.3","cookie@0.2.0","css-shop-tag@1.0.1","map-iframe-dp@0.1.1","main-authbox@1.0.9","css-rating@1.0.2","midas-log@0.0.3","request@0.2.8","css-shop-tag@0.1.3","tpl@0.2.1","switch@0.1.0","hippo@1.2.28","placeholder@0.1.1","easy-login@0.4.39","cookie@0.1.2","mbox@1.0.4","request@1.0.8","mix@1.0.1","fx@2.0.0","attributes@1.4.1","asset@1.0.2","class@2.0.5","lang@1.0.1","hexrgb@0.0.1","jquery@1.9.2","underscore@1.5.3","events@1.0.5","clone@0.1.13","util@1.0.5","json@1.0.1"], graph:{"1":["0.1.3"],"3":["1.9.2"],"6":["1.0.1"],"5":["1.0.5",{"json@~1.0.0":6}],"4":["1.0.5",{"util@~1.0.0":5}],"7":["0.0.1"],"8":["1.0.1"],"2":["2.0.0",{"jquery@~1.9.2":3,"events@~1.0.5":4,"hexrgb@~0.0.1":7,"lang@~1.0.0":8,"util@~1.0.4":5}],"9":["1.2.28"],"10":["0.0.3",{"jquery@^1.9.2":3}],"12":["1.0.2"],"14":["0.1.13",{"util@~1.0.2":5}],"15":["1.5.3"],"13":["2.0.5",{"clone@~0.1.11":14,"events@~1.0.0":4,"underscore@~1.5.2":15,"util@~1.0.0":5}],"11":["0.2.8",{"json@~1.0.0":6,"lang@~1.0.0":8,"asset@~1.0.0":12,"class@~2.0.0":13}],"17":["1.4.1",{"clone@~0.1.11":14,"util@~1.0.0":5}],"18":["1.0.1"],"16":["0.1.0",{"jquery@~1.9.2":3,"fx@~2.0.0":2,"events@~1.0.5":4,"attributes@~1.4.0":17,"clone@~0.1.12":14,"mix@~1.0.1":18,"underscore@~1.5.3":15,"util@~1.0.4":5}],"19":["0.2.1"],"0":["0.6.12",{"css-shop-tag@~0.1.0":1,"fx@^2.0.0":2,"hippo@~1.2.2":9,"jquery@~1.9.2":3,"json@~1.0.1":6,"midas-log@~0.0.0":10,"request@~0.2.4":11,"switch@~0.1.0":16,"tpl@~0.2.1":19}],"21":["0.2.0"],"22":["1.0.2"],"23":["1.0.1"],"25":["0.1.2"],"26":["1.0.4",{"class@~2.0.5":13,"jquery@~1.9.2":3,"lang@~1.0.0":8}],"27":["1.0.8",{"class@~2.0.0":13,"asset@~1.0.0":12,"json@~1.0.0":6,"lang@~1.0.0":8}],"28":["0.4.39"],"29":["0.1.1",{"jquery@~1.9.2":3}],"24":["1.0.9",{"jquery@~1.9.2":3,"cookie@~0.1.0":25,"mbox@~1.0.1":26,"request@~1.0.7":27,"easy-login@~0.4.39":28,"placeholder@~0.1.1":29}],"30":["0.1.1",{"jquery@~1.9.2":3}],"20":["1.2.15",{"class@^2.0.5":13,"cookie@~0.2.0":21,"css-rating@^1.0.0":22,"css-shop-tag@^1.0.1":23,"hippo@^1.2.28":9,"jquery@~1.9.2":3,"main-authbox@^1.0.0":24,"map-iframe-dp@~0.1.0":30,"mbox@^1.0.0":26,"request@~0.2.0":11,"tpl@~0.2.1":19}],"31":["0.1.3"],"_":{"app-midas@*":0,"app-main-search@*":20,"pic-monitor@*":31}}})</script>
<script async src="//www.dpfile.com/mod/app-midas/0.6.12/app-midas.js"></script>
<script async src="//www.dpfile.com/mod/app-midas/0.6.12/js/mkt.js"></script>
<script async src="//www.dpfile.com/mod/app-main-search/1.2.15/app-main-search.js"></script>
<script async src="//www.dpfile.com/mod/pic-monitor/0.1.3/pic-monitor.js"></script>
<script async src="//www.dpfile.com/mod/cookie/0.2.0/cookie.js"></script>
<script async src="//www.dpfile.com/mod/css-shop-tag/1.0.1/css-shop-tag.js"></script>
<script async src="//www.dpfile.com/mod/map-iframe-dp/0.1.1/map-iframe-dp.js"></script>
<script async src="//www.dpfile.com/mod/main-authbox/1.0.9/main-authbox.js"></script>
<script async src="//www.dpfile.com/mod/css-rating/1.0.2/css-rating.js"></script>
<script async src="//www.dpfile.com/mod/midas-log/0.0.3/midas-log.js"></script>
<script async src="//www.dpfile.com/mod/request/0.2.8/request.js"></script>
<script async src="//www.dpfile.com/mod/css-shop-tag/0.1.3/css-shop-tag.js"></script>
<script async src="//www.dpfile.com/mod/tpl/0.2.1/tpl.js"></script>
<script async src="//www.dpfile.com/mod/switch/0.1.0/switch.js"></script>
<script async src="//www.dpfile.com/mod/hippo/1.2.28/hippo.js"></script>
<script async src="//www.dpfile.com/mod/placeholder/0.1.1/placeholder.js"></script>
<script async src="//www.dpfile.com/mod/easy-login/0.4.39/easy-login.js"></script>
<script async src="//www.dpfile.com/mod/cookie/0.1.2/cookie.js"></script>
<script async src="//www.dpfile.com/mod/mbox/1.0.4/mbox.js"></script>
<script async src="//www.dpfile.com/mod/request/1.0.8/request.js"></script>
<script async src="//www.dpfile.com/mod/mix/1.0.1/mix.js"></script>
<script async src="//www.dpfile.com/mod/fx/2.0.0/fx.js"></script>
<script async src="//www.dpfile.com/mod/attributes/1.4.1/attributes.js"></script>
<script async src="//www.dpfile.com/mod/asset/1.0.2/asset.js"></script>
<script async src="//www.dpfile.com/mod/class/2.0.5/class.js"></script>
<script async src="//www.dpfile.com/mod/lang/1.0.1/lang.js"></script>
<script async src="//www.dpfile.com/mod/hexrgb/0.0.1/hexrgb.js"></script>
<script async src="//www.dpfile.com/mod/jquery/1.9.2/jquery.js"></script>
<script async src="//www.dpfile.com/mod/underscore/1.5.3/underscore.js"></script>
<script async src="//www.dpfile.com/mod/events/1.0.5/events.js"></script>
<script async src="//www.dpfile.com/mod/clone/0.1.13/clone.js"></script>
<script async src="//www.dpfile.com/mod/util/1.0.5/util.js"></script>
<script async src="//www.dpfile.com/mod/json/1.0.1/json.js"></script>
<script>facade({entry:"app-midas", data: {
        query: {
            userId: 806549341,
            userip: '45.77.19.102',
            cityId: 2,
            keyword: '',
            regionId: 0,
            channelId: 10,
            categoryId: 10,
            pageId: 1,
            cookieid: '2625f114-04d8-4f64-fe6f-92928895794d.1541144367',
            multiregionIds: '',
            adShops: [92020785,],
            notAdShops: [  107151368,  5618484,  23919667,  69719009,  93389432,  95137467,  74597797,  69619894,  507576,  69788171,  111599817,  19210686,  22740088,  18146141, ],
        },
        server: '/searchads/ajax/suggestads'
    }});
facade({entry:"app-midas/js/mkt.js", data: {
        query: {
            pageId: 1,
            cityId: 2,
            shopType: 10,
            categoryId: 10,
            regionId: 0,
            keyword: ''
        },
        server: '/mkt/ajax/getNewItems'
    }});
facade({entry:"app-main-search", data: {
        cityId: 2,
        shopIDs: [ 92020785,107151368,5618484,23919667,69719009,93389432,95137467,74597797,69619894,507576,69788171,111599817,19210686,22740088,18146141,]
    }});
facade({entry:"pic-monitor", data: {
        pageType: 'search-list',
        selector: '.shop-list .pic img'
    }});
</script></body>
</html>"""

        foodMap = {}
        print "*****开始了*******"
        for p in range(2,50):
            print "url = " + url % (page)
            response = sess.post(url % (page), headers=headers)
            # print html
            print response.text
            content = etree.HTML(response.text)
            # content = etree.HTML(html)
            # list = content.xpath('//ul/li[1]//div[@class="promo-icon J_promo_icon"]/a[@class="igroup"]/@href')
            # list = content.xpath('//div[@class="txt"]/div[@class="tit"]')
            # foodTitle_list = content.xpath('//div[@class="txt"]/div[@class="tit"]/a/@title')
            foodTitle_list = content.xpath('//div[@class="txt"]/div[@class="tit"]/a/h4/text()')
            foodUrl_list = content.xpath('//div[@class="promo-icon J_promo_icon"]/a[1]/@href')


            
            index = 0
            for i in range(0, len(foodTitle_list)):
                item = {
                    "title": foodTitle_list[i],
                    "url": foodUrl_list[i]
                }
                foodMap[str(index)] = item
                print foodTitle_list[i]
                print foodUrl_list[i]
                index+=1
            sleepTime = random.uniform(10, 20)
            print "结束，等待%ds......." %(sleepTime)

            print "******************************************************"
            print json.dumps(foodMap, ensure_ascii=False).encode("utf-8")
            print "******************************************************"

            page+=1
            time.sleep(sleepTime)

        print json.dumps(foodMap, ensure_ascii=False).encode("utf-8")



if __name__ == "__main__":
    # DaZhongDianPingSpider().login("15017328411","121212")
    DaZhongDianPingSpider().foodList()
