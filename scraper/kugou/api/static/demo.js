function searchsong() {

    var elemt = document.getElementById('keywords');

    var keywords = elemt.value;

    var ajax = new XMLHttpRequest();
    //步骤二:设置请求的url参数,参数一是请求的类型,参数二是请求的url,可以带参数,动态的传递参数starName到服务端
    ajax.open('get', '/get_song?keywords=' + keywords);
    //步骤三:发送请求
    ajax.send();
    //步骤四:注册事件 onreadystatechange 状态改变就会调用
    var songlist;
    ajax.onreadystatechange = function () {
        if (ajax.readyState == 4 && ajax.status == 200) {
            //步骤五 如果能够进到这个判断 说明 数据 完美的回来了,并且请求的页面是存在的
            songlist = ajax.responseText; // 默认返回值类型是string

            ap5 = new APlayer({
                element: document.getElementById('player5'),
                autoplay: true,
                mutex: true,
                theme: '#ad7a86',
                mode: 'random',
                listmaxheight: '180px',
                music: JSON.parse(songlist), // 需要将字符串解析成json数组
            });
        };
    }

}

$(document).ready(function () {

    //步骤一:创建异步对象
    var ap5 = new APlayer({
        element: document.getElementById('player5'),
        autoplay: false,
        showlrc: true,
        mutex: true,
        theme: '#ad7a86',
        mode: 'random',
        listmaxheight: '180px',
        music: {},
    });

    var ajax = new XMLHttpRequest();
    //步骤二:设置请求的url参数,参数一是请求的类型,参数二是请求的url,可以带参数,动态的传递参数starName到服务端
    ajax.open('get', '/get_song');
    //步骤三:发送请求
    ajax.send();
    //步骤四:注册事件 onreadystatechange 状态改变就会调用
    var songlist;
    ajax.onreadystatechange = function () {
        if (ajax.readyState == 4 && ajax.status == 200) {
            //步骤五 如果能够进到这个判断 说明 数据 完美的回来了,并且请求的页面是存在的
            songlist = ajax.responseText; // 默认返回值类型是string

            ap5 = new APlayer({
                element: document.getElementById('player5'),
                autoplay: false,
                mutex: true,
                theme: '#ad7a86',
                mode: 'random',
                listmaxheight: '180px',
                music: JSON.parse(songlist), // 需要将字符串解析成json数组
            });
        };
    }


    $("#keywords").keydown(function (e) {
        var curKey = e.which;
        if (curKey == 13) {
            var elemt = document.getElementById('keywords');
            var keywords = elemt.value;
            console.log(keywords);
        }
    });
});