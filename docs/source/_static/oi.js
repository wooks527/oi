window.MathJax = {
    AuthorInit: function () {
        MathJax.Hub.Register.StartupHook("Begin",function () {
            MathJax.Hub.Queue(function () {
                maths = document.getElementsByClassName('math notranslate nohighlight');
                for (var i in maths) {
                    try {
                        var w = $(maths[i]).find('.MathJax')[0].offsetWidth, W = maths[i].parentNode.offsetWidth-40;
                        if (w > W) {
                            maths[i].style.fontSize = (95*W/w)+"%";
                            MathJax.Hub.getAllJax(maths[i])[0].Rerender();
                        }
                    }
                    catch (e) {}
                }
            });
        });
    }
}