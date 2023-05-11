function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event){
       // $this代表当前按钮的jquery对象
       var $this = $(this).text("")

       //阻止默认事件
       event.preventDefault();
       var email = $("input[name='email']").val();
       $.ajax({
           // http://127.0.0.1:500
           // /auth/captcha/email?email=xxx@qq.com
           url: "/auth/captcha/email?email="+email,
           method: "GET",
           success: function (result){
               var code = result['code'];
               if(code == 200){
                   var countdown = 5;
                   alert("验证码已发送到您的邮箱!");
                   $this.off("click");
                   var timer = setInterval(function (){
                       $this.text(countdown);
                       countdown -= 1;
                       if(countdown <= 1){
                           clearInterval(timer);
                           $this.text("获取验证码");
                           bindEmailCaptchaClick();
                       }
                   }, 1000);
               }
               else
                   alert(result['message'])
           },
           fail: function (error){
               console.log(error)
           }
       })
   });
}

$(function (){
    bindEmailCaptchaClick();
});