/**
 * Created by Administrator on 2018/11/7 0007.
 */
var imgIndex = 0;
$(function () {
    //点击右按钮
    $('.right').click(function () {
        var showIndex = imgIndex;
        imgIndex++;
        //临界条件
        if (imgIndex == 2) {
            imgIndex = 0;
        }
        $('.img').eq(showIndex).fadeOut(1000);
        $('.img').eq((showIndex + 1) % 2).fadeIn(1000);
    })

    //点击左按钮
    $('.left').click(function () {
        var showIndex = imgIndex;
        imgIndex--;
        //临界条件
        if (imgIndex == -1) {
            imgIndex = 1;
        }
        $('.img').eq(showIndex).fadeOut(1000);
        $('.img').eq((showIndex - 1) % 2).fadeIn(1000);
    })
})
