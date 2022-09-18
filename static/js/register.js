function bindCaptchaBtnClick()
{
    $("#get_vcode").on("click", function()
    {
        var $this = $(this);
        var phonenum = $("#id_mobile_phone").val();
        if(!phonenum)
        {
            alert("请先输入手机号！");
            return;
        }
        //通过js发送网络请求
        $.ajax
        ({
            url:"/user/get_sms_vcode/",
            method: "POST",
            dataType: 'json',
            data:
            {
                "phonenum":phonenum,

            },
            success: function(res)
            {
                var code = res['code'];
                if(code == 200)
                {
                // 验证码发送成功后，取消点击事件
                    $this.off("click");
                    //开始倒计时
                    var countDown = 60;
                    var timer = setInterval(function()
                    {
                            countDown -= 1;
                            if(countDown>0)
                            {
                                $this.val(countDown+"秒后重新发送");
                            }
                            else
                            {
                                $this.val("获取验证码");
                                bindCaptchaBtnClick();
                                //清除定时器
                                clearInterval(timer);
                            }
                        }, timeout=1000);
                        alert('验证码发送成功');
                    }
                else
                {
                    alert(res['message']);
                }
            }
        });
    });
}
// 网页文档所有元素加载完成后再执行
$(function(){
    bindCaptchaBtnClick();
});

